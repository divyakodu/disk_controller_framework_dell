#Generic SCSI Class.
class SCSIController:
# Initiation
    def __init__(self, controller):
        self.is_scsi_controlller_available = controller.is_scsi_controlller_available
        self.list_scsi_controller = controller.list_scsi_controller
        self.get_scsi_performance = controller.get_scsi_performance

#Function to detect if controller is available
    def detect_controllers(self):
        return self.is_scsi_controlller_available()

#Function to list all devices supported by the controller
    def list_devices(self):
        return self.list_scsi_controller()

#Function to list all devices supported by the controller
    def get_performance(self):
        return self.get_scsi_performance()

#Function to get performance stats
    def test_initialization(self):
        #return self.list_ahci_controllers
        pass

#Generic function. To be defined
    def test_configuration(self):
        pass