print("to quit game enter 0")

number = 50
guess = 0
attempt = 0


while  True:
  guess = int(input("Guess a number: "))

  if guess == 0 :
    print("You loose!")
    break
  
  if guess == number:
    print(f"You gussed it right! in {attempt} attempts")
    break
  
  attempt += 1


