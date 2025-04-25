import random
import time
import sys
import textwrap
import shutil

"""
THE OATHKEEPER

Developed by:       Alfarooq Dahoum
                    "Nathan Hawkes
                    Katy Jones
                    Hamse Mahamed
                    Kyle Marsden
                    Euan Penn
                    Dean Robinson
                    Matthew Sheldon
"""

terminal_width = shutil.get_terminal_size(fallback=(130, 40)).columns

# Check choice is valid and return
# DEV: Nathan Hawkes
def make_choice(options, prompt = "Which choice do you make?"):
    # Arguments
    # options (dict)    : List of options in dictionary format. 
    #                     eg. {1:["home", "return"], 2:["leave"], 3:["quit"]}
    #                     Allows for multiple keywords
    # Returns associated int value, or prompts to re-enter choice

    prompt += "\n> "

    response = input(prompt).strip().lower()

    # Try numeric match
    try:
        num_choice = int(response)
        if num_choice in options:
            return num_choice
    except ValueError:
        pass

    # Try keyword match (exact or in a sentence)
    for num, keywords in options.items():
        for keyword in keywords:
            if keyword in response:
                return num

    # If no valid choice is detected
    print_slow("Sorry, I didn't recognise your choice.")
    return make_choice(options)

# Set global variables
# DEV: Nathan Hawkes
player_inventory = []
player_name = input("What is your name?\n> ").upper()

# Select Player Gender
print("1: Male")
print("2: Female")
print("3: Non-binary")
print("4: Gender-fluid")

gender_choice = make_choice({
    1:["m", "male"],
    2:["f", "female"],
    3:["non-binary", "nonbinary", "nb", "enby"],
    4:["gender-fluid", "genderfluid", "fluid", "gf"]
}, "What is your character's gender identity?")

if gender_choice == 1:
    player_gender = "MALE"
elif gender_choice == 2:
    player_gender = "FEMALE"
elif gender_choice == 3:
    player_gender = "NON-BINARY"
else:
    player_gender = "GENDER-FLUID"

# Select Player Class
print("1: I am a FIGHTER")
print("2: I am an ARCHER")
print("3: I am a MAGE")
player_choice = make_choice({
    1:['fighter'],
    2:['archer'],
    3:['mage']
}, "Select your player class:")

if player_choice == 1:
    player_class = "FIGHTER"
elif player_choice == 2:
    player_class = "ARCHER"
elif player_choice == 3:
    player_class = "MAGE"
else:
    print("I don't recognise that option")

# Select Reading Speed
print("Set your reading speed")
print("1: I can read QUICKLY")
print("2: I am AVERAGE")
print("3: I want to take my TIME")
reading_choice = make_choice({
    1:['quickly', 'quick'],
    2:['average'],
    3:['time', 'slow'],
    9:['instant']
}, "Select your reading speed:")

reading_speed = 0.075
if reading_choice == 1:
    reading_speed = 0.03
elif reading_choice == 2:
    reading_speed = 0.075
elif reading_choice == 3:
    reading_speed = 0.125
elif reading_choice == 9:
    reading_speed = 0.0
else:
    print("I don't recognise that option")

# Show display text
# DEV: Alfarooq Dahoum
def print_slow(text, delay=None):
    global reading_speed

    if delay == None:
        delay = reading_speed
    # Arguments
    # text  (str)       : String of text to display
    # delay (float)     : Time (in seconds) to reveal the text

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Set character status
# DEV: Nathan Hawkes
status_vizier = "CURSE"
status_guard = "ALIVE"
status_king = "CURSE"
status_bbeg = "ALIVE"

# Check if item is in the inventory
# DEV: Nathan Hawkes
def check_inventory(item):
    # Arguments
    # item (str)    : Name of the item to be checked in the inventory
    global player_inventory

    if item in player_inventory:
        return True
    else:
        return False

# Add and remove from inventory
# DEV: Nathan Hawkes
def add_to_inventory(item, current_inventory = False):
    # Arguments
    # item (str)                : Name of item to be included in inventory
    # curent_inventory (bool)   : Option to force display of the current inventory, even if nothing has been added (defaults to False)
    global player_inventory

    if check_inventory(item) == False:
        player_inventory.append(item)
        print_slow(f"{item} has been added to your inventory.")

        current_inventory = True
    else:
        print_slow(f"You already have {item} in your inventory.")

    if current_inventory == True:
        inventory = ", ".join(player_inventory)
        print_slow(f"Your current inventory contains: {inventory}")

def remove_from_inventory(item, current_inventory = False):
    # Arguments
    # item (str)                : Name of item to be removed from inventory
    # curent_inventory (bool)   : Option to force display of the current inventory, even if nothing has been removed (defaults to False)
    global player_inventory

    if check_inventory(item) == True:
        player_inventory.remove(item)
        print_slow(f"{item} has been removed from your inventor.")

        current_inventory = True
    else:
        print_slow(f"You do not have {item} in your inventory.")

    if current_inventory == True:
        inventory = ", ".join(player_inventory)
        print_slow(f"Your current inventory contains: {inventory}")

# Change text colour
# DEV: Nathan Hawkes
def text_color(text, fg=None, bg=None):
    # Arguments:
    # text (str)  : The text to color.
    # fg (str)    : The foreground color. Options: black, red, green, yellow, blue, magenta, cyan, white.
    # bg (str)    : The background color. Same options as foreground.

    colors = {
        'black':    0,
        'red':      1,
        'green':    2,
        'yellow':   3,
        'blue':     4,
        'magenta':  5,
        'cyan':     6,
        'white':    7
    }

    # Checks for foreground colour
    if fg in colors:
        fg = f"\033[3{colors[fg]}m"
    else:
        fg = ""

    # Checks for background colour
    if bg in colors:
        bg = f"\033[4{colors[bg]}m"
    else:
        bg = ""

    # Returns colourised string
    return f"{fg}{bg}{text}\033[0m"

# Roll dice - generates random number with a maximum limit
# DEV: Nathan Hawkes
def roll_dice(d):
    # Arguments
    # d (int)   : "Dice" number - maximum limit.
    roll = random.randint(1,d)
    return roll

# Let's play!!!
# DEV: Nahtan Hawkes
def game_start():
    # Set global variables
    global player_inventory

    # Clears inventory on start / restart
    player_inventory.clear()

    # Print story
    print_slow("--------------")
    print_slow("THE OATHKEEPER")
    print_slow("--------------")
    print_slow("")

    full_text = f"""
Vel'Rath is a broken world. Shattered in a cataclysm known only as "{text_color('The Sundering','cyan')}", its lands still bleed with the memory of a war between {text_color('the Unbound','red')} - ruinous spirits of chaos - and the {text_color('Old Gods','green')} who once kept the world whole. The war raged for centuries, devouring cities, toppling empires, and leaving the mortal races clinging tightly to survival.

In a final, desperate act, the {text_color('Old Gods','green')} bound their fading essences into the very bones of the earth. Their souls now sleep beneath the forests, mountains, and rivers they forged in their creation. Forgotten, but not gone.

{text_color('The Unbound','red')} lingered in ruins and dreams, haunting the remnants of the world they so nearly claimed. Time itself has frayed. Magic twists unnaturally, corrupted by the dark whispers that seek to unravel what little order remains.

Yet even in the smallest parts of society, hope still endures. Whispers speak of a band of mortals, united under a secret banner: a crescent moon cradling a heart engulfed in fire. They move from shadow to shadow, bearing no name, only purpose: to restore the Gods and cleanse Vel'Rath of the corruption of {text_color('the Unbound','red')}.

You, {text_color(player_name,'green')}, are a traveller. A blade for hire, from a band known as {text_color('The Oathkeepers','green')}. Your garments are worn but clean; your eyes are sharper than your steel. A sigil on your shoulder - a flame encased within a sickle - marks your lineage. It was passed down from your father, as from his mother before him. You are the latest in a long, solemn line."""

    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow("But your oath is your own. And your story begins now.")
    time.sleep(1.5)
    print_slow("")
    time.sleep(0.5)
    print_slow("")
    time.sleep(0.5)
    start_on_ship()

