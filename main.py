from Input import Plate,Date,Time

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
            try:                
                option=int(input("0.\tValidate\n1.\tExit\n"))
            except:
                print("Error in the input data\nTry again")


if __name__ == "__main__":
    Main.start()