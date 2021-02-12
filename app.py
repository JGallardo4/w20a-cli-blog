# Now that we can connect our python application to our DB, let's go ahead and create a strange application! This application will allow users to create blog posts from their terminal and see posts as well!

import db
from getpass import getpass

username = None

def login():
	while True:
		print("Options:\n")
		print("1. Log in")
		print("2. Create new user")
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
			if authenticate():
				print("\n✓ Log in successful!\n")
				while True:
					app()
			else:
				print("\n✗ Incorrect username or password\n")
				continue
		elif (selection == 2):
			createUser()
			continue
		elif (selection == 3):
			quit()
	

def authenticate():
	global username
	usernameInput = input("Username: ")
	password = getpass()

	if db.login(usernameInput, password):
		username = usernameInput
		return True
	else:
		return False

def createUser():
	username = input("Username: ")
	password = getpass()

	db.createUser(username, password)	

def writeNewPost(user):
	content = input("Your post:\n")
	db.createNewPost(user, content)
	print()

def showAllPosts():
	result = db.getPosts()

	if len(result) == 0:
		print("    No results found")
	else:
		print("> ", len(result), "posts:")
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

login()


 

# ADDITIONAL BONUS (Feb 11):

#     Avoid duplicating your try/except code between multiple queries.  Is there a way to make this more efficient and less repetitive by leveraging functions (or even objects if you're feeling really keen)???
