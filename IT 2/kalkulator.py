# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:00:25 2022

@author: eiaaa001
"""

import re
import operator

ops = {                 #Bibliotek for å konvertere operatorer i stringformat til vanlige operatorer
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

print("Kalkolatoren godtar operatorene */+-, og regner ut med så mange ledd du ønsker, i riktig regnerekkefølge. Du kan ikke starte regnestykket med en operator, og du kan heller ikke ha to operatorer stående etter hverandre. Du kan heller ikke benytte deg av parenteser.")
equ = input("Skriv inn regnestykket her:")

def solve (equinn):                                 #Funksjon for utregning
    array_oper = re.findall("[+*/\-]", equinn)      #Finner tall og operatorer, og splitter i to arrayer
    array_numb = re.split("[+*/\-]", equinn.replace(' ', '').replace(',','.'))
    i = 0
    while (i < len(array_oper)):            #Setter først sammen tall det står * eller / mellom 
        if (array_oper[i] in ["*","/"]):
            nyttall = ops[array_oper[i]](float(array_numb[i]), float(array_numb[i+1]))
            del array_numb[i]
            del array_numb[i]
            del array_oper[i]
            array_numb.insert(i,nyttall)
        else:
            i += 1
    j = 0
    while (j < len(array_oper)):            #Setter sammen tall det står + eller - mellom 
        if (array_oper[j] in ["+","-"]):
            nyttall = ops[array_oper[j]](float(array_numb[j]), float(array_numb[j+1]))
            del array_numb[j]
            del array_numb[j]
            del array_oper[j]
            array_numb.insert(j,nyttall)
        else:
            j += 1
    print(array_numb[0])        #Printer tallet som står igjen i arrayen med tall
    
    
solve(equ)


#Liste med alle regneoperasjonene i riktig rekkefølge