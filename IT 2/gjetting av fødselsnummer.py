print("Fødselsnummere er ikke sensitiv informasjon, men er noe som man likevel ønsker å holde personlig. Nummeret består av 11 sifre: 6 sifre som utgjør fødselsdatoen og 5 sifre kalt personnummeret. Disse 5 sifrene kan virke vilkårlige, men for de som ønsker å fåtak i andres personnummer bygger de heldigvis på et sett strenge regler. Vet man fødselsdato og kjønn kan antall fødselsnummre reduseres ned til 250 (rundt 210 i praksis). Dette programmet gjør nettopp dette.")
print("Skriv på formen: Kjønn:Mann/Kvinne Dag:XX Måned:XX Tiår: XX Årtusen: XX")
kjønn = input("Kjønn:")
dag = input("Dag:")
måned = input("Måned:")
tiår = input("Tiår:")
årtusen = input("Årtusen")

tallrekke1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
tallrekke2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

fødselsnummer = list((dag + måned + tiår).replace(' ',''))
muligheter = []


def finnnummere (inn):
    if int(årtusen) % 2 == 0:
        if kjønn.lower() == "mann":
            for i in range(501,999, 2):
                ctr_nr1 = inn.copy()
                ctr_nr1 += list(map(int, str(i)))
                ctr_nr1.append(0)
                for j in range(0,9):
                    ctr_nr1.pop()
                    ctr_nr1.append(j)
                    sum1 = 0
                    for k in range(0,len(tallrekke1)):
                        sum1 += tallrekke1[k] * int(ctr_nr1[k])
                    if int(sum1) % 11 == 0:
                        ctr_nr2 = ctr_nr1.copy()
                        ctr_nr2.append(0)
                        for l in range(0,9):
                            ctr_nr2.pop()
                            ctr_nr2.append(l)
                            sum2 = 0
                            for m in range(0,len(tallrekke2)):
                                sum2 += tallrekke2[m] * int(ctr_nr2[m])
                            if sum2 % 11 == 0:
                                muligheter.append(''.join(str(x) for x in ctr_nr2))
            for n in muligheter:
                print(n)
        else:
            for i in range(500,998, 2):
                ctr_nr1 = inn
                ctr_nr1.append(0)
                for j in range(0,9):
                    ctr_nr1.pop()
                    ctr_nr1.append(j)
                    sum1 = 0
                    for k in range(0,len(tallrekke1)-1):
                        sum1 += tallrekke1[k] * int(ctr_nr1[k])
                    if sum1 % 11 == 0:
                        ctr_nr2 = ctr_nr1
                        ctr_nr2.append(0)
                        for l in range(0,9):
                            ctr_nr2.pop()
                            ctr_nr2.append(l)
                            sum2 = 0
                            for m in range(0,len(tallrekke2)-1):
                                sum1 += tallrekke2[m] * int(ctr_nr1[m])
                            if sum2 % 11 == 0:
                                muligheter.append(''.join(str(x) for x in ctr_nr2)) 
            for n in muligheter:
                print(n)
finnnummere(fødselsnummer)
#http://www.fnrinfo.no/Info/Oppbygging.aspx

#morradi
#heihei