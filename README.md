# MECHMANIA PROJECT
# By Dane Zieman, Mark Dabler, Karol Stolarski
This repository contains the code for the MechMania 2018 named "Luke".
The challaenge was an RPG style rock paper scissors game, where players
can move around a map, slay monsters and gain stats in preparation for
the final duel at the end. 

Code in this repository consists of provided game code and our written bot code. The MyBot.py code was written by us, the rest was given by the competition

The code in this repository created a bot that used a decision tree 
that took in information of the current board state and decided where to move
the dueling algorithm attempted to determine what strategy the opponent was
using and counter it.

This team placed 8/41 at the competition.

The code was created over a span of 24 hours, and is left in its original state to reflect the program at the conclusion of the competition

# Mechmania Python Starter Pack

Here's all the code you need to get started with making a bot for Mechmania in Python. Just do these steps:

* Pre-Setup -- install Docker, Node, and the `mm` command line tools
* Setup -- Clone this repository and start running your bot!

# Windows Pre-Setup

1. First, install Node. To do this, go [here](https://nodejs.org/en/download/) and download the Windows Installer.

2. Next, install Docker Toolbox for Windows.
   * Go to [this](https://docs.docker.com/toolbox/toolbox_install_windows/) site and click the button that says "Get Docker Toolbox for Windows".
   * Open the installer and follow the instructions to install Docker
   * If you don't already have Oracle VM VirtualBox, you will also go through a series of prompts to install VirtualBox.
   * Once Docker is installed, open the "Docker Quickstart Terminal" application (It will take a few minutes to get set up the first time you start it.  This process may involve more Windows prompts for permissions.)
3. Within Docker, run `npm install -g mechmania`.  This gets the `mm` command line tools, which are used to test and submit bots for the tournament.

# Mac Pre-Setup

1. First, install Node. To do this, go [here](https://nodejs.org/en/download/) and download the macOS Installer.

2. Next, install Docker for Mac.
   * You can find the installer [here](https://store.docker.com/editions/community/docker-ce-desktop-mac).
   * Open the installer and follow the instructions to install Docker

3. Run `npm install -g mechmania`.  This gets the `mm` command line tools, which are used to test and submit bots for the tournament.

# Setup

1. Clone this repo (or fork it or download it somewhere as a ZIP)
2. Modify the script at `MyBot.py`.
    * Write your code after the `YOUR CODE BELOW` comment, making sure to call `game.submit_decision()` once per turn.
    * You may also add other files or dependencies, but if you do, make sure to update the `.dockerignore` and `Dockerfile`s accordingly. If you have any questions about this, we're here to help!
3. Run `mm play .`
    * This will build the bot in the given directory (`.`) and then starts a game in which your bot fights against itself.
4. To run two different bots against each other, run `mm play bot1_directory bot2_directory`.
    * You must have valid `.dockerignore` and `Dockerfile` files in each directory.  We reccomend cloning this repository multiple times to achieve this.

Use `mm help` for more information!

# Game_API Information
Within the file `Game_API.py`, there are a variety of helpful functions for writing your bot.  You can use the `game` object in the `MyBot.py` script to run any of these functions (e.g. `game.get_turn_num()`).

__IMPORTANT__: Do NOT use `print()` for debugging, as this will make your bot fail when the game runs.  Instead, use the `game.log()` function in `Game_API.py`.

Within `Game_API`, three other classes are defined -- `Player`, `Monster`, and `DeathEffects`.  We recommend only accessing the fields in these classes, since changing them might cause the `game` object to not properly represent the current state of the game.

##### The following fields are in the `Player` class:
- `player_num` : `int` (either 1 or 2)
- `name` : `str` (either "Player1" or "Player2")
- `stance` : `str` -- string representation of the player's stance -- "Rock", "Paper", or "Scissors" (Note: on the first turn, each player's stance will be "Invalid Stance", since neither player has yet chosen a stance)
- `health` : `int` -- the player's health.  If a player's health reaches 0, they die.
- `speed` : `int` -- the player's speed.
- `movement_counter` : `int` -- the movement counter will go down by 1 each turn.  Once a player's movement counter is equal to their speed, they will move to their destination.
- `location` : `int`
- `destination` : `int` (Note: on the first turn, the player's destination will be -1, since the player hasn't yet set a destination)
- `dead` : `bool` (This should always be `False`, since once a player dies, the game is over)
- `rock` : `int` -- the player's Rock attack stat
- `paper` : `int` -- the player's Paper attack stat
- `scissors` : `int` -- the player's Scissors attack stat

##### The following fields are in the `Monster` class:
- `name` : `str` -- represents the class of this monster.  All monsters with the same name should have the same base stats (health, attack, respawn_rate, death_effects, and attack)
- `stance` : `str`
- `health` : `int`
- `respawn_rate` : `int` -- number of turns for the monster to respawn after dying
- `respawn_counter` : `int` -- turns until this monster will respawn (Note: if `dead=False`, then you should ignore the value of this field.)
- `location` : `int`
- `dead` : `bool`
- `death_effects` : `DeathEffects` -- Gives information on the buffs given to the player when this monster dies on the same node as them.
- `attack` : `int` -- the amount of damage the monster deals per turn
- `base_health` : `int` -- the health that the monster will have after respawning

##### The following fields are in the `DeathEffects` class.
Each field corresponds to the buff provided to a player's stat from defeating a monster:
- `rock` : `int`
- `paper` : `int`
- `scissors` : `int`
- `health` : `int`
- `speed` : `int`

#### The following are all functions in `Game_API`
(Note: For any function that returns Player, Monster, or DeathEffects structs, the data in the structs may change between one turn and another, so you should make sure to only use structs returned during the current turn)

`log(strn)`
Logs the string `str` to `stderr` for debugging.

`get_duel_turn_num()`
Returns the turn number when the duel will occur

`get_adjacent_nodes(node)`
Takes an int `node` and returns a list of `int`s representing the nodes adjacent to `node`.

`get_all_monsters()`
Returns a list of all the monsters in the game.

`get_self()`
Returns a `Player` object representing the player you are controlling.

`get_opponent()`
Returns a `Player` object representing your opponent.  (Note: the opponent's destination will always appear to be -1.  This is by design -- neither player can see the other's destination)

`submit_decision(destination, stance)`
Takes an `int` `destination` and a string `stance` and sends this decision to the game engine.  You should call this method exactly once per turn.

`shortest_paths(start, end)`
Returns a list of all shortest paths between `start` and `end` nodes (passed in as `int`s).
Each element of the returned list will be a list of integers, representing the steps required to follow the path to `end`.  These lists will include `end`, but will not include `start` unless `start==end`.

So, as a hypothetical example (that doesn't necessarily match the game map), `shortest_paths(1,5)` could return the following:
```
[[2, 3, 4, 5]
[2, 6, 7, 5]
[9, 8, 7, 5]]
```
In this example, there are 3 paths, each of length 4, that can get from node `1` to node `5`.

`has_monster(node)`
Returns a `bool` indicating whether there is a monster at node `node`.

`get_monster(node)`
Returns a `Monster` struct for the monster located at `node`.  It is reccomended to check if there is a monster at `node` first, using `has_monster(node)`.  If you call `get_monster` for a node without a monster, an invalid monster will be returned.

`nearest_monsters(node, search_type)`
Returns a list of `Monster` structs for all monsters nearest to `node` (including on `node` itself), only considering monsters according to the `search_mode` parameter:
- `search_mode = 0`: Searches all monsters
- `search_mode = 1`: Only searches for live monsters
- `search_mode = 2`: Only searches for dead monsters

`nearest_monsters_with_name(node, name, search_type)`
Same as `nearest_monsters`, but only considers monsters with name `name`.
(Note: since, on our map, there is only one monster with any given name, the list returned by this method will contain a maximum of 1 monster)
# mechmania2018
# mechmania_2018
