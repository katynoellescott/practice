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
    giving birth your calf. You'll be traveling with your calf, a friend, and her
    calf.

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
         '----'._____________.'_'._:_:_.-'--'         
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
         '----'._____________.'_'._:_:_.-'--'         
  ~^~^~^~^~^~^~^~^~^~^~^~^~ ~^~^~^~^~^~^~^~^~^~^~^~^~ 
  """
    global friend
    friend = raw_input("Your friend's name: ")
    print """
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""
    global friend_calf
    friend_calf = raw_input("Your friend's calf's name: ")
    #how do I pass these variables to other functions?
    #do i need to write a separate function for each name, to pass the variable along with "return"?
    prepare()



#PREPARE FUNCTION
# raw_input for how long to stay and eat and rest, to build up fat store for journey
# and to ensure calf is ready for journey
#function to translate this into an integer
#function uses this integer as one input to determine health throughout journey
def prepare():
    print "\n" * 80
    print """

    You need to build up your fat stores before you leave on your long journey.
    You also need to be sure %s is ready for such a grueling trip. You
    will need to spend some time eating krill and small fish and resting up.

<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><
      <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  
<o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><   <o)))><  <o)))><  <o)))><

    However, you don't want to leave too late, or xxxxx.

    """ % calf
    departure = raw_input("When would you like to leave?\n1 - xxxxx\n2 - xxxxx\n3 - xxxxxx\n")
    #need to add details, based on real stats


#main function
def main():
    intro_page()


if __name__ == '__main__':
    main()


#VISUALS
#whale traveling through waters at top of every page
#health, speed, hunger (weight?) displayed on each page
#page changes with every input option
#for new page, clear terminal with print "\n" * 80

#CONSTANT TRAVELING OPTIONS
#function with while loop to return to traveling option page at any time
# raw_input for how fast to travel -- whales travel 3-5 mph, but travel 100 miles
# per day bc travel 24 hours

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