# Start game journey - from ship
# DEV: Nathan Hawkes
def start_on_ship():
    # Print story
    print_slow("--------------")
    print_slow("YOU ARRIVE ...")
    print_slow("--------------")
    print_slow("")

    full_text = f"""
The raging waves of Poseidon's wrath fade behind you as your vessel nears the harbour. You stand at the starboard rail, inhaling the briny air, your gaze fixed on the approaching shoreline. Around you, sailors move with seasoned purpose, securing cargo, shouting orders, and preparing for landfall. On the docks, crews scramble to make space, ropes ready to catch, boots thudding against weather-worn planks. Your ship is no galleon, but here, amid the lean cutters and battered skiffs, it looms large. Even so, it feels strangely out of place.
    
This is {text_color('Silvermoon Wharf','yellow')}, perched on the southern edge of Vel'Rath. It was once a thriving hub of commerce and camaraderie. The banners still flutter above the boardwalk, painted in faded hues of crimson and gold. The market still bustles, but with an undertone of caution, of something long faded. Life lingers here, but joy feels like a memory.

You haven't set foot here since infancy. But some part of you remembers it, albeit vaguely. Like a dream glimpsed through fog.

\"Land ahoy!\"

The unmistakable rasp of {text_color('Captain Sykes','cyan')} shatters your thoughts, echoing across the deck. Anchors splash. Ropes coil mid-air. Dockhands shout and grumble in the dance of docking and clearance.

You gather your few possessions - well-worn gear, a satchel, and the weight of your past - and swing your pack over your shoulder. With one final glance at the ship, you nod silently in gratitude to the {text_color('the Captain','cyan')}. He returns the gesture, already barking orders to the crew.

With boots on wood and a heart full of questions, you step onto the docks of {text_color('Silvermoon Wharf','yellow')}."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    time.sleep(0.75)
    print_slow("")
    time.sleep(0.75)
    go_to_docks()

# Go to (or return) to docks
# DEV: Nathan Hawkes
def go_to_docks(first_time = True):
    # Arguments
    # first_time (bool)     : Checks if this is the first time running the function
    #                         If False, then will run straight to go_to_crossroads(), otherwise will display choice to change direction, as per the game

    # Print story
    full_text = f"""
You follow a winding path of weathered stone, worn smooth by countless boots before yours. On either side, traders call out in melodic bursts, offering skewered meats, spiced wines, fragrant herbs, and the occasional trinket that promises more than it can deliver. The scent of cinnamon and charcoal lingers in the air. It feels welcoming, yet also not.
    
Now and then, a flashy figure weaves between the stalls. Part jester, part salesman, and unmistakably a conman. He catches your eye for the briefest moment, smirks, then moves on. He pays you no heed, and you continue on your way.
    
The market fades behind you, replaced by the hush of trees and birdsong. The path meanders through a stretch of woodland separating the harbour from the inland roads. The cool shade is a welcome reprieve from the midday sun, and for the first time today, the noise of the world slips away."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    # Checks if this is being run for the first time
    if first_time == False:
        print_slow(f"Press 1 to go to the {text_color('CROSSROADS','magenta')}")
        player_choice = make_choice({
            1:['crossroads']
        })
        if player_choice == 1:
            go_to_crossroads()
        else:
            print_slow("I don't recognise that option")
    else:
        go_to_crossroads()

# Go to crossroads - central meeting point
# DEV: Matthew Sheldon
def go_to_crossroads():
    # Print story
    print_slow("You come to a crossroads.")
    print_slow("")
    full_text = f"""
1: To the {text_color('NORTH','magenta')} lies to {text_color('Castle Malus','yellow')}, seat of King Esylron - a name whispered with awe or anger, depending on the speaker.\n
2: To the {text_color('WEST','magenta')} is the humble village of {text_color('Bleakhollow','yellow')}, nestled in the valley's curve.\n
3: To the {text_color('EAST','magenta')} lays an unmarked path, worn by many, claimed by none.\n
4: Behind you to the {text_color('SOUTH','magenta')} lays the market, the docks, and the salty wind of the sea."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    # Make player choice
    player_choice = make_choice({
        1:['north','castle'],
        2:['west','bleakhollow'],
        3:['east','unmarked','path'],
        4:['south','docks','harbour','market']
    }, "Which way do you go?")

    # Select player choice
    if player_choice == 1:
        go_to_castle()
    elif player_choice == 2:
        go_to_bleakhollow()
    elif player_choice == 3:
        go_to_lake()
    elif player_choice == 4:
        go_to_docks(False)
    else:
        print_slow("I don't recognise that option")

# Go to village - villager, tavern, armoury
# DEV: Matthew Sheldon
def go_to_bleakhollow(first_time = True):
    # Arguments
    # first_time (bool) : Checks if function is running for the first time
    #                     If True, gives entry narrative
    #                     If False, returns you to village

    # Check if running for the first time and print story
    if first_time == True:
        full_text = f"""
You approach the village of {text_color('Bleakhollow','yellow')}, a name that feels both fitting and misleading.

The homes are worn to ruin, their stone foundations cracked and sagging. Cobblestone streets lie deserted, and shuttered windows creak faintly in the wind. A foul stench hangs in the air—a reek of sewage, blood, and something older.

The silence is complete. Unnatural. Every corner feels watched.

But through the stillness, you glimpse echoes of what was. You can almost see children darting through alleyways, their laughter rising above the bustle. You hear the calls of bakers hawking warm pasties, the cheerful bellow of butchers guiding cattle through the square. It lingers like a fading dream. Now, only shadows remain.

A lone villager creaks past, pulling a rickety trolley with crooked wheels and a downcast gaze. To your left, the warped sign of a tavern sways in the breeze - a place that no doubt once overflowed with song and revelry. Ahead and to the right, a rusted hanging blade marks the armoury."""
    else:
        full_text = f"""
You are back in the village of {text_color('Bleakhollow','yellow')}. The villager is still walking back and forthwith his trolley. The tavern stands tall with its sign, and the blade that marks the armoury is still clear"""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow("Where do you go?")
    print_slow(f"1: Go {text_color('INSIDE','magenta')} to the Tavern")
    print_slow(f"2: {text_color('SPEAK','magenta')} to the Villager")
    print_slow(f"3: Continue {text_color('WEST','magenta')} to the Armory")
    print_slow(f"4: {text_color('RETURN','magenta')} to the crossroad")
    
    # Make player choice
    player_choice = make_choice({
        1:["inside", "tavern"],
        2:["speak", "villager"],
        3:["west", "armoury", "armory"],
        4:["return", "crossroad"]
    }, "Which way do you go?")

    # Select player choice
    if player_choice == 1:
        go_to_tavern()
    elif player_choice == 2:
        talk_to_villager()
    elif player_choice == 3:
        go_to_armoury()
    elif player_choice == 4:
        go_to_crossroads()
    else:
        print_slow("I don't recognise that option")

# Talk to the villager - cut scene
# DEV: Matthew Sheldon
def talk_to_villager():
    # Print story
    full_text = f"""
You spot a hunched villager dragging a battered cart behind him. Bodies, wrapped in soiled cloth and twisted in unnatural shapes, lie piled within. The wheels groan under the weight, scraping against the cobbles as he trudges through the filth.

You step forward and call out.

He glances up, a sunken-eyed man with a face like weathered leather. He exhales a low, disgruntled groan but lifts a shaking hand and points toward the tavern.

\"Ask the innkeeper. He'll know what the likes of you want.\"

Before you can reply, he's already turned away. The cart creaks and squeals as he disappears around the corner, swallowed once more by silence."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow(f"1: Go {text_color('INSIDE','magenta')} to the Tavern")
    print_slow(f"2: Continue {text_color('WEST','magenta')} to the Armory")
    print_slow(f"3: {text_color('RETURN','magenta')} to the crossroad")
    
    # Make player choice
    player_choice = make_choice({
        1:["inside", "tavern"],
        2:["west", "armoury", "armory"],
        3:["return", "crossroad"]
    }, "Which way do you go?")

    # Select player choice
    if player_choice == 1:
        go_to_tavern()
    elif player_choice == 2:
        go_to_armoury()
    elif player_choice == 3:
        go_to_crossroads()
    else:
        print_slow("I don't recognise that option")

# Enter the Tavern
# DEV: Matthew Sheldon
def go_to_tavern():
    # Print story
    full_text = f"""
The tavern's old, decrepit sign creaks on rusted chains above the most miserable-looking hovel you've ever seen.

You push open the heavy oak doors. The inside is dim, thick with the scent of old ale and soot, but it feels almost welcoming compared to the silence outside. The alcohol taps still drip, and a faint fire smoulders in the hearth.

You approach the bar. The weary innkeeper glances up. \"What can I get you, friend?\"

You lean against the counter. \"What's going on here? The whole place feels dead.\"

A wry smirk pulls at his lips. \"Wise choice of words.\"

You take a seat, and as he begins pouring a drink, he speaks quietly, as though afraid the walls might listen. He tells you of the rot that took hold after the king's death, how a blight of shadowed magic now festers within the castle. The crops failed. The air changed. People began to vanish.

As he speaks, his voice slows. He's staring at you now, not the drink. His eyes drift to your shoulder.

\"Hey…\" he says, in more of a whisper than a voice. \"Are you ...?\" He nods toward the patch stitched into your cloak.

You glance down and smile faintly. \"Perhaps.\"

Something flickers in him. Hope, maybe. Long-buried, but not dead yet.

\"You might actually stand a chance,\" he mutters. \"Many have come before, thinking they could fix this, but you… you feel different.\"

He rummages in his coat and presses something small and cold into your hand.

\"Here,\" he whispers. \"Leave the village. Follow the woodland path east to the lake. The locals call her the Goddess of the Lake. If she sees you… if she chooses you… she might just show you how to lift the curse.\""""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    add_to_inventory("AMULET")
    print_slow("")
    print_slow(f"1: {text_color('LEAVE','magenta')} the Tavern")
    print_slow(f"2: {text_color('SPEAK','magenta')} to the tavern keeper")
    print_slow(f"3: {text_color('START','magenta')} a fight")
        
    # Make player choice
    player_choice = make_choice({
        1:["leave", "tavern"],
        2:["talk", "speak", "keeper", "innkeeper", "inkeeper"],
        3:["fight", "start", "brawl", "barney"]
    }, "What do you want to do?")

    # Select player choice
    if player_choice == 1:
        go_to_bleakhollow(False)
    elif player_choice == 2:
        talk_to_innkeeper()
    elif player_choice == 3:
        fight_in_tavern()

