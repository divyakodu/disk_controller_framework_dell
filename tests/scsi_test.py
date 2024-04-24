import utils.common as common
import time

def test_scsi_initialization(file_prefix, scsi_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "scsi_initialization"
    status = "Failed"
    actual_result = scsi_controller.is_scsi_controlller_available()
    if expected_result == actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)

def test_scsi_enumeration(file_prefix, scsi_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "scsi_enumeration"
    status = "Failed"
    #print(ahci_controller.list_ahci_controller())
    actual_result = len(scsi_controller.list_scsi_controller())
    #print(actual_result)
    if expected_result == actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)
    #print(scsi_controller.list_scsi_controller())

def test_scsi_performance(file_prefix, scsi_controller, expected_result):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_case_name = "scsi_performance"
    status = "Failed"
    actual_result = scsi_controller.get_performance()
    if actual_result:
        status = "Passed"
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    common.log_test_result(file_prefix, start_time, end_time, test_case_name, status)