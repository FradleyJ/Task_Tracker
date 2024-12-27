# Task_Tracker
Track your task to do with a convenient task-tracker. After viewing the menu or items in the current file. The user will have 5 options 

What task would you like to do?
 0. See the Menu
 1. Create a New Task
 2. Delete an Existing Task
 3. What task would you like to mark as completed?
 4. Exit Program

# User will select the option then walk through program. For example Option 0:]
***Current Menu***

1:Completed
 2:Completed
 4:Completed
 5:eeeeeeeeeeee
 3:Completed
 :Completed
 Upgrade M92P BIOS:Completed


***Current Menu***

# -- The current menu is now posted. Done through reading the file designated in code.
It returns you to the menu option once the action is completed. 
What task would you like to do?
 0. See the Menu
 1. Create a New Task
 2. Delete an Existing Task
 3. What task would you like to mark as completed?
 4. Exit Program
:1
What is the Task Name?
Fradley Test Task

# If we use option 0 we can see the task has been added with the addition of ':Pending: to demonstrate the task
    1:Completed
 2:Completed
 4:Completed
 5:eeeeeeeeeeee
 3:Completed
 :Completed
 Upgrade M92P BIOS:Completed

 Fradley Test Task:Pending

 # Next we can delete an Existing Task
   You need to type the entire line exactly including the :'Status' of the task. 
   Let's delete task 2:Completed
   
:2
What lines to delete?
2:Completed

We can verify they were deleted by checking the Menu using option 0 again. 
:0

***Current Menu***

1:Completed
 4:Completed
 5:eeeeeeeeeeee
 3:Completed
 Upgrade M92P BIOS:Completed
 Fradley Test Task:Pending

***Current Menu***
# Change a Task from Pending to Complete
Lets use option 3 to turn 'Fradley Test Task:Pending' into Completed. 

What task would you like to do?
 0. See the Menu
 1. Create a New Task
 2. Delete an Existing Task
 3. What task would you like to mark as completed?
 4. Exit Program
:3
What task would you like completed?
Fradley Test Task:Pending

We can verify this by running option 0. 
***Current Menu***

1:Completed
 4:Completed
 5:eeeeeeeeeeee
 3:Completed
 Upgrade M92P BIOS:Completed
 Fradley Test Task:Completed


***Current Menu***

# Finally Exit Program
Once you choose option 4 the while loop ends and the program exits. 

