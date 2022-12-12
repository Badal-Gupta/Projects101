print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("Enter your age: "))
  if age > 12 and age < 18 :
    bill = 7
    print("Youth ticket are $7.")
  elif age < 12:
    bill = 5
    print("Child ticket are $5.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. You can ride for     free")
  else:
    bill = 12
    print("Adult ticket are $12.")
  photo = input("Do you want a photo taken? Y or N. ")
  if photo == 'Y':
    bill += 3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")
