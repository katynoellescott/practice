#Title page with whale image and opening player choices (directions, play, quit)
def intro_page():
    print "\n" * 80
    print """
    ********************************************************************************

                              
                               WELCOME TO WHALE TRAIL!


                                ','. '. ; : ,','
                                  '..'.,',..'
                                     ';.'  ,'
                                      ;;
                                      ;'
                        :._   _.------------.___
                __      :__:-'                  '--.           .
         __   ,' .'    .'             ______________'.        ":"
       /__ '.-  _\___.'          0  .' .'  .'  _.-_.'       ___:____     |"\/"|
          '._                     .-': .' _.' _.'_.'      ,'        `.    \  /
             '----'._____________.'_'._:_:_.-'--'         |  O        \___/  |
      ~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~


    ********************************************************************************


    """
    while True:
        intro = raw_input("What would you like to do?\n1 - Instructions\n2 - Start playing\n3 - Quit\n")
        if intro == "1" or intro == "2" or intro == "3":
            break
        else:
            print "I don't understand. Please choose 1, 2, or 3."
    if intro == "1":
        print intro #instructions go here
        # Instructions: background on whale migration; you are female whale traveling north
        # with your calf
    elif intro == "2":
        print "Get ready for a WHALE of a good time!"
        #insert a pause
        names() #run names function to begin play
    else:
        print "Come back soon!"
        exit()


#function to collect names of player and other members of whale pod, names will 
#be global variables used throughout rest of game
def names():
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
  ~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~     
  """
    global player 
    player = raw_input("Your name: ")
    print """
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""
    global calf
    calf = raw_input("Your calf's name: ")
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
  ~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~
  """
    global family1
    family1 = raw_input("Your first family member's name: ")
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
  ~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~
  """
    global family2
    family2 = raw_input("Your second family member's name: ")
    prepare()



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
        departure = raw_input("When would you like to leave?\n1 - February\n2 - March\n3 - April\n4 - May\n")
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
#function with while loop to return to traveling option page at any time
# raw_input for how fast to travel -- whales can travel up to 5 mph, but average
#1mph on journey, can travel up to 100 miles per day bc travel 24 hours
#research: http://www.nmfs.noaa.gov/pr/species/mammals/whales/humpback-whale.html




def health():
    departure_health = prepare()

    #need to create algorithm to calculate health from combination of inputs
    print "Health:", departure_health


#main function
def main():
    intro_page()
    health()
    


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
