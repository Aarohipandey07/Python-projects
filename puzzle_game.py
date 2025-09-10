import random

print("welcome to the alphabet puzzle game!")
print("try to guess the word from A to Z")

# generate the word puzzle
guess=0
attempt=5
print(f"you have {attempt} attempts to guess the word correctly.\n")

def display_puzzle(words):
   
   

   while attempt>0:
    guess=input("enter your guess: ")
    display_puzzle()

