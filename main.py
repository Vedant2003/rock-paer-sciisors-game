rocks = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papers= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissorss = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image=[rocks,papers,scissorss]
n1="rock"
n2="paper"
n3="scissors"
name=[n1,n2,n3]
import random
comp=random.randint(0,2)
user=int(input("please enter the number betwwen 0-2 for playing this  0 for rock,1 for paper,2 for siccor\n"))
if user>=3 or user<0:
    print("Invalid choice")
else:
  print(image[user])
  print(name[user])
  print(image[comp])
  print(name[comp])
  if comp>user:
      print("You lose")
  elif user>comp:
      print("You win!")
  elif user==comp:
      print("its a draw")
  elif user==2 and comp==0:
      print("You loose")
  elif user==0 and comp==2:
     print("You win!")

