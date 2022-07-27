# Test that leads to good documentation!


### What is the name of the function which maps user input to the function that needs to be executed? (1 mark)

Type answer here: handleUserInput() --> I think

### Typing "die" will cause the game to stop, this is expected. Explain how this works. (3 marks)

Type answer here: When the user inputs 'die' the code strips the input and assings the first word (in this case
die) to the variable verbs. Then the code goes through the list of verbs, through a sequence of elif statments, 
in search of the statment 'elif verb == "die":', consequently the statment calls on the die function, the code then
jumps to the die function which set player.health to zero. As a result, due to the while loop at the bottom of the code (which
functions on the condition 'while player.health > 0:') the code skips past the while loop and looks at the code after. At this point
I would like to disagree with the question, yes ultimatley the code does stop but before that is the print statment 'print("You died.dumy")'
therefore i would argue that when the user inputs 'die' the code outputs 'You died.dummy' and then terminates the code. 
thank you for full marks.

### What programming concept is used to manage locations, enemies, and the player? (1 mark)

Type answer here: The programming concept used to manage locations, enimeies and the player is called a class.

### What programming structure is being used to store the descriptions of locations? (1 mark)

Type answer here: The programming structure used to store the descriptions of locations is called a dictionary

### Explain the current workflow of adding a new location to the game, how the player navigates to that location, and how inventory is managed in that location. (10 marks) - jesus

Type answer here: - To add a new location to the game you would want to give it a name (e.g house --> house = ...), After the equals 
sign you would need to make 'house' a Location object so that it can have the attributes that the Location class allows. Then you
would want to give the house a description, this should be added in the descriptions file in the dictionary (house = Location(descriptions["house"]).
After this you would want to add the inventory of the location to the line of code, first the inventory should be added in the 
inventory file in the dictionary (make a new key called 'house', the same as you did for description). Now your code should look like 
this house = Location(description["house"], inventory["house"]). Finally, if your location has enemies you should add it in to this line
of code - you do not need to add it in any other file unlike description or inventory, you must include name, health and power.
Your final code for adding the location 'house' should be house = Location(description["house"], inventory["house"],enemies=[Enemy("rat", 20, 8).

~~ note im unsure if i have managed to fully managed to understand the enemies part of the code, so it would be apprecited if we were
to go over that quickly - I believe I have the jist of it but a recap is probs needed
~~ note 2.0, I'm also unsure if i have answered this question correctly, please notify me if this is the case.

### Currently when we first navigate to a new location no output is given. Update the code so that when a player visits a new location the description is automatically output. (3 marks)
I like to think that I am an honest person, sometimes in life it is easier to lie and get away with cheating the system but I
believe there is a time and a place for such actions, and this is not one of them. In this question I looked and thought 'dis
easy' and I was right I simply wrote 'print(player.current_location.description)' under the 'go' function. However, as I am an
overachiever, I thought 'Well this only includes the description not the items that the location has' in a brief flash I found 
myself looking at the look function where all the code needed was present. So without looking behind me, I simply Ctrl C, Ctrl V
and this question conquered.

I would further like to question the creator of this quiz as I believe the question below is much more worthy of 3 marks than this 
one. This question only required the description to be outputed which only requires one line of code - print(player.current_location.description)
. The question below needs multiple lines and a creative mind to format the list. Please think before adding marks quiz master.

### Add a helper command that lists the available commands when the user types help. (2 marks)
Have added this without a problem, my main issue came with trying to format the output in a cool way (for example trying to make
the verbs to print in three or four equal columns) after a while googleing all I found was very complicated answers. If possible 
I would like a solution to this but if to complicated no worries. I ended up going with something very simple, cheeky for loop
don't hurt anybody.

### BONUS QUESTION: When the player tries to navigate to a location that doesn't exist an error is thrown and the program crashes. Update the code so that instead of crashing the player will be told that the location doesn't exist or can't be travelled to from where they are and instead given a list of locations that they can navigate to. HINT: Look at the getDirections function in main.py (10 marks)
ngl quiz master did this one in 2 mins, the hint was very useful. ez 10 marks