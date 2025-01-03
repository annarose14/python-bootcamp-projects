print("Welcome to Treasure island!\n Your mission is to find the tressure\n")
first=input('you\'re at a cross road , where do you want to go? "left" or "right"\n').lower()
if first=="right": 
    print("Oops! sorry, game over")
elif first=="left":
    second=input("Do you wanna swim or wait? swim or wait\n").lower()
    if second=="swim":
        print("Aww! you drowened, game over")
    elif second=="wait":
        third=input("At which door do you wanna wait? Red, Blue or Yellow\n").lower()
        if third=="blue":
            print("Game over")
        elif third=="red":
            print("Game over")
        else:
            print("Yaay you won, congragulations!")


