#Treasure Haunt#

import time 

#game items
#------------------------------------------#
#pearl DONE
take_pearl = 0
#ring ()
take_ring = 0
#trinket
take_trinket = 0
#watch
take_watch = 0
#monkeys paw
take_monkey_paw = 0
#take doll
take_doll = 0

total_score = 0
game_flags = {'ending': False } 
#fix being able to take items multiple times. Item flags?
#fix using function?
# add timers to make text flow better
# use if statment to confirm item found with additional items?
def intro():
    print('''you've heard stories of the mansion down the street has many artifacts
       that are worth quite a bit of money. So tonight, you've decided to go 
       take a look.''')
    time.sleep(3)
    print('''As you enter the mansion, the air around you becomes heavy. This place
       is dangerous. However you need the money. There are 3 rooms from the
       main enterence. Which will you enter?''')

def intro2():
    time.sleep(2)
    print('''There are 3 rooms from the
       main enterence. Which will you enter?''')
    time.sleep(1)
    print('Kitchen: 1 - Bedroom: 2 - living room: 3 - leave: 4')

def roomchoice(room_number):
    # returns the chosen room number in a string to use for game flow 
    return room_number

def ending():
    # depending on score, gives player a differnet ending
    # need to fix score order
    global total_score
    game_flags['ending'] = True
    if total_score >= 600:
        print('''backpack full of loot you walk out of the house satisfied with your
                gains.''')
    elif total_score == 400:
        print('''aquiring this many items was risky, but it will pay off once these items
                 get sold for a quick buck.''')
    elif total_score == 200:
        print('''after taking something from the house, A presence follows you home. 
              After only a few hours, you become incredibly ill and pass shortly after''')
    elif total_score == -200:
        print('''After grabbing some item, you tried to leave. However, the front doors were locked.
              turning around a dark presence consumes you.''')
    elif total_score == -400:
        print('''After grabbing that last item, you feel an overwelmingly dark force approach you,
        quickly erasing you from existance. Nobody will remember you''')
    else:
        print('''After feeling the dark presence, you decided to turn around
              and leave.''')

def living_room():
    global game_flags
    global total_score
    global take_pearl
    global take_ring
    area_check = ''
    if area_check != '2':
        print('''The living room seems anicent, not a single tv in sight.
there are plenty of end tables other places to look.''')
        time.sleep(3)
        print('fireplace: 1 - end tables: 2 - between cushions: 3')
        area_check = input()
    #checks area and loops back till player finds the watch
    if area_check == '1':
        if take_pearl == '1' or take_pearl == '2':
            print('You already found the pearl')
        else:
            print('''you reach your hand up into the fireplace, and feel a hidden metal door. 
You open it and find a large pearl.''')
            time.sleep(2)
            print('Take (1) | Leave (2)')
            take_pearl = input()
            if take_pearl == '1':
                print('you put the pearl into your backpack')
                total_score = total_score + 200
            else:
                print('you slip the pearl back into the compartment and close the door')
    elif area_check == '2':
        if take_ring == '1' or take_ring == '2':
            print('You already found the ring')
        else:
            print('''after searching all the end tables you come across a bloodied ring. Take it?''')
            time.sleep(2)
            print('Take (1) | Leave (2)')
            take_ring = input()
            if take_ring == '1':
                print('You put the bloodied ring in your backpack')
                total_score = total_score - 200
            else:
                print('You stick the bloodied ring back in the end table that you found it in.')
    else:
        print('''you find some pocket lent''')

def kitchen():
    global game_flags
    global total_score
    global take_monkey_paw
    global take_watch
    area_check = ''
    if area_check != '2':
        print('''The kitchen is quite large and luxurious. There are many
             cupboards and shelves to check. What would you like to look at?''')
        time.sleep(3)
        print('cupbards: 1 - shelves: 2 - appliances: 3')
        area_check = input()
    #checks area and loops back till player finds the watch
    if area_check == '1':
        if take_monkey_paw == '1' or take_monkey_paw == '2':
            print("you already have the monkey paw, no need to search here again.")
        else:
            print('''You check around all the dusty cupboards and find a monkeys paw. Take it?''')
            time.sleep(2)
            print('Take (1) | Leave (2)')
            take_monkey_paw = input()
            if take_monkey_paw == '1':
                print('You put the monkeys paw in your backpack')
                total_score = total_score - 200
            else:
                print('You put the paw back in the cupboard. Why is this even here?')
    elif area_check == '2':
        if take_watch == '1' or take_watch == '2':
            print('You already have the watch, no need to search here again.')
        else:
            print('''While looking through the kitchen shelves,
you come across old watch. Take it?''')
            print('Take (1) | leave (2)')
            take_watch = input()
            if take_watch == '1':
                print('you put the watch in your backpack')
                total_score = total_score + 200
                game_flags['kitchen'] = game_flags['kitchen'] = True
            else:
                print('you put the watch back on the shelf')
    else:
        print('''you check the dusty appliances but find nothing but rotted food''')

def bedroom():
    global game_flags
    global total_score
    global take_trinket
    global take_doll
    area_check = ''
    if area_check != '3':
        print('''The bedroom is very spacous and enough dressers to fill
an entire house. What would you like to search?''')
        time.sleep(3)
        print('dressers: 1 - under bed: 2 - closets: 3')
        area_check = input()
    #checks area and loops back till player finds the diamond necklace
    if area_check == '1':
        if take_trinket == '1' or take_trinket == '2':
            print('You already found the trinket, no need to search here again.')
        else:
            print('''after rummaging through the dressers,in-between some clothes
you find a trinket. take it?''')
            time.sleep(2)
            print('Take (1) | Leave (2)')
            take_trinket = input()
            if take_trinket == '1':
                print('You put the trinket in your backpack')
                total_score = total_score - 200
            else:
                print('You tuck the trinket back into the dresser')
    elif area_check == '2':
        if take_doll == '1' or take_doll == '2':
            print('You already found the doll, no need to search here again.')
        else:
            print('''checking underneath the bed reveals an ominous looking doll. Take it?''')
            time.sleep(2)
            print('Take (1) | Leave (2)')
            take_doll = input()
            if take_doll == '1':
                total_score = total_score - 200
                print('You stuff the doll into your backpack')
            else:
                print('You stuff the doll back under the bed.')
    else:
        print('''Inside the closet you notice a little box, inside is a
very expensive diamond necklace.''')
        time.sleep(1)
        print('Take (1) | Leave (2)')
        take_necklace = input()
        if take_necklace == '1':
            print('you put the necklace in your backpack')
            total_score = total_score + 200
        else:
            print('you put the necklace back into the closet')

intro()

playagain = 'yes'
#Fix play again score not reseting
while playagain == 'yes' or playagain == 'y':
    time.sleep(2)
    intro2()
    room_number = input()
    if roomchoice(room_number) == '1':
        kitchen()
    elif roomchoice(room_number) == '2':
        bedroom()
    elif roomchoice(room_number) == '3':
        living_room()
    else:
        playagain = 'no'
        ending()
        time.sleep(2)
        print('Would you like to play again? yes or no?')
        playagain = input()
# check if play again adds total score into previous play.
print(f'Your total score was {total_score}')

