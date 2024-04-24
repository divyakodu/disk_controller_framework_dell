#Configuration file for controller
class ControllerConfig:

    def __init__(self):
        pass

    def get_controller_config(self):
        controller_config = {"log_dir":"C:\python_projects\logs", "report_dir":"C:\python_projects\\reports", "data_dir":"C:\python_projects\\data", "load_dir":"C:\python_projects\\load", "perf_dir":"C:\python_projects\\perf", "perf_report_dir":"C:\python_projects\\perf_report"}

        return controller_config