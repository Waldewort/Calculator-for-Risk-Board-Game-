import random
import time 
def würfeln():
    return random.randint(1,6)

def normalwürfeln():
    x = [würfeln(), würfeln(), würfeln()]
    x.sort()
    #print("Angreifer: ", x)
    y = [würfeln(), würfeln()] 
    y.sort()
    #print("Verteidiger: ", y)
    return x, y 


a = a1 = int(input("Anzahl Angreifer: "))
v = v1 = int(input("Anzahl Verteidiger: "))
ü = int(input("Anzahl der Angreifer die übrig bleiben sollen: "))
i = 1 
t1 = time.time()

while a > ü and v > 0:
    if a >=3 and v >=2:
        #print("Runde: ", i)
        x, y = normalwürfeln()
        if x[1] > y[0]:
            v -= 1
            #print("Verteidiger verliert 1 Soldat: ", v)
        elif x[1] <= y[0]:
            a -= 1
            #print("Angreifer verliert 1 Soldat: ", a)
    
        if x[2] > y[1]:
            v -= 1
            #print("Verteidiger verliert 1 Soldat: ", v)
        elif x[2] <= y[1]:
            a -= 1
            #print("Angreifer verliert 1 Soldat: ", a)
        i += 1
    if v < 2 and v > 0:
        if a >= 3:
            x = [würfeln(), würfeln(), würfeln()]
            x.sort()
            #print("Angreifer: ", x)
            z = 3
        if a == 2:
            x = [würfeln(), würfeln()]
            x.sort()
            #print("Angreifer: ", x)
            z = 2
        if a == 1:
            x = [würfeln()]
            #print("Angreifer: ", x)
            z = 1 
        y = [würfeln()]
        #print("Verteidiger: ", y)

        if x[z-1] > y[0]:
            v -= 1
            #print("Verteidiger verliert letzten Soldat: ", v)
        elif x[z-1] <= y[0]:
            a -= 1
            #print("Angreifer verliert 1  Soldat: ", a)
   
    if a < 3 and a > 0:
        if v >= 2:
            y = [würfeln(), würfeln()]
            y.sort()
            #print("Verteidiger: ", y)
            z = 2
        if v == 1:
            y = [würfeln()]
            #print("Verteidiger: ", y)
            z = 1 
        if a == 2:
            x = [würfeln(), würfeln()]
            x.sort()
            #print("Angreifer: ", x)
            z1 = 2
        if a == 1:
            x = [würfeln()]
            x.sort()
            #print("Angreifer: ", x)
            z1 = 1
        #Comparison of the last attacking soldiers
        if x[z1-1] > y[z-1]:
            v -= 1
            #print("Verteidiger verliert 1 Soldat: ", v)
        elif x[z1-1] <= y[z-1]:
            a -= 1
            if a == 0:
                #print("Angreifer verliert letzten Soldat: ", a)
                pass
            else:
                #print("Angreifer verliert den vorletzten Soldat: ", a)
                pass

verhältnis = (a1-a)/(v1-v)
print("Es bleiben, ", a, " Angreifer übrig")
print("Es bleiben, ", v, " Verteidiger übrig")
print("Rechenzeit: ", time.time()-t1 , " Sekunden")
#print("Verhältnis der Verluste(1 = Ausgeglichen): ", verhältnis)