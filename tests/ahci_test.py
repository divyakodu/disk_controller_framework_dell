import utils.common as common
import time

def test_ahci_initialization(file_prefix, ahci_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "ahci_initialization"
    status = "Failed"
    actual_result = ahci_controller.is_ahci_controlller_available()
    if expected_result == actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)

def test_ahci_enumeration(file_prefix, ahci_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "ahci_enumeration"
    status = "Failed"
    #print(ahci_controller.list_ahci_controller())
    actual_result = len(ahci_controller.list_ahci_controller())
    if expected_result == actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)

def test_ahci_performance(file_prefix, ahci_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "ahci_performance"
    status = "Failed"
    actual_result = ahci_controller.get_performance()
    if actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)