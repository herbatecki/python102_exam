class Item:
    def __init__(self, name, description):   # class for items and theri descriptions
        self.name = name
        self.description = description

class Room:     # clas for rooms and their descriptions and respective items, required to describe during making instance
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items else []  # long form of this below

        """
        if items:
            self.items = items
        else:
            self.items = []    
        """

    def add_item(self, item):
        self.items.append(item)

   
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        return None


    def display_description(self):    # class for printing descriptions and collected items
        print(f"Room: {self.name}")
        print(self.description)
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")
        else:
            print("There are no items in this room.")

class FinalRoom(Room):   # child class for asking user

 
    def enigma_func(self):
        enigma = input("A Dwarf, a friend of Legolas: ").lower()
        return enigma

            
class Player:                 # class for player and his activities
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def collect_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} collected!")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                print(f"Using {item.name}: {item.description}")
                self.inventory.remove(item)
                return True
        print(f"No item named {item_name} in inventory.")
            
        
    
    def display_inventory(self):
        if self.inventory:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item.name}")
            if len(self.inventory) == 3:
                print("Congratulations! You've collected all items!")
                
        else:
            print("Your inventory is empty.")


    def explore(self):            # may it be in Class Room?
        code_lock = input("In old era, year of foundation of Rome: ")
        return code_lock
        


# Create items - instances of items
key = Item("key", "A small rusty key.")
book = Item("book", "An old dusty book with strange symbols.")
writing = Item("writing", "A secret dusted writing on the wall.")

# Create rooms - instances of rooms
room1 = Room("Library", "A room filled with ancient books. There is a door to the north.", [book])
room2 = Room("Vault", "A small room with a locked treasure chest.", [key])
room3 = FinalRoom("Secret Chamber","Great hall with a throne with the puzzle to win a crown!", [writing])

# Create player - instance of player
player = Player("Adventurer")

# Game state at the beginning
current_room = room1
game_over = False

# Game loop - condiditons of playing/quitting the game
while not game_over:
        print("\n-- Current Room --")
        current_room.display_description()

        command = input("\nEnter a command (help for list of commands): ").strip().lower() # changing for lowercase and removing any whitespaces

        if command == "help":
            print("\nCommands:")
            print("description - Describe the current room")
            print("collect [item] - Collect an item")
            print("use [item] - Use an item in second room")
            print("inventory - Show your inventory")
            print("move [direction] - Move to another room")
            print("quit - Quit the  game")
            print("enigma - in final room! puzzle to solve and to win the game!")
        elif command == "description":
            current_room.display_description()
        elif command.startswith("collect "):
            item_name = command.split(" ", 1)[1]       # dividing command and taking second indice
            item = current_room.remove_item(item_name)
            if item:
                player.collect_item(item)
            else:
                print(f"No item named {item_name} found in this room.")
        elif command.startswith("use ") and current_room == room2:
            item_name = command.split(" ", 1)[1]
            if player.use_item(item_name) == True and item_name == "key":   # if we act "use book" only description of book will appear, but not possibility to open a chest
                print(f"Open the chest with {item_name} and write proper code.")
                while True:                     # player has many chances to open a chest
                    code = player.explore()
                    if code == '753':
                        print("You've opened a chest and found a treasure! Just try escape with it or die here!")
                        break
                    else:
                        print("Wrong code. Let's try again.")
                        continue
                
        elif command == "inventory":
            player.display_inventory()

        elif command.startswith("move "):
            direction = command.split(" ", 1)[1]
            if direction == "north" and current_room == room1:
                current_room = room2
            elif direction == "south" and current_room == room2:
                current_room = room1
            elif direction == "east" and current_room == room2:
                current_room = room3
            else:
                print("You can't go that way.")
        elif command == "quit":
            game_over = True
            print("Thanks for playing!")
        elif command == "enigma" and current_room == room3:
            answer = room3.enigma_func()
            if answer == "gimli":
                game_over = True
                print("Good answer! Thanks for playing!")
            else:
                print("Wrong answer. Let's start again.")
                break
        else:
            print("Invalid command. Type 'help' for a list of commands.")
