class Car:
    def __init__(self,plateNumber):
        self.plateNumber=plateNumber
    def __str__(self) -> str:
        return self.plateNumber
    def disableDrive(self):
        self.drive=False
    def enableDrive(self):
        self.drive=True