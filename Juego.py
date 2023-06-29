import pygame 


def create_map(level):
    map_height = 10
    map_width = 10
    
    map = []
    for row in range(map_height):
        if row == 0:
            map.append(" " * map_width)  # Empty top row
        elif row == map_height - 1:
            map.append("#" * map_width)  # Bottom row represents ground
        else:
            map.append(" " * map_width)  # Empty rows in between

    # Add zombies at the top of the screen
    zombie_position = (map_width // 2) - 1
    map[0] = map[0][:zombie_position] + "Z" + map[0][zombie_position + 1:]

    return map

def create_map(level):
    map_height = 10
    map_width = 10
    map = []

    for row in range(map_height):
        if row == 0:
            map.append(" " * map_width)  # Empty top row
        else:
            map.append("#" * map_width)  # Walls in other rows

    # Add zombies at the top row
    zombie_position = level % map_width
    map[0] = map[0][:zombie_position] + "Z" + map[0][zombie_position + 1:]

    return map

def move_player(map, player_position):
    map_height = len(map)
    map_width = len(map[0])

    # Update the map to reflect the player's new position
    map[player_position[0]] = map[player_position[0]][:player_position[1]] + "P" + map[player_position[0]][player_position[1] + 1:]

    # Check if a zombie touches the player
    if map[0][player_position[1]] == "Z":
        # Decrease player's life by 1
        player_life -= 1
        if player_life == 0:
            # Game over condition
            return "Game Over"

    return map

def choose_weapon():
    weapons = [
        {"name": "Pistol", "ammo": 10},
        {"name": "Shotgun", "ammo": 6},
        {"name": "Rifle", "ammo": 20}
    ]
    
    print("Available weapons:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']} (Ammo: {weapon['ammo']})")
    
    while True:
        choice = input("Choose a weapon (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            chosen_weapon = weapons[int(choice)-1]
            print(f"You have chosen {chosen_weapon['name']} with {chosen_weapon['ammo']} ammunition.")
            return chosen_weapon["name"], chosen_weapon["ammo"]
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")

weapon_name, ammo_count = choose_weapon()
print(f"Player has chosen {weapon_name} with {ammo_count} ammunition.")

def create_map(level):
    map_height = 10
    map_width = 10

    # Create an empty map with spaces
    map_list = [' ' * map_width for _ in range(map_height)]

    # Calculate the position where zombies appear
    zombie_position = map_width // 2

    # Place the zombies at the top row of the map
    map_list[0] = ' ' * zombie_position + 'Z' + ' ' * (map_width - zombie_position - 1)

    # Place the player at the bottom row of the map
    player_position = map_width // 2
    map_list[map_height - 1] = ' ' * player_position + 'P' + ' ' * (map_width - player_position - 1)

    # Return the map
    return map_list

def move_player(map, position):
    # Display current map
    display_map(map)
    
    # Get user input for movement
    direction = input("Enter 'up' or 'down' to move: ")
    
    # Update player position based on user input
    if direction == 'up':
        if position > 0:
            # Move player up
            map[position] = map[position][:5] + 'P' + map[position][6:]
            map[position+1] = map[position+1][:5] + ' ' + map[position+1][6:]
            position -= 1
    elif direction == 'down':
        if position < len(map) - 1:
            # Move player down
            map[position] = map[position][:5] + 'P' + map[position][6:]
            map[position-1] = map[position-1][:5] + ' ' + map[position-1][6:]
            position += 1
    
    # Check if player is touched by a zombie
    if 'Z' in map[0]:
        print("Player is touched by a zombie!")
        decrease_life()
    
    return map, position


def decrease_life():
    global life
    life -= 1
    print("Player's life decreased by 1. Remaining life:", life)
    
    if life == 0:
        print("Game over!")
        exit()


def display_map(map):
    for row in map:
        print(row)


# Game initialization
life = 6
position = 5  # Initial player position
level = 1

# Create map for level 1
map = create_map(level)

while True:
    map, position = move_player(map, position)

def choose_weapon(available_weapons):
    print("Available weapons:")
    for i, weapon in enumerate(available_weapons):
        print(f"{i + 1}. {weapon['name']} (Ammunition: {weapon['ammunition']})")
    
    while True:
        try:
            choice = int(input("Choose a weapon: "))
            if 1 <= choice <= len(available_weapons):
                weapon = available_weapons[choice - 1]
                return weapon['name'], weapon['ammunition']
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage
available_weapons = [
    {"name": "Pistol", "ammunition": 10},
    {"name": "Shotgun", "ammunition": 6},
    {"name": "Rifle", "ammunition": 20}
]

chosen_weapon, ammunition = choose_weapon(available_weapons)
print(f"Chosen weapon: {chosen_weapon} (Ammunition: {ammunition})")

def create_map(level):
    map_height = 10
    map_width = 10

    # Initialize an empty map
    map = [[' ' for _ in range(map_width)] for _ in range(map_height)]

    # Add the player to the map
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row][player_col] = 'P'

    # Add the zombies to the map
    zombie_col = map_width // 2
    for row in range(level):
        map[row][zombie_col] = 'Z'

    # Convert the map to a list of strings
    map_strings = [''.join(row) for row in map]

    return map_strings

def create_map(level):
    map_height = 10
    map_width = 10

    # Initialize an empty map
    map = [[' ' for _ in range(map_width)] for _ in range(map_height)]

    # Add the player to the map
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row][player_col] = 'P'

    # Add the zombies to the map
    zombie_col = map_width // 2
    for row in range(level):
        map[row][zombie_col] = 'Z'

    # Convert the map to a list of strings
    map_strings = [''.join(row) for row in map]

    return map_strings

