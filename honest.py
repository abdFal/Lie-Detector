import random

questions = [
    'Apakah kamu sudah sholat subuh hari ini?',
    'Kalo lagi dikamar mandi suka nyanyi',
    'Udah ga onani selama 6 bulan',
    'Kamu berbakti sama ortu',
    'Bosen ga sama hidup?',
]

# checking proccess
for q in questions:
    response = input(q + "(yes or no)").lower()
    if response == "yes":
        answer = True
    else:
        answer = False
        
    honest_or_lie = bool(random.getrandbits(1))
    if answer == honest_or_lie:
        print("You lie!")
    else:
        print("You honest!")

#this is only for fun guys:)