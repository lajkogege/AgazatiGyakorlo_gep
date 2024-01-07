def elso_feladat():
    muzeum_neve:str=str(input("Add meg a múzeum nevét: "))
    latogato_neve:str=str(input("Add meg a látogató nevét: "))
    ertekeles:int=int(input("Add meg az értékelést: "))
    print("I/A:")
    print(f"\tMúzeum neve: {muzeum_neve}")
    print(f"\tLátogató neve: {latogato_neve}")
    print(f"\tÉrtékelés (1-20): {ertekeles}")
    print("I/B")
    if ertekeles ==0 or ertekeles<0:
        print("Az érétkelés nem lehet negatív")
    elif ertekeles>20 :
        print("20 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést! ")


