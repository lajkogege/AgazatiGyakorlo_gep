from Osztaly import Osztaly

def fajlbeolvas():
    fajl=open ("gep.txt","r", encoding="utf-8")
    fajl.readline()
    fajlbol_sorok_lista=fajl.readlines()
    fajl.close()
    osztaly_lista=[]
    for i in range(0,len(fajlbol_sorok_lista),1):
        aktelem=fajlbol_sorok_lista[i]
        sor_lista=aktelem.strip().split('!')
        osztalyom=Osztaly(int(sor_lista[0]), str(sor_lista[1]), str(sor_lista[2]), str(sor_lista[3]))
        osztaly_lista.append(osztalyom)
    return osztaly_lista

import math
def atlag(osztaly_lista):
    atlag:float=0
    db:int=0
    osszeg:int=0
    for i  in range(0,len(osztaly_lista),1):
        if osztaly_lista[i].id %2==0:
            osszeg=osszeg +osztaly_lista[i].id
            db+=1
    atlag=math.floor(osszeg/db)
    return atlag

def legkisebb(osztaly_lista):
    min:int=76
    index:int=0
    for i in range(0,len(osztaly_lista),1):
        if osztaly_lista[i].id <min:
            min= osztaly_lista[i].id
            index==i
    return index

