

def races(num):
    print("\nCollecting race info: ")
    race=[]
    for j in range(num):
            time=str(input("How long did it take to complete this race? "))
            if ":" in time:
                a=time.split(":")
                a[0]=float(a[0])
                a[1]=float(a[1])/60.0
                time=float(round(a[0]+a[1],2))
            elif (";"in time)or("."in time)or(","in time):
                time=time.replace(";",":")
                time=time.replace(".",":")
                time=time.replace(",",":")
                a=time.split(":")
                a[0]=float(a[0])
                a[1]=float(a[1])/60.0
                time=float(round(a[0]+a[1],2))
            else:
                time=time+":00"
                a=time.split(":")
                a[0]=float(a[0])
                a[1]=float(a[1])/60.0
                time=float(round(a[0]+a[1],2))
            race.append(time)
    return race
#print(races(1))

def BoatClass():
    BoatClass=str(input("enter boat class: "))
    if BoatClass=="420" or BoatClass=="29er" or BoatClass=="Laser" or BoatClass=="laser" or BoatClass=="Laser 2" or BoatClass=="Laser II" or BoatClass=="laser 2" or BoatClass=="laser II"  or BoatClass=="L2" or BoatClass=="LII" or BoatClass=="l2" or BoatClass=="lII" or BoatClass=="Radial" or BoatClass=="radial" or BoatClass=="Feva" or BoatClass=="feva" or BoatClass=="Opti" or BoatClass=="opti" or BoatClass=="SL 16" or BoatClass=="sl 16" or BoatClass=="SL16" or BoatClass=="sl16" or BoatClass=="CAT" or BoatClass=="Finn" or BoatClass=="finn":
        pass
    else:
        print("Invalid class, try again. ")
        BoatClass=BoatClass()
    return BoatClass

def day_num():
    z=input("Is this the first day of racing? y/n ")
    if z=="y" or z=="n":
        pass
    else:
        day_num()
    return z

def newBoat(y,z):
    try:
        print("\nCollecting new boat information: ")
        sail=input("What is the sail number? ")
        skip=input("enter skipper name: ")
        cr=input("enter crew name: ")
        Boat=BoatClass()
        race=[]
        race=races(y)
        if z=="n":
            score=int(input("What is this boat's score before these races?"))
        else:
            score=0
        List=[skip,cr,Boat,race,score,sail]
        return List
    except:
        print("Error: please re-enter this boat's information")
        List=newBoat(y,z)
        return List


def info():
    info=[]
    x=int(input("how many boats are there? "))
    y=int(input("how many races were there? "))
    z=day_num()
    for i in range(x):
        info.append(newBoat(y,z))
    return info
#info=info()
#print(info)
#print(len(info[0][3]))
  

def handicap(Class,race): 
    if Class=="420":
        for i in race:
            races[i]*=100/97.6
    elif Class=="29er":
        for i in race:
            races[i]*=100/84.5
    elif Class=="Laser" or Class=="laser":
        for i in race:
            races[i]*=100/91.1
    elif Class=="Radial" or Class=="radial":
        for i in race:
            races[i]*=100/96.7
    elif Class=="Feva" or Class=="feva":
        for i in race:
            races[i]*=100/105.2
    elif Class=="Opti" or Class=="opti":
        for i in race:
            races[i]*=100/123.6
    elif Class=="Laser 2" or Class=="laser 2" or Class=="Laser II" or Class=="laser II" or Class=="L2" or Class=="l2" or Class=="LII" or Class=="lII":
        for i in race:
            races[i]*=100/92.8
    elif Class=="SL 16" or Class=="sl 16" or Class=="SL16" or Class=="sl16" or Class=="CAT":
        for i in race:
            races[i]*=100/73
    elif Class=="Finn" or Class=="finn":
        for i in race:
            races[i]*=100/90.1
    else:
        print("Class not recognized. Please try again")
        x=input("enter boat class: ")
        handicap(x,race)
    return race


def scoring(info):
    for i in range(len(info[0][3])): #iterate through x times, x=# races
        for j in range(len(info)): #iterate through the entire list of competitors to compare times
            if info[j][3][i]<info[j-1][3][i]:
                info[j-1],info[j]=info[j],info[j-1]
        for k in range(len(info)):
            info[k][4]+=k+1
    return info
#info=scoring(info)
#print(info)

def sorting(info):
    for i in range(len(info)-1):
        for j in range(1, len(info)):
            if info[j][4] < info[j-1][4]:
                info[j], info[j-1] = info[j-1],info[j]
            elif info[j][4]==info[j-1][4]:
                if info[j][3][-1]<info[j-1][3][-1]:
                    info[j], info[j-1] = info[j-1],info[j]
    return info
#info=sorting(info)
#print(info)


def main():
    name=input("Today's date or regatta day(ie.Saturday July 1st) ")
    makefile=open(name,"w")
    info=info()
    for i in range(len(info)):
        times=handicap(info[i][2],info[i][3])
        info[i][3]=times
    
    info=scoring(info)
    info=sorting(info)
    
    firstline="{0:5} {1:8} {2:20} {3:20} {4:8} {5:35} {6:3}".format("Place","Sail \#","Skipper","Crew","Class","Races","Score") ###
    makefile.write(firstline,"\n") 
    for i in range(len(info)):
        line=info[i]
        raceString=""
        for j in range(len(line[i][3])):
                raceString+="{0:5}".format(line[i][3][j])
        entry="{0:5} {1:8} {2:20} {3:20} {4:8} {5:35} {6:3}".format(i+1,line[5],line[0],line[1],line[2],raceString,line[4]) #####
        makefile.write(entry,"\n")
    
    makefile.close()
    print("File ",name," succesfully created")

#main()