def move_player(map, player_pos):
    # Update the map to reflect the player's new position
    map[player_pos] = map[player_pos].replace('P', ' ')
    new_pos = player_pos + 1 if player_pos < len(map) - 1 else 0
    map[new_pos] = map[new_pos].replace(' ', 'P')
    
    # Check if a zombie touches the player
    if 'Z' in map[new_pos]:
        # Decrease player's life by 1
        life = int(map[0].split(':')[1])
        life -= 1
        map[0] = f"Life: {life}"
        
        # Check if player's life reaches 0
        if life == 0:
            map.append("Game Over!")
    
    return map

def choose_weapon(weapons):
    print("Available weapons:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']} - Ammo: {weapon['ammo']}")
    
    while True:
        choice = input("Choose a weapon: ")
        if choice.isdigit() and int(choice) in range(1, len(weapons)+1):
            weapon = weapons[int(choice)-1]
            print(f"You have chosen {weapon['name']} with {weapon['ammo']} ammo.")
            return weapon
        else:
            print("Invalid choice. Please try again.")

# Example usage
weapons = [
    {"name": "Pistol", "ammo": 10},
    {"name": "Shotgun", "ammo": 5},
    {"name": "Rifle", "ammo": 20}
]

chosen_weapon = choose_weapon(weapons)
print(chosen_weapon)

