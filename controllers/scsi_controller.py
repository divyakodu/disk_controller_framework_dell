class SCSIController:
    def __init__(self, controller):
        self.is_scsi_controlller_available = controller.is_scsi_controlller_available
        self.list_scsi_controller = controller.list_scsi_controller
        self.get_scsi_performance = controller.get_scsi_performance

    def detect_controllers(self):
        return self.is_scsi_controlller_available()

    def list_devices(self):
        return self.list_scsi_controller()

    def get_performance(self):
        return self.get_scsi_performance()

    def test_initialization(self):
        #return self.list_ahci_controllers
        pass
    def test_configuration(self):
        pass