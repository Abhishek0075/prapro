from commandLine import parseCommandLineAndSum

if __name__ == "__main__" :
    # Need to insert args in the form "python main.py num1 num2 num3 num4" 
    numbers, sum = parseCommandLineAndSum()
    print(f"The sum of the numbers {numbers} is {sum}")
    