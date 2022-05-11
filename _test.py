from Car import Car
from Input import Plate,Date,Time
from TransitAgent import TransitAgent
import datetime

def test_checkFalseLower():
    car=Car("555")
    dateStr = "11/05/22 06:36:00"
    dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
    agent=TransitAgent()
    assert agent.checkCar(car,dateObj) == False

def test_checkFalseUpper():
    car=Car("156")
    dateStr = "11/05/22 20:58:00"
    dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
    agent=TransitAgent()
    assert agent.checkCar(car,dateObj) == False

def test_checkTrueLower():
    car=Car("555")
    dateStr = "11/05/22 09:36:00"
    dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
    agent=TransitAgent()
    assert agent.checkCar(car,dateObj) == True

def test_checkTrueUpper():
    car=Car("156")
    dateStr = "11/05/22 21:58:00"
    dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
    agent=TransitAgent()
    assert agent.checkCar(car,dateObj) == True
