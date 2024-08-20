number = 50
guess = 0
attempt = 0


while guess != number:
  guess = int(input("Guess a number: "))
  attempt += 1

print(f"You gussed it right! in {attempt} attempts")