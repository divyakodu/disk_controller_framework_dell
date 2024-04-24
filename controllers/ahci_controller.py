#Generic AHCI Class.
class AHCIController:
#Initiation
    def __init__(self, controller):
        self.is_ahci_controlller_available = controller.is_ahci_controlller_available
        self.list_ahci_controller = controller.list_ahci_controller
        self.get_ahci_performance = controller.get_ahci_performance

#Function to detect if controller is available
    def detect_controllers(self):
        return self.is_ahci_controlller_available()

#Function to list all devices supported by the controller
    def list_devices(self):
        return self.list_ahci_controller()

#Function to get performance stats
    def get_performance(self):
        return self.get_ahci_performance()

#Generic function. To be defined
    def test_initialization(self):
        #return self.list_ahci_controllers
        pass

#Generic function. To be defined
    def test_configuration(self):
        pass