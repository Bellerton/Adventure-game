#Modules
import random
import time

#Variables
    #Settings
Difficulty = 'Medium'     #affects game difficulty
Difficulties = ['Easy', 'Medium', 'Hard']
    #Character
Currentcharacter = ''
Characters = ['Fighter', 'Builder', 'Fisher', 'Hunter', 'Crafter']
        #STATS
HP = 0              #set on gamestart, according to difficulty
Hunger = 0          #set on gamestart, according to difficulty  
Thirst = 0          #set on gamestart, according to difficulty
Carrycapacity = 0  #How many items the player can carry        modified by backpacks

        #ITEMS
Inventory = []      #contains every item the player is currently carrying
Itemuse = []        #for using items with usecommand
Eatable = []        #collection of all eatable items for refrences
Tools = ['basic', ]          #collection of all Tools for refrences

        #SKILLS
Searchskill = 0     #improved by searching
Huntskill = 0       #improved by hunting
Craftskill = 0      #improved by crafting
Buildskill = 0      #improved by building
Fightskill = 0      #improved by fighting
Fishskill = 0       #improved by Fishing

    #Locations
Location = 'Mainmenu'   #Where the player is currently located

        #SHELTER
Shelterbuildings = []           #contains every building that is built
Possibleshelterbuildings = ['campfire', 'tent', 'mudhut', 'brickhut', 'sleeping area', 'bed', ]   #contains every building that can be built
ShelterInventory = []           #contains every item stored in the shelter
Sheltersafety = 0

        #BEACH
Beachfirst = True
            #searching
Beachnormal = 1     #Huntcrab, Fish, gather driftwood
Beachspecial = 1    #knife, 

        #FOREST
Forestfirst = True
Foundshelter = False
Foundwaterspring = False
Forestknife = True
           

        #DEEPFOREST
Dforestfirst = True
            

        #LAKE
Lakefirst = True
Lakefishpopulation = 77    #Is this needed             ????????
            

        #PLAIN
Plainfirst = True
            

        #MOUNTAIN
Mountainfirst = True
            

        #CLIFF
Clifffirst = True
            

        #CAVE
Cavefirst = True
            

        #DEEPCAVE
Dcavefirst = True
            
    


    #CHARACTER
        #Health change
def HPchange (amount):
    global HP
    HP += (amount)

        #Hunger change
def Hungerchange (amount):
    global Hunger
    Hunger += (amount)

        #Thirst change
def Thirstchange (amount):
    global Thirst
    Thirst += (amount)

        #Inventory change
def Inventorychange (item, action):
    global Inventory
    if action == 'add' and len(Inventory) < 10:
        Inventory.append (item)
        print (Inventory)
        print (item + ' added to Inventory')
    elif action == 'del' and item in Inventory:
        Inventory.remove (item)
    else:
        print ('Something is wrong')

        #Statshowcase
def Statshow ():
    print ('\n\n' + '-'.center(77, '-'))
    print ('HP: ' + (str(HP)) + '\t\tHunger: ' + (str(Hunger)) + '\t\tThirst: ' + (str(Thirst)))
    print ('-'.center(77, '-'))
    print (Location)

def Fullstatview ():
    print ('\n\n''HP: ' + str(HP) + '\nHunger: ' + str(Hunger) + '\nThirst: ' + str(Thirst))
    print ('fightskill: ' + str(Fightskill) + '\nHuntskill: ' + str(Huntskill) + '\nFishskill: ' + str(Fishskill))
    print ('Buildskill: ' + str(Buildskill) + '\nCraftskill: ' + str(Craftskill) + '\nSearchskill: ' + str(Searchskill))
    input ()

        #Characterview
def Character ():
    print ('Stats\tInventory')
    Action = input ()
    Action = Action.lower ()
    if Action == 'stats':
        Fullstatview ()
    elif Action == 'inventory':
        Inventorymanagment ()
    
        #Inventory managment
def Inventorymanagment ():
    global Inventory
    global ShelterInventory
    global Fastuse
    global Itemuse
    global Eatable
    global Carrycapacity
    while True:
        print ('view \t swap \t use \t move \t')
        Action = input ()
        Action = Action.lower ()
        if Action == 'view':
            while True:
                
#Prints the players Inventory
                
                if (len(Inventory)) >= 1 :      
                    print ('your Inventory contains')
                    print (Inventory)
                    if Location == 'Shelter':
                        print ('The shelter contains')
                        print (ShelterInventory)
                    if input () == '':
                        break
                elif (len(Inventory)) == 0:
                    print ('your Inventory is empty')
                    if input () == '':
                        break

