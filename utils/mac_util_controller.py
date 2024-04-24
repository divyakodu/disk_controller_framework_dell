import subprocess
from utils.common import parse_csv_to_dicts

class MacController:

    def __init__(self):
        pass

    def is_ahci_controlller_available(self):
        #Add Mac-specific code to list AHCI controllers
        result = subprocess.run(["system_profiler", "SPSerialATADataType", "/format:csv"], capture_output=True, text=True)
        controller_dicts = parse_csv_to_dicts(result.stdout)
        if len(controller_dicts)==0:
            return False
        else:
            return True

    def is_scsi_controlller_available(self):
        #Add Mac-specific code to list SCSI controllers
        result = subprocess.run(["system_profiler", "SPSCSIDataType", "/format:csv"], capture_output=True, text=True)
        controller_dicts = parse_csv_to_dicts(result.stdout)
        if len(controller_dicts)==0:
            return False
        else:
            return True

    def list_ahci_controller(self):
        #Add Windows-specific code to list AHCI controllers
        result = subprocess.run(["system_profiler", "SPSerialATADataType", "/format:csv"], capture_output=True, text=True)
        controller_dicts = parse_csv_to_dicts(result.stdout)
        return controller_dicts

    def list_scsi_controller(self):
        #Add Windows-specific code to list SCSI controllers
        result = subprocess.run(["system_profiler", "SPSerialATADataType", "/format:csv"], capture_output=True, text=True)
        controller_dicts = parse_csv_to_dicts(result.stdout)
        return controller_dicts


    def get_ahci_performance(self):
        #Add Windows-specific code to list AHCI controllers
        result = subprocess.run(["system_profiler", "SPSerialATADataType", "/format:csv"],capture_output=True, text=True)
        controller_performance = parse_csv_to_dicts(result.stdout)
        return controller_performance

    def get_scsi_performance(self):
        #Add Windows-specific code to list SCSI controllers
        result = subprocess.run(["system_profiler", "SPSerialATADataType", "/format:csv"], capture_output=True, text=True)
        controller_performance = parse_csv_to_dicts(result.stdout)
        return controller_performance