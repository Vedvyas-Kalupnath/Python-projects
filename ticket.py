Name=input("Enter your name:")
Surname=input("Enter your surname:")
StartingStation=input("Enter Starting Station:")
DestinationStation=input("Enter Destination Station:")
print("")

def journeyDetails(para1,para2,para3,para4):

    print("Name:",Name)
    print("Surname:",Surname)
    print("Start:",StartingStation)
    print("Destination:",DestinationStation)


def getPrice():
    price=(25*10*1.15)
    print("Price:",price)

print("******************")
journeyDetails(Name,Surname,StartingStation,DestinationStation)
getPrice()
print("***************")

