#function for all input, which will allow user to use universal commands like
#'exit' and 'help'
def user_input():
    while True:
        input = raw_input("")
        if input.lower() == 'exit': 
          exit()
        elif input.lower() == 'help':
          intructions()
        elif input.lower() == 'migrate':
          migrate()
        elif input == "":
         print "Please type your option."
        else:
          return input


#function to display instructions for play
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
#what if they select this option but haven't yet entered their whale names?
    else:
        print "Come back soon!"
        exit()


#Title page with whale image and opening player choices (directions, play, quit)
def intro_game():
    print "\n" * 80
    print """
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
        import time
        time.sleep(1) #these two lines of code insert a 1-second pause
        input_names() #run input_names function to begin play
    else:
        print "Come back soon!"
        exit()


# collect names of player and other members of whale pod; names defined as 
# global variables b/c used throughout multiple functions and don't change
def input_names():
    print "\n" * 80
    print """
    You're a humpback whale traveling from the waters near Hawaii back to Alaska, 
    after giving birth your calf in September. You'll be traveling in a pod consisting 
    of you, your calf, and two male family members.

    """
    print """

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
    print "Your name: "
    global player 
    player = user_input()
    print """
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""
    print "Your calf's name: "
    global calf
    calf = user_input()
    print """

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
    print "Your first family member's name: "
    global family1
    family1 = user_input()
    print """

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
    print "Your second family member's name: "
    global family2
    family2 = user_input()
    #does prepare() need to be called here or in main code???



# PREPARE FUNCTION: input how long to stay and eat and rest, to build up fat store 
# for journey and to ensure calf is ready for journey
def prepare():
    print "\n" * 80
    print """

<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><
    <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  
<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><

    You and your pod are migrating north, to abundant feeding grounds. You have
    spent the winter in the warm waters near Hawaii, where you gave birth to %s
    in September. These waters don't have much food, so you have been fasting and 
    living off of your fat stores since you left Alaska several months ago.

    """ % calf

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

          """ % (calf, calf)
        else:
          print "I don't understand. Please choose 1, 2, 3, 4, or 5."
    if departure == "1":
        return -2
    elif departure == "2":
        return 5
    elif departure == "3":
        return -2
    else:
        return -5



#CONSTANT TRAVELING OPTIONS
# raw_input for how fast to travel -- whales can travel up to 5 mph, but average
#1mph on journey, can travel up to 100 miles per day bc travel 24 hours
#research: http://www.nmfs.noaa.gov/pr/species/mammals/whales/humpback-whale.html
#how can player return to game if exit game to reset migration speed?
def migrate():
    print "\n" * 80
    print "Type 'migrate' to return to this page and change your choice at any time."
    while True:
        print """

    How fast do you want to travel?
    1 - 5mph
    2 - 3mph
    3 - 1mph
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
        return -5
    elif speed == "2":
        return -2
    else:
        return 2


# function that loops game play: constant image of whales migrating, with readout of health, speed, location
# randomly calls new events; these new events should return to this function after running,
# to continue the looped game play; loop only breaks with win or death
def play_game():
  departure_health = prepare()
  speed_health = migrate()
  while True: #how do I break this loop? It should only break if you die or win...
    import random
    random_event = random.randrange(20)
    print """


