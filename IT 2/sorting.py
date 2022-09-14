import random

array1 = [3,1,2,5,4,2,4,5]

funcs = [selectionsort, bubblesort, quicksort]   #Må fikse.

for f in funcs:
    a = time()
    f(array1)
    print("Funksjonen ", f.__name__, "tok ", round(time()-a, 6), "sekunder å utføre.")

def selectionsort (inn):            #Funker
    for i in range(1,len(inn)-1):
        min = inn[i-1]
        index = i-1
        for j in range(i,len(inn)):
            if inn[j]<min:
                min = inn[j]
                index = j
        inn.insert(i-1, inn.pop(index))
    return inn

def bubblesort (inn):               #Funker
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(inn)-1):
            if inn[i] > inn[i+1]:
                inn[i], inn[i+1] = inn[i+1], inn[i]
                sorted = False
    return inn

"""
def quicksort (inn, low, high):             #Funker ikke
    if low < high:
        pi = partition(inn, low, high)
        quicksort(inn, low, pi-1)
        quicksort(inn, pi+1, high)

def partition (inn, low, high):
    pivot = inn[high]
    i = low - 1
    for j in range(low, high-1):
        if inn[j]<pivot:
            i += 1
            inn[i], inn[j] = inn[j], inn[i]
    inn[i+1], inn[high] = inn[high], inn[i+1]
    return i+1 """


def quicksort (array_inn):
    if len(array_inn) < 1:
        return array_inn
    pivot = array_inn[random.randint(0,len(array_inn)-1)]
    low = []
    mid = []
    high = []
    for element in array_inn:
        if element < pivot:
            low.append(element)
        elif element > pivot:
            high.append(element)
        else:
            mid.append(element)
    low = quicksort(low)
    high = quicksort(high)
    array_inn = low+mid+high
    return array_inn


#def mergesort (inn):

#Binary search

#Rekursiv funksjon for primtallsfaktorisering.

print(quicksort(array1))