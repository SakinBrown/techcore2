import turtle
import update as up
import game1 as g1
import random
# import game2 as g2
#import Pygame type: ignore
user_data = {}
print(up.open_code_link())
print('Hello! Welcome to Wender!')

# Signup function
def signup():
    email = input('Please enter your email: ')
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')

    # Store the user information in the dictionary
    user_data['email'] = email
    user_data['username'] = username
    user_data['password'] = password

    print(f'Welcome {username}!')

# Login function
def login():
    if not user_data:
        print("No user account exists. Please signup first!")
        return False

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Validate credentials
    if username == user_data.get('username') and password == user_data.get('password'):
        print(f"Welcome back, {username}!")
        return True
    else:
        print("Incorrect username or password. Please try again.")
        return False

# Main flow
logsign = input('Login or Signup: ').lower()

if logsign == 'signup':
    signup()
elif logsign == 'login':
    if not login():
        print("Exiting program. Try again later.")
        exit()
  # Now includes a print statement

game = input('Choose a game 1 or 2: ')
game = int(game)

if game == 1:
    g1.guessing_numbers()
    print('Well Done!')
    lev = input('Next level?: ')
    if lev == 'yes':
        g1.guessing_numbers2()
    elif lev == 'no':
        print('Ending Sequence...')
        breakpoint
elif game == 2:
    import game2 as g2
    g2.level1()
    print('That is good. Keep it up!')
    g2.level2()

