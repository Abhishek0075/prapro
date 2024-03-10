import argparse

def parseCommandLineAndSum() :
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="Enter the numbers you want to add",type=int, nargs="+")
    args = parser.parse_args()
    return args.numbers, sum(args.numbers)

    