#Swaps 2 items in the players Inventory
                    
        elif Action == 'swap':              
            print ('which items do you wish to switch?')
            print (Inventory)
            ItemA = input ('Firstitem\n')
            ItemB = input ('seconditem\n')
            if (ItemA) in Inventory and (ItemB) in Inventory:
                a, b = Inventory.index(ItemA), Inventory.index(ItemB)
                Inventory[b], Inventory[a] = Inventory[a], Inventory[b]
                print ('Items switched')
                print (Inventory)
            else :
                print ('Atleast One of those items is not in your Inventory')
                
#Calls the use item function
                
        elif Action == 'use':
            print (Inventory)
            if Location == 'Shelter':
                print(ShelterInventory)
            Itemuse (input('wich item do you wish to use?\n'))
            
#Move items between Inventory and ShelterInventory
            
        elif Action == 'move':
            print ('Inventory:' + str(Inventory))
            print ('ShelterInventory:' + str(ShelterInventory))
            ItemA = input ('Which item do you wish to move?')
            if ItemA in Inventory:
                ShelterInventory.append (ItemA)
                Inventory.remove (ItemA)
            elif ItemA in ShelterInventory and len(Inventory) < (Carrycapacity):
                Inventory.append (ItemA)
                ShelterInventory.remove (ItemA)
            elif ItemA in ShelterInventory and len(Inventory) >= (Carrycapacity):
                print ('you can not carry anyhing more')
            print ('Item moved')
            print ('Inventory:' + str(Inventory))
            print ('ShelterInventory:' + str(ShelterInventory))
        elif Action == '':
            break
        else :
            print ('You wonder if that is really an option')      



def Itemuse (item):                         #   Use an item from the players Inventory
    global Inventory
    global Itemuse
    global Fastuse
    global ShelterInventory
    global Eatable
    global Tools
    if item in Inventory:

#Eating something
        
        if item in Eatable:
            Hungerchange (Eatable [Eatable.index(item) + 1])
            Thirstchange (Eatable [Eatable.index(item) + 2])
            Inventory.remove (item)
    elif item in ShelterInventory and Location == 'Shelter':
        if item in Eatable:
            Hungerchange (Eatable [Eatable.index(item) + 1])
            Thirstchange (Eatable [Eatable.index(item) + 2])
            ShelterInventory.remove (item)
    else:
        print ('You do not have that item')

#Starting the game
def Setstats (difficulty):
    global Character
    global Characters
    global HP
    global Hunger
    global Thirst
    global Carrycapacity
    global Searchskill
    global Huntskill
    global Fightskill
    global Buildskill
    global Craftskill
    global Fishskill
    HP = (15 * difficulty)
    Hunger = (25 * difficulty)
    Thirst = (20 * difficulty)
    Carrycapacity = (5 * difficulty)
    Searchskill = (2 * difficulty)
    Fightskill = ((2 * difficulty) - 1)
    Buildskill = ((2 * difficulty) - 1)
    Craftskill = ((2 * difficulty) - 1)
    Fishskill = ((2 * difficulty) - 1)
    Huntskill = ((2 * difficulty) - 1)
    if Currentcharacter == 'Fighter':
        Fightskill += 2
    elif Currentcharacter == 'Builder':
        Buildskill += 2
    elif Currentcharacter == 'Crafter':
        Craftskill += 2
    elif Currentcharacter == 'Fisher':
        Fishskill += 2
    elif Currentcharacter == 'Hunter':
        Huntskill += 2



#ACTIONS
    #Searching
def Searchoutcome () :
    global Searchskill
    global Forestknife
    global Inventory
    if Location == 'Beach':
        pass
    elif Location == 'Forest':
        Hungerchange (-(random.randint(0, 3)))
        Thirstchange (-(random.randint(1, 4)))
        if random.randint(0,Searchskill) > 4 and Forestknife == True and len(Inventory) < 10:
            Forestknife = False
            Inventory.append ('Knife')
            print ('You found a Knife')
            print (Inventory)
        else:
            print ('you did not find anything')
            

    #Hunting
def Huntoutcome (animal) :
    global Huntskill
    if animal.lower () == 'crab' :
        Hungerchange (-(random.randint(0, 3)))
        Thirstchange (-(random.randint(1, 4)))
        if (random.randint(0,10)) > 4:
            print ('You search the beach and find a crab')
