# WHALE TRAIL, A CHOOSE YOUR OWN ADVENTURE GAME BY KATY SCOTT
import random
import time
from datetime import datetime, timedelta

# Assign game start time, so elapsed time can be used to calculate the date of the journey in the calculate_date() function
# is this an appropriate use of a global variable, or is there a better way?
# start_time = time.time() 

# DICTIONARIES to pass player names, health score, and location info
# Assign default player names, in case player bypasses names screen accidentally
names_dict = {"player": "you", "calf":"your calf", "family1":"your brother","family2":"your cousin"}
health_dict = {"prepare_health":0, "speed_health": 0, "migration_health":0, "game_play_loop":0}
location_dict = {"game_play_loop":0, "gps":0}

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

    Humpback whales migrate from Alaska to Mexico each winter, in one of the longest
    migrations of any mammal on Earth. In the warm waters of Mexico, the whales breed 
    and, about 11 months later, return to give birth. Although these waters have less 
    food, they also have fewer predators, making them safer for newborn calves. 

    In this game, you have just given birth to your calf near Mexico. Now, after 
    months of fasting, you are about to make the 6,000-mile journey back to the 
    abundant feeding grounds near Alaska. On your journey, you'll need to find food, 
    protect your pod and avoid hazards like weather, ocean pollution, boats, and 
    killer whales.

    TO PLAY: follow the prompts on each screen to make your next decision. The health
    of your pod depends on these decisions -- you'll see this health displayed on
    each screen of play.

    Once you select an option, you're tied to it, with one exception. TO ADJUST
    YOUR SPEED: type 'migrate' at any time.

    TO QUIT: type 'exit' at any time.
    TO RETURN TO THIS PAGE: type 'help' at any time.

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
    You're a humpback whale traveling from your mating and calving area near Mexico 
    back to your feeding grounds near Alaska, after giving birth your calf in September. 
    You'll be traveling in a pod consisting of you, your calf, and two male family 
    members.

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
def prepare():
    print "\n" * 80
    print BAIT_BALL_ART
    print """

    You and your pod are migrating north, to abundant feeding grounds. You have
    spent the winter in the warm waters near Mexico, where you gave birth to %s
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
    1 - 3mph
    2 - 5mph
    3 - 10mph
    4 - help me decide

        """
        speed = user_input()
        if speed == "1" or speed == "2" or speed == "3":
            break
        elif speed == "4":
            print """
        
    Humback whales can travel as fast as 15mph, in quick bursts when escaping danger. 
    However, they travel 24 hours per day during their migration and can get fatigued 
    at such high speeds. During migration, humpbacks average about 2-3 mph.

        """
        else:
            print "I don't understand. Please choose 1, 2, 3, or 4."
    if speed == "1":
        health_dict["speed_health"] = 5
    elif speed == "2":
        health_dict["speed_health"] = 0
    else:
        health_dict["speed_health"] = -5
    play_game()


# MAIN PLAY FUNCTION loops game play: randomly calls new events, loop only breaks with win or death
def play_game():
  while True:
    location_dict["game_play_loop"] += 1
    current_health = calculate_health()
    current_location = calculate_location()
    if location_dict["gps"] > 6000:
      win()
      break
    elif current_health <= -30:
      death()
      break
    else:
      random_event = random.randrange(20)
      print "\n" * 80
      print POD_ART
      if random_event == 0:
        health_dict["migration_health"] += boat_hazard()
      elif random_event == 2:
        health_dict["migration_health"] += orca_hazard()
      elif random_event == 4:
        health_dict["migration_health"] += entanglement_hazard()
      elif random_event == 6:
        health_dict["migration_health"] += gyre_hazard()
      elif random_event == 8:
        health_dict["migration_health"] += weather_choice()
      elif random_event == 10:
        health_dict["migration_health"] += feed_choice()
      elif random_event == 12:
        health_dict["migration_health"] += communicate_choice()
      else:
        print "Day:", calculate_date()
        print "Health:", current_health
        print "Miles Traveled:", int(location_dict["gps"])
        print "Location:" , current_location
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
    print "\n" * 80
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
    print FAIL_WHALE_ART
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale #pulls random pod member name
    continue_game()
    return -10
  elif boat_choice == "1" and random_boat == 1:
    print CAMERA_ART
    print """

    They loved it! Photos of your pod appear on Instagram, and lead to thousands 
    of people donating to pro-whale NGOs.

    """
    continue_game()
    return 5
  elif boat_choice == "2" and random_boat == 0:
    print FAIL_WHALE_ART
    print "Oh, no! You extend your route, but the current is heavy and there's no food."
    continue_game()
    return -5
  elif boat_choice == "2" and random_boat == 1:
    print BAIT_BALL_ART
    print "You discover schools of anchovies on this new route and fill your bellies. Yum!"
    continue_game()
    return 10
  elif boat_choice == "3" and random_boat == 0:
    print FAIL_WHALE_ART
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale
    continue_game()
    return -10
  else:
    print "You continue and are able to avoid the boat, which changes direction."
    continue_game()
    return 5


