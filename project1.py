# WHALE TRAIL, A CHOOSE YOUR OWN ADVENTURE GAME BY KATY SCOTT
import random
import time

# Assign game start time, so elapsed time can be used to calculate the date of the journey in the calculate_date() function
# is this an appropriate use of a global variable, or is there a better way?
start_time = time.time() 

# Assign default player names, in case player bypasses names screen accidentally
names_dict = {"player": "you", "calf":"your calf", "family1":"your brother","family2":"your cousin"}

# Assign initial health score
health_dict = {"prepare_health":0, "speed_health": 0, "migration_health":0}

# INPUT FUNCTION for all player input, which will allow user to use universal commands like 'exit' and 'help'
def user_input():
    while True:
        user_choice = raw_input("")
        if user_choice.lower() == 'exit': 
          exit()
        elif user_choice.lower() == 'help':
          intructions()
        elif user_choice.lower() == 'migrate':
          migrate()
        elif user_choice == "":
         print "Please type your option."
        else:
          return user_choice


# INSTRUCTIONS FUNCTION to display instructions for play
def instructions():
    print "\n" * 80
    print """

~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~

    Welcome to Whale Trail, the game where YOU are a migrating humpback whale,
    making life and death decisions for yourself and your pod.

    Humpback whales migrate from Alaska to Hawaii each winter, in one of the longest
    migrations of any mammal on Earth. This where the whales breed and, about 11 
    months later, return to give birth in the warm waters. In this game, you have 
    just given birth to your calf near Hawaii. Now, after months of fasting, you 
    are about to make the 3,000-mile journey back to the abundant feeding grounds 
    near Alaska.

    On your journey, you'll need to find food, protect your pod and avoid hazards
    like weather, ocean pollution, boats, and killer whales.

    To play, follow the prompts on each screen to make your next decision. The health
    of your pod depends on these decisions -- you'll see this health displayed on
    each screen of play.

    Once you select an option, you're tied to it, with one exception. To adjust
    your speed, type 'migrate' at any time.

    To quit, type 'exit' at any time.
    To return to this page, type 'help' at any time.

~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~

    """

    while True:
        print "What would you like to do?\n1 - Start game from beginning\n2 - Continue play\n3 - Quit\n"
        next_step = user_input()
        if next_step == "1" or next_step == "2" or next_step == "3":
            break
        else:
            print "I don't understand. Please choose 1, 2, or 3."    
    if next_step == "1":
      intro_game()
    elif next_step == "2":
      play_game()
    else:
        print "Come back soon!"
        exit()


# TITLE PAGE with whale image and opening player choices (directions, play, quit)
def intro_game():
    print "\n" * 80
    print WELCOME_ART
    while True:
        print "What would you like to do?\n1 - Instructions\n2 - Start playing\n3 - Quit\n"
        intro = user_input()
        if intro == "1" or intro == "2" or intro == "3":
            break
        else:
            print "I don't understand. Please choose 1, 2, or 3."
    if intro == "1":
        instructions() 
    elif intro == "2":
        print "Get ready for a WHALE of a good time!"
        time.sleep(1) #these two lines of code insert a 1-second pause
        input_names() #run input_names function to begin play
    else:
        print "Come back soon!"
        exit()


# NAMES FUNCTION: input names of player and other members of whale pod
def input_names():
    print "\n" * 80
    print """
    You're a humpback whale traveling from the waters near Hawaii back to Alaska, 
    after giving birth your calf in September. You'll be traveling in a pod consisting 
    of you, your calf, and two male family members.

    """
    print PLAYER_ART
    print "Your name: "
    names_dict["player"] = user_input()
    print CALF_ART
    print "Your calf's name: "
    names_dict["calf"]  = user_input()
    print FAMILY_ART
    print "Your first family member's name: "
    names_dict["family1"]  = user_input()
    print FAMILY_ART
    print "Your second family member's name: "
    names_dict["family2"]  = user_input()
    return names_dict



# PREPARE FUNCTION: input how long to stay and eat and rest before starting journey
    print "\n" * 80
    print BAIT_BALL_ART
    print """

    You and your pod are migrating north, to abundant feeding grounds. You have
    spent the winter in the warm waters near Hawaii, where you gave birth to %s
    in September. These waters don't have much food, so you have been fasting and 
    living off of your fat stores since you left Alaska several months ago.

    """ % names_dict["calf"]

    #prompt user to declare a month to begin journey, validate choice, assign choice
    #a health impact, with March being ideal
    while True:
        print "When would you like to leave?\n1 - February\n2 - March\n3 - April\n4 - May\n5 - help me decide"
        departure = user_input()
        if departure == "1" or departure == "2" or departure == "3" or departure == "4":
          break
        elif departure == "5":
          print """
    
    Before you leave, you need to be sure %s is ready for such a grueling trip. 
    You will need to spend some time weaning and training %s to dive. This usually
    takes about 5-6 months from the time a calf is born.

    You'll also need to rest up to prepare for your migration. However, you don't 
    want to leave too late, or you won't have enough fat stores to make your long 
    journey.

          """ % (names_dict["calf"], names_dict["calf"])
        else:
          print "I don't understand. Please choose 1, 2, 3, 4, or 5."
    if departure == "1":
        health_dict["prepare_health"] -= 2
    elif departure == "2":
        health_dict["prepare_health"] += 5
    elif departure == "3":
        health_dict["prepare_health"] -= 2
    else:
        health_dict["prepare_health"] -= 5



