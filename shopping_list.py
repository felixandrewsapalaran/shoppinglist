#This program lets you make a list and print them out after typing DONE.


#make a list to hold onto our items
shopping_list = []

#print out instructions on how to use the app
print("To do list:")
print("Enter 'DONE' to stop adding items.")

#This while condition will keep asking for input until you met its condition.
while True:
  #ask for new items
  new_item = input("- ")
  
  #This if condition will stop the while loop for asking input when you type DONE.
  #be able to quit the app
  if new_item  == 'DONE': 
  #This break keyword will terminate the while loop.  
    break

#add new items to our list. We called shopping_list to add new item in our list. In addtion we gave it a parameter or argument new_item so that way it will ask the user for more items to add in our list.
  shopping_list.append(new_item) 

#print out the list. After typing DONE this message below print that along with the list we have listed during the process.
print("Here's your list:")

#Here we used for loop to repeat printing each list we have listed.
for item in shopping_list:
  print(item)