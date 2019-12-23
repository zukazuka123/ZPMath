#* Copyright (C) Zurab Phertsuliani - All Rights Reserved
#* Unauthorized copying of this file, via any medium is strictly prohibited
#* Proprietary and confidential
#* Written by Zurab Phertsuliani <zukazuka314@gmail.com>

import cmath, time, platform, subprocess, sympy
try:
    command = ""
    inf = "oo"
    real = "R"
    complx = "C"
    decimal = "D"
    a = 0
    b = 0
    c = 0
    expression = ""
    if platform.system() =="Windows":
        command = "cls"
    else:
        command = "clear"

    def lineareq():
        print("Linear equation: ax + b")
        a = float(input("\nEnter the value for a: "))
        b = float(input("Enter the value for b: "))
        d = b / a
        x = 0 - d
        print("\nThe x-intercept's coordinates are: ",(x,0))
        print("The y-intercetp's coordinates are: ",(0,b))
        if type(x) == "int":
            print("Domain : {}".format(real))
        else:
            print("Domain : {}".format(decimal))

    def quadraticeq():
        print("Quadratic equation: ax^2 + bx + c")
        a = float(input("Enter the value for a: "))
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        x = sympy.Symbol("x")
        delta = 4*a*c
        delta2 = 2*a
        x1 = (-b + cmath.sqrt(b**2 - delta))/delta2
        x2 = (-b - cmath.sqrt(b**2 - delta))/delta2
        vertex = -b/(2*a)
        expression = sympy.sympify(a*x**2+b*x+c)
        print("The possible factored version is :",sympy.factor(expression))
        print("The x-intercept's coordinates are: ",(x1,0),(x2,0))
        print("The y-intercept's coordinates are: ",(0,c))
        print("The vertex's coordinates are: ",((vertex),(a*vertex**2+b*vertex+c)))
        if type(x1) and type(x2) == "int":
            print("Domain : {}".format(real))
        elif type(x1) and type(x2) == "float":
            print("Domain : {}".format(decimal))
        else:
            print("Domain : {}".format(complx))
        sympy.plot(expression)


    def launch():
        subprocess.call(command,shell=True)
        print("--------------------------")
        print("-                        -")
        print("-    By Zurab            -")
        print("-        V1.0            -")
        print("-                        -")
        print("--------------------------\n")

        print("\n1) Analysis of linear equation")
        print("2) Analysis of quadratic equation")
        print("3) Exit the program")
        choise = int(input("Enter Your choise: "))
        if choise == 1:
            lineareq()
        elif choise == 2:
            quadraticeq()
        elif choise == 3:
            exit(1)
        else:
            print("There no {} choise, bye!".format(choise))
            time.sleep(5)
            exit(1)
    while True:
        launch()
        time.sleep(15)
except KeyboardInterrupt:
    print("\nHope this script helped you, thank you!")
    time.sleep(5)
except ZeroDivisionError:
    print("\nYou want to test me? You know you can't divide by zero.")
    time.sleep(5)
except TypeError:
    print("\nYou can't do that, please rerun the program.")
    time.sleep(5)
except ValueError:
    print("\nYou can't do that, please rerun the program.")
    time.sleep(5)