Image of whales migrating

  """
    if random_event == 0:
      boat_hazard()#will this break the loop bc it sends it to a function with a return?
    # elif random_event == 2:
    #   #insert event function
    # elif random_event == 4:
    #   #insert event function
    # elif random_event == 6:
    #   #insert event function
    # elif random_event == 8:
    #   #insert event function
    else:
      print "Health:", calculate_health(departure_health, speed_health)
      print "Location:" #, calculate_location()
      import time #how do I not repeat imports???
      time.sleep(3) #these two lines of code insert a 3-second pause




#INTERMITTENT TRAVELING OPTIONS
#route choices at key points, based on location, based on speed and time passed
#weather choices -- random
#stop to eat
#join other pods
#communicate with other whales



#HAZARDS
#function to determine which hazards happen when -- based on traveling options
#hazards include plastic gyre, killer whales, weather, whalers, starving and
#illness
# entanglement in fishing gear (bycatch)
# ship strikes
# whale watch harassment
# habitat impacts
# harvest



def boat_hazard():
  import random
  random_boat = random.randrange(2)
  random_whale = random.choice([player, calf, family1, family2])
  while True:
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
  from random import choice
  if boat_choice == "1" and random_boat == 0:
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale
    return -10
  elif boat_choice == "1" and random_boat == 1:
    print """

    They loved it! Photos of your pod appear on Instagram, and lead thousands 
    of people donating to pro-whale NGOs.

    """
    return 5
  elif boat_choice == "2" and random_boat == 0:
    print "Oh, no! You extend your route, but the current is heavy and there's no food."
    return -5
  elif boat_choice == "2" and random_boat == 1:
    print "You discover schools of anchovies on this new route and fill your bellies."
    return 10
  elif boat_choice == "3" and random_boat == 0:
    print "Oh, no! %s collides with the boat and is seriously injured." % random_whale
    return -10
  else:
    print "You continue and are able to avoid the boat, which changes direction."
    return 5



# function to calculate location
# def calculate_location(): need agorithm based on time within game
# combined with hazards/choices


#function to calculate health, based on speed and hazards
def calculate_health(departure, speed):
    #need to repeatedly recalculate this, based on changing user input... use while loop?
    #how do I recalculate without re-running functions that the user doesn't want? Maybe
    #two functions are needed -- one to call functions, based on game order and user choices.
    #a second function to calculate health based on passed variables

#need to modify algorithm -- this is just for testing
    health = 5 + departure + speed

#need to add threshold for death
    if health <= -5:
      health_return = "Very poor"
    elif health <=0 and health > -5:
      health_return = "Poor"
    elif health <=5 and health > 0:
      health_return = "Fair"
    elif health <=10 and health > 5:
      health_return = "Good"
    else:
      health_return = "Excellent"

    return health_return

    #health increases with more food (baby whales gain 200 pounds per day)
    #health decreases with less food, plastic gyre, fights with orcas, whalers
    #health decreases with fast pace
    #health increases with communication with other whales, joining other pods
    #does each whale need a health calculator, or one for the whole pod and then
    #randomly select who gets ill, with player being less likely? OR do I need to have
    #a health function for EACH member of the pod??? Maybe do this if making it more complex


#WIN SCREEN
#make it to northern feeding grounds and win --> based on location function?

#DEATH SCREEN
#health drops too low and you die --> based on health function?


#main function
def main(): 
    intro_game()
    play_game()



if __name__ == '__main__':
    main()


#VISUALS
#whale traveling through waters at top of every page
#health, speed, hunger (weight?) displayed on each page
#page changes with every input option
#for new page, clear terminal with print "\n" * 80




#VISUALS
#fish visuals: 
# <o)))><

# humpback whale visuals:
#       .
#       ":"
#     ___:____     |"\/"|
#   ,'        `.    \  /
#   |  O        \___/  |
# ~^~^~^~^~^~^~^~^~^~^~^~^~
  # .-------------'```'----....,,__                        _,
  # |                               `'`'`'`'-.,.__        .'(
  # |                                             `'--._.'   )
  # |                                                   `'-.<
  # \               .-'`'-.                            -.    `\
  #  \               -.o_.     _                     _,-'`\    |
  #   ``````''--.._.-=-._    .'  \            _,,--'`      `-._(
  #     (^^^^^^^^`___    '-. |    \  __,,..--'                 `
  #      `````````   `'--..___\    |`
  #                            `-.,'


  #                           ','. '. ; : ,','
  #                             '..'.,',..'
  #                                ';.'  ,'
  #                                 ;;
  #                                 ;'
  #                   :._   _.------------.___
  #           __      :__:-'                  '--.      
  #    __   ,' .'    .'             ______________'.      
  #  /__ '.-  _\___.'          0  .' .'  .'  _.-_.'       
  #     '._                     .-': .' _.' _.'_.'      
  #        '----'._____________.'_'._:_:_.-'--'         
  #~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~ 



# orca (bad guy) visuals:

#     ~                           ~              ~
#        ~~~~     ~          ~~ ~        ~      ~    ~~    
#   ~~             _,-''-.     ~~        .-._       ~  ~~~
#             ,---':::::::\`.            \_::`.,...__    ~ 
#      ~     |::`.:::::::::::`.       ~    )::::::.--'       
#            |:_:::`.::::::::::`-.__~____,'::::(        
#  ~~~~       \```-:::`-.o:::::::::\:::::::::~::\       ~~~
#              )` `` `.::::::::::::|:~~:::::::::|      ~   ~~
#  ~~        ,',' ` `` \::::::::,-/:_:::::::~~:/           
#          ,','/` ,' ` `\::::::|,'   `::~~::::/  ~~        ~
# ~       ( (  \_ __,.-' \:-:,-'.__.-':::::::'  ~    ~   
#     ~    \`---''   __..--' `:::~::::::_:-'               
#           `------''      ~~  \::~~:::'               
#        ~~   `--..__  ~   ~   |::_:-'                    ~~~
#    ~ ~~     /:,'   `''---.,--':::\          ~~       ~~
#   ~         ``           (:::::::|  ~~~            ~~    ~
# ~~      ~~             ~  \:~~~:::             ~       ~~~
#              ~     ~~~     \:::~::          ~~~     ~
#     ~~           ~~    ~~~  ::::::                     ~~
#           ~~~                \::::   ~~
#                        ~   ~~ `--'


#                 O          .
#              O            ' '
#                o         '   .
#              o         .'
#           __________.-'       '...___
#        .-'                      ###  '''...__
#       /   a###                 ##            ''--.._ ______
#       '.                      #     ########        '   .-'
#         '-._          ..**********####  ___...---'''\   '
#             '-._     __________...---'''             \   l
#                 \   |                                 '._|
#                  \__;
