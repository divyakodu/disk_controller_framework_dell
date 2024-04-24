Author: Divya Kodukula

When testing AHCI (Advanced Host Controller Interface) and SCSI (Small Computer System Interface) functionalities, we want to ensure that the disk drivers and controllers perform as expected and meet the required
standards.

Running the test case:
1) Run the Python file: controller_features.py
python controller_features.py

This will execute all the test cases. This program will produce logs in stdout. Also, the logs will be captured in logs directory defaulted to : "C:\python_projects\logs". The code creates the folder if not available.
At the end of execution, the code will open the directory selection prompt. Any files from the logs directory can be selected. This will show a plot of passed vs failed test cases. Post displaying the plot, the code will 
generate a report defaulted at the directory : "C:\python_projects\reports". The report will be in html format and can be shared.

Running the performance test case:
1) Run the Python file: controller_performance_test.py
python controller_performance_test.py

This will execute performance test cases. At present only read performance test is enabled. The code will be extended for write performance testing. The code will also be extended to capture the results in exportable
format. At present these features are disabled.
