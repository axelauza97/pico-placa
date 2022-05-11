from Car import Car
from Input import Plate,Date,Time
from TransitAgent import TransitAgent
import datetime

class Main:
    '''Main'''
    def start():
        print("Welcome")
        option=int(input("0.\tValidate\n1.\tExit\n"))
        while(option!=1):
            plate=Plate()
            date=Date()
            time=Time()

            plate.retrieve()
            plate.check()            
            date.retrieve()
            date.check()                 
            time.retrieve() 
            time.check()

            agent=TransitAgent()
            car=Car(plate.getValue())
            dateStr = date.getValue()+" "+time.getValue()+":00"
            dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
            agent.checkCar(car,dateObj)
            print(car)
            try:                
                option=int(input("0.\tValidate\n1.\tExit\n"))
            except:
                print("Error in the input data\nTry again")


if __name__ == "__main__":
    Main.start()