def orca_hazard():
  random_orca = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print ORCA_ART
    print """
    
    As you're traveling, you see a pod of orcas.
    
    What do you do?

      1 - Approach the orcas.
      2 - Make your route longer to avoid the orcas.

      """
    orca_choice = user_input()
    if orca_choice == "1" or orca_choice == "2":
      break
    else:
      print "I don't understand. Please choose 1 or 2."
  if orca_choice == "1":
    print ORCA_ART
    if "calf" in names_dict == True:
      print """
      Oh, no! The orcas attack. They pull %s to the bottom of the ocean by 
      the tail, and drown the calf. They eat its tongue and move along.
      """ % names_dict["calf"]
      del names_dict["calf"]
      continue_game()
      return -20
    else:
      print """
      Oh, no! The orcas attack %s. The whale is able to get away, but sustained
      serious injury.

      """ % random_whale
      continue_game()
      return -20
  elif orca_choice == "2" and random_orca == 0:
    print FAIL_WHALE_ART
    print """
    Oh, no! You extend your route, but the orcas chase you. You must increase 
    your speed. You get away, but your pod is fatigued and hungry."""
    feed_choice()
    return -5
  else:
    print "Good thinking! You avoid the orcas and continue safely on your journey."
    continue_game()
    return 5


def entanglement_hazard():
  random_entangle = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print ENTANGLE_ART
    print """
    
    Oh, no! While traveling, %s became entangled in a gillnet.
    What do you do?

      1 - Work as a team to try to remove the net.
      2 - Continue traveling, and hope the net will fall away.

      """ % random_whale
    entangle_choice = user_input()
    if entangle_choice == "1" or entangle_choice == "2":
      break
    else:
      print "I don't understand. Please choose 1 or 2."
  if entangle_choice == "1" and random_entangle == 0:
    print FAIL_WHALE_ART
    print "Oh, no! The gillnet became even more entangled, leading to serious injury." 
    continue_game()
    return -10
  elif entangle_choice == "1" and random_entangle == 1:
    print POD_ART
    print "The pod managed to remove the net. Good work!"
    continue_game()
    return 5
  elif entangle_choice == "2" and random_entangle == 0:
    print FAIL_WHALE_ART
    print "Oh, no! The gillnet became even more entangled, leading to serious injury."
    continue_game()
    return -5
  else:
    print FAMILY_ART
    print "You continue and the net falls away in a few hours, without injury."
    continue_game()
    return 5


def gyre_hazard():
  random_gyre = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print """
    
    In this part of the journey, you can travel farther out, in the deeper ocean, 
    where the route is clearer, but there is less food. Or you can travel closer 
    to shore, where there is more food, but there are more people and boats.
    
    What do you do?

      1 - Travel in the deeper ocean.
      2 - Travel closer to shore.

    """
    gyre_choice = user_input()
    if gyre_choice == "1" or gyre_choice == "2":
      break
    else:
      print "I don't understand. Please choose 1 or 2."
  if gyre_choice == "1":
    print GYRE_ART
    print """
    Oh, no! In the deep ocean, you come across the Pacific gyre -- where the ocean 
    is like a soup of plastic trash. You can't avoid it, so you must swim through
    it. In the gyre, while eating, your pod accidentally eats a lot of tiny plastic
    pieces mixed in with your prey. %s gets sick.

    """ % random_whale 
    continue_game()
    return -10
  elif gyre_choice == "2" and random_gyre == 0:
    print BOAT_ART
    print "Oh, no! Closer to shore, a boat runs into %s, seriously injuring the whale." % random_whale
    continue_game()
    return -5
  else:
    print BAIT_BALL_ART
    print "Closer to shore, you come across schools of anchovies. Yum!"
    continue_game()
    return 5
    

