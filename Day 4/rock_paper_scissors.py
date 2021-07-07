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
      (____)2
---.__(___)
'''
game = [rock, paper, scissors]
human_choice = int(input("Choose any one: 0 for rock, 1 for paper, 2 for scissors \n"))
print(game[human_choice])
computer_choice = random.randint(0, 2)
print(game[computer_choice])
if human_choice == 0 and computer_choice == 2:
    print("Win the match!")
elif computer_choice == 0 and human_choice == 2:
    print("Lost the match!")
elif human_choice > computer_choice:
    print("Win the match!")
elif computer_choice > human_choice:
    print("lost the match!")
elif human_choice == computer_choice:
    print("Match draw!")
