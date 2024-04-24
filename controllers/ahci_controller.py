class AHCIController:
    def __init__(self, controller):
        self.is_ahci_controlller_available = controller.is_ahci_controlller_available
        self.list_ahci_controller = controller.list_ahci_controller
        self.get_ahci_performance = controller.get_ahci_performance

    def detect_controllers(self):
        return self.is_ahci_controlller_available()

    def list_devices(self):
        return self.list_ahci_controller()

    def get_performance(self):
        return self.get_ahci_performance()

    def test_initialization(self):
        #return self.list_ahci_controllers
        pass
    def test_configuration(self):
        pass