'''
This project is about rock paper scissors game between user and computer
'''
import random


def user_comp_points(user_choice, comp_choice, user_points, comp_points):
    if (user_choice == "rock" and comp_choice == "scissors") or \
            (user_choice == "paper" and comp_choice == "rock") or \
            (user_choice == "scissors" and comp_choice == "paper"):
        user_points += 1
    elif user_choice == comp_choice:
        # No points for user or computer
        pass
    else:
        comp_points += 1
    return user_points, comp_points


items = ["rock", "paper", "scissors"]
user_points, comp_points = 0, 0
while True:
    user_choice = input("Enter a choice: ")
    if user_choice not in items:
        print("Invalid choice ! Please try again.")
        continue
    comp_choice = random.choice(items)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
    user_points, comp_points = user_comp_points(
        user_choice, comp_choice, user_points, comp_points
    )
    print(f"Current points: User = {user_points}, Computer = {comp_points}")
    if user_points == 10:
        print("User won !!")
        break
    elif comp_points == 10:
        print("Computer won !!")
        break
