import sys


def dog():
    print("Woof")
def cat():
    print("Meow")
def default():
    print("hello")

def main():
    if sys.argv[1]=="cat":
        cat()
    elif sys.arg[1]=="dog":
        dog()
    else:
        
        default()





if __name__=="__main__":
    main()
