print('''
*******************************************************************************
                 )       \   /      (
                /|\      )\_/(     /|\
*              / | \    (/\|/\)   / | \             *
|`.___________/__|__o____\`|'/___o__|__\__________.'|
|                  '^`    \|/   '^`                 |
|                          V                        |
|                                                   |
|                                                   |
| ._______________________________________________. |
|'      l    /\ /     \\            \ /\   l       `|
*       l  /   V       ))            V   \ l        *
        l/            //                  \I
                      V
*******************************************************************************
''')
print("Welcome to Dragon Island.")
print("Your mission is to find the treasure.") 

first = input("Which way? Left or right? ").lower()
if first != "left":
    print("You fall into a hole. GAME OVER!")
else:
    second = input("Swim or wait? ").lower()
    if second != "wait":
        print("You're attacked byb a trout. GAME OVER!")
    else: 
        third = input("Which door? Red, blue or yellow? ").lower()
        if third == "red":
            print("You're burned by fire. GAME OVER!")
        elif third == "yellow":
            print("You win!")
        elif third == "blue":
            print("You're eaten by beasts. GAME OVER!")
        else: 
            print("GAME OVER!")