# Talk to innkeeper
# DEV: Euan Penn
def talk_to_innkeeper():
    # Print story
    full_text = f"""
The innkeeper's eyes dart to the door, and his hand shakes slightly as he finishes wiping down the counter. It's clear the conversation's over for him. He leans in close, his voice dropping even lower.

\"I've said too much already. You should head out now, before more folk show up with questions I can't answer. But do me one favour—find that Goddess. She's your best shot, and ours too. The rest is beyond my reach.\"

You look down at the amulet in your hand. The innkeeper's eyes linger on it for a moment, his gaze almost pleading.

\"Take care. I won't stop you, but you'll need to move quickly. There's more danger here than I can say. Go.\"

With that, he turns away, busying himself with a stack of old tankards, his back already half-turned as though eager for the conversation to end."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow(f"1: {text_color('LEAVE','magenta')} the Tavern")
    print_slow(f"2: {text_color('START','magenta')} a fight")
    
    # Make player choice
    player_choice = make_choice({
        1:["leave", "tavern"],
        2:["fight", "start", "brawl", "barney"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        go_to_bleakhollow(False)
    elif player_choice == 2:
        fight_in_tavern()
    else: 
        print_slow("I don't recognise that option")

# Go tot he armoury
# DEV: Hamse Mahamed
def go_to_armoury():
    # Print story
    full_text = f"""
You approach the armoury, an imposing stone building nestled against the edge of {text_color('Bleakhollow','yellow')},  its weathered sign swinging slightly in the breeze. The town's eerie quiet seems to cling to this place, a thick layer of dust coating the windows, as if even the air itself is hesitant to enter. The building is old, far older than the rest of the village, with a few crooked shutters and an air of abandonment—like it's seen far better days.

The door creaks as you push it open, and the dim light inside barely cuts through the gloom. Rows of rusted swords, dented shields, and cobweb-laden armor line the walls. The musty scent of old leather and iron fills the air, along with a faint hint of decay that lingers in the corners of the room. Everything seems to be in its place, but something about the silence is unsettling. The shop looks as though it hasn't seen a customer in ages, as if it's merely waiting for someone to come along and disturb the stillness.

A figure behind the counter stirs slightly as you enter, but no words are exchanged. The tension in the air is palpable, the silence heavy with unspoken stories."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    # Check inventory for STAKE and if vizier is ALIVE.
    # If True then can collect potions from armoury
    # Else, browse inventory and leave
    if check_inventory("STAKE") == True and status_vizier == "ALIVE":
        # Print story
        full_text = f"""
You push open the door to the armoury once again, and this time, the air feels different. The stale atmosphere still lingers, but there's a sense of anticipation, like you've come with purpose. The same weary figure stands behind the counter, but when you approach, he doesn't immediately ask what you're after. Instead, he eyes you carefully, then nods as if confirming something.

\"You're here about the... well, let's call it an order,\" the man says, his voice gravelly. His eyes narrow for a moment, assessing you.

You nod, reaching into your pocket and pulling out the small satchel the Vizier gave you. The man's expression softens ever so slightly, though his demeanour remains guarded.

\"Ah, that would be it then.\" He shuffles around behind the counter, rummaging through a set of drawers with a faint creak of old wood. After a moment, he pulls out a small, weathered pouch and places it on the counter in front of you.

\"These,\" he mutters, handing you the pouch, \"are sleeping potions. Not the prettiest or most elegant, but they'll do the job just fine. All you have to do is throw them at your target, and they'll drop like a stone. Knock them out cold—easy as that.\"

You peek inside the pouch to find two vials, each containing a swirling, shimmering liquid, faintly glowing with an eerie greenish hue. They're small, but enough to make a difference, you suppose. The man nods in satisfaction.

\"Take care with them. Don't waste 'em, or you might find yourself in a spot of trouble when the rest of your plans fall apart.\" He shrugs, his tone implying he's seen his fair share of failed attempts.

With the satchel now in your hand, you nod your thanks and slip it into your bag, ready to continue your journey. The man gives you a single, curt nod before returning to his work, his eyes already turned to the next task, and the door creaks closed behind you."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs

        add_to_inventory("POTION")
    else:
        # Print story
        full_text = f"""
You step inside the dim armoury, and the heavy door shuts behind you with a quiet thud. The smell of rust and dust fills your nose, a stark contrast to the open, fresh air of the village. The shop is small, cramped with an assortment of swords, axes, and shields that have seen better days. The light filters through grimy windows, casting shadows across the shop. Everything looks worn down, like it hasn't been touched in years, yet there's an unsettling sense of being watched here.

Behind the counter stands a middle-aged man, his hands calloused and scarred from years of welding metal. His face is sharp, but his eyes are tired, hollowed by the weight of whatever burdens the village bears. He looks up at you as you approach, raising an eyebrow at your appearance.

\"Looking for something, eh?\" he asks, his voice low and hoarse, a tone that suggests neither enthusiasm nor welcome.

You glance at the various weapons, your eyes lingering on the worn blades and rusty shields, but you realize you have no money to speak of. You clear your throat, apologizing, and begin to back away.

\"I'm afraid I don't have the coin for anything today,\" you mutter, offering a sheepish smile.

The man's gaze softens just slightly, but only a little. He nods, the weight of countless similar exchanges weighing him down. \"Aye, that's how it goes. You're not the first one to come in without a pouch full of coin. Best be on your way then, if you've no use for anything here.\"

You step back toward the door, the heavy weight of the silence once again filling the room as you exit, the door creaking closed behind you."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs

    print_slow("Press 1 to leave the armoury")

    # Player input to leave armoury
    player_choice = make_choice({
        1:['leave', 'armoury', 'armory']
    })

    # Select player choice
    if player_choice == 1:
        go_to_bleakhollow(False)
    else:
        print_slow("I don't recognise that option")

# Leave the king in the dungeon
# DEV: Matthew Sheldon
def go_to_castle():
    # Print story
    print_slow("------------------------")
    print_slow("ONWARD TO THE CASTLE ...")
    print_slow("------------------------")
    print_slow("")
    full_text = f"""
The path to the castle leads through a gnarled stretch of forest, where twisted trees claw at the sky like skeletal hands. As you press forward, you spot movement in the undergrowth. A creature lumbers into view—hulking, furred, with feathered tufts across its shoulders and cruel talons dragging behind it.

Its face is a terrible cross between a bear and a bird of prey—eyes too intelligent for its bestial form, fixed on you with unmistakable hunger. It snorts, pawing at the earth. Whatever it is, it looks mean, tired of squirrels, and ready to snack on adventurers.

The villagers whisper of such a thing: {text_color('the Gloomclaw','red')}, a nocturnal predator said to stalk the old forest paths for centuries. Of course, legends say a lot of things."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow(f"1: {text_color('RETURN','magenta')} to the crossroads")
    print_slow(f"2: {text_color('FIGHT','magenta')} the Gloomclaw")

    # Make player choice
    player_choice = make_choice({
        1:['back','return','crossroads'],
        2:['fight','gloomclaw','beast']
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        go_to_crossroads()
    elif player_choice == 2:
        fight_gloomclaw()
    else:
        print_slow("I don't recognise that option")

# Leave the king in the dungeon
# DEV: Euan Penn
def fight_gloomclaw():
    global status_guard
    
    # Check if inventory contains STAKE and POTION
    # If false, flee scene
    # If true, engage in fight
    if check_inventory("STAKE") == False and check_inventory("POTION") == False:
        full_text = f"""
You assess the situation quickly. You are brave, perhaps, but not reckless—and currently very unequipped to fight anything resembling a mythological nightmare.

Discretion being the better part of valour (and of keeping all your limbs), you decide to back away slowly, making no sudden movements. The Gloomclaw watches you, curious but not hungry enough to pursue. Not today, at least.

