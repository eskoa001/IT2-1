tallrekke1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
tallrekke2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

print("Programmet vil kontrollere om de to siste siffrene stemmer")
inn = input("Skriv inn fødselsnummeret ditt her:")

def verifiser (fødselsnummer):
    array = list(fødselsnummer.replace(' ',''))
    sum = 0
    for i in range(0, len(tallrekke1)):
        sum += int(fødselsnummer[i]) * tallrekke1[i]
    if sum % 11 == 0:
        sum = 0
        for j in range(0, len(tallrekke2)):
            sum += int(fødselsnummer[j]) * tallrekke2[j]
        if sum % 11 == 0:
            print("Fødselsnummeret er gyldig.")
        else:
            print("Fødselsnummeret er ikke gyldig.")
    else:
        print("Fødselsnummeret er ikke gyldig.")

verifiser(inn)