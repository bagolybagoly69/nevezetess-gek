f = open("nevezetessegek.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    #print(sor)
    kislista=sor[:-1].split("-")
    #print(kislista)
    nagylista.append(kislista)
f.close()
ans=True
print("""1.menü
2.menü
3.menü""")

while True:
    try:
        ans=int(input("Melyik menupont kell?" ))
        if ans==1: 
            print("elso menupont")
            break
        elif ans==2:
            print("masodik menupont")
            break
        elif ans==3:
            print("harmadik menupont")
            break
        elif ans==4:
            print("anyád:DDD")
            break

    except ValueError:
        print("hibás érték")
##nemethdani :D
