#Common utilities for Framework

import os
import platform
import csv
import json
import time
import logging
import config.controller_config as controller_config
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

logging.basicConfig(level=logging.INFO, format='\033[1;34m%(asctime)s - %(levelname)s -%(message)s\033[0m')

#Detect platform on which code runs
def detect_platform():
    return platform.system().lower()


#Capture log results in file and stdout
def log_test_result(file_prefix, start_time, end_time, test_case_name, status):
    platform = detect_platform()
    config = controller_config.ControllerConfig().get_controller_config()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
    log_entry = {"platform": platform, "test_case": test_case_name, "start_time": start_time, "status": status}
    logging.info(f"-----------------------------------------")
    logging.info(f"Test Case: {test_case_name} on  {platform}")
    logging.info(f"Start Time: {start_time}")
    logging.info(f"End Time: {end_time}")
    logging.info(f"Status: {status}")
    logging.info(f"-----------------------------------------")

    #print(log_entry)

    log_dir = config.get("log_dir")
    log_file_name = platform + "_controller_test_" + file_prefix + ".json"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    try:
        with open(os.path.join(log_dir, log_file_name), "r") as json_file:
            existing_entries = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_entries = []

    with open(os.path.join(log_dir, log_file_name), "w") as json_file:
        #print(existing_entries)
        existing_entries.append(log_entry)
        #pass
        json.dump(existing_entries, json_file, indent=4)

#Parse the stdout and produces dictionary for further processing
def parse_csv_to_dicts(csv_output):
    dicts = []
    row = 0
    for line in csv_output.strip().split('\n'):
        if line.strip() != "":
            pass
            if row == 0:
                dict_name_list = line.strip().split(',')
                row += 1
            else:
                temp_dict = dict()
                dict_value_list = line.strip().split(',')
                for i in range(len(dict_value_list)):
                    temp_dict[dict_name_list[i]] = dict_value_list[i]
                dicts.append(temp_dict)
    return dicts

#Basic visualisation in form of plot and html file for sharing
def visualize():
    platform = detect_platform()
    root = tk.Tk()
    root.withdraw()

    config = controller_config.ControllerConfig().get_controller_config()
    report_dir = config.get("report_dir")
    report_file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
    report_file_name = platform + "_report_controller_test_" + report_file_prefix + ".html"

    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    df = pd.read_json(file_path)

    #print(df)

    status_counts = df['status'].value_counts()
    plt.figure(figsize=(8, 6))
    status_counts.plot(kind='bar', color=['green', 'red'])
    plt.title('Test Results')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

    html_report = df.to_html()

    with open(os.path.join(report_dir, report_file_name), 'w') as f:
        f.write(html_report)