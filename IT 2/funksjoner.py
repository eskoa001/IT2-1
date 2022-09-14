import math

string = "abcba"


def telltegn(tekst: str) -> int:
    """
    Funksjonen tar en string som argumentog returnerer antall tegn som et heltall
    """
    return len(tekst.replace(" ", ""))

def returnermidt(tekst: str) -> str:
    """
    Funksjonen tar en string som argument og returnerer den midterste karakteren. Hvis antall tegn er et partall, returneres de to midterste.
    """
    if len(tekst) % 2 == 0:
        midt = int(math.floor((len(tekst) - 1) / 2))
        return tekst[midt] + tekst[midt + 1]
    else:
        midt = int((len(tekst) - 1) / 2)
        return tekst[midt]



def sjekkpalindrom (tekst: str) -> bool:
    """
    Funksjonen tar en string som et argument, og sjekker om den er et palindrom eller ikke. Den returnerer true/false.
    """
    if len(tekst) % 2 == 0:
        midt = int(len(tekst) / 2)
    else:
        midt = int((len(tekst) - 1) / 2)
    palindrom = True
    for i in range(0, midt):
        if tekst[i] != tekst[len(tekst) - 1 - i]:
            palindrom = False
    return palindrom




print(telltegn(string))
print(returnermidt(string))
print(sjekkpalindrom(string))