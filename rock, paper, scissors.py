import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user = input("What do you choose? Type 0 for rock, 1 for paper or 2 for sciccors.\n")
l1 = [rock,paper,scissors]
random1 = random.randint(0,2)
if user == '0':
  print(rock)
  print(random1)
  if random1 == 0:
    print(rock+"\n It's a draw")
  elif random1 == 1:
    print(paper+"\n You loose")
  else:
    print(scissors+"\n You win")
elif user == '1':
  print(paper)
  if random1 == 0:
    print(rock+"\n You win")
  elif random1 == 1:
    print(paper+"\n It's a draw")
  else:
    print(scissors+"\n You loose")
else:
  print(scissors)
  if random1 == 0:
    print(rock+"\n You win")
  elif random1 == 1:
    print(paper+"\n You loose")
  else:
    print(scissors+"\n It's a draw")