# MIGRATE FUNCTION: input migration speed; can return and change this option at any time, which changes health
def migrate():
    print "\n" * 80
    print POD_ART
    print "Type 'migrate' to return to this page and change your choice at any time."
    while True:
        print """

    How fast do you want to travel?
    1 - 1mph
    2 - 3mph
    3 - 5mph
    4 - help me decide

        """
        speed = user_input()
        if speed == "1" or speed == "2" or speed == "3":
            break
        elif speed == "4":
            print """
        
    Humback whales can travel as fast as 5mph. However, they travel 24 hours
    per day during their migration and can get fatigued at such high speeds.
    In ideal conditions during migration, humpbacks usually average between
    1-2 mph.

        """
        else:
            print "I don't understand. Please choose 1, 2, 3, or 4."
    if speed == "1":
        health_dict["speed_health"] = 5
    elif speed == "2":
        health_dict["speed_health"] = 2
    else:
        health_dict["speed_health"] = -5
    play_game()


# MAIN PLAY FUNCTION loops game play: randomly calls new events; loop only breaks with win or death
def play_game():
  while True:
    current_health = calculate_health()
    #if location....
      #win()
      #break
    #elif current_health <= -30
    if current_health <= -30:
      death()
      break
    else:
      random_event = random.randrange(20)
      print "\n" * 80
      print POD_ART
      if random_event == 0:
        health_dict["migration_health"] += boat_hazard()#will this break the loop bc it sends it to a function with a return?
      # elif random_event == 2:
      #   health_dict["migration_health"] += orca_hazard()
      # elif random_event == 4:
      #   health_dict["migration_health"] += entanglement_hazard()
      # elif random_event == 6:
      #   health_dict["migration_health"] += gyre_hazard()
      # elif random_event == 8:
      #   health_dict["migration_health"] += weather_choice()
      # elif random_event == 10:
      #   health_dict["migration_health"] += feed_choice()
      # elif random_event == 12:
      #   health_dict["migration_health"] += communicate_choice()
      else:
        print "Day:", calculate_date()
        print "Health:", current_health
        print "Location:" #, calculate_location()
        time.sleep(3)


# Function to continue game play after random event; gives user regular option to exit
def continue_game():
    while True:
        print "Type '1' to continue."
        response = user_input()
        if response == "1":
          play_game()
          break


# FUNCTIONS FOR VARIOUS CHOICES/HAZARDS:
def boat_hazard():
  random_boat = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print BOAT_ART
    print """
    
    As you're traveling, you see a whale-watching boat ahead.
    
    What do you do?

      1 - Approach the boat and give them a show!
      2 - Make your route longer to avoid the boat.
      3 - Continue on your planned route and see what happens.

      """
    boat_choice = user_input()
    if boat_choice == "1" or boat_choice == "2" or boat_choice == "3":
      break
    else:
      print "I don't understand. Please choose 1, 2, or 3."
  if boat_choice == "1" and random_boat == 0:
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale #pulls random pod member name
    continue_game()
    return -10
  elif boat_choice == "1" and random_boat == 1:
    print CAMERA_ART
    print """

    They loved it! Photos of your pod appear on Instagram, and lead thousands 
    of people donating to pro-whale NGOs.

    

    """
    continue_game()
    return 5
  elif boat_choice == "2" and random_boat == 0:
    print "Oh, no! You extend your route, but the current is heavy and there's no food."
    continue_game()
    return -5
  elif boat_choice == "2" and random_boat == 1:
    print "You discover schools of anchovies on this new route and fill your bellies."
    continue_game()
    return 10
  elif boat_choice == "3" and random_boat == 0:
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale
    continue_game()
    return -10
  else:
    print "You continue and are able to avoid the boat, which changes direction."
    continue_game()
    return 5
  
#def orca_hazard()
#def entanglement_hazard()
#def gyre_hazard()
#def weather_choice()
#def feed_choice()
#def communicate_choice()

# OTHER POSSIBLE HAZARDS/CHOICES
# route choices at key points, based on location, based on speed and time passed
# whalers/harvest
# starving and illness
# habitat impacts




# LOCATION FUNCTION to calculate pod's location
# def calculate_location(): need agorithm based on time within game
# combined with hazards/choices and migration map


# DATE FUNCTION to function to calculate date, using elapsed time in game and input start date
def calculate_date():
  elapsed_time = (time.time() - start_time)/10
  return int(elapsed_time)
# need to pull start date from prepare(); then, need to use elapsed time to decide how much to add
# >>> from datetime import datetime, timedelta
# >>> s = '2004/03/30'
# >>> date = datetime.strptime(s, "%Y/%m/%d")
# >>> modified_date = date + timedelta(days=1)
# >>> datetime.strftime(modified_date, "%Y/%m/%d")
# '2004/03/31'


