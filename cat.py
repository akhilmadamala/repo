import sys


def dog():
    print("woof")
def cat():
    print("meow")
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
