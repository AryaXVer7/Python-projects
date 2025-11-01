print(r'''                   _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-' 
 ''')
print("***Welcome to Treasure Island. Your mission is to find the treasure.***")
direction = input("You are at a crossroad, which way do you want to go? Left or Right: ")
if direction.lower() == "left":
    Way_to_island = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim: ")
    if Way_to_island.lower() == "wait":
        choose_portal = input("You have arrived at an island unharmed. There is are 3 portals. Which portal do you want to choose? Red, Yellow or Blue: ")
        if choose_portal.lower() == "yellow":
            choose_option1 = input("'Shadow Woods', will you 'trust' the spirits or 'banish' them with light?: ")
            if choose_option1.lower() == "banish":
                print("The darkness fades, reveals the chest. You Win!")
            else:
                print("The spirits lead you into a trap. Game Over!")
        elif choose_portal.lower() == "blue":
            choose_option2 = input("'Ice Realm', will you 'brave' the cold or 'seek' magical warmth?: ")
            if choose_option2.lower() == "brave":
                print("You found the treasure. You Win!")
            else:
                print("You can't find fire place for warmth. Game Over!")
        elif choose_portal.lower() == "red":
            choose_option3 = input("'Fire Realm', will you 'fight' the dragon or 'bargain' with it?: ")
            if choose_option3 == "bargain":
                print("You bargained the dragon and found the treasure. You Win!")
            else:
                print("You cant't defeat the dragon. Game Over!")
        else:
            print("You choose a portal that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")
