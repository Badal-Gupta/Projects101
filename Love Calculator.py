#love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_str = name1 + name2
lowercase_name = combined_str.lower()

t = lowercase_name.count('t')
r = lowercase_name.count('r')
u = lowercase_name.count('u')
e = lowercase_name.count('e')
total_true = t+r+u+e
l = lowercase_name.count('l')
o = lowercase_name.count('o')
v = lowercase_name.count('v')
e = lowercase_name.count('e')
total_love = l+o+v+e
str1 = str(total_true) + str(total_love)
str2 = int(str1)
if str2 < 10 or str2 > 90:
    print(f"Your score is {str1}, you go together like coke and mentos.")
elif str2 >= 40 and str2 <= 50:
    print(f"Your score is {str1}, you are alright together.")
else:
    print(f"Your score is {str1}.")