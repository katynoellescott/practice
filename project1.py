
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
            migration()
        else:
            return input


#function to display instructions for play
def instructions():
    #add more to these instructions, including following prompts to type in answers
    # Instructions: background on whale migration; you are female whale traveling north
    # with your calf; add info about migration speed here or in migrate function???
    print "\n" * 80
    print """

    To change your migration options, type "migrate" at any time.

    To quit, type 'exit' at any time.
    To return to this page, type 'help' at any time.


    """
    while True:
        #how can the player CONTINUE from last screen, rather than starting over,
        #when instructions are called????
        print "What would you like to do?\n1 - Continue play\n2 - Quit\n"
        next_step = user_input()
        if next_step == "1" or next_step == "2":
            break
        else:
            print "I don't understand. Please choose 1 or 2."
    if next_step == "1":
        print "Katy has to code this to back to the game..."
        #go back to game; how do I do this?
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
        time.sleep(3) #these two lines of code insert a 3-second pause
        input_names() #run input_names function to begin play
    else:
        print "Come back soon!"
        exit()


# collect names of player and other members of whale pod; names defined as 
# global variables b/c used throughout multiple functions and don't change
def input_names():
    print "\n" * 80
    print """
    You're a humpback whale traveling from the equator back to the arctic, after
    giving birth your calf in September. You'll be traveling in a pod consisting 
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



#PREPARE FUNCTION
# raw_input for how long to stay and eat and rest, to build up fat store for journey
# and to ensure calf is ready for journey
def prepare():
    print "\n" * 80
    print """

    You and your pod are migrating north, to abundant feeding grounds. You have
    spent the winter in the warm waters near Hawaii. These waters don't have much
    food, so you have been fasting and living off of your fat stores since you
    left Alaska several months ago.

<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><
    <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  
<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><

    Before you leave, you need to be sure %s is ready for such a grueling trip. 
    You will need to spend some time weaning and training %s to dive. You'll also
    need to rest up to prepare for your migration.

    However, you don't want to leave too late, or you won't have enough fat stores
    to make your long journey.

    """ % (calf, calf)

    #prompt user to declare a month to begin journey, validate choice, assign choice
    #a health impact, with March being ideal
    while True:
        print "When would you like to leave?\n1 - February\n2 - March\n3 - April\n4 - May\n"
        departure = user_input()
        if departure == "1" or departure == "2" or departure == "3" or departure == "4":
            break
        else:
            print "I don't understand. Please choose 1, 2, 3, or 4."
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
def migrate():
    print "Type 'migrate' to return to this page and change your choices at any time."
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




def calculate_health():
    departure_health = prepare()
    speed_health = migrate()
    #need to repeatedly recalculate this, based on changing user input... use while loop?
    #how do I recalculate without re-running functions that the user doesn't want? Maybe
    #two functions are needed -- one to call functions, based on game order and user choices.
    #a second function to calculate health based on passed variables


    #need to create algorithm to calculate health from combination of inputs
    #decide on threshholds for "poor," "fair" and "good", as well as what leads to death
    print "Health:", departure_health + speed_health


#main function
def main():
    intro_game()
    calculate_health()



if __name__ == '__main__':
    main()


#VISUALS
#whale traveling through waters at top of every page
#health, speed, hunger (weight?) displayed on each page
#page changes with every input option
#for new page, clear terminal with print "\n" * 80


#INTERMITTENT TRAVELING OPTIONS
#route choices at key points, based on location, based on speed and time passed
#weather choices -- random
#stop to eat
#join other pods
#communicate with other whales

#HEALTH function
#health increase with more food (baby whales gain 200 pounds per day)
#health decreases with less food, plastic gyre, fights with orcas, whalers
#health decreases with fast pace
#health increases with communication with other whales, joining other pods

#HAZARDS
#function to determine which hazards happen when -- based on traveling options
#hazards include plastic gyre, killer whales, weather, whalers, starving and
#illness
# entanglement in fishing gear (bycatch)
# ship strikes
# whale watch harassment
# habitat impacts
# harvest

#GOAL
#make it to northern feeding grounds

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