def weather_choice():
  random_weather = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print WEATHER_ART
    print """
    
    There's a heavy storm approaching from off-shore. What do you do?

      1 - Continue along your route.
      2 - Slow down, rest and feed while you wait for the storm surge to pass.
      3 - Move closer to shore, to try to avoid the worst of the storm surge.
      4 - Move farther out to the deep sea, to try to maneuver around the storm.

      """
    weather_choice = user_input()
    if weather_choice == "1" or weather_choice == "2" or weather_choice == "3" or weather_choice == "4":
      break
    else:
      print "I don't understand. Please choose 1, 2, 3 or 4."
  if weather_choice == "1" and random_weather == 0:
    print POD_TAIL_ART
    print "The storm surge passes without a problem, and you continue on your way."
    continue_game()
    return 3
  elif weather_choice == "1" and random_weather == 1:
    print FAIL_WHALE_ART
    print """
    
    Oh, no! You get stuck in the storm surge and %s in the heavy currents.
    Your pod needs to double-back to find the whale. You find her, but she's fatigued and
    hungry after trying to swim against the current.

    """ % random_whale
    continue_game()
    return -10
  elif weather_choice == "2" and random_weather == 0:
    print FAIL_WHALE_ART
    print """
    
    Oh, no! While waiting for the storm to pass, your pod gets stuck in a strong
    current and pulled way off route. You're all fatigued and hungry by the time
    you're able to escape the surge.

    """
    continue_game()
    return -5
  elif weather_choice == "2" and random_weather == 1:
    print BAIT_BALL_ART
    print """
    
    Well done! You fill your bellies and get some much needed rest, while the storm
    passes. Then, you continue on your route.

    """
    continue_game()
    return 5
  elif weather_choice == "3" and random_weather == 0:
    print FAIL_WHALE_ART
    print """

    Oh, no! Closer to shore, the current pushes %s onto the beach, where he gets 
    stranded. After the storm passes, locals are eventually able to push him back
    out to sea, but he's fatigued and sick.

    """ % random_whale
#if possible, kill this random_whale and remove from dictionary

    continue_game()
    return -10
  elif weather_choice == "3" and random_weather == 1:
    print BAIT_BALL_ART
    print """
    
    You take shelter in an inlet, where the storm surge is minimal. While waiting
    for the storm to pass, you find schools of small fishes and feast!

    """
    continue_game()
    return 5
  elif weather_choice == "4" and random_weather == 0:
    print FAIL_WHALE_ART
    print """
    
    It takes longer than expected to fight the current to get around the storm.
    You succeed, but it the pod is tired and %s is getting dangerously thin.

    """ % random_whale
    continue_game()
    return -5
  else:
    print POD_ART
    print """

    Success! You make your way around the storm and are back on route quicker
    than expected.
    
    """
    continue_game()
    return 5


def feed_choice():
  random_feed = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print FISH_ART
    print """
    
    Your pod is fatigued and needs food.
    What do you do?

      1 - Communicate with your pod to work as a team to capture sardines.
      2 - Split up and hunt independently.
      3 - Move closer to shore, where there are more schools of smaller fishes.

      """
    feed_choice = user_input()
    if feed_choice == "1" or feed_choice == "2" or feed_choice == "3":
      break
    else:
      print "I don't understand. Please choose 1, 2, or 3."
  if feed_choice == "1":
    print BAIT_BALL_ART
    print """
    
    Great job! Your pod works together to go underwater and blow bubbles that form 
    a sort of bubble net, trapping schools of fishes. Then, you take turns feasting on 
    the trapped food. Your pod is full and happy!

    """
    continue_game()
    return 10
  elif feed_choice == "2" and random_feed == 0:
    print FAIL_WHALE_ART
    print """
    Oh, no! You lose track of %s and the pod must spend hours searching to find 
    the calf. After you're reunited, you're all even more fatigued and hungry.

    """ % names_dict["calf"]
    continue_game()
    return -5
  elif feed_choice == "2" and random_feed == 1:
    print BAIT_BALL_ART
    print "You're all able to find and eat krill. Yum!"
    continue_game()
    return 5
  elif feed_choice == "3" and random_feed == 0:
    print FAIL_WHALE_ART
    print """
    Oh, no! Closer to shore, there are more people. %s collides with a boat and 
    is seriously injured.""" % random_whale
    continue_game()
    return -10
  else:
    print BAIT_BALL_ART
    print "Good plan! Closer to shore, you find several schools of sardines to feast upon."
    continue_game()
    return 5


