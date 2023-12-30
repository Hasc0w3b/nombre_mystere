
import random 
from random import randint

nombre_mystere = random.randint (0, 100)
a = 0

while (a != nombre_mystere ):

    a = int(input("demander a l'utilisateur"))
    if (a > 100):
        print ("ta mere la pute to nombre choisis est superieur a 100 ")
    elif (a < nombre_mystere ):
         print ("votre nombre est trop petit") 
    elif (a > nombre_mystere):
         print("votre nombre est trop grand")
    else:
         print ("votre nombre est correct")