# HEALTH FUNCTION to calculate health, based on speed and hazards
def calculate_health():
#need to modify algorithm -- this is just for testing
    health = 5 + health_dict["prepare_health"] + health_dict["speed_health"] + health_dict["migration_health"]

    if health <= -10:
      health_return = "Very poor"
    elif health <=0 and health > -10:
      health_return = "Poor"
    elif health <=10 and health > 0:
      health_return = "Fair"
    elif health <=20 and health > 10:
      health_return = "Good"
    else:
      health_return = "Excellent"

    return health_return

# Possible project expansion: separate health calculator for each whale in the pod



#WIN SCREEN
# make it to northern feeding grounds and win --> based on location function
# def win():
# if statement based on calculate_location()
#   print exciting win statement


# DEATH FUNCTION defines how player can lose
def death():
  print """
  Image of dead whale.

  You died. Sad."""


#MAIN FUNCTION to call all other functions
def main(): 
    intro_game()
    prepare()
    migrate()


#ASCII art: global constants; listed here to keep code clean
PLAYER_ART = """

                            ','. '. ; : ,','
                              '..'.,',..'
                                 ';.'  ,'
                                  ;;
                                  ;'
                    :._   _.------------.___
            __      :__:-'                  '--.      
     __   ,' .'    .'             ______________'.      
   /__ '.-  _\___.'          0  .' .'  .'  _.-_.'       
      '._                     .-': .' _.' _.'_.'      
  ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~     
  """

CALF_ART = """
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""

FAMILY_ART = """

                    :._   _.------------.___
            __      :__:-'                  '--.      
     __   ,' .'    .'             ______________'.      
   /__ '.-  _\___.'          0  .' .'  .'  _.-_.'       
      '._                     .-': .' _.' _.'_.'      
  ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
  """

POD_ART = """

  Image of all 4 whales migrating

"""

PLAYER_CALF_ART = """
                                ','. '. ; : ,','
                                  '..'.,',..'
                                     ';.'  ,'
                                      ;;
                                      ;'
                        :._   _.------------.___               .
                __      :__:-'                  '--.          ":"
         __   ,' .'    .'             ______________'.      ___:____     |"\/"|  
       /__ '.-  _\___.'          0  .' .'  .'  _.-_.'     ,'        `.    \  / 
          '._                     .-': .' _.' _.'_.'      |  O        \___/  |
      ~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
"""

WELCOME_ART = """

    ********************************************************************************

                              
                               WELCOME TO WHALE TRAIL!


                                ','. '. ; : ,','
                                  '..'.,',..'
                                     ';.'  ,'
                                      ;;
                                      ;'
                        :._   _.------------.___               .
                __      :__:-'                  '--.          ":"
         __   ,' .'    .'             ______________'.      ___:____     |"\/"|  
       /__ '.-  _\___.'          0  .' .'  .'  _.-_.'     ,'        `.    \  / 
          '._                     .-': .' _.' _.'_.'      |  O        \___/  |
      ~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
      

    ********************************************************************************


    """


ORCA_ART = """

    ~                           ~              ~
       ~~~~     ~          ~~ ~        ~      ~    ~~    
  ~~             _,-''-.     ~~        .-._       ~  ~~~
            ,---':::::::\`.            \_::`.,...__    ~ 
     ~     |::`.:::::::::::`.       ~    )::::::.--'       
           |:_:::`.::::::::::`-.__~____,'::::(        
 ~~~~       \```-:::`-.o:::::::::\:::::::::~::\       ~~~
             )` `` `.::::::::::::|:~~:::::::::|      ~   ~~
 ~~        ,',' ` `` \::::::::,-/:_:::::::~~:/           
         ,','/` ,' ` `\::::::|,'   `::~~::::/  ~~        ~
~       ( (  \_ __,.-' \:-:,-'.__.-':::::::'  ~    ~   
    ~    \`---''   __..--' `:::~::::::_:-'               
          `------''      ~~  \::~~:::'               
       ~~   `--..__  ~   ~   |::_:-'                    ~~~
   ~ ~~     /:,'   `''---.,--':::\          ~~       ~~
  ~         ``           (:::::::|  ~~~            ~~    ~
~~      ~~             ~  \:~~~:::             ~       ~~~
             ~     ~~~     \:::~::          ~~~     ~
    ~~           ~~    ~~~  ::::::                     ~~
          ~~~                \::::   ~~
                       ~   ~~ `--'

"""

BAIT_BALL_ART = """
<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><
    <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  
<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><
"""

FISH_ART = """

        <o)))><

"""

BOAT_ART = """


                        __/___            
                  _____/______|           
         _______/_____\_______\_____     
         \              < < <       |    
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

CAMERA_ART = """


                                    .---.
                                    |[O]|
                             _.==._.'''''.______
                            d __ ___.-''-. _____b
                            |[__]  /.''''.\ _   |
                            |     // /''\  \_)  |
                            |     \  \__/ //    |
                            |      \`.__.'/     |
                            \=======`-..-'======/
                             `-----------------'  

"""


# Calls the main function, to activate all code
if __name__ == '__main__':
    main()