def communicate_choice():
  random_communicate = random.randrange(2)
  random_whale = random.choice(names_dict.values())
  while True:
    print "\n" * 80
    print POD_TAIL_ART
    print """
    
    In the distance, you see another pod of migrating humpbacks. What do you do?

      1 - Approach the pod and communicate to learn about the area.
      2 - Adjust your route to avoid the pod.

      """
    comm_choice = user_input()
    if comm_choice == "1" or comm_choice == "2":
      break
    else:
      print "I don't understand. Please choose 1 or 2."
  if comm_choice == "1":
    print COMM_ART
    print """
    
    You use a series of movements to communicate with the pod (whale songs are only
    used for mating), and learn about a food source nearby. You work with this other
    pod to trap schools of small fishes and feast on them. Everyone is full and happy!

    """
    continue_game()
    return 10
  elif comm_choice == "2" and random_communicate == 0:
    print FAIL_WHALE_ART
    print """
    
    Oh, no! In your attempt to avoid the pod, you lead your pod too close to some
    underwater rocks. %s gets scratched pretty badly.

    """ % random_whale
    continue_game()
    return -10
  else:
    print POD_ART
    print "You successfully avoid the pod and continue on your journey."
    continue_game()
    return 0



# LOCATION FUNCTION to calculate pod's location
def calculate_location():
  speed = health_dict["speed_health"]

#use current speed per 8 hours to re-assign miles traveled (b/c each game loop is 8 hours)
  if speed == "1":
    location_dict["gps"] += 24
  elif speed == "2":
    location_dict["gps"] += 40
  else:
    location_dict["gps"] += 80 

#report location based on miles traveled
  if location_dict["gps"] >= 0 and location_dict["gps"] < 750:
    return "waters off Baja, Mexico"
  elif location_dict["gps"] >= 750 and location_dict["gps"] < 1500:
    return "waters off Southern California"
  elif location_dict["gps"] >= 1500 and location_dict["gps"] < 2250:
    return "Monterey Bay"
  elif location_dict["gps"] >= 2250 and location_dict["gps"] < 3000:
    return "waters off Northern California"
  elif location_dict["gps"] >= 3000 and location_dict["gps"] < 3750:
    return "waters off Oregon"
  elif location_dict["gps"] >= 3750 and location_dict["gps"] < 4500:
    return "waters off Washington"
  elif location_dict["gps"] >= 4500 and location_dict["gps"] < 6000:
    return "waters off British Columbia, Canada"
  elif location_dict["gps"] >= 6000:
    return "waters off Alaska!"
  else:
    return "???"#test to ensure this function is working properly


# DATE FUNCTION to calculate date, using number of game play loops and input start date
def calculate_date():
  elapsed_time = (location_dict["game_play_loop"])/3
  if health_dict["prepare_health"] == 2:
    starting_date = 'February 15'
  elif health_dict["prepare_health"] == 5:
    starting_date = 'March 15'
  elif health_dict["prepare_health"] == -2:
    starting_date = 'April 15'
  else:
    starting_date = 'May 15'
  date = datetime.strptime(starting_date, "%B %d")
  current_date = date + timedelta(days=elapsed_time)
  return datetime.strftime(current_date, "%B %d")


# HEALTH FUNCTION to calculate health, based on speed and hazards
def calculate_health():
#need to modify algorithm -- this is just for testing
#instead of changing speed health, add to it, like migration health so there's impact if wrong speed for extended periods of time
  health = health_dict["prepare_health"] + health_dict["speed_health"] + health_dict["migration_health"]

  if health <= -20:
    death()
  elif health <= -10 and health > -20:
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

    #when health gets too low, one of the whales dies and is removed from dictionary -- NOT player
    #after death of a whale, health increases slightly to stop all the whales from dying in a row
    #when all whales dead, you die/lose?


#WIN SCREEN
def win():
  print """

YOU WIN WHALE TRAIL!!!

Image of happy whales and lots of fish.

Hooray! You arrived at your summer feeding grounds! You and your pod will spend the
next 6 months feeding on the abundant food here before returning to Mexico to breed.

  """
  print "GAME OVER"
  exit()


