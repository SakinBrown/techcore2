code_to_print = print('Welcome to Update 1.1')
code_to_print = print('Patch Notes: \nAdded Login \nFixes Bugs')

# update.py
import webbrowser

def open_code_link():
    link = "https://docs.google.com/document/d/1eqPlcjlbJkklPiCWUrvADeQsBiKYFlgHSVWiA8dUH8c/edit?usp=sharing"
    print(f"History of Patch Notes: {link}")
    webbrowser.open(link)
