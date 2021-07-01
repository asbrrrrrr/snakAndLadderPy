from random import random
from os import system



def tas():#shut the dice
    return int(random()*10)%(6)+1


def snaks(map):#input the snakes
    for i in range(25):
        m = int (random()*1000)%(167-10+1)+10
        z = int (random()*100)%(100-5+1)+5
        map[m] = -z
        if (m - z) < 0:
            map[m] = 0 ;
def clash(location , location1):
    if (location == location1):
            print ("yes:)")
            location1 = 0 ;
    return location ,location1
        
def lodders(map):#input lodders
    for i in range(25):
        m = int (random()*1000)%(160-10+1)+10
        z = int (random()*100)%(100-5+1)+5
        map[m] = z
        if (m + z) > 167:
            map[m] = 0
def zeroLocation():
    for i in range(3):
        input("Enter to shut a dice")
        tase = tas()
        print ("random number is : " , tase)
        if (tase == 6 ) :
            input ("You can continiue clicking")
            return True
        if ( i == 2 and tase !=6):
            print ("sory you have to stay")
            return False
        
def printLine(number):#print line
    for i in range(number):
        print()
        
def player(player, location , location1 ,map):
    print ("player ", player ,"your location befor a shut a dice is : ", location)
    flag = True
    if (location == 0 ):
        flag = zeroLocation()
    while (flag):
        input ("Enter to shut a dice")
        tase = tas()
        print ("random number is : " , tase)
        if ((location + tase ) > 169):
            print ("oops Sory you have to wait")
        else :
           location =  location + tase
           location , location1 = clash(location , location1)

        while (map[location]> 0 ):
            print ("You reched the ledder and moved ",map[location] , "the house")
            print ("Your location before moved = ",location)
            location = location + map[location]
            print ("Your location after moved = ",location)
            location , location1 = clash(location , location1)
        while (map[location]< 0 ):
            print ("You reched the snake and moved ",map[location] , "the house")
            print ("Your location before moved = ",location)
            location = location + map[location]
            print ("Your location after moved = ",location)
            location , location1 = clash(location , location1)
            
        print ("player ", player ,"your location after a shut a dice is : ", location)
        
        if (tase != 6 ):
            break;
        input ("Enter to reshut dice...")
    return location ,location1
def menu():
    map = [0] * 170
    snaks(map)
    lodders(map)
    locationA = 0
    locationB = 0

    printLine(6)
    print ("\t\t\twelcome to snack game's")
    printLine(6)
    input ("Enter to countinuation...")
    system("cls")
    print ('\n','-' * 70, '\n' , '-'*70)
    print ("\n loadder is :")
    j = 0 
    for i in range (169):
        if (map[i]> 0 )  :
            print ("location is ", i , "and "  , map[i], "moves house" , end = "\t")
            j = j + 1 
            if ((j%2) == 0 ):
                print()
    print ('\n','-' * 70 , '\n' , '-'*70)
    print('\n' , "snaks is : " )
    j = 0 
    for i in range (169):
        if (map[i]< 0 )  :
            print ("location is ", i , "and "  , map[i], "moves house" , end = "\t")
            j = j + 1 
            if ((j%2) == 0 ):
                print()
    print ('\n','-' * 70 , '\n' , '-'*70)
    input ("Enter to start game")
    
    while(True):
        input("player A is your turn press Enter ...")
        locationA , locationB  = player('A' , locationA , locationB , map)
        printLine(6)
        if (locationA == 169):
            print ("player A won")
            return 0
        input("player B is your turn press Enter ...")
        locationB , locationA  = player('B' , locationB , locationA , map)
        if (locationB == 169):
            print ("player B won")
            return 0
        print ('\n','_' * 70 , '\n' , '_'*70)
        
    
menu()
