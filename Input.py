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

class Plate(Input):
    def retrieve(self):
        self.value=input("Input plate:\t")    
    def check(self):
        pass
    
class Date(Input):
    def retrieve(self):
        self.value=input("Input date:\t")

    def check(self):
        pass

class Time(Input):
    def retrieve(self):
        self.value=input("Input time:\t")
    def check(self):
        pass