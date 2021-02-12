# Now that we can connect our python application to our DB, let's go ahead and create a strange application! This application will allow users to create blog posts from their terminal and see posts as well!

import db

username = None

def writeNewPost(user):
	content = input("Your post:\n")
	db.createNewPost(user, content)
	print()

def showAllPosts():
	result = db.getPosts()

	if len(result) == 0:
		print("    No results found")
	else:
		print("> Posts:")
		for row in result:
			print(row)
	print("\n***\n")

def hr():
	print("---------------\n")

def app():
	print("Options:\n")
	print("1. Write a new post")
	print("2. See all other posts")
	print("3. Quit")

	while True:
		try:
			selection = int(input("\nYour choice: "))
			if selection < 1 or selection > 3:
				raise ValueError("Invalid option")
			break
		except:
			print("\n**Please make a valid selection**")
			continue
	hr()

	if (selection == 1):
		writeNewPost(username)
	elif (selection == 2):
		showAllPosts()
	elif (selection == 3):
		quit()

username = input("Create a username: ")

while True:
	try:
		app()
	except KeyboardInterrupt:
		print('You pressed ctrl+c')
		quit()

# ADDITIONAL REQUIREMENTS (Feb 11):

#     Handle empty result sets from the SELECT statement
#     Display the row count from your SELECT statement
#     Add try/except to catch possible mariadb exceptions

 

# HINTS:

#     I recommend you make extensive use of functions for this assignment. You should at least have 2 functions, one for running the insert and one for running the select

 

# BONUS:

#     Make the application run in a loop. After the user selects option 1 or option 2 and enters the information if needed, the application should keep running. This also requires you to give the user an option to exit the application
#     Give the application a real login functionality. This requires you to add modifications to the database to create a users table. The user should be prompted to enter a username and password to gain access. These users can be created using Dbeaver for testing.

 

# ADDITIONAL BONUS (Feb 11):

#     Avoid duplicating your try/except code between multiple queries.  Is there a way to make this more efficient and less repetitive by leveraging functions (or even objects if you're feeling really keen)???
