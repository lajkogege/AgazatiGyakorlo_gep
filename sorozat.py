import random


def veletlen_szamok():
    lista=[]
    for i in range(0,15,1):
        szam:int=random.randint(-90,500)
        lista.append(szam)
    return lista

def konzolra(lista):
    for i in range (0,len(lista),1):
        if i == len(lista)-1:
            print(lista[i])
        else:
            print(lista[i], end="*")


def oszthatok_szama(lista):
    tizzel_soztahtok_szama:int=0
    for i in range (0,len(lista),1):
        if lista[i] %10 ==0:
            tizzel_soztahtok_szama+=1
    return tizzel_soztahtok_szama

def konzolra_ir(tizzel_soztahtok_szama):
    print(f"\tTizzel oszthatok száma: {tizzel_soztahtok_szama}")


def fajl_ir(tizzel_soztahtok_szama):
    fajlnev:str="kimutatas.txt"
    print(f"\tTizzel osztható számok száma: {tizzel_soztahtok_szama}")
    f=open("kimutatas.txt", "w", encoding="utf-8")
    f.write (f"\tTizzel osztható számok száma: {tizzel_soztahtok_szama}")
    f.close()


