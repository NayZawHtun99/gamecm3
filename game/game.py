import random
def main():
    while True:
        l=int(input("level:"))
        r=random.randint(0,l)
        print(r)
        break
    while True:
        g=int(input("Guess:"))
        if(g==r):
            print("Just Right")
            break
        if(g>r):
            print("Too Large")
        if(g<r):
            print("Too small")
if __name__ == "__main__":
    main()