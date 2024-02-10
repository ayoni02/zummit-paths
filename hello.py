# Description: This program prints "Hello, World!" if no arguments are given, 
# otherwise it prints "Hello, <argument>!" where <argument> is the first argument given to the program.
def hello(*args):
    if len(args) == 0:
        print("Hello, World!")
    else:
        print("Hello, " + args[0] + "!")
        
if __name__ == "__main__":
    import sys
    hello(*sys.argv[1:])