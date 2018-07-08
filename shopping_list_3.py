#I want to clear the screen between states.
#Whenever we show the list, or the help, or we add a new item, whatever, I want to clear the screen.
#This will make the app seem just a little bit more polished.

#To do all that fist we need to import os
import os

shopping_list = []


#And then we need to make a new function here. Let's call it clear screen.
def clear_screen():
  #os.system which is a function in the OS library.
  #the os library lets me loo at infomartion about the system that my code is running on.
  #It also let's me run system level scripts with this system function. Like the clear script if you non windows computer.
  #This OS.name check tells me whether or not I'm on windows, bu the nt there is for all the modern versions of windows.
  #So if we're on a modern version of windows it will run cls otherwise it'll run clear because we're probably on Linux or Mac.
  #We can add this up into our show help.
  os.system("cls" if os.name == "nt" else "clear")
  


  
def show_help():  
  clear_screen()
  print("What should we pick up at the store?")
  print("""
Enter 'DONE' to stop addig items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list


  """) 
  


    
    

def add_to_list(item):
  #Let's go ahead and show the list.
  show_list() 
  #if there are items in the shopping list.
  if len(shopping_list):
    #The do these tasks below.
    #That's where we put the user input between the two brackets
    position = input("Where should I add {}?\n"
                     "Press ENTER to add to the end of the list\n"
                     "> ".format(item))
    #if this is the first item that goes into the list though then do this task below.
    #If there's nothing on add_to_list there we're gonna assume position is 0
  else:
    position = 0
      
    #Now we have the problem of what if somebody has given us a string because of input?  
    #What if they give us like, some strange random negative number maybe know this is python, they know negative numbers indexes exist.
    #We don't necessarily want to confuse people though by having them accidentally typing -2 and the item goes to the -2 index, when they actually meant for it to go to 2.
    #They're going to try to turn the position into an integer.
    #This ABS stands for absolute. So this gets us the absolute value of the number example: -5 absoute value 5.
    
  try:
    position = abs(int(position))
  #Which when we can't turn position into an integer 
  #If they've given me a string like an "a", then that's turn into valueerror 
  except ValueError:
    #Then make the position = none
    position = None
  #If the position isn't none,
  if position is not None:
    #Position minus 1 because I've been showing them the positions with the one.
    #So we need to decrement this back so it's zero based.
    #The the position minus 1 then we're gonna insert the item.
    shopping_list.insert(position-1, item)
  else:
    #append to whetever the new item is.
    #If they have given us some position or turns out to be none then we're going to just append it to the end of the list no matter what.
    shopping_list.append(new_item)
  
  #Now we call the show_list again 
  show_list()
  
  
  
def show_list():
  clear_screen()
  
  print("Here's your list:")
  
  #let's add new variable here named index and set to 1.
  #So we start counting from 1 
  index = 1
  for item in shopping_list:
    #For each item that's in the shopping list, I'm going to print out a string with a placeholder,
    #a period and another place holder.
    #Then we are going to format that with index and item.
    print("{}. {}".format (index, item))
    #And then we gonna do index += 1. This means increment.
    #This will increment it to 2 and keep going up. Just updates the number each time.
    index += 1
    
    #then we print hypens 10 times
    #At the end we're just gonna print the hypen just to indicate that's the end of the list.
  print("-"*10)  
  
#Here we create a function that will remove items in our list.
def remove_from_list():
  show_list()
  what_to_remove = input('What would you like to remove?\n> ')
  try:
    shopping_list.remove(what_to_remove)
  except ValueError:
    #Then we're just gonna pass or skip over that.
    pass
  #Then we show the list again.
  show_list()

show_help()  


while True:
  
  new_item = input("> ")
  
  #if you type DONE OR QUIT then program breaks.
  if new_item.upper  == 'DONE' or new_item.upper() == 'QUIT':
    break
  #if you type HELP we'll show help  
  elif new_item.upper == 'HELP': 
    show_help() 
    continue 
  #if you type SHOW it will show list  
  elif new_item.upper == 'SHOW': 
    show_list()  
    continue
  elif new_item.upper() == 'REMOVE':
    #Then we want to run the function remove from list
    remove_from_list()
  #We'll make this one else. Anything that comes in is going to automatically be added to the lists,
  #if its not done quit, help, or show.
  else:
    add_to_list(new_item) 
  
show_list() 





