from cgi import test
import datetime

class TransitAgent:
    def __init__(self):
        self.dayReestrictions={
            "0":["1","2"],
            "1":["3","4"],
            "2":["5","6"],
            "3":["7","8"],
            "4":["9","0"],
        }
        self.intervalReestrictions={
            "0":["06:00","09:30"],
            "1":["16:00","21:00"]
        }
    def checkCar(self,car,testDatetime):
        weekday=testDatetime.weekday()
        lastDigit=str(car.getPlatenumber())[-1]
        hour=testDatetime.hour
        minute=testDatetime.minute 
        dateReestrict=datetime.datetime(testDatetime.year, testDatetime.month, testDatetime.day)
        reestrictPlates=self.dayReestrictions[str(weekday)]

        if(lastDigit in reestrictPlates):   
            for key, value in self.intervalReestrictions.items():
                newdateLower = dateReestrict.replace(hour=int(value[0].split(":")[0]), minute=int(value[0].split(":")[1]))
                newdateUpper = dateReestrict.replace(hour=int(value[1].split(":")[0]), minute=int(value[1].split(":")[1]))
                if(testDatetime<=newdateUpper and testDatetime>=newdateLower):
                    car.disableDrive()
                    return
                else:
                    car.enableDrive()