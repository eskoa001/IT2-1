# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:58:03 2022

@author: eiaaa001
"""

#if array i lenght == 1, add "00"+i, else if array from i lenght == 2, add "0"+i, else add i.

print("Fødselsnummere er ikke sensitiv informasjon, men er noe som man likevel ønsker å holde personlig. Nummeret består av 11 sifre: 6 sifre som utgjør fødselsdatoen og 5 sifre kalt personnummeret. Disse 5 sifrene kan virke vilkårlige, men for de som ønsker å fåtak i andres personnummer bygger de heldigvis på et sett strenge regler. Vet man fødselsdato og kjønn kan antall fødselsnummre reduseres ned til 250 (rundt 210 i praksis). Dette programmet gjør nettopp dette.")
print("Skriv på formen: Kjønn:Mann/Kvinne Dag:XX Måned:XX Tiår: XX Årtusen: XX")
kjønn = input("Kjønn: ")
dag = input("Dag: ")
måned = input("Måned: ")
tiår = input("Tiår: ")
årtusen = input("Årtusen: ")

fødselsnummer = list((dag + måned + tiår).replace(' ','')) #Lager array av fødselsnummeret

muligheter = []
spenn = [0]

def århundre_og_kjønn (fødselsnummer): #Sjekker kjønn og om personen er født i odde- eller partallsårhundre.
    global spenn
    if int(årtusen) % 2 == 0:
        if kjønn.lower() == "mann":
            spenn = [501, 1000]
        else:
            spenn = [500, 999]
    else:
        if kjønn.lower() == "mann":
            spenn = [1, 500]
        else:
            spenn = [0, 499]
    treførste(fødselsnummer)
    for n in muligheter:
        print(n)
    print("Antall mulige fødsellsnumre er: ",len(muligheter))


def treførste (nummerinn): #Går gjennom alle mulige kombinasjoner av de tre første sifrene.
    for i in range(spenn[0],spenn[1], 2):
        treførste = nummerinn.copy()
        if len(list(map(int, str(i)))) == 1:
            treførste += [0,0] + list(map(int, str(i))) ####FIKS
        elif len(list(map(int, str(i)))) == 2:
            treførste += [0] + list(map(int, str(i)))    ####FIKS        
        else:
            treførste += list(map(int, str(i))) ####FIKS
        ctr_1(treførste)
    
    


def ctr_1 (ferdig0): #Sjekker mulige 1. kontrollsifre
    tallrekke1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
    ctr_nr1 = ferdig0.copy()
    ctr_nr1.append(0)
    for j in range(0,10):
        ctr_nr1.pop()
        ctr_nr1.append(j)
        sum1 = 0
        for k in range(0,len(tallrekke1)):
            sum1 += tallrekke1[k] * int(ctr_nr1[k])
        if int(sum1) % 11 == 0:
            ctr_2(ctr_nr1)


def ctr_2 (ferdig1): #Sjekker mulige 2. kontrollsiffer
    tallrekke2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    ctr_nr2 = ferdig1.copy()
    ctr_nr2.append(0)
    for l in range(0,10):
        ctr_nr2.pop()
        ctr_nr2.append(l)
        sum2 = 0
        for m in range(0,len(tallrekke2)):
            sum2 += tallrekke2[m] * int(ctr_nr2[m])
        if sum2 % 11 == 0:
            muligheter.append(''.join(str(x) for x in ctr_nr2))
            
århundre_og_kjønn(fødselsnummer)