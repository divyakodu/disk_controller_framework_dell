import os
from utils.common import detect_platform, visualize
import controllers.ahci_controller as ahci
import controllers.scsi_controller as scsi
import tests.ahci_test as ahci_test
import tests.scsi_test as scsi_test
import utils.windows_util_controller as windows_utils
import utils.mac_util_controller as mac_utils
import time
import config.controller_config as controller_config
import json

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

def run_tests():
    config = controller_config.ControllerConfig().get_controller_config()
    data_dir = config.get("data_dir")
    input_data_file_name = "controller_expected_results.json"

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with open(os.path.join(data_dir, input_data_file_name), "r") as json_file:
        expected_results = json.load(json_file)

    file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
    platform = detect_platform()
    ahci_controller, scsi_controller = create_controller(platform)
    ahci_test.test_ahci_initialization(file_prefix, ahci_controller, expected_results.get("test_ahci_initialization"))
    scsi_test.test_scsi_initialization(file_prefix, scsi_controller, expected_results.get("test_scsi_initialization"))
    ahci_test.test_ahci_enumeration(file_prefix, ahci_controller, expected_results.get("test_ahci_enumeration"))
    scsi_test.test_scsi_enumeration(file_prefix, scsi_controller, expected_results.get("test_scsi_enumeration"))
    ahci_test.test_ahci_performance(file_prefix, ahci_controller, expected_results.get("test_ahci_performance"))
    scsi_test.test_scsi_performance(file_prefix, scsi_controller, expected_results.get("test_ahci_performance"))

if __name__ == '__main__':
    run_tests()
    visualize()