def create_map(level):
    map_height = 10
    map_width = 10

    # Create an empty map
    map = [[' ' for _ in range(map_width)] for _ in range(map_height)]

    # Add the player to the map
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row][player_col] = 'P'

    # Add the zombies to the top row of the map
    zombies = level * 2
    for i in range(zombies):
        zombie_col = i * (map_width // zombies)
        map[0][zombie_col] = 'Z'

    # Convert the map to a list of strings
    map_strings = [''.join(row) for row in map]

    return map_strings

# Test the function
level = 1
map = create_map(level)
for row in map:
    print(row)


def move_player(map, position):
    # Get player's current position
    row, col = position

    # Update the map to reflect the player's new position
    map[row] = map[row][:col] + ' ' + map[row][col+1:]

    # Allow the player to move up or down
    direction = input("Enter 'u' to move up or 'd' to move down: ")

    if direction == 'u':
        # Check if the player is already at the top row
        if row == 0:
            print("Cannot move up further")
        else:
            # Update the player's position
            row -= 1
    elif direction == 'd':
        # Check if the player is already at the bottom row
        if row == len(map) - 1:
            print("Cannot move down further")
        else:
            # Update the player's position
            row += 1

    # Update the map to reflect the player's new position
    map[row] = map[row][:col] + 'P' + map[row][col+1:]

    return map, (row, col)

def choose_weapon():
    weapons = [
        {"name": "Pistol", "ammo": 10},
        {"name": "Shotgun", "ammo": 6},
        {"name": "Machine Gun", "ammo": 30}
    ]
    
    print("Available weapons:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']}")

    while True:
        choice = input("Choose a weapon (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            chosen_weapon = weapons[int(choice)-1]
            return chosen_weapon["name"], chosen_weapon["ammo"]
        else:
            print("Invalid choice. Please try again.")

# Test the function
weapon_name, ammo_count = choose_weapon()
print(f"You have chosen {weapon_name} with {ammo_count} ammunition.")

def create_map(level):
    map_height = 10
    map_width = 10

    # Create an empty map
    map = [" " * map_width for _ in range(map_height)]

    # Add the player to the map
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row] = map[player_row][:player_col] + "P" + map[player_row][player_col + 1:]

    # Add the zombies to the map
    zombie_row = 0
    zombie_col = player_col
    map[zombie_row] = map[zombie_row][:zombie_col] + "Z" + map[zombie_row][zombie_col + 1:]

    # Return the map
    return map

def move_player(map, player_position):
    # Update the map to reflect the player's new position
    updated_map = map.copy()
    row, col = player_position
    updated_map[row] = updated_map[row][:col] + 'P' + updated_map[row][col+1:]

    # Check if a zombie touches the player
    for i in range(len(updated_map)):
        if i != row and updated_map[i][col] == 'Z':
            # Decrease player's life by 1
            updated_map[row] = updated_map[row][:col] + 'B' + updated_map[row][col+1:]
            break

    return updated_map

def choose_weapon(weapons):
    print("Available weapons:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']} (Ammunition: {weapon['ammo']})")
    
    while True:
        choice = input("Choose a weapon (enter the corresponding number): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(weapons):
                chosen_weapon = weapons[choice-1]
                print(f"You have chosen {chosen_weapon['name']} with {chosen_weapon['ammo']} ammunition.")
                return chosen_weapon
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

def create_map(level):
    map_height = 10
    map_width = 10

    # Create an empty map
    map = []
    for _ in range(map_height):
        map.append([' '] * map_width)

    # Add zombies at the top row
    for i in range(map_width):
        map[0][i] = 'Z'

    # Add player at the bottom row
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row][player_col] = 'P'

    # Convert the map to a list of strings
    map_strings = []
    for row in map:
        map_strings.append(''.join(row))

    return map_strings

def move_player(current_map, player_position):
    # Get the dimensions of the map
    num_rows = len(current_map)
    num_cols = len(current_map[0])
    
    # Get the player's current row and column
    player_row, player_col = player_position
    
    # Update the map to reflect the player's new position
    updated_map = current_map.copy()
    updated_map[player_row] = updated_map[player_row][:player_col] + ' ' + updated_map[player_row][player_col+1:]
    
    # Move the player up or down
    direction = input("Enter 'up' or 'down' to move the player: ")
    if direction == 'up':
        player_row -= 1
    elif direction == 'down':
        player_row += 1
    
    # Check if the player's new position is valid
    if player_row < 0 or player_row >= num_rows:
        print("Invalid move! Please try again.")
        return current_map, player_position
    
    # Update the map to reflect the player's new position
    updated_map[player_row] = updated_map[player_row][:player_col] + 'P' + updated_map[player_row][player_col+1:]
    
    # Check if a zombie touched the player
    if 'Z' in updated_map[player_row]:
        print("A zombie touched you!")
        return updated_map, (player_row, player_col), -1
    
    return updated_map, (player_row, player_col), 0

def choose_weapon(weapons):
    print("Choose a weapon:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']} - Ammunition: {weapon['ammo']}")
    
    while True:
        choice = input("Enter the number of the weapon you want to choose: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(weapons):
                chosen_weapon = weapons[choice-1]
                print(f"You have chosen {chosen_weapon['name']} with {chosen_weapon['ammo']} ammunition.")
                return chosen_weapon['name'], chosen_weapon['ammo']
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

# Example usage
weapons = [
    {"name": "Pistol", "ammo": 20},
    {"name": "Shotgun", "ammo": 10},
    {"name": "Rifle", "ammo": 30}
]
chosen_weapon, ammo_count = choose_weapon(weapons)
print(f"Chosen weapon: {chosen_weapon}")
print(f"Ammunition count: {ammo_count}")

def create_map(level):
    map_height = 10
    map_width = 10

    # Create an empty map
    map = []
    for _ in range(map_height):
        map.append([' '] * map_width)

    # Place the zombies at the top of the map
    zombies_row = 0
    zombies_col = map_width // 2
    map[zombies_row][zombies_col] = 'Z'

    # Place the player in the middle of the map
    player_row = map_height - 1
    player_col = map_width // 2
    map[player_row][player_col] = 'P'

    # Convert the map to a list of strings
    map_strings = []
    for row in map:
        map_strings.append(''.join(row))

    return map_strings

def move_player(map, player_pos):
    # Display the current map
    for row in map:
        print(row)
    
    # Get the player's movement input
    move = input("Enter 'up' or 'down' to move: ")
    
    # Update the player's position
    if move == "up" and player_pos > 0:
        map[player_pos] = map[player_pos].replace("P", " ")
        player_pos -= 1
        map[player_pos] = map[player_pos].replace(" ", "P")
    elif move == "down" and player_pos < len(map) - 1:
        map[player_pos] = map[player_pos].replace("P", " ")
        player_pos += 1
        map[player_pos] = map[player_pos].replace(" ", "P")
    
    # Check if the player is touched by a zombie
    if "Z" in map[player_pos]:
        print("You were touched by a zombie!")
        map[player_pos] = map[player_pos].replace("Z", " ")
        life -= 1
        if life == 0:
            print("Game over!")
            return
    
    # Return the updated map and player's position
    return map, player_pos

def choose_weapon(weapons):
    print("Available weapons:")
    for i, weapon in enumerate(weapons):
        print(f"{i+1}. {weapon['name']} (Ammunition: {weapon['ammo']})")
    
    while True:
        choice = input("Choose a weapon: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(weapons):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter a number corresponding to the weapon.")
    
    chosen_weapon = weapons[choice-1]
    print(f"You have chosen {chosen_weapon['name']} with {chosen_weapon['ammo']} ammunition.")
    return chosen_weapon['name'], chosen_weapon['ammo']

# Example usage
weapons = [
    {'name': 'Pistol', 'ammo': 10},
    {'name': 'Shotgun', 'ammo': 6},
    {'name': 'Rifle', 'ammo': 20}
]

chosen_weapon, ammo_count = choose_weapon(weapons)
print(f"Chosen weapon: {chosen_weapon}, Ammunition: {ammo_count}")

