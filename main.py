# --------------------------------------------------------
#        Name: Lessly Ortiz (This project was done without partners)
# Course Info: CSC111 - Fall 2020
# Description: Submission for Assignment 2
#        Date: 9/29/2020
# --------------------------------------------------------
#Made on Repl.it, if ran on Python IDE change the font size to something lower to appreciate the art or run in linux terminal
#I assumed this was being ran in Python IDE sorry for the lack of color

import random #imports the module needed for the randomizer
from art import * #imports module needed for the banner
#https://pypi.org/project/art/   
#https://medium.com/dev-genius/ascii-art-library-for-python-b37b45ed72fd

lil_acrobat_dudes = text2art("The Magic 8-Ball", font='acrobat') #makes the banner
print(lil_acrobat_dudes) #prints the banner
print("""                                               
                   @@@@@@@@@@@@@@@@@@@@&#                   
               @@@@@@@@@@@@&&&&&&&&&@@@@@@@@#               
            /@%%%@@&&@@@@@@@@&&%@&#((/%&&@@@@@@             
          %#%%%%%&@@@@@%@@&,...... @&#%/*@&%%%@@@           
         (@%%%&&&&&@@@,,,,,,,.......   *@#((///&%@&         
        @#%%&&&&&@@@*,,,,,,,,,,,....      @((/*,*@&@        
       @#%%&&&&&@&@,,,,,,,/@(*@@@@,..      @((/***@@(       
      @##%%&&&&&&@,,,,,,,*@/,,,,,/@...      @((/***@@       
      @#%%&&&&&&&@,,,,,**,*@@@@@//@@...     @##(///%@%      
     *&#%%&&&&&&&@,*,******&@*,,,,,@,...    @##((/(#%(      
      %#%%&&&&&@&@@,,,,,,,,*@@/&@@@,.....  @&%%%###%#/      
      (#%&&&&&@@@@@@,,,,,,,,,,,,,,,...... @&&&&%%%#%(       
       #%%&&&@@@@@@@@@*,,,,,,,,,,,.....,@&&&&&&&&%%#*       
        #%&&&&@@@@@@@@@@&@%,,,,,,,,#@@&&&&&&&&&&%%#/        
         %%&&&@@&@@@@@@@@@@@@@@@@@&@@@@&&&&&&&%%#(,         
           %&&&@@@@@@@@@@@@@@@@@&@&&&&&&&&&&%%%##           
             #&&&@@@@@@@@@@@@@@@@&&&&&&&&&%%%#              
                 &&&@@@@@@@@@@@&&&&&&&&&%%#                 
                      %&&&&&&&&&&&&%%%     """)   #https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
                      #To generate the image of the eight ball
print("Made By:\nLessly Ortiz")
print("Made on Repl.it, \nif ran on Python IDE change the font size to something lower to appreciate the art")
print("_" * 60)

def Eightball():
  question = input("Your question?: ") 
  random_num = random.randint(0, 11) #randomizer 
  if random_num == 0:#these lines 45- 68 are possible outputs and their code
    print("No!!!")
  elif random_num == 1:
    print("Yes...")
  elif random_num == 2:
    print("Maaybeeee????")
  elif random_num == 3:
    print("Ask me later")
  elif random_num == 4:
    print("No, leave me alone")
  elif random_num == 5:
    print("yes <3")
  elif random_num == 6:
    print("i don't think i should answer that question...")
  elif random_num == 7:
    print("i don't know actually")
  elif random_num == 8:
    print("( ͡~ ͜ʖ ͡°)")
  elif random_num == 9:
    print("no <3")
  elif random_num == 10:
    print("yessir")
  elif random_num == 11:
    print("Accept the things you cannot change. Have the courage to change the things you can and have the wisdom to know the difference.")#Source: Justice League-Flashpoint movie
  user_input = input("Would you like to continue?")#asks the user for input
  user_input = user_input.lower() #for in case the inputed "no" has some form of capitalization 
  if user_input == "no": 
    print("")
  else:
    Eightball()
  #^ restarts the program from the top

Eightball() #starts the definition 

  

 






    