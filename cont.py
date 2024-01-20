#import keys to check the key the user clicks
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#Defines fucntion
def cont():
  #tells the user to click enter to continue
  print ("Press Enter to continue")
  #while true does error catching
  while True:
    #gets user input
    Enter = getkey()
    #if user clicks enter key the loop breaks
    if Enter == keys.ENTER:
      break
  #screen gets cleared
  os.system('clear')