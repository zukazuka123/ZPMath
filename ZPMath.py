#* Copyright (C) Zurab Phertsuliani - All Rights Reserved
#* Unauthorized copying of this file, via any medium is strictly prohibited
#* Proprietary and confidential
#* Written by Zurab Phertsuliani <zurab.pertsuliani23@gmail.com>

import time
import platform
import subprocess
import sympy
import matplotlib.pyplot as plt
import numpy as np

def clear_screen():
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.call(command, shell=True)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid number.")

def lineareq():
    print("Linear equation: ax + b")
    a = get_float("\nEnter the value for a: ")
    b = get_float("Enter the value for b: ")
    if a == 0:
        print("The value of a cannot be 0 for a linear equation.")
        return
    x_intercept = -b / a
    y_intercept = b
    print("\nThe x-intercept's coordinates are:", (x_intercept, 0))
    print("The y-intercept's coordinates are:", (0, y_intercept))
    print("Domain: Real numbers (R)")
    plot_choice = input("Would you like to plot this equation? (yes/no): ").strip().lower()
    if plot_choice == 'yes':
        plot_linear(a, b)

def quadraticeq():
    print("Quadratic equation: ax^2 + bx + c")
    a = get_float("Enter the value for a: ")
    b = get_float("Enter the value for b: ")
    c = get_float("Enter the value for c: ")
    if a == 0:
        print("The value of a cannot be 0 for a quadratic equation.")
        return
    x = sympy.Symbol("x")
    roots = sympy.solve(a*x**2 + b*x + c, x)
    vertex = -b / (2*a)
    expression = sympy.sympify(a*x**2 + b*x + c)
    print("The possible factored version is:", sympy.factor(expression))
    print("The x-intercept's coordinates are:", [(root.evalf(), 0) for root in roots])
    print("The y-intercept's coordinates are:", (0, c))
    print("The vertex's coordinates are:", (vertex, a*vertex**2 + b*vertex + c))
    if all(root.is_real for root in roots):
        print("Domain: Real numbers (R)")
    elif any(root.is_imaginary for root in roots):
        print("Domain: Complex numbers (C)")
    else:
        print("Domain: Decimal numbers (D)")
    plot_choice = input("Would you like to plot this equation? (yes/no): ").strip().lower()
    if plot_choice == 'yes':
        plot_quadratic(a, b, c)

def cubiceq():
    print("Cubic equation: ax^3 + bx^2 + cx + d")
    a = get_float("Enter the value for a: ")
    b = get_float("Enter the value for b: ")
    c = get_float("Enter the value for c: ")
    d = get_float("Enter the value for d: ")
    if a == 0:
        print("The value of a cannot be 0 for a cubic equation.")
        return
    x = sympy.Symbol("x")
    roots = sympy.solve(a*x**3 + b*x**2 + c*x + d, x)
    expression = sympy.sympify(a*x**3 + b*x**2 + c*x + d)
    print("The possible factored version is:", sympy.factor(expression))
    print("The x-intercept's coordinates are:", [(root.evalf(), 0) for root in roots])
    print("The y-intercept's coordinates are:", (0, d))
    if all(root.is_real for root in roots):
        print("Domain: Real numbers (R)")
    elif any(root.is_imaginary for root in roots):
        print("Domain: Complex numbers (C)")
    else:
        print("Domain: Decimal numbers (D)")
    plot_choice = input("Would you like to plot this equation? (yes/no): ").strip().lower()
    if plot_choice == 'yes':
        plot_cubic(a, b, c, d)

def plot_linear(a, b):
    x = np.linspace(-10, 10, 400)
    y = a*x + b
    plt.plot(x, y, label=f'{a}x + {b}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.title('Linear Equation Plot')
    plt.show()

def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.title('Quadratic Equation Plot')
    plt.show()

def plot_cubic(a, b, c, d):
    x = np.linspace(-10, 10, 400)
    y = a*x**3 + b*x**2 + c*x + d
    plt.plot(x, y, label=f'{a}x^3 + {b}x^2 + {c}x + {d}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.title('Cubic Equation Plot')
    plt.show()

def main_menu():
    clear_screen()
    print("--------------------------")
    print("-                        -")
    print("-    By Zurab            -")
    print("-        V3.0            -")
    print("-                        -")
    print("--------------------------\n")

    menu_items = {
        '1': "Analysis of linear equation",
        '2': "Analysis of quadratic equation",
        '3': "Analysis of cubic equation",
        '4': "Exit the program"
    }

    for key, value in menu_items.items():
        print(f"{key}) {value}")
    choice = input("Enter your choice: ")
    return choice

def main():
    try:
        while True:
            choice = main_menu()
            if choice == '1':
                lineareq()
            elif choice == '2':
                quadraticeq()
            elif choice == '3':
                cubiceq()
            elif choice == '4':
         