# DEATH FUNCTION if player loses
def death():
  print DEAD_POD_ART
  print "Your pod died of" #, NEED TUPLE OF DEATHS TO PULL FROM RAMDONLY
  print "GAME OVER"
  exit()


#MAIN FUNCTION to call all other functions
def main(): 
    intro_game()
    prepare()
    migrate()


# POSSIBLE PROJECT EXPANSIONS:
  # separate health calculator for each whale in the pod
  # hunger function and read-out
  # more choices embedded in hazards, based on result of choice
  # route choices at key points, based on location, based on speed and time passed
  # whalers/harvest
  # starving and illness
  # habitat impacts



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

       ___.------------._   _.: 
   .--'                  '-:__:      __ 
 .'______________             '.    '. ',    __  
  '._-._  '.  '. '.  0          '.____\_  -.' __\      
     '._'._ '._ '. :'-.                     _.'        
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
  """

POD_ART = """

         ','. '. ; : ,','             ','. '. ; : ,','                              ','. '. ; : ,','
          '..'.,',..'                   '..'.,',..'                                   '..'.,',..'
            ';.'  ,'                      ';.'  ,'                                      ';.'  ,'
             ;;                            ;;                  .                         ;;
             ;'                            ;'                 ":"                        ;'
:._   _.------------.___      :._   _.------------.___      ___:____      :._   _.------------.___        
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^  

"""

POD_TAIL_ART = """


           \`''\/''`/   \`''\/''`/    \`''\/''`/
            \      /     \      /      \      /    |"\/"|
             |    |       |    |        |    |      \  /
             /    \       /    \        /    \      /  |
^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

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

COMM_ART = """

                            ','. '. ; : ,','
                              '..'.,',..'
                                 ';.'  ,'
                                  ;;
                                  ;'
                    :._   _.------------.___               ___.------------._   _.: 
            __      :__:-'                  '--.       .--'                  '-:__:      __ 
     __   ,' .'    .'             ______________'.   .'______________             '.    '. ',    __    
   /__ '.-  _\___.'          0  .' .'  .'  _.-_.'     '._-._  '.  '. '.  0          '.____\_  -.' __\      
      '._                     .-': .' _.' _.'_.'         '._'._ '._ '. :'-.                     _.'        
  ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~ 


"""

WELCOME_ART = """

  ********************************************************************************

                                    WELCOME TO
                      _           _           _             _ _    _
                     | |         | |         | |           (_) |  | |
            __      _| |__   __ _| | ___     | |_ _ __ __ _ _| |  | |
            \ \ /\ / / '_ \ / _` | |/ _ \    | __| '__/ _` | | |  |_|
             \ V  V /| | | | (_| | |  __/    | |_| | | (_| | | |   _
              \_/\_/ |_| |_|\__,_|_|\___|     \__|_|  \__,_|_|_|  |_|



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


FAIL_WHALE_ART = """

 _|||||||||||||||||\  \____/ 
||||||| =| ; | | ||||   ||  
||||_||_||_|_|_|__|||___||
_____|||||||||||||||/     

"""

#recreate upside down
DEAD_ART = """

       ___.------------._   _.: 
   .--'                  '-:__:      __ 
 .'______________             '.    '. ',    __  
  '._-._  '.  '.| |.  XX        '.____\_  -.' __\      
     '._'._ '._ |_| :'-.                   _.'        
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

"""

#rereate upside down
DEAD_POD_ART = """


                        :._   _.------------.___               
                __      :__:-'                  '--.          
         __   ,' .'    .'             ______________'.      ________     |x\/x|  
       /__ '.-  _\___.'         XX  .| | .'  .'  _.-_.'   ,'        `.    \  / 
          '._                     .-'|_|' _.' _.'_.'      |  X        \___/  |
      ~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~



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

GYRE_ART = """

~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

                               mmm      ~
                  o            )-(                              m
           b                  (   )         o
                              |   |
                              |   |   n
    n              o          |___|
                                                          `   ~


"""


WEATHER_ART = """

                            000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /

"""

ENTANGLE_ART = """



                                    _H_
                                   /___\ 
                                   \888/
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~U~^~^~^~^~^~^~^
                      ~              |
      ~                        o     |        ~
                           o         |
                              O      |
                                     |   ~
                                     #
                                     #
                                   #  _#, 
                                 `#((' \        ~
                                    ))  \ 
                                   ((   ))
                       ~            \  ((
                                      )) `



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
