class Car:
    def __init__(self,plateNumber):
        self.plateNumber=plateNumber
    def __str__(self):
        if self.drive:
            return "Car with plate "+self.plateNumber+" able to drive"
        else:
            return "Car with plate "+self.plateNumber+" not able to drive"
    def disableDrive(self):
        self.drive=False
    def enableDrive(self):
        self.drive=True