You'll need to return later—ideally with something sharp, magical, or thrown directly at its head."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs
            
        print_slow("")
        time.sleep(0.5)
        go_to_crossroads()
    else:
        # If gloomclaw is ALIVE, engage in class-based fight
        # Else, gloomclaw is DEAD and you can pass
        if status_guard == "ALIVE":
            # Print story
            print_slow("---------------------")
            print_slow("A DEADLY CREATURE ...")
            print_slow("---------------------")
            print_slow("")
            
            # If player is FIGHTER
            if player_class == "FIGHTER":
                full_text = f"""
Your warrior's blood boils at the sight of the beast. This is no time for hesitation.

With a mighty roar, you charge the Gloomclaw, your battleaxe gleaming in the pale light. It lunges—but you are already mid-swing. The blade connects with a satisfying thwack, and the creature's monstrous head sails through the air in a graceful arc, landing somewhere in the underbrush with a wet thud.

The body slumps to the ground, twitching once, then still. You wipe your blade clean and press forward.

Onward to the castle. No beast stands between you and your destiny."""
    
                paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

                for para in paragraphs:
                    lines = textwrap.wrap(para.strip(), width=terminal_width)
                    for line in lines:
                        print_slow(line)
                    print_slow("")  # adds the blank line between paragraphs
                
                status_guard = "DEAD"

                fight_gloomclaw()

            # If player is MAGE
            elif player_class == "MAGE":
                full_text = f"""
You draw your focus crystal and whisper an incantation under your breath. As the Gloomclaw charges, you complete the final syllable, and a burst of shimmering light floods its vision.

The creature skids to a confused halt, blinking rapidly. Then, gently swaying on its feet, it turns and begins to amble in the opposite direction, dazed. It bumps into a tree—bonk—and slumps to the forest floor in a dreamy, bewildered heap.

You tuck your crystal away, muttering something arcane and self-satisfied, and continue along the path."""
    
                paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

                for para in paragraphs:
                    lines = textwrap.wrap(para.strip(), width=terminal_width)
                    for line in lines:
                        print_slow(line)
                    print_slow("")  # adds the blank line between paragraphs
                    
                status_guard = "DEAD"

                fight_gloomclaw()

            # If player is ARCHER
            elif player_class == "ARCHER":
                # If ARCHER has POTION in inventory
                if check_inventory("POTION") == True:
                    full_text = f"""
The Gloomclaw bellows and hurls itself toward you, claws flailing. But you are already moving, nimble, practised, one with the trees. You roll beneath its first swipe, uncap the small vial from the satchel, and lob it backwards as you spring to your feet.

The potion smashes against the creature's side. A hiss of purple mist erupts across its fur. It snarls, staggers… and then, with a pathetic yawn, collapses mid-lunge. Its snores are instant and prodigious.

You adjust your quiver and give the now-slumbering beast a small, smug nod.

Nothing to see here. Just a professional at work."""
    
                    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

                    for para in paragraphs:
                        lines = textwrap.wrap(para.strip(), width=terminal_width)
                        for line in lines:
                            print_slow(line)
                        print_slow("")  # adds the blank line between paragraphs
                        
                    status_guard = "UNCON"

                    fight_gloomclaw()
                
                # If ARCHER does not have POTION in inventory, return to village
                else:
                    full_text = f"""
You dash sideways, firing an arrow mid-roll. It soars gloriously through the air and thunks harmlessly into a tree several feet to the left of the beast.

The Gloomclaw locks onto you instantly. You duck and weave, firing two more arrows that both miss wildly, one of which somehow arcs back and nearly hits you in the foot.

Realising you are rapidly running out of both arrows and options, you spin and sprint, the Gloomclaw growling behind you. Fortunately, it gets distracted by a squirrel. You don't question your luck.

Panting, you make it back to {text_color('Bleakhollow','yellow')}. The village looks a little less bleak now that it isn't full of teeth."""
    
                    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

                    for para in paragraphs:
                        lines = textwrap.wrap(para.strip(), width=terminal_width)
                        for line in lines:
                            print_slow(line)
                        print_slow("")  # adds the blank line between paragraphs 

                    print_slow("")
                    time.sleep(1)
                    go_to_bleakhollow(False)
            else:
                print_slow("I don't recognise what you wish to do")
        else:
            # Guard Dead
            print_slow("The creature lies there, defeated, but you know your quest is still unfinished.")
            print_slow("")
            print_slow(f"1: {text_color('CONTINUE','magenta')} onto the castle")
            print_slow(f"2: {text_color('RETURN','magenta')} to the crossroads")
                
            # Make player choice
            player_choice = make_choice({
                1:["continue", "castle"],
                2:["return", "crossroads"]
            }, "What do you do?")

            # Select player choice
            if player_choice == 1:
                arrive_at_castle()
            elif player_choice == 2:
                go_to_crossroads()
            else: 
                print_slow("I don't recognise that option")

# Fight in tavern - dependant on player_class
# DEV: Katy Jones
def fight_in_tavern():
    # If player is FIGHTER
    if player_class == "FIGHTER":
        full_text = f"""
You spot a couple of rowdy locals eyeing each other from across the tavern, their fists clenched in what seems to be a silent, unspoken challenge. It's all too easy to feel the tension in the air, your blood pumping in anticipation.

You step forward, cracking your knuckles with a grin. The bar's atmosphere changes immediately as a few eyes fall on you. You're no stranger to a brawl, and you're sure you can handle yourself.

Before you can take another step, one of the tavern patrons looks at you with a knowing smirk. \"You look like you're itching for a fight, friend,\" he says, his voice a mixture of mockery and amusement. \"Well, you're not the first to try.\"

With an exaggerated roll of his eyes, he swings at you—a punch that would've been a solid hit to anyone else, but you easily sidestep, letting it sail past your ear. But then - SMACK! A stray mug to the back of your head, thrown by an unseen hand, knocks you off balance. You spin in a daze, trying to regain your footing. It's like something out of a cartoon — your arms windmilling as you try to keep your balance.

The next thing you know, a pair of rough hands is shoving you out the door. You stumble out onto the street, blinking, your face flushed with embarrassment.

\"Try again when you're sober!\" a voice calls from behind you."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs
            
    # If player is MAGE
    if player_class == "MAGE":
        full_text = f"""
You lean against the bar, your eyes scanning the room for anything of interest, when your gaze lands on a small table in the far corner.

A group of locals are hunched over a game of cards, their eyes flashing with the excitement of a high-stakes wager.

You feel an odd pull to join, something about the cards calling to you. Maybe it's your magical intuition or just the need for distraction, but before you can stop yourself, you find yourself sitting at the table, your fingers twitching with excitement. 

The players exchange glances, a bit wary, but one of them hands you a stack of coins and nods toward the deck.

\"Sure you're up for this, stranger?\" he asks, eyebrow raised.

You glance at the cards and, with a deep breath, you start to focus. Counting the cards... anticipating the next moves... But... wait... there's something off. Every card seems to flicker with energy, magical auras blurring your focus. You're so deep into your spellwork that you lose track of the game entirely.

Suddenly, the dealer slams the cards down, eyes blazing. \"That's enough of that!\" In an instant, you find yourself swept off the chair and tossed bodily out of the tavern with a hearty kick. The door swings shut behind you with a bang, leaving you blinking on the street.\"Next time, maybe stick to basic spells!\" someone yells through the window."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs
        
    # If player is ARCHER
    if player_class == "ARCHER":
        full_text = f"""
You can't help but notice a wealthy-looking merchant sitting alone at the bar, his coin pouch bulging in a most suspiciously inviting way. The tavern is full, and a few patrons are sloshing around, distracted by their own affairs. Perfect.

You slip into the shadows, your fingers twitching with the desire to lighten his load. You wait for just the right moment—when his attention is on the bartender—and in one fluid motion, your hand darts toward his belt.

But as your fingers graze the pouch, you misstep on a loose floorboard, and the sharp squeak echoes through the tavern.

The merchant whips around, eyes wide with shock, and before you can make a graceful exit, his hand grabs yours in a vice-like grip. His voice booms across the room, and suddenly everyone's attention is on you.

\"Thief!\" he yells, shaking you like a ragdoll. \"Thief!\"

The next thing you know, you're flying through the air, landing with a soft thud in the dirt outside, your pride suffering more than your physical form.

\"That'll teach you to pick pockets in MY tavern!\" he yells as the door slams shut behind you."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs

    # Go to village, first_start = False
    print_slow("")
    time.sleep(0.5)
    print_slow("")
    time.sleep(0.5)
    go_to_bleakhollow(False)
    
# GO TO LAKE
# DEV: Matthew Sheldon
def go_to_lake():  # Without Amulet
    global status_vizier

    # Check if inventory contains AMULET
    # If False, cannot remove curse from monster/vizier, player dies
    # Else, curse is removed
    if check_inventory("AMULET") == False:    
        full_text = f"""
You tread the narrow dirt path, its curves hemmed in by trees whispering secrets on the breeze. Faint rustling follows your footsteps, movement in the underbrush, perhaps birds... perhaps not. The forest breathes around you, alive and watching.

Ahead, a clearing opens like a held breath, revealing a still, silver lake nestled among the trees. The water laps gently against smooth pebbles, a calming contrast to the morning's raging sea.

You step closer, drawn by the quiet. But something shifts. The wind sharpens. Leaves tremble. Your instincts flare. Muscles tense. Eyes scan. Left. Right. Behind you. A sudden rustle. A burst of motion from the undergrowth. You spin, heart pounding.

A deer.

Its soft, dappled coat glints in the sunlight. It blinks at you—calm, curious—then darts away, vanishing into the trees.

You exhale. Tension drains from your shoulders.

But then… silence.

Too much silence.

A shadow falls across the ground.

You turn, slowly.

Something rises from the lake—slow, deliberate, massive. Its form breaks the water like a waking nightmare. Ten feet tall. No—fifteen. Maybe more. Towering and wet, crowned in lake weed and bones.

Its body is a twisted amalgamation of limbs—arms that end in claws, mouths where none should be. Its skin glistens with slime, mottled like drowned flesh left too long beneath the surface. Milky, pupil-less eyes blink sideways, like a predator of the deep. An ancient symbol—half-eroded and glowing faintly—pulses from beneath its collarbone.

The water around it roils, darkening as if curdling with shadow.

You try to move. You don't get the chance.

It lunges."""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs

        game_over()
    else: # With Amulet
        full_text = f"""
You arrive at the lake, and as soon as your feet touch the muddy bank, the wind howls like an indignant cat who's just been put in the bath.

Then, from the murky depths, a massive, wretched creature surges forward—a hulking mass of writhing tentacles, pulsating with an unnerving amount of teeth that seem to go on forever. It towers over you, a horrible, slithering thing, its body covered in goo and strange barnacles.

With a squelch, the creature lurches toward you, and a grotesque tentacle raises, winding toward you like an oversized snake. You brace yourself for impact, but as the tentacle draws closer, it suddenly lets out a high-pitched squeal, shuddering in pain as if it's the one in distress. It's almost as though it's been slapped by a very unhappy cosmic mother.

Then, warmth radiates from your pocket, where you placed the amulet from the innkeeper. You feel the familiar flicker of something magical, and just before the tentacle strikes, a brilliant burst of light consumes your vision. Your ears are assaulted by a chorus of screams, a cacophony of the most melodramatic shrieking you've only ever heard once before - when your nephew tried out for recorder in the school band.

And then... silence.

When the light fades, standing in front of you, not a 10-foot-tall abomination, but an old, decrepit man. His hair is so wild it looks like a cross between an overgrown bush and a particularly unfriendly broom. His clothes hang loosely off his frail frame, and his face... well, let's just say \"weathered\" doesn't begin to cover it.

\"Ahh! Finally!\" he exclaims, rubbing his eyes dramatically as if he'd just woken from the most unreasonable nap in history. \"I don't know how long I've been trapped in that infernal lake! It could've been days... or decades, or possibly... I don't know, ten minutes? Time works a little funny in there.\"

He takes a deep, exaggerated breath, blinking at you with a mixture of relief and profound confusion.

\"Thank you, by the way. What's your name?\"

\"Uh, it's {text_color(player_name,'green')}, I guess...\"

He nods, seeming somewhat satisfied, then motions toward the now-mildly offended lake. \"I suppose you're here to slay the beast of the castle, aren't you, {text_color(player_name,'green')}?\"

You cross your arms, clearly sceptical, and raise an eyebrow. \"I was told you were a goddess.\"

\"Goddess?!\" The old man almost chokes on his own indignation, and for a moment, you're concerned he might keel over. \"Goddess! What were you expecting, a glowing, ethereal being with a harp and a crown? Long flowing dress like something out of the Renaissance? Bit of cleavage for the lads in the peanut gallery?\"

He shakes his head with a sigh, looking rather put out. \"Well, that's just rude, quite frankly. I apologise for not getting my hair all nice and neat while I was stuck in that accursed lake. I wasn't exactly granted a spa day, you know!\"

\"Right... well, what's going on at the castle then?\"

\"Ahhh, Lenore Bordreaux, that cruel, conniving wretch. She's the reason I'm in this state. Cursed me! Do you know how long I've been looking for a way to stop her reign of terror? I had a great plan, I swear! I was going to free the king, stop her, save the day—be a hero, you know? But then—bam! Wham! She turned me into… this!\"

He gestures to his withered form with an exaggerated flourish, clearly annoyed at the lack of glamour in his current state.

\"I'm too weak now, too frail to continue on this quest alongside you. I've endured years of dark magic and… frankly, it's all a bit much for me, if I'm being honest.\"

With an almost comical air of finality, he hobbles over to you, pulls something from beneath his tattered cloak, and presses a small, ornate stake into your hands.

\"Take this,\" he whispers, \"The Yggdrasil Stake. A truly remarkable weapon. No idea how it works, but it's definitely the thing that'll stop Lenore. You need to strike her right through the cold, dead heart. That's the only way to end this madness. Her reign must end.\""""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs

        print_slow("")
        time.sleep(0.5)
        add_to_inventory("STAKE")
        time.sleep(0.5)
        print_slow("")
            
        print_slow(f"1: {text_color('TALK','magenta')} to the wise man")
        print_slow(f"2: {text_color('RETURN','magenta')} to the crossroads")

        # Set vizier status to ALIVE
        status_vizier = "ALIVE"
            
        # Make player choice
        player_choice = make_choice({
            1:["talk", "wise", "man", "vizier"],
            2:["return", "crossroads"]
        }, "What do you do?")

        # Select player choice
        if player_choice == 1:
            talk_to_vizier()
        elif player_choice == 2:
            go_to_crossroads()
        else: 
            print_slow("I don't recognise that option")

# Talk to vizier (cursed demon)
# DEV: Nathan Hawkes
def talk_to_vizier():
    # Print story
    full_text = f"""
You decide to stay and chat a little longer with the wizened man. He leans in closer, his wrinkled face suddenly looking quite serious, as if the weight of the world is upon him.

\"Ah, well, while you're out there... you'll need something. There's an armoury not far from here. I highly suggest you visit it before you head to the castle. The owner is... well, he's a bit of a character. But you can't miss him, I promise. If he asks who sent you, just say...\" He hesitates for a moment, like he's about to reveal a great secret. His eyes gleam, and he clears his throat dramatically.

\"Say... say that Visier Darnalious, the Grandmaster of the Searing Horizon, Keeper of the Shifting Moons, and Protector of the Sacred Dunes sent you.\" He smiles, pleased with his own pomp and circumstance. \"Yes, yes, that's exactly it.\"

You raise an eyebrow, expecting something impressive to follow.

The smile fades as he senses your scepticism. \"...Or... just tell him {text_color('Roland','green')} sent you.\"

\"{text_color('Roland','green')}?” you ask, blinking in disbelief.

He shrugs nonchalantly, as if {text_color('Roland','green')} is the most natural and expected name for someone of his... distinguished stature. \"Well, it's shorter, isn't it?\"

You stare at him for a moment, processing.

\"...Right.\"

\"Look, I'm proud of my title, ok? I didn't spend 19 gold pieces and 27 minutes waiting in line at the Post Office to be called \"Mr {text_color('Roland','green')}\", thank you very much. But ... I'm sure {text_color('Roland','green')} will suffice for this\" He leans back, looking annoyed. \"Now, off you go. The armoury isn't far. You'll know it by the... uh... well, you'll know it when you see it.\"

You leave {text_color('Roland','green')} to his musing, a bit bewildered by the whole encounter, but with a sense of something even stranger awaiting you in the armoury."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow(f"1: {text_color('TALK','magenta')} to the wise man")
    print_slow(f"2: {text_color('RETURN','magenta')} to the crossroads")
        
    # Make player choice
    player_choice = make_choice({
        1:["talk", "wise", "man", "vizier"],
        2:["return", "crossroads"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        annoy_vizier()
    elif player_choice == 2:
        go_to_crossroads()
    else: 
        print_slow("I don't recognise that option")

# Continue to talk to vizier
# DEV: Nathan Hawkes
def annoy_vizier():
    # Print story, then go to crossroads, no player input
    print_slow(f"You try to catch {text_color('Roland','green')}'s attention. You have many more questions that need answering.")
    print_slow("However, he seems more interested in arguing with a beetle he has spotted on a felled oak tree, so you decide to walk away ...")
    time.sleep(0.5)
    print_slow("Quickly ...")

    time.sleep(0.5)
    print_slow("")
    go_to_crossroads()

# Arrive at castle
# DEV: Dean Robinson
def arrive_at_castle():
    # Print story
    full_text = f"""
The drawbridge is down, and a cold, unpleasant breeze emerges as you step into the castle grounds. The bridge creaks beneath your feet, and you hear a voice carried on the breeze.

\"Ahhh, it appears I have a guest for dinner. It has been some time since I enjoyed good food and good company.\" There is a pause before the voice returns. \"I will have to decide which you shall be.\"

A rumble reverberates around the walls, as though the castle itself is chuckling.

\"Follow the light, let it guide you to me, as it has for the many who have come before you. We can play a while before the feast. It should be entertaining.\"

The voice fades into the stonework, with a parting punctuation.

\"For me.\"

You step through the castle's massive entryway, where the cold air feels strangely heavier, as if laced with centuries of despair and perfume. The grand hall before you stretches into darkness, save for a flickering trail of candles that seem to float mid-air, casting long shadows on the cracked marble floor.

A portrait on the wall watches you with hollow eyes. As you pass, it subtly shifts—first facing left, then right, then somehow upside down, despite the frame never moving. You pause. It stops. You move again. It sighs audibly.

You keep moving. The air thickens as you walk along the corridor, a large set of doors ahead of you. Candles light one by one as you approach, as if welcoming you … or perhaps warning you.

And then you hear her voice again, velvet and venom:

\"You're nearly there. I must admit, anticipation is my favourite flavour. Will you be brave, or will you be ... delicious?\""""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow(f"1: {text_color('CONTINUE','magenta')} into the castle")
    print_slow(f"2: {text_color('LEAVE','magenta')} and return to the crossroads")
        
    # Make player choice
    player_choice = make_choice({
        1:["continue", "castle"],
        2:["leave","run","flee"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        inside_the_castle()
    elif player_choice == 2:
        get_out_of_there()
    else: 
        print_slow("I don't recognise that option")

# Leave the king in the dungeon
# DEV: Nathan Hawkes
def get_out_of_there():
    # Print story
    narrative_lines = [
        {"text": "The large wooden doors stand in front of you, imposing, intimidating. You know what lurks behind them, who waits there for you."},
        {"text": "You step forward, closing the distance between you and your destiny. But from within your core, something takes takes hold."},
        {"text": "Call it fear, call it self-preservation, call it sanity."},
        {"text": "Whatever it is, you hear its call."},
        {"text": "\"Run.\"", "pause": 0.5},
        {"text": "\"Run.\"", "pause": 0.5},
        {"text": "\"RUN!!!\"", "pause": 0.25},
        {"text": "You turn and bolt from the door, charging through the castle grounds. From behind you, you hear a maniacal laughter seeping through the stone. It settles in your ears, working its way through to your brain, stoking the fires of horror that still reside within you.", "pause": 0.5},
        {"text": "You have failed your mission. But, on the bright side, there's always tomorrow."}
    ]
    
    # Loop through each block of narration
    for line in narrative_lines:
        wrapped = textwrap.wrap(line["text"], width=terminal_width)
        for subline in wrapped:
            print_slow(subline)
        if line["pause"]:
            time.sleep(line["pause"])

    play_again()

# Main fight
# DEV: Dean Robinson
def inside_the_castle():
    # Print story
    full_text = f"""
The sound of orchestral organs pulses through the air, distant yet all-encompassing. It's not music, not really—more like the memory of music, half-forgotten and barely held together by bone-dry strings and keys older than time. It coils through the castle like smoke, setting your nerves on edge.

You push open the towering doors to the banquet hall, and for a moment, the sight robs you of breath.

The room is obscene in its grandeur. A vaulted ceiling stretches far above, lost to shadows and cobwebbed chandeliers that sway despite the absence of wind. Gilded mirrors line the walls, cracked in places, their reflections just slightly off, as though recalling past horrors they'd rather forget. Every surface glimmers with excess—gold-trimmed chairs, silken drapes stained with the faintest hint of rust-red, and a feast spread across the long mahogany table that defies nature. Roasted beasts you cannot name. Fruits too vibrant to be real. Goblets of wine so dark they might be ink—or something far worse.

At the head of the table, she waits.

Lady Lenore Bordreaux.

She reclines as though sculpted from moonlight and shadow. Her skin is porcelain-pale, but the kind of porcelain that cracks beneath pressure. Her eyes, glowing faintly violet, appraise you with predatory amusement. She is beautiful in the way a thorn is beautiful—elegant, poised, and certain to draw blood.

Her gown flows like spilt oil, impossibly dark, yet shimmering with the colours of deep space. The fabric moves on its own, subtly shifting like it breathes. Jewels glisten at her throat—rubies, maybe, or crystallised hearts. A crown of delicate bone rests atop her head, too elegant to be barbaric, too grotesque to be comforting. When she speaks, her voice is velvet wrapped around a blade:

\"Darling. You made it. I was beginning to think you'd lost your nerve.\"

She lifts her goblet, the contents clinging unnaturally to the sides.

\"Please, sit. Eat. There's so much to discuss before the killing starts.\"

But you have other plans ..."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    time.sleep(2.5)
    
    # Fight with ARCHER
    if player_class == "ARCHER": 
        print_slow("Lenore scoffs as you draw your bow, her voice laced with venomous amusement")
        print_slow("\"Is this all you've brought? A bit of string tied to a stick? Is this what remains of the Oathkeepers? How utterly quaint.\"")

        # Dice roll - 1 in 6 loss
        if roll_dice(6) == 1:    
            full_text = f"""
You fire the arrow. It cuts through the air, perfect in aim and speed.

But not perfect enough.

In a blur, Lenore moves, her arm flashing upward with predatory grace. She plucks the arrow from the air like a falling leaf, examines it for a moment, then snaps it between her fingers with a delicate crack.

\"Oh dear,\" she coos, voice dripping with mock sorrow. \"You almost had me there.\"

Before you can blink, she dissolves into mist, only to reappear inches from your face, her eyes gleaming with cruel delight.

You feel her breath, ice-cold and tinged with decay.

And then pain.

A dagger slips past your ribs, straight into your heart. You gasp, but no sound comes.

\"My sweet child,\" she whispers, twisting the blade. \"If only you were a little faster.\""""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs
            
            time.sleep(0.5)
            game_over()
        else:
            full_text = f"""
You've had enough of her theatrics. Enough of the games. Enough of the talking

With a silent breath, you notch the stake to your arrow. For a heartbeat, time stands still.

Then — release.

The arrow whistles through the air, glowing faintly as it soars. Lenore's expression shifts—not to fear, but to recognition. Too late.

The stake drives cleanly through her heart, and the impact sends her reeling. Her eyes widen in disbelief as a scream tears from her throat—not of pain, but of rage. The shadows recoil. Her form flickers.

She collapses to her knees, clawing at the stake protruding from her chest. The ground trembles beneath her.

\"No... not from the likes of you…\"

And then, silence."""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs
            
            time.sleep(0.5)
            defeat_lenore()

    # Fight with FIGHTER
    elif player_class == "FIGHTER":
        print_slow("Lenore tilts her head, appraising you with disdainful amusement.")
        print_slow("\"All brawn and no brain… I suppose that makes you dinner, then.\"")
        
        # Dice roll - 1 in 6 loss
        if  roll_dice(6) == 1:
            full_text = f"""
Rage overtakes reason. With a howl, you charge—battleaxe raised, every muscle burning with fury.

But fury is not enough.

Lenore vanishes in a whisper of mist, your axe cutting only air. You skid to a halt, too late.

She reappears behind you, a shadow of wicked grace, and plunges a frozen dagger into your shoulder. You cry out, staggering forward, but she holds fast.

\"You filthy animal,\" she hisses in your ear, dragging the blade downward in a slow, deliberate line along your spine. \"You should've put your brain to better use.\"

Darkness takes you as her laughter echoes through the halls"""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs
            
            time.sleep(0.5)
            game_over()
        else:
            full_text = f"""
The blood rushes in your ears. Rage crackles in your chest, white-hot and unyielding.

\"Eat this.\"

With a snarl, you launch forward—not to strike, but to throw.

The stake whistles through the air with brutal precision, a blur of silver and fury. It slams into Lenore's chest with a sickening crunch, burying itself deep in her heart.

She staggers, her mouth agape in silent disbelief as cracks of light ripple across her skin.

\"No… you…\"

Her form convulses, then collapses into a heap of silk and shadow. The castle itself groans around you, the spell broken."""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs
            
            time.sleep(0.5)
            defeat_lenore()
    # Fight with MAGE
    else:
        full_text = f"""
Lenore rises from her throne, eyes glinting like dying stars. Her voice drips with serpentine allure.

\"Finally… a worthy adversary. Or perhaps… a welcome ally ...\" She pauses, before extending her hand. \"Join me, and I can show you power beyond your wildest imagination.\""""
    
        paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

        for para in paragraphs:
            lines = textwrap.wrap(para.strip(), width=terminal_width)
            for line in lines:
                print_slow(line)
            print_slow("")  # adds the blank line between paragraphs
        
        # Dice roll - 1 in 6 loss
        if roll_dice(6) == 1:
            full_text = f"""
You smirk, meeting her gaze.

\"You have no idea how far my imagination can reach.\"

Your wand glows with arcane fury. The stake rises, spinning in the air before launching itself toward Lenore like a bolt of judgment.

But with a calm gesture, she lifts her hand.

The stake halts mid-air.

\"Oh, but I do,\" she purrs.

She twists her wrist. The stake trembles, then turns—its tip now aimed at you.

With a wicked cackle, she flicks her hand. The stake hurtles back, piercing your chest with unholy precision.

\"And it seems it's not far enough.\"

Darkness blooms as you fall, the castle whispering its last lullaby."""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs

            time.sleep(0.5)
            game_over()
        else:
            full_text = f"""
You narrow your eyes, unfazed.

\"I am a Mage of the Oathkeepers. Your trivial parlour games have no effect on me.\"

You raise your wand with a quiet authority. The air shimmers, humming with raw energy. The stake lifts from your satchel, suspended in a sphere of magic.

With a pulse of intent, it shoots forward—faster than the eye can track.

It slams into Lenore's chest with a sharp crack, embedding itself in her heart.

Her mouth opens in a wordless scream, her body convulsing in a burst of light and shadow. She collapses, her reign extinguished by your will alone."""
    
            paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

            for para in paragraphs:
                lines = textwrap.wrap(para.strip(), width=terminal_width)
                for line in lines:
                    print_slow(line)
                print_slow("")  # adds the blank line between paragraphs
            
            time.sleep(0.5)
            defeat_lenore()

# Player defeats BBEG
# DEV: Kyle Marsden
def defeat_lenore():
    # Print story
    full_text = f"""
Shock flickers across Lenore's face—a rare crack in her porcelain poise. Her hands claw at the stake embedded in her heart, but it's too late.

Flames erupt from the wound, licking across her dress, her skin, her throne. She lets out a guttural scream, the sound shrill and inhuman, echoing through the castle like the last note of a funeral dirge.

The fire consumes her quickly. Where once there was flesh, now only blackened crystal remains. Her body twists and writhes as the blaze eats away at her until, piece by piece, she calcifies—an obsidian statue frozen mid-agony.

As the final flame dies and the air stills, a brittle crack slices the silence. Lenore's face, caught in a final gasp, locks in place—entombed for all eternity.

You step closer, the heat still lingering in the air. Around her neck, untouched by fire or flame, sits her choker. At its centre, the gem gleams—vivid, pulsing faintly. It is the only thing left unmarred by the blaze.

Whatever power it holds, it endured. Just like you."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow(f"1: {text_color('TAKE','magenta')} the gem")
    print_slow(f"2: {text_color('LEAVE','magenta')} it behind and raid the castle")
        
    # Make player choice
    player_choice = make_choice({
        1:["take", "gem"],
        2:["leave","behind", "raid"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        take_gem()
    elif player_choice == 2:
        raid_castle()
    else: 
        print_slow("I don't recognise that option")

# Leave the king in the dungeon
# DEV: Kyle Marsden
def take_gem():
    # Print story
    full_text = f"""
You can't help it. The gem's pulsating grows stronger, urging you forward, guiding your every step. It calls to something deep within you, an instinct you've learned to trust in this dark world.

Reluctantly, you turn away from the treasure and head deeper into the castle. The eerie silence presses in on you, and as you approach the dungeon doors, the gem in your hand beats like a heart—louder now, quicker.

Something compels you to open the door. You feel an overwhelming urge to descend into the bowels of the castle, the gem leading you down the winding, damp stone staircase.

The dungeon is vast, its shadows concealing unknown horrors. But the gem's pull intensifies, and it soon becomes clear: you are not alone here. As you reach the lowest level, a flicker of movement catches your eye—figures, bound and weak, but unmistakably alive.

They look at you with desperation, as if they have been waiting for someone - you, perhaps - to free them. The gem, now throbbing in your hand, seems to be reaching out to them. Could it be... they were once its protectors? Or perhaps something far darker?

You stand at the threshold of a new mystery, unsure of what lies ahead, but certain that whatever it is, the gem has brought you here for a reason."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow(f"1: {text_color('FOLLOW ','magenta')} the gem")
    print_slow(f"2: {text_color('LEAVE','magenta')} the castle")
        
    # Make player choice
    player_choice = make_choice({
        1:["follow", "gem"],
        2:["leave","behind", "castle"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        find_king()
    elif player_choice == 2:
        leave_castle()
    else: 
        print_slow("I don't recognise that option")

# Find king in dungeon
# DEV: Kyle Marsden
def find_king():
    # Print story
    full_text = f"""
The pull of the gem is irresistible, and as if compelled by some invisible force, you begin walking toward the dungeon's depths. Each step brings you closer to the source of the gem's power, its energy vibrating in your very bones.

The stone walls close in around you as you descend, the flickering light of the single candle growing ever stronger. Finally, you reach the bottom of the staircase, and you find yourself facing a lone cell, its iron bars rusted and worn. The air is thick with the stench of dampness, and from within the cell, you hear the unmistakable sound of chains rattling.

As you peer inside, your heart skips a beat. The man lying there is like nothing you expected. His hair, tangled and matted, covers his face in wild knots. His once regal form has withered into a frail, almost skeletal frame, and his sunken eyes seem to gleam with a desperate, almost maddened light.

He looks up at you, and in his cracked voice, he cries out.

\"Please! Get me out of here! I'm {text_color('King Eryndor','cyan')}! I will shower you in riches! Please, just get me out of here!\"

You step closer, your mind racing. Could this be the true {text_color('King Eryndor','cyan')}, the lost ruler of the land? Or is this another twisted trick, a creature playing on your empathy? His gaunt features and broken demeanour suggest that he was once powerful, but now, he seems nothing more than a shell of his former self.

The gem in your hand thrums loudly, as if urging you to make a decision."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow(f"1: I {text_color('SAVE ','magenta')} the man")
    print_slow(f"2: I {text_color('LEAVE','magenta')} the man")
    print_slow(f"3: I {text_color('KILL','magenta')} the man")
        
    # Make player choice - multiple endings
    player_choice = make_choice({
        1:["save"],
        2:["leave"],
        3:["kill"]
    }, "What do you do?")

    # Select player ending
    if player_choice == 1:
        save_king()
    elif player_choice == 2:
        leave_king()
    elif player_choice == 3:
        kill_king()
    else: 
        print_slow("I don't recognise that option")

# Raid the castle
# DEV: Kyle Marsden
def raid_castle():
    # Print story
    full_text = f"""
The gem calls to you, but you ignore it, your focus shifting to the grandeur of the castle. You walk past the charred remains of Lenore, feeling the weight of your victory settling in. The gold and jewels scattered throughout the hallways shine like a treasure trove awaiting a worthy taker.

With a grin, you scour the lavish rooms of the castle, filling your pockets with riches. Gold chalices, priceless ornaments, and shimmering jewels—the spoils of Lenore's reign are yours for the taking. You gather what you can carry, knowing full well that these treasures will fetch a hefty price back in {text_color('Bleakhollow','yellow')}.

As you step over the wreckage of the once-feared queen's reign, you make your way to the castle's entrance. The drawbridge beckons you back to the outside world, leaving the haunted halls behind.

The castle fades in the distance as you head toward your next adventure, the sound of the wind carrying the faintest echoes of Lenore's final screams."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow("")
    print_slow("")
    play_again()

# Leave the castle, raid for gold
# DEV: Kyle Marsden
def leave_castle():
    # Play story
    full_text = """
You stand there for a moment, the pulsating gem still warm in your hand, but its allure starts to fade. The decision feels heavy, but you know in your gut that this is not the time to let some cursed object drag you deeper into the castle's web.

With one last glance at Lenore's remnants, you turn your back on the dungeon door. You step out of the darkened corridors and into the open air, the castle behind you now a crumbling memory. The gem still hums in your hand, but you shove it deep into your pack, out of sight.

You make your way through the castle grounds, past the gold and treasures you left untouched. As you cross the drawbridge, the cool night air feels like a release—a breath of freedom. The haunting whispers of the castle fade away, replaced by the serenity of the outside world.

The forest awaits, and though you don't know what adventures lie ahead, you're certain of one thing: this was not your fight. Not today. The treasure of the castle will stay buried, its mysteries unsolved, as you move on with your life."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow("")
    play_again()

# Rescue the king frmo the dungeon
# DEV: Kyle Marsden
def save_king():
    # Print story
    full_text = f"""
You hesitate for a moment, weighing the consequences. The pitiful sight of the man chained in the dungeon pulls at your heart, but the gem's pull on you is undeniable. You approach the cell and with a firm hand, you unlock the chains that bind him.

The man stumbles to his feet, his once-grand posture now slumped in weakness. His eyes look into yours with gratitude, a glimmer of the ruler he once was shining through.

\"You… you truly will save me? Thank you, I shall reward you beyond your wildest dreams. You have my word.\"

With the gem in your possession and the king freed from his chains, you lead him out of the dungeon. His progress is slow at first, but soon he gathers strength, thanks to the gem's strange energy.

Once back in {text_color('Bleakhollow','yellow')}, the village is in shock at your return with the king. Word quickly spreads, and soon the village celebrates. The people, who once doubted your strength, now revere you as the one who rescued their king. The air is filled with feasts, cheers, and music. Eryndor, for all his frailty, commands the people, restoring his kingdom to life in {text_color('Bleakhollow','yellow')}.

You're honored with wealth, accolades, and a place by his side. King Eryndor rules in benevolence, as he always has, assuaging your trepidation when you first met. The legend of the Oathkeeper who saved {text_color('Bleakhollow','yellow')} - nay, Vel'Rath - spread around the tavern like wildfire. Travelling bards embellish those stories, talking of your heroic conquests against devils and demons that you have yet to meet. While some are elaborate in ways you could not foresee, you leave them to their merriment, enjoying the ballads and odes in your honour."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow("")
    print_slow("")
    play_again()

# Leave the king in the dungeon
# DEV: Kyle Marsden
def leave_king():
    # Print story
    full_text = f"""
You look down at the withered man, uncertainty gnawing at you. He pleads for your help, but something doesn't sit right. His words, his desperation—it all feels too orchestrated, too manipulative.

With a final glance at him, you make your choice. You turn on your heel, leaving the king chained in the dungeon. The gem pulsates weakly in your hand, but you ignore it as you ascend the stairs and make your way back to {text_color('Bleakhollow','yellow')}.

When you arrive, you report what you found: \"Lenore killed the king. I couldn't stop her in time.\" The village, understandably, is distraught, but they appreciate your efforts. They mourn the loss of their ruler, and a solemn silence falls over {text_color('Bleakhollow','yellow')} as they prepare for what comes next.

You know the truth — Eryndor is still alive, his fate is sealed in that dungeon—but the village seems at ease, for now."""

    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow("")
    print_slow("")
    play_again()

# Kill the king
# DEV: Kyle Marsden
def kill_king():
    global player_class

    # Print story
    print_slow("The gem pulses with malevolent energy, the temptation almost too much to resist. You make your decision.")

    # King NPC death dependant on player_class
    if player_class == "FIGHTER":
        kill_method = "In one swift motion, you raise your weapon and strike."
    elif player_class == "MAGE":
        kill_method = "Your hands start to move, shaping, light eminating from your fingertips."
    elif player_class == "ARCHER":
        kill_method = "You notch your arrow and raise your bow, your target in point blank range."
    else:
        kill_method = "In one swift motion, you raise your weapon and strike."

    # Continue story
    full_text = f"""
{kill_method} The king barely has time to react, his eyes wide with shock before he collapses to the stone floor. His body spasms briefly before it stills, and the cold silence of the dungeon is broken only by your heavy breathing.

You take the gem, still thrumming with power, and leave the king's lifeless form behind. You make your way back to {text_color('Bleakhollow','yellow')}, the village none the wiser.

When you arrive, you tell them what you found: \"Lenore is gone. I found someone in the dungeon, likely her aide. They were dangerous, but I dealt with it.\"

The villagers seem to accept your version of the story, although there's a glimmer of unease in their eyes. Still, they are grateful for your return, though they don't know the full truth of what transpired in the dungeon.

The gem remains in your possession, and you wonder whether its true purpose will ever reveal itself. Perhaps you have just made a deal with a force much darker than you can imagine."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line)
        print_slow("")  # adds the blank line between paragraphs
    
    print_slow("")
    print_slow("")
    play_again()

# Game over - death scehe
# DEV: Nathan Hawkes
def game_over():
    # Print story, with delays for effect
    time.sleep(0.75)
    print_slow("")
    time.sleep(0.75)
    print_slow("")
    time.sleep(0.75)
    print_slow("")
    time.sleep(0.75)

    narrative_lines = [
        {"text": "Darkness takes you. And in that silence, peace.", "pause": 0.25},
        {"text": "There is no pain. No body. No gravity pulling you down—only the weightless drift of a soul unanchored.", "pause": 0.25},
        {"text": "Around you, nothing. An infinite hush, as if the world itself is holding its breath.", "pause": 0.5},
        {"text": "Then, a glimmer. A white speck on the horizon of black. It grows slowly and steadily. Is it moving towards you? Are you moving toward it? You can't be sure.", "pause": 0.25},
        {"text": "As the light nears, so too does dread. Not fear, but something colder. Something older.", "pause": 0.25},
        {"text": "From the white, a face begins to form. Porcelain smooth. Eyes like endless wells of night. Lips like crimson wax. Golden threads suspend the mask in place, shimmering with divine stillness.", "pause": 0.5},
        {"text": "The mask fills your sight, then shrinks again.", "pause": 0.25},
        {"text": "She stands before you. Raven-haired. Still as marble. Wrapped in black, adorned in silence.", "pause": 0.65},
        {"text": "\"It is time,\" she whispers.", "pause": 0.25},
        {"text": "The words fall like feathers. Inevitable. Final. Not unkind. She does not rejoice to see you, nor does she mourn. You pass her, or she passes you. Her light dims behind you.", "pause": 0.25},
        {"text": "You travel on to whatever lies beyond her veil.", "pause": 0},
    ]
    
    # Loop through each block of narration
    for line in narrative_lines:
        wrapped = textwrap.wrap(line["text"], width=terminal_width)
        for subline in wrapped:
            print_slow(subline)
        if line["pause"]:
            time.sleep(line["pause"])

    time.sleep(0.5)
    print_slow("")
    print_slow("")
    play_again()

# Ends game, credits
# DEV: Nathan Hawkes
def game_end():
    # Print credits
    print_slow(f"Thanks for playing {text_color('THE OATHKEEPER', 'cyan')}! This text-based adventure game was created by:")
    print_slow("")
    print_slow("Alfarooq Dahoum")
    print_slow("Nathan Hawkes")
    print_slow("Katy Jones")
    print_slow("Hamse Mahamed")
    print_slow("Kyle Marsden")
    print_slow("Euan Penn")
    print_slow("Dean Robinson")
    print_slow("Matthew Sheldon")
    print_slow("")
    time.sleep(0.75)
    print_slow(f"{text_color('Special Thanks To ...', 'yellow')}")
    print_slow("")
    print_slow("The Staff at Code Nation")
    print_slow("Mr Python")
    print_slow("Whoever created coffee")
    print_slow("ChatGPT for creating the world")
    print_slow("Skynet for letting us live in it")
    print_slow("Our Lord and Saviour, Matthew Mercer")
    print_slow("The hand of Vecna")
    print_slow("")
    print_slow("")
    full_text = """
This game is owned and developed by The Hype Squad. Any resemblance to actual vampires, gloomclaws, or competent adventurers is purely coincidental... mostly. We may have borrowed a few ideas after a particularly enthusiastic and panic-fuelled afternoon session. No actual gloomclaws were harmed in the making of this game. Except the one that you killed. You murderer. Side effects of playing may include an uncontrollable urge to roll dice, speak in a dramatic fantasy voice, and argue about obscure rules. The Hype Squad is not responsible for any lost sleep, failed real-world quests, or sudden urges to acquire a twenty-sided die collection. Play responsibly."""
    
    paragraphs = textwrap.dedent(full_text).strip().split('\n\n')

    for para in paragraphs:
        lines = textwrap.wrap(para.strip(), width=terminal_width)
        for line in lines:
            print_slow(line, 0.0015)
        print_slow("")  # adds the blank line between paragraphs

    print_slow("")
    print_slow("")
    print_slow("The Unbound will return.")
    exit()

# Asks if player wants to start again or quit
# DEV: Nathan Hawkes
def play_again():
    # Make choice to restart
    print_slow("Do you want to play again?")
    print_slow("")
    print_slow(f"1: {text_color('YES','magenta')}, play again")
    print_slow(f"2: {text_color('NO','magenta')}, I'm good")
        
    # Make player choice
    player_choice = make_choice({
        1:["yes","y"],
        2:["no","n"]
    }, "What do you do?")

    # Select player choice
    if player_choice == 1:
        game_start()
    elif player_choice == 2:
        game_end()
    else: 
        print_slow("I don't recognise that option")

# Run Game
# DEV: Hype Squad
game_start()