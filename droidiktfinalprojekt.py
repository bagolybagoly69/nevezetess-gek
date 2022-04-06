f=open("nevezetessegek.txt","r",encoding="utf8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split("-")
    nagylista.append(kislista)
f.close()
#évszámos
def asd12():
    bemenet=int(input("Adj meg egy évszámot: "))
    for i in range(0,len(nagylista)):
        if bemenet==int(nagylista[i][1]):
            print(nagylista[i][0])
#országos
def asd13():
    bemenet=input("Adj meg egy orszagot: ")
    for i in range(0,len(nagylista)):
        if bemenet==nagylista[i][0]:
            print(nagylista[i][1])
#nevezetességes
def asd14():
    for i in range(0,len(nagylista)):
        print(nagylista[i][2])
    nevezetes=input("kérlek add meg a nevezetesség nevét")
    for i in range(0,len(nagylista)):
        if nevezetes==nagylista[i][2]:
            print(nagylista[i][0])
            print(nagylista[i][1])

#menu rendszer
print("1. menupont","2. menupont","3. menupont","4.kilepes")
választás=input("add meg a menupont választott számjegyét")
while választás!="4":
        if választás=="1":
            asd12()
        if választás=="2":
            asd13()
        if választás=="3":
            asd14()
        else:
            print("nincs ilyen menupont")
        választás=input("add meg a menupont választott számjegyét")
       
