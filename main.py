from Car import Car
from Input import Plate,Date,Time
from TransitAgent import TransitAgent
import datetime

class Main:
    def mainInput():
        option=int(input("0.\tValidate\n1.\tExit\n"))
        if not(option==0 or option==1):
            raise Exception
        return option
    
    def dataInput(plate,date,time):
        plate.retrieve()
        plate.check()            
        date.retrieve()
        date.check()                 
        time.retrieve() 
        time.check()
        return plate,date,time

    def start():
        print("Welcome")
        option=0
        while(option!=1):
            try:                
                option=Main.mainInput()
                if option==1:
                    break
                plate=Plate()
                date=Date()
                time=Time()
                plate,date,time=Main.dataInput(plate,date,time)                
                agent=TransitAgent()
                car=Car(plate.getValue())
                dateStr = date.getValue()+" "+time.getValue()+":00"
                dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S')
                agent.checkCar(car,dateObj)
                print(car)
            except:
                print("Error in the input data\nTry again")
            
if __name__ == "__main__":
    Main.start()