##            time.sleep (4)
            while True :
                print ('Capture \t Kill \t Leave'.center(77))
                crabdestiny = input ()
                crabdestiny = crabdestiny.lower ()
                if crabdestiny == 'capture' :
                    if Inventory == 'craptrap' :
                        print ('You manage to get capture the crab and put it in the trap')
                        print ('it does pinch you however\nYou lose 1 HP')
                        HPchange (-1)
                    else :
                        print ('You pick up the crab but drop it as it pinches you')
                        print ('You lose 1 HP')
                        HPchange (-1)
                elif crabdestiny == 'kill' and 'Knife' not in Inventory :
                    print ('you do not have anything to kill the crab with')
                elif crabdestiny == 'kill' and 'Knife' in Inventory :
                    Inventory.append ('dead crab')
                    print ('You kill the crab and add it to your Inventory')
##                    time.sleep (4)
                    print ('you now have' + str(Inventory) + 'in your Inventory')
                    break
                elif crabdestiny == 'leave':
                    print ('The crab lives to fight another day')
                    break
        else:
            print ('You can\'t find a crab to hunt')
            print ('You will have to try again')

    #Fighting
def Fightoutcome () :
    global Fightskill
    

    #Building
def Buildoutcome () :
    global Buildskill
    

    #Fishing
def Fishoutcome () :
    global Fishskill
    global Inventory
    if Location == 'Lake' and (('basic rod' or 'improved rod' or 'master rod') in Inventory) and 'bait' in Inventory:
        Hungerchange (-(random.randint(0, 3)))
        Thirstchange (-(random.randint(1, 4)))
        if (random.randint(1,10)) > 7:
            print ('After waiting for some time a fish takes the bait')
    elif Location == 'Beach':
        pass

    #Crafting
def Craftoutcome () :
    global Craftskill
    pass
    

                        #LOCATIONS
        
    #Main menu
        
def Mainmenu ():            #Consist of the main menu and settings
    global Difficulty
    global Difficulties
    global Location
    global Currentcharacter
    global Characters
    while Location == 'Mainmenu' :
        print ('1. Start game'.center(77))
        print ('2. settings'.center(77))
        Action = input ()
        Action = Action.lower ()
    #GAMESTART
        if Action == '1' or Action == '1.' or Action == 'start' or Action == 'start game' :
            print ('loading game...')
##            for i in range(1, 101, 8):
##                print ( str(i) + '%')
##                time.sleep((random.randint(1, 10)) / 10)
            if Difficulty == 'Easy':
                Setstats (3)
            elif Difficulty == 'Medium':
                Setstats (2)
            elif Difficulty == 'Hard':
                Setstats (1)
            print('Load succesfull')
##            time.sleep (1)
            Location = 'Beach'
            break
    #SETTINGS
        elif Action.lower () == '2' or Action.lower () == '2.' or Action.lower () == 'settings' :
            while True:
                print ('Difficulty \t Character')
                Action = input ()
                Action = Action.lower ()
                if Action == 'difficulty':
                    print ('\t\t\t\t\tHard Medium Easy')
                    tempDifficulty = input ()
                    if tempDifficulty in Difficulties :
                        Difficulty = tempDifficulty
                        print ('Difficulty successfully set to')
                        print (Difficulty)
    ##                    time.sleep (1)
                    elif tempDifficulty == '':
                        break
                    else :
                        print ('That is not a valid Difficulty')
                elif Action == 'character':
                    print (Characters)
                    tempCharacter = input ()
                    if tempCharacter in Characters :
                        Currentcharacter = tempCharacter
                        print ('Character successfully set to')
                        print (Currentcharacter)
    ##                    time.sleep (1)
                    elif tempCharacter == '':
                        break
                    else :
                        print ('That is not a valid Character')
                elif Action == '':
                    break
    #EXIT
        elif Action.lower () == 'exit' or Action.lower () == 'quit' :
            Location = 'exit'
        else:
            print ('What to do? What to do?')


    #SHELTER
def Shelter ():
    global Location
    pass

    #WATERSOURCE
def Waterspring ():
    global Location
    pass


    #BEACH

def Beach ():
    global Location
    global Beachfirst
    while Location == 'Beach':
#First visit
        if Beachfirst == True:
            print ('\n\n\nYou find yourself waking up, washed ashore on an unknown beach.'.ljust(77))
##            time.sleep (4)
            print ('In front of you lies a forest, it stretches both far to the left and far to \nthe right of you and eventually curves out of sight.'.ljust(77))
##            time.sleep (7)
            print ('All around you driftwood has been washed up on the shore.'.ljust(77))
##            time.sleep (4)
            Beachfirst = False
#Action menu
        Statshow()
        print ('\n' + 'Search \t Hunt (crab) \t Gather (Wood) \t Character'.center(77))
        print ('Forest')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'hunt':
            Huntoutcome ('crab')
        elif Action == 'character':
            Character ()
        elif Action == 'gather' and not 'Driftwood' in Inventory:
            Inventorychange ('Driftwood', 'add')
            Hungerchange (-(random.randint(0, 3)))
            Thirstchange (-(random.randint(1, 4)))
        elif Action == 'forest':
            Location = 'Forest'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #FOREST
def Forest ():
    global Location
    global Forestfirst
    global Foundshelter
    global Foundwaterspring
    while Location == 'Forest':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Beach \t Deepforest \t Plain \t Lake', end="", flush=True)
        if Foundshelter == True:
            print (' \t Shelter', end="", flush=True)
            if Foundwaterspring == True:
                print (' \t Waterspring')
        elif Foundwaterspring  == True:
            print (' \t Watersource')
        else:
            print ('')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'beach':
            Location = 'Beach'
        elif Action == 'deepforest':
            Location = 'Deepforest'
        elif Action == 'plain':
            Location = 'Plain'
        elif Action == 'lake':
            Location = 'Lake'
        elif Action == 'shelter' and Foundshelter == True:
            Location = 'Shelter'
        elif Action == 'waterspring' and Foundwaterspring == True:
            Location = 'Waterspring'
        elif Action == 'exit':
            Location = 'Mainmenu'
        

    #DEEPFOREST
def Deepforest ():
    global Location
    global Dforestfirst
    while Location == 'Deepforest':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Forest \t Cave \t Mountain')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'forest':
            Location = 'Forest'
        elif Action == 'cave':
            Location = 'Cave'
        elif Action == 'mountain':
            Location = 'Mountain'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #PLAIN
def Plain ():
    global Location
    global Plainsfirst
    while Location == 'Plain':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Forest \t Mountain')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'forest':
            Location = 'Forest'
        elif Action == 'mountain':
            Location = 'Mountain'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #MOUNTAIN
def Mountain ():
    global Location
    global Mountainfirst
    while Location == 'Mountain':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Deepforest \t Plain \t Cliff')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'deepforest':
            Location = 'Deepforest'
        elif Action == 'plain':
            Location = 'Plain'
        elif Action == 'cliff':
            Location = 'Cliff'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #CLIFF
def Cliff ():
    global Location
    global Clifffirst
    while Location == 'Cliff':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Mountain')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'mountain':
            Location = 'Mountain'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #CAVE
def Cave ():
    global Location
    global Cavefirst
    while Location == 'Cave':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Deepforest \t Deepcave')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'deepforest':
            Location = 'Deepforest'
        elif Action == 'deepcave':
            Location = 'Deepcave'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #DEEPCAVE
def Deepcave ():
    global Location
    global Dcavefirst
    while Location == 'Deepcave':
        Statshow()
        print ('\n' + 'Search \t Character'.center(77))
        print ('Cave')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'cave':
            Location = 'Cave'
        elif Action == 'exit':
            Location = 'Mainmenu'

    #LAKE
def Lake ():
    global Location
    global Lakefirst
    while Location == 'Lake':
        Statshow()
        print ('\n' + 'Search \t Fish \t Character'.center(77))
        print ('Forest \t Deepforest \t Plain')
        print ('-'.center(77, '-'))
        Action = input ()
        Action = Action.lower ()
        if Action == 'search':
            Searchoutcome ()
        elif Action == 'fish':
            Fishoutcome ()
        elif Action == 'character':
            Character ()
        elif Action == 'forest':
            Location = 'Forest'
        elif Action == 'deepforest':
            Location = 'Deepforest'
        elif Action == 'plain':
            Location = 'Plain'
        elif Action == 'exit':
            Location = 'Mainmenu'



    




while True:
    if Location == 'Mainmenu':
        Mainmenu ()
    elif Location == 'Shelter':
        Shelter ()
    elif Location == 'Beach':
        Beach ()
    elif Location == 'Forest':
        Forest ()
    elif Location == 'Deepforest':
        Deepforest ()
    elif Location == 'Plain':
        Plain ()
    elif Location == 'Mountain':
        Mountain ()
    elif Location == 'Cliff':
        Cliff ()
    elif Location == 'Cave':
        Cave ()
    elif Location == 'Deepcave':
        Deepcave ()
    elif Location == 'Lake':
        Lake ()
    elif Location == 'exit':
        break
    else :
        print ('A problem seems to have ocurred')
        print ('Somehow the current location variable became: ' + Location)
        break






            

print ('test succesful')
