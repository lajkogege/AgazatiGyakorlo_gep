import minosites
minosites.elso_feladat()

import sorozat
print("II/A.B.C")
listam=sorozat.veletlen_szamok()
kiiras=sorozat.konzolra(listam)

print("II/D,E")
tizzel=sorozat.oszthatok_szama(listam)
kiir=sorozat.konzolra_ir(tizzel)

print("II/F:")
tizzel=sorozat.oszthatok_szama(listam)
fajlba=sorozat.fajl_ir(tizzel)

import Beolvas
print("III/A,B:")
osztaly_listam=Beolvas.fajlbeolvas()
print(f"\tA gépek száma: {len(osztaly_listam)}")

print(f"III/C:")
atlag=Beolvas.atlag(osztaly_listam)
print(f"\tA páros teremszámú termek átlaga: {atlag}")

print("III/D:")
index=Beolvas.legkisebb(osztaly_listam)
print(f"\tA legkisebb asztali gép azonositoja: {osztaly_listam[index].id}, helye: {osztaly_listam[index].hely}")
