# Have a HELP command 
# Have a SHOW command
#  clean code up in general


#make a list to hold onto our items
shopping_list = []


def show_help():  

  #print out instructions on how to use the app
  print("What should we pick up at the store?")
  print("""
Enter 'DONE' to stop addig items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
  """) #We used miltiline comments here
  

#This part will show the list we have already listed  
def show_list():
  #print out the list.
  print("Here's your list:")
  
  for item in shopping_list:
    print(item)
    
#This function will take new lists. 
def add_to_list(new_item):
  #add new items to our list
  shopping_list.append(new_item)
  print("Added {}. List now has {} items.".format(new_item, len(shopping_list))) # first {} contains somthing and second {} contains some number. len stands for length of the shopping_list. So len is a function that tells us how many things are in a list or an iterable.
  
#Let's just show the help right here right above the while true. So that way the hlp gets shown before the while loop starts running.  
show_help()  


while True:
  #ask for new items 
  new_item = input("> ")
  
  #be able to quit the app
  if new_item  == 'DONE': #What this does is when you type in DONE the program quit using the break keyword.
    break
  elif new_item == 'HELP': #Here we need to check to see if they put in help
    show_help() #Calling out function named show_help()
    continue # Since we don't want to add help into our list, and we don't wanna break, we don't wanna end the loop. We actually just wanna go to the next step of the loop. We wanna run the loop again so we say continue.
  elif new_item == 'SHOW': #Here by typing SHOW this show up our list that we have listed down.
    show_list()  #Calling out our show_list function to display the list.
    continue #And again you wanna go on to the next step of the loop so we say continue again.
  add_to_list(new_item) #We could do an else here but we dont have to. We called funcion add_to_list(new_item) with its parameter named new_item.
  
show_list() #Calling function  named show_list





