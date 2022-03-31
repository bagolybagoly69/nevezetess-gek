f=open("nevezetessegek.txt","r",encoding="utf8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split("-")
    nagylista.append(kislista)
f.close()

bemenet=int(input("Adj meg egy évszámot: "))
for i in range(0,len(nagylista)):
    if bemenet==int(nagylista[i][1]):
        print(nagylista[i][0])

bemenet=input("Adj meg egy orszagot: ")
for i in range(0,len(nagylista)):
    if bemenet==nagylista[i][0]:
        print(nagylista[i][1])

for i in range(0,len(nagylista)):
    print(nagylista[i][2])
nevezetes=input("kérlek add meg a nevezetesség nevét")
for i in range(0,len(nagylista)):
    if nevezetes==nagylista[i][2]:
        print(nagylista[i][0])
        print(nagylista[i][1])
    
