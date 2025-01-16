# HIT 137 Software Now 

# Assignment 2

# Group: CAS/DAN 21
# Abu Saeed Md Shafiqur Rahman (Shafiq Rahman) - S386795
# Annafi Bin Alam (Rafin Alam) - S387086
# Neville James Doyle (Nev Doyle) - S371207
# Yuvraj Singh (Yuvraj Singh) - S383324

# GitHub Repository: https://github.com/shafiqsaeed/HIT137-G21-Asign2

# Submitted: 17 January 2025


import turtle

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left branch
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Return to the original position
    t.right(angle_left + angle_right)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Return to the starting angle
    t.left(angle_right)
    t.backward(branch_length)

def main():
    try:
        # Get parameters from the user
        angle_left = float(input("Enter the left branch angle (in degrees): "))
        angle_right = float(input("Enter the right branch angle (in degrees): "))
        branch_length = float(input("Enter the starting branch length: "))
        depth = int(input("Enter the recursion depth: "))
        reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

        if branch_length <= 0 or depth <= 0 or reduction_factor <= 0 or reduction_factor >= 1:
            print("Error: Ensure all inputs are positive and the reduction factor is between 0 and 1.")
            return

        # Set up the turtle graphics environment
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Recursive Tree Pattern")

        t = turtle.Turtle()
        t.speed(0)
        t.left(90)  # Start facing upward
        t.penup()
        t.goto(0, -250)  # Move to the base of the screen
        t.pendown()

        # Draw the tree
        draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor)

        # Finish
        screen.mainloop()

    except ValueError:
        print("Error: Please enter valid numeric values.")

main()