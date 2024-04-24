import threading
import time
import config.controller_config as controller_config
import os
from utils.common import detect_platform, visualize
import controllers.ahci_controller as ahci
import controllers.scsi_controller as scsi
import utils.windows_util_controller as windows_utils
import utils.mac_util_controller as mac_utils
import json
import pandas as pd

stop_event = threading.Event()

def create_controller(platform):
    if platform == "windows":
        ahci_controller = ahci.AHCIController(windows_utils.WindowsController())
        scsi_controller = scsi.SCSIController(windows_utils.WindowsController())
    elif platform == "darwin":
        ahci_controller = ahci.AHCIController(mac_utils.MacController())
        scsi_controller = scsi.SCSIController(mac_utils.MacController())
    else:
        raise NotImplementedError("Platform not supported")

    return ahci_controller, scsi_controller


def read_from_storage():
    config = controller_config.ControllerConfig().get_controller_config()
    load_dir = config.get("load_dir")
    load_file_name = "load_file.txt"
    perf_dir = config.get("perf_dir")
    perf_file_name = "perf_file.json"
    existing_entries = []
    try:
        while not stop_event.is_set():
            start_time = time.time()
            with open(os.path.join(load_dir, load_file_name), "r") as load_file:
                load_file_txt = load_file.read()
            #print(load_file_txt)
# Function to simulate read operation
# Simulate read operation
            time.sleep(1)
            elapsed_time = time.time() - start_time
            platform = detect_platform()
            ahci_controller, scsi_controller = create_controller(platform)
            performance_data = ahci_controller.get_performance()
            print(performance_data)
            #try:
            #    with open(os.path.join(perf_dir, perf_file_name), "r") as perf_file:
            #        existing_entries = json.load(perf_file)
            #except (FileNotFoundError, json.JSONDecodeError):
            existing_entries = []

            with open(os.path.join(perf_dir, perf_file_name), "w") as perf_file:
                # print(existing_entries)
                existing_entries = existing_entries + performance_data
                # pass
            #print(existing_entries)
            #json.dump(existing_entries, perf_file, indent=4)
    except Exception as e:
        print(f"Exception in read thread: {e}")

# Function to simulate write operation

# Main function for performance test
def performance_test(duration_minutes):
    global stop_event
    file_suffix = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config = controller_config.ControllerConfig().get_controller_config()
    perf_dir = config.get("perf_dir")
    perf_file_name = "perf_file.json"
    perf_report_dir = config.get("perf_report_dir")
    perf_report_file_name = "perf_report_"+file_suffix+".html"
# Create threads for read and write operations
    read_thread = threading.Thread(target=read_from_storage)
    #write_thread = threading.Thread(target=write_to_storage)

# Start the threads
    read_thread.start()
    #write_thread.start()

# Wait for the specified duration
    stop_event.wait(duration_minutes * 60)

# Signal threads to stop
    print("Performance test stopping...")
    stop_event.set()
    read_thread.join() # Wait for read thread to finish
    #write_thread.join() # Wait for write thread to finish
    print("Performance test stopped.")

    #df = pd.read_json(os.path.join(perf_dir, perf_file_name))
    #html_report = df.to_html()
    #with open(os.path.join(perf_report_dir, perf_report_file_name), 'w') as f:
    #    f.write(html_report)


# Entry point
if __name__ == "__main__":
    duration_minutes = 1 # Change this to the desired duration
    performance_test(duration_minutes)