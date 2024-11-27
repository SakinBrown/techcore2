print('-------Welcome to the Classic Game known as MadLib---------')
print('\n You have 2 levels of fun!!')
print('\nLevel 1')

def level1():
    adjective = input('Name an adjective (pretty, bold, tall): ')
    animal = input('Name an animal (cat, dog, kangaroo): ')
    name = input('Name please: ')
    person_occupation = input('Name an occupation: ')
    verb = input('Name a verb: ')
    plural_noun = input('Name a plural noun: ')
    noun = input('Name a noun: ')
    color = input('Name a color: ')
    piece_of_clothing = input('Name a piece of clothing: ')
    tool = input('Name a tool: ')

    print(f'Today, I went to the beach and saw a(n) {adjective} {animal} playing in the sand. It was building a(n) {adjective} sandcastle shaped like a(n) {noun}. I decided to join in, but first, I put on my {color} {piece_of_clothing} and grabbed my {tool}. As I was digging, I found a(n) {adjective} treasure chest filled with {plural_noun}! Suddenly, a {adjective} {person_occupation} appeared and said, "That is my {noun}!" We decided to {verb} together instead. It was the most {adjective} beach day ever!')

if __name__ == "__main__":
    level1()


def level2():
    print('\n level 2')
    verb_ing = input("Enter a verb ending in 'ing': ")
    adjective2 = input("Enter another adjective: ")
    number2 = input("Enter a number: ")
    body_part_plural = input("Enter a body part (plural): ")
    noun2 = input("Enter another noun: ")
    exclamation = input("Enter an exclamation (e.g., Wow!): ")
    room_in_a_house = input("Enter a room in a house: ")
    plural_food = input("Enter a plural food: ")
    verb2 = input("Enter another verb: ")
    print(f'One night, while I was {verb_ing} in my backyard, I saw a(n) {adjective2} UFO land right next to my {noun2}. Out came a(n) {adjective2} alien with {number2} {body_part_plural} and a {adjective2} {noun2} in its hand. It said, "{exclamation}!" The alien wanted to {verb2} with me, so we went to my {room_in_a_house} and ate {plural_food}. Afterward, it showed me how to {verb2} using its {adjective2} spaceship. Before it left, it gave me a {noun2} as a souvenir. Now, every time I see a {adjective2} {noun2}, I think of my alien friend!')

if __name__ == "__main__":
    level2()