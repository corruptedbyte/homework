print("Warning! The program only works with two numbers (x + x)")
print("Supported operators: +, -, /, *.")
equasion = input("Enter an equasion (sepecrate the operator using space): ").split(" ")

match equasion[1]:
    case "+":
        print(int(equasion[0])+int(equasion[2]))
    case "-":
        print(int(equasion[0])-int(equasion[2]))
    case "/":
        print(int(equasion[0])/int(equasion[2]))
    case "*":
        print(int(equasion[0])*int(equasion[2]))