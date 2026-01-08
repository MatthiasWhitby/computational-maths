"""
Contains all the code for the problem-solving framework
"""

def main():
    prob = input("Enter your problem >>> ")
    print_framework(prob)

def print_framework(problem):
    print(f"Your problem: '{problem}")
    print("1. Fully understand the problem.")
    print("2. Identify aspects (variables/sections).")
    print("3. Choose a method for solving the problem.")
    print("4. Implement a solution.")
    print("5. Verify the solution.")

main()