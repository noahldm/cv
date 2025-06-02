import time
import pygame
import sys

print("Welkom bij de command line maze! Verzamel alle letters en bereik de finish.")
print("De timer is gestart.")

# code voor het spelen van muziek
pygame.mixer.init()
pygame.mixer.music.load("songs/lied.mp3")
pygame.mixer.music.play(-1)

# code voor de tijd
start_time = time.time()

def elapsed_time():
    return time.time() - start_time

# functie zodat de tijd telkens geprint wordt
def tijd():
    print(f"Je hebt {elapsed_time():.2f} seconden gespeeld.")

# alle kamers in het doolhof
maze = {
    "start": {
        "1": "room1",
    },

    "room1": {
        "1": "room2",
        "2": "room12",
    },
    "room2": {
        "1": "room1",
        "2": "room3",
        "3": "room5",
        "4": "room4"
    },
    "room3": {
        "1": "roomH",
        "2": "room2",
    },
    "room4": {
        "1": "start",
    },
    "room5": {
        "1": "room6",
        "2": "finish",
        "3": "room2",
    },
    "room6": {
        "1": "room5",
        "2": "room7",
        "3": "room8",
    },
    "room7": {
        "1": "roomT",
        "2": "room6",
    },
    "room8": {
        "1": "room10",
        "2": "room9",
        "3": "room6",
    },
    "room9": {
        "1": "start",
    },
    "room10": {
        "1": "room8",
        "2": "room11",
    },

    "room11": {
        "1": "roomM",
        "2": "room10",
    },

    "room12": {
        "1": "room13",
        "2": "room1",
        "3": "room16",
    },

    "room13": {
        "1": "room12",
        "3": "room14",
    },

    "room14": {
        "1": "room15",
        "2": "room13",
    },

    "room15": {
        "1": "start",
    },

    "room16": {
        "1": "room17",
        "3": "room12",
    },

    "room17": {
        "1": "room16",
        "2": "roomL",
        "3": "room18",
    },
    
    "room18": {
        "1": "start",
    },

    "roomL": {
        "2": "room17",
    },
    "roomM": {
        "1": "room11",
    },
    "roomT": {
        "1": "room7",
    },
    "roomH": {
        "1": "room3",
    },
}

# alle kamers die je moet bezoeken
visited_rooms = set()   
required_rooms = {"roomH", "roomT", "roomM", "roomL"}
current_room = "start"

# pas als alle letters gehaald zijn kan de finish bereikt worden
while True:
    tijd()
    print(f"Je bent nu in {current_room}.")
    if current_room == "finish":
        if required_rooms.issubset(visited_rooms):
            print("Gefeliciteerd! Je hebt de finish bereikt! Bedankt voor het spelen!")
            time.sleep(2)
            sys.exit()
        else:
            print("Je moet langs room H, T, M en L geweest zijn om de finish te betreden.")
            continue

    # code om alle rooms te kunnen bezoeken
    visited_rooms.add(current_room)
    print("Je kunt naar de volgende kamers gaan:")
    for option, room in maze[current_room].items():
        print(f"{option}: {room}")

    choice = input("Maak een keuze: ")
    if choice in maze[current_room]:
        current_room = maze[current_room][choice]
    else:
        print("Ongeldige keuze, probeer opnieuw.")

    # code voor behaalde letter
    if current_room in required_rooms:
        print(f"Je hebt de letter {current_room[-1]} gehaald!")
        
        # code voor dead ends
        if current_room in {"room4", "room9", "room15", "room18"}:
            print("Dead end! Je gaat terug naar start.")
            visited_rooms.add(current_room)
            current_room = "start"
        # Add the room to visited_rooms if it contains a required letter
        visited_rooms.add(current_room)
        current_room = "start"