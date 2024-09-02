import time
import platform
import subprocess
import sympy
import matplotlib.pyplot as plt
import numpy as np
import logging
from tkinter import Tk, Label, Button, messagebox, simpledialog

# Configure logging
logging.basicConfig(filename='equation_solver.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def clear_screen():
    """Clears the console screen based on the operating system."""
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.call(command, shell=True)


def plot_equation(x, y, title, xlabel='x', ylabel='y', legend_label=None):
    """General plotting function for various equations."""
    plt.plot(x, y, label=legend_label)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    if legend_label:
        plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


class EquationSolver:
    """Class to handle various equation analyses and plotting."""

    def __init__(self):
        self.x_range = (-10, 10)
        self.num_points = 400

    def lineareq(self, a, b):
        """Handles the processing of a linear equation of the form ax + b."""
        if a == 0:
            raise ValueError("The value of a cannot be 0 for a linear equation.")
        x_intercept = -b / a
        y_intercept = b
        result = f"Linear Equation: y = {a}x + {b}\n" \
                 f"X-Intercept: ({x_intercept}, 0)\n" \
                 f"Y-Intercept: (0, {y_intercept})\n" \
                 "Domain: Real numbers (R)\n"
        return result, sympy.Eq(a * sympy.Symbol('x') + b, 0)

    def quadraticeq(self, a, b, c):
        """Handles the processing of a quadratic equation of the form ax^2 + bx + c."""
        if a == 0:
            raise ValueError("The value of a cannot be 0 for a quadratic equation.")
        x = sympy.Symbol("x")
        roots = sympy.solve(a * x ** 2 + b * x + c, x)
        vertex = -b / (2 * a)
        y_vertex = a * vertex ** 2 + b * vertex + c
        expression = sympy.sympify(a * x ** 2 + b * x + c)
        factored_form = sympy.factor(expression)
        domain = "Real numbers (R)" if all(root.is_real for root in roots) else "Complex numbers (C)"
        result = f"Quadratic Equation: y = {a}x^2 + {b}x + {c}\n" \
                 f"Factored Form: {factored_form}\n" \
                 f"X-Intercepts: {[(root.evalf(), 0) for root in roots]}\n" \
                 f"Y-Intercept: (0, {c})\n" \
                 f"Vertex: ({vertex}, {y_vertex})\n" \
                 f"Domain: {domain}\n"
        return result, expression

    def cubiceq(self, a, b, c, d):
        """Handles the processing of a cubic equation of the form ax^3 + bx^2 + cx + d."""
        if a == 0:
            raise ValueError("The value of a cannot be 0 for a cubic equation.")
        x = sympy.Symbol("x")
        roots = sympy.solve(a * x ** 3 + b * x ** 2 + c * x + d, x)
        expression = sympy.sympify(a * x ** 3 + b * x ** 2 + c * x + d)
        factored_form = sympy.factor(expression)
        domain = "Real numbers (R)" if all(root.is_real for root in roots) else "Complex numbers (C)"
        result = f"Cubic Equation: y = {a}x^3 + {b}x^2 + {c}x + {d}\n" \
                 f"Factored Form: {factored_form}\n" \
                 f"X-Intercepts: {[(root.evalf(), 0) for root in roots]}\n" \
                 f"Y-Intercept: (0, {d})\n" \
                 f"Domain: {domain}\n"
        return result, expression

    def exponentialeq(self, a, b):
        """Handles the processing of an exponential equation of the form a * b^x."""
        domain = "Real numbers (R)" if b > 0 else "Complex numbers (C)"
        result = f"Exponential Equation: y = {a} * {b}^x\n" \
                 f"Domain: {domain}\n"
        return result, sympy.Eq(a * b ** sympy.Symbol('x'), 0)

    def logeq(self, a, b):
        """Handles the processing of a logarithmic equation of the form a * log_b(x)."""
        if b <= 0 or b == 1:
            raise ValueError("Base of logarithm must be positive and not equal to 1.")
        result = f"Logarithmic Equation: y = {a} * log_{b}(x)\n" \
                 "Domain: Real numbers (R) for x > 0\n"
        return result, sympy.log(sympy.Symbol('x'), b) * a

    def plot_linear(self, a, b):
        """Plots a linear equation of the form y = ax + b."""
        x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y = a * x + b
        plot_equation(x, y, title='Linear Equation Plot', legend_label=f'{a}x + {b}')

    def plot_quadratic(self, a, b, c):
        """Plots a quadratic equation of the form y = ax^2 + bx + c."""
        x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y = a * x ** 2 + b * x + c
        plot_equation(x, y, title='Quadratic Equation Plot', legend_label=f'{a}x^2 + {b}x + {c}')

    def plot_cubic(self, a, b, c, d):
        """Plots a cubic equation of the form y = ax^3 + bx^2 + cx + d."""
        x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y = a * x ** 3 + b * x ** 2 + c * x + d
        plot_equation(x, y, title='Cubic Equation Plot', legend_label=f'{a}x^3 + {b}x^2 + {c}x + {d}')

    def plot_exponential(self, a, b):
        """Plots an exponential equation of the form y = a * b^x."""
        x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y = a * (b ** x)
        plot_equation(x, y, title='Exponential Equation Plot', legend_label=f'{a} * {b}^x')

    def plot_logarithmic(self, a, b):
        """Plots a logarithmic equation of the form y = a * log_b(x)."""
        x = np.linspace(0.1, self.x_range[1], self.num_points)  # Start from 0.1 to avoid log(0) issues
        y = a * np.log(x) / np.log(b)  # Change of base formula
        plot_equation(x, y, title='Logarithmic Equation Plot', legend_label=f'{a} * log_{b}(x)')


class EquationSolverCLI:
    """Command Line Interface for Equation Solver."""

    def __init__(self):
        self.solver = EquationSolver()

    def run(self):
        """Runs the CLI interface for equation solving."""
        while True:
            clear_screen()
            print("Equation Solver - CLI Mode")
            print("--------------------------")
            print("1) Linear Equation")
            print("2) Quadratic Equation")
            print("3) Cubic Equation")
            print("4) Exponential Equation")
            print("5) Logarithmic Equation")
            print("6) Exit")
            choice = input("Choose an equation type (1-6): ")

            try:
                if choice == '1':
                    a = float(input("Enter the value for a: "))
                    b = float(input("Enter the value for b: "))
                    result, expression = self.solver.lineareq(a, b)
                    print(result)
                    sympy.pprint(expression, use_unicode=True)
                    self.ask_to_plot(lambda: self.solver.plot_linear(a, b))
                elif choice == '2':
                    a = float(input("Enter the value for a: "))
                    b = float(input("Enter the value for b: "))
                    c = float(input("Enter the value for c: "))
                    result, expression = self.solver.quadraticeq(a, b, c)
                    print(result)
                    sympy.pprint(expression, use_unicode=True)
                    self.ask_to_plot(lambda: self.solver.plot_quadratic(a, b, c))
                elif choice == '3':
                    a = float(input("Enter the value for a: "))
                    b = float(input("Enter the value for b: "))
                    c = float(input("Enter the value for c: "))
                    d = float(input("Enter the value for d: "))
                    result, expression = self.solver.cubiceq(a, b, c, d)
                    print(result)
                    sympy.pprint(expression, use_unicode=True)
                    self.ask_to_plot(lambda: self.solver.plot_cubic(a, b, c, d))
                elif choice == '4':
                    a = float(input("Enter the base multiplier (a): "))
                    b = float(input("Enter the base (b): "))
                    result, expression = self.solver.exponentialeq(a, b)
                    print(result)
                    sympy.pprint(expression, use_unicode=True)
                    self.ask_to_plot(lambda: self.solver.plot_exponential(a, b))
                elif choice == '5':
                    a = float(input("Enter the base multiplier (a): "))
                    b = float(input("Enter the base of logarithm (b): "))
                    result, expression = self.solver.logeq(a, b)
                    print(result)
                    sympy.pprint(expression, use_unicode=True)
                    self.ask_to_plot(lambda: self.solver.plot_logarithmic(a, b))
                elif choice == '6':
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print(f"Invalid choice: {choice}. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")
                time.sleep(2)

    def ask_to_plot(self, plot_function):
        """Asks the user if they want to plot the equation."""
        plot_choice = input("Would you like to plot this equation? (yes/no): ").strip().lower()
        if plot_choice == 'yes':
            plot_function()


class EquationSolverGUI:
    """Graphical User Interface for Equation Solver using Tkinter."""

    def __init__(self, master):
        self.master = master
        self.solver = EquationSolver()
        self.master.title("Equation Solver")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the GUI."""
        self.label = Label(self.master, text="Choose Equation Type:")
        self.label.pack()

        self.linear_button = Button(self.master, text="Linear Equation", command=self.linear_input)
        self.linear_button.pack()

        self.quadratic_button = Button(self.master, text="Quadratic Equation", command=self.quadratic_input)
        self.quadratic_button.pack()

        self.cubic_button = Button(self.master, text="Cubic Equation", command=self.cubic_input)
        self.cubic_button.pack()

        self.exponential_button = Button(self.master, text="Exponential Equation", command=self.exponential_input)
        self.exponential_button.pack()

        self.logarithmic_button = Button(self.master, text="Logarithmic Equation", command=self.logarithmic_input)
        self.logarithmic_button.pack()

    def linear_input(self):
        """Prompts user for input for a linear equation and displays results."""
        try:
            a = float(simpledialog.askstring("Input", "Enter the value for a:"))
            b = float(simpledialog.askstring("Input", "Enter the value for b:"))
            result, _ = self.solver.lineareq(a, b)
            self.display_result(result)
            if messagebox.askyesno("Plot", "Would you like to plot this equation?"):
                self.solver.plot_linear(a, b)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in linear equation input: {e}")

    def quadratic_input(self):
        """Prompts user for input for a quadratic equation and displays results."""
        try:
            a = float(simpledialog.askstring("Input", "Enter the value for a:"))
            b = float(simpledialog.askstring("Input", "Enter the value for b:"))
            c = float(simpledialog.askstring("Input", "Enter the value for c:"))
            result, _ = self.solver.quadraticeq(a, b, c)
            self.display_result(result)
            if messagebox.askyesno("Plot", "Would you like to plot this equation?"):
                self.solver.plot_quadratic(a, b, c)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in quadratic equation input: {e}")

    def cubic_input(self):
        """Prompts user for input for a cubic equation and displays results."""
        try:
            a = float(simpledialog.askstring("Input", "Enter the value for a:"))
            b = float(simpledialog.askstring("Input", "Enter the value for b:"))
            c = float(simpledialog.askstring("Input", "Enter the value for c:"))
            d = float(simpledialog.askstring("Input", "Enter the value for d:"))
            result, _ = self.solver.cubiceq(a, b, c, d)
            self.display_result(result)
            if messagebox.askyesno("Plot", "Would you like to plot this equation?"):
                self.solver.plot_cubic(a, b, c, d)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in cubic equation input: {e}")

    def exponential_input(self):
        """Prompts user for input for an exponential equation and displays results."""
        try:
            a = float(simpledialog.askstring("Input", "Enter the base multiplier (a):"))
            b = float(simpledialog.askstring("Input", "Enter the base (b):"))
            result, _ = self.solver.exponentialeq(a, b)
            self.display_result(result)
            if messagebox.askyesno("Plot", "Would you like to plot this equation?"):
                self.solver.plot_exponential(a, b)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in exponential equation input: {e}")

    def logarithmic_input(self):
        """Prompts user for input for a logarithmic equation and displays results."""
        try:
            a = float(simpledialog.askstring("Input", "Enter the base multiplier (a):"))
            b = float(simpledialog.askstring("Input", "Enter the base of logarithm (b):"))
            result, _ = self.solver.logeq(a, b)
            self.display_result(result)
            if messagebox.askyesno("Plot", "Would you like to plot this equation?"):
                self.solver.plot_logarithmic(a, b)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in logarithmic equation input: {e}")

    def display_result(self, result):
        """Displays the result in a message box."""
        messagebox.showinfo("Result", result)
        logging.info(f"Displayed result: {result}")


def main():
    """Main function to run the equation solver."""
    choice = input("Would you like to use the GUI or CLI? (Enter 'gui' or 'cli'): ").strip().lower()
    if choice == 'gui':
        root = Tk()
        app = EquationSolverGUI(master=root)
        root.mainloop()
    elif choice == 'cli':
        cli = EquationSolverCLI()
        cli.run()
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
