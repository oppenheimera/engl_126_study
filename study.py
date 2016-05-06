import nltk
from nltk.tokenize import sent_tokenize
import random

lifted_veil = [sent_tokenize(open('lifted_veil.txt').read())]
lifted_veil += ["The Lifted Veil"]
sign_four = [sent_tokenize(open('sign_four.txt').read())]
sign_four += ["The Sign of the Four"]
howards_end = [sent_tokenize(open('howards_end.txt').read())]
howards_end += ["Howard's End"]
good_soldier = [sent_tokenize(open('good_soldier.txt').read())]
good_soldier += ["The Good Soldier"]
lord_jim = [sent_tokenize(open('lord_jim.txt').read())] 
lord_jim += ["Lord Jim"]
ulysses = [sent_tokenize(open('ulysses.txt').read())]
ulysses += ["Ulysses"]
watt = [sent_tokenize(open('watt.txt').read())]
watt += ["Watt"]
waves = [sent_tokenize(open('waves.txt').read())]
waves += ["Waves"]


source = [lifted_veil, sign_four, lord_jim, howards_end, good_soldier, ulysses, watt]
variables = {0: "The Lifted Veil", 1: "The Sign of the Four", 2: "Lord Jim", 
             3: "Howard's End", 4: "The Good Soldier", 5: "Ulysses", 6: "Waves", 
             7: "Watt"}

safe_advance = lambda n, length: (n + 1) % length
randint = lambda low, high: random.randint(low, high)

def corpus_generator(text, no_sent):
    """takes in a tokenized corpus and returns a random
    sampling of that corpus"""
    length = len(text[0]) - 1
    start_pt = randint(0, length - 1)
    pararaph = ""
    for x in range(no_sent):
        pararaph += text[0][start_pt] + " "
        start_pt = safe_advance(start_pt, length)
    return pararaph

while True:
    novel = source[randint(0, len(source) - 1)]
    text = corpus_generator(novel, 5)    

    print(text + "\n")
    print("In which of the following novels does the passage appear?")
    print("0) The Lifted Veil\n1) Sign of the Four \n2) Lord Jim \
         \n3) Howard's End\n4) The Good Soldier\n5) Ulysses \n6) The Waves \n7) Watt")
    answer = input(">>> ")
    if answer == 'q':
        exit()
    answer = int(answer)
    if variables[answer] == novel[-1]:
        print("Correct!\n")
    else:
        print("Nice try, but it's actually " + novel[1] + "\n")

