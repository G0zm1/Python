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
    _________
---'   _______)
          _________)
          ___________)
         __________)
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

computer_arsenal = [rock, paper, scissors]
computer_pick = random.choice(computer_arsenal)
user_input = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors?: "))



if user_input == 0 and computer_pick == computer_arsenal[2]:
    print(rock +"\nComputer chose:\n" + scissors + "You won!")
elif user_input == 0 and computer_pick == computer_arsenal[0]:
    print(rock +"\nComputer chose:\n" + rock + "It's a draw!")
elif user_input == 0 and computer_pick == computer_arsenal[1]:
    print(rock +"\nComputer chose:\n" + paper + "You lose!")

elif user_input == 1 and computer_pick == computer_arsenal[2]:
    print(paper + "\nComputer chose:\n" + scissors + "You lose!")
elif user_input == 1 and computer_pick == computer_arsenal[0]:
    print(paper + "\nComputer chose:\n" + rock + "You won!")
elif user_input == 1 and computer_pick == computer_arsenal[1]:
    print(paper + "\nComputer chose:\n" + paper + "It's a draw!")

elif user_input == 2 and computer_pick == computer_arsenal[2]:
    print(scissors + "\nComputer chose:\n" + scissors + "It's a draw!")
elif user_input == 2 and computer_pick == computer_arsenal[0]:
    print(scissors + "\nComputer chose:\n" + rock + "You lose!")
elif user_input == 2 and computer_pick == computer_arsenal[1]:
    print(scissors + "\nComputer chose:\n" + paper + "You won!")

else:
    print("You have to choose 0, 1 or 2!")

