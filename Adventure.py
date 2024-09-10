import time 

total_score = 0
game_flags = {'kitchen':False,'living room':False, 'bedroom': False, 'ending': False } # might be redundent
# maybe change scores?
# adjust code to correlate with the right room
# add timers to make text flow better
# add negative score multipliers for bad ends?
# use if statment to confirm item found?
print('hello')
def intro():
    print('''you've heard stories of the mansion down the street has many artifacts
       that are worth quite a bit of money. So tonight, youve decided to go 
       take a look and see what you can find.''')
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
    global total_score
    game_flags['ending'] = True
    if total_score > 200:
        print('''after taking only 1 item, the presence became too much
                 and you fled into the night. After only a few hours, 
                  you become incredibly ill and pass shortly after''')
    elif total_score > 400:
        print('''aquiring 2 items was risky, but it will pay off once these items
                 get sold for a quick buck.''')
    elif total_score > 600:
        print('''pockets full of look you walk out of the house satisfied with your
                gains.''')
    else:
        print('''After feeling the dark presence, you decided to turn around
              and leave.''')

def living_room():
    global game_flags
    global total_score
    area_check = ''
    if area_check != '2':
        print('''The living room seems anicent, not a single tv in sight.
                 there are plenty of end tables other places to look.''')
        time.sleep(3)
        print('fireplace: 1 - end tables: 2 - between cushions: 3')
        area_check = input()
    #checks area and loops back till player finds the watch
    if area_check == '1':
        print('''you reach your hand up into the fireplace, and feel
                a hidden metal door. You open it and find a large pearl.''')
        time.sleep(2)
        print('take: 1 leave as is: 2')
        take_watch = input()
        if take_watch == '1':
            print('you put the pearl into your back pocket')
            total_score = total_score + 200
            game_flags['living room'] = game_flags['living room'] = True
        else:
            print('you slip the pearl back into the compartment and close the door')
    elif area_check == '2':
        print('''after searching all the end tables you come back empty handed''')
    else:
        print('''you find some pocket lent''')

def kitchen():
    global game_flags
    global total_score
    area_check = ''
    if area_check != '2':
        print('''The kitchen is quite large and luxurious. There are many
             cupboards and shelves to check. What would you like to look at?''')
        time.sleep(3)
        print('cupbards: 1 - shelves: 2 - appliances: 3')
        area_check = input()
    #checks area and loops back till player finds the watch
    if area_check == '1':
        print('''You check around all the dusty cupboards
                 and find nothing worth of value.''')
    elif area_check == '2':
        print('''While looking through the kitchen shelves,
                 you come across old watch. Take it?''')
        print('take: 1 leave as is: 2')
        take_watch = input()
        if take_watch == '1':
            print('you put the watch in your left pocket')
            total_score = total_score + 200
            game_flags['kitchen'] = game_flags['kitchen'] = True
        else:
            print('you put the watch back on the shelf')
    else:
        print('''you check the dusty appliances but find nothing but rotted food''')

def bedroom():
    global game_flags
    global total_score 
    area_check = ''
    if area_check != '3':
        print('''The bedroom is very spacous and enough dressers to fill
                 an entire house. What would you like to search?''')
        time.sleep(3)
        print('dressers: 1 - under bed: 2 - closets: 3')
        area_check = input()
    #checks area and loops back till player finds the diamond necklace
    if area_check == '1':
        print('''after rummaging thorugh the dressers, the only
                thing of substance is the amount of dust now on you.''')
    elif area_check == '2':
        print('''checking underneath the bed reveals nothing but the wall
                 on the other side of the room.''')
    else:
        print('''Inside the closet you notice a little box, inside is a
                very expensive diamond necklace.''')
        time.sleep(1)
        print('take: 1 leave as is: 2')
        take_necklace = input()
        if take_necklace == '1':
            print('you put the necklace in your right pocket')
            total_score = total_score + 200
            game_flags['bedroom'] = game_flags['bedroom'] = True
        else:
            print('you put the necklace back into the closet')

intro()

playagain = 'yes'
while playagain == 'yes' or playagain == 'y':
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
# get play again to function properly
ending()
time.sleep(2)
print(f'Your total score was {total_score}')
print('Would you like to play again? yes or no?')
playagain = input()