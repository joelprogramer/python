import random

print("\n---------------------------\n")
print(".:GissaTalet:.")

print("Gissa ett tal mellan 1-10, du får 3 försök!\n")
slumptal = random.randint(1,10)
print(slumptal)
i = 0
hittat = False
#loop
while i < 3:
    gissatal =input ("mata in tal: ")
    
    if slumptal == int(gissatal):
        hittat = True
        print("\n rätt svar! \n")
        break
    
    i = 1
    if hittat :
        print("\n Bra jobbat, du får en miljon")
    else :
        print("\n YOU FUCKING WANKER!!")
    


if hittat :
    print("\n Bra jobbat, du får en miljon")
    
else :
    print("\n YOU FUCKING WANKER!")
    
print("\n-----------")