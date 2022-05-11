from abc import ABC, abstractmethod
import datetime
import re

class Input(ABC):
    @abstractmethod
    def retrieve(self):
        pass
    @abstractmethod
    def check(self):
        pass
    def getValue(self):
        return self.value

class Plate(Input):
    def retrieve(self):
        self.value=input("Input plate:\t")    
    def check(self):
        if(not self.value.isdigit()):
            raise Exception("Error-> plate must be number")
        if not (len(self.value) ==4 or len(self.value) ==3):
            raise Exception("Error-> plate must have 3 to 4 number")
    
class Date(Input):
    def retrieve(self):
        self.value=input("Input date:\t")

    def check(self):
        size=len(self.value.split("/"))
        if(size!=3):
            raise Exception("Error-> plate must be sliced with '/' ")
        day, month, year = self.value.split('/')
        try:
            self.date=datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            raise Exception("Error-> Wrong date format ")

class Time(Input):
    def retrieve(self):
        self.value=input("Input time:\t")
    def check(self):
        size=len(self.value.split(":"))
        if(size!=2):
            raise Exception("Error-> time must be sliced with ':' ")
        ocurrences=re.match(r'([01]?[0-9]|2[0-3]):[0-5][0-9]',self.value)
        if(ocurrences==None):
            raise Exception("Error-> Wrong time format ")