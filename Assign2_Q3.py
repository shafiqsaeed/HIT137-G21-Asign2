# HIT 137 Software Now 

# Assignment 2

# Group: CAS/DAN 21
# Abu Saeed Md Shafiqur Rahman (Shafiq Rahman) - S386795
# Annafi Bin Alam (Rafin Alam) - S387086
# Neville James Doyle (Nev Doyle) - S371207
# Yuvraj Singh (Yuvraj Singh) - S383324

# GitHub Repository: https://github.com/shafiqsaeed/HIT137-G21-Assign2

# Submitted: 17 January 2025

# Question 3 - Turtle Tree
# This program draws a tree using recursive function of Python's Turtle graphics based on user inputs.


import turtle

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor, thickness, is_brown):
    if depth == 0:
        return

    # Set the colour and thickness for the current branch
    if is_brown:
        t.color("brown")
    else:
        t.color("green")
    t.pensize(thickness)

    # Draw the current branch
    t.pendown()  # Ensure drawing is enabled
    t.forward(branch_length)
    t.penup()  # Stop drawing after the branch to avoid overlapping

    # Move to draw the left branch
    t.left(angle_left)
    draw_branch(
        t,
        branch_length * reduction_factor,
        angle_left,
        angle_right,
        depth - 1,
        reduction_factor,
        max(1, thickness - 3),  # Reduce thickness for next level
        False,  # All child branches are green
    )
    t.right(angle_left)  # Restore heading

    # Move to draw the right branch
    t.right(angle_right)
    draw_branch(
        t,
        branch_length * reduction_factor,
        angle_left,
        angle_right,
        depth - 1,
        reduction_factor,
        max(1, thickness - 3),  # Reduce thickness for next level
        False,  # All child branches are green
    )
    t.left(angle_right)  # Restore heading

    # Return to the base of the branch
    t.backward(branch_length)

# Setup the screen and turtle
def main():
    # Get user input
    angle_left = int(input("Enter the left branch angle (e.g., 20): "))
    angle_right = int(input("Enter the right branch angle (e.g., 25): "))
    starting_length = int(input("Enter the starting branch length (e.g., 100): "))
    recursion_depth = int(input("Enter the recursion depth (e.g., 5): "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))
        
    # Create the turtle environment and object
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Turtle Tree by Group21")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)  # Start at the bottom of the screen
    t.pendown()
    t.setheading(90)  # Point upwards

    # Draw the tree
    draw_branch(t, starting_length, angle_left, angle_right, recursion_depth, reduction_factor, 15, True)

    t.hideturtle()

    # Keep the window open until clicked
    screen.exitonclick()


main()
