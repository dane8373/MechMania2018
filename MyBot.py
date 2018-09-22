# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # DO NOT REMOVE
health_time=0
early_flag=True
mid_flag=False
late_flag=False
path_pointer=0
# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game
    #health_spawns=[0,40,80,120,160,200,240,280];
    me = game.get_self()
    if (early_flag):
        monsters = [10, 6, 1, 0, 3]
        if me.location == me.destination: # check if we have moved this turn
            for i in monsters:
                if game.get_monster(i).dead == False or game.get_monster(i).respawn_counter <= 3:
                    paths = game.shortest_paths(me.location, i)
                    destination_node = paths[random.randint(0, len(paths)-1)][0]
            # get all living monsters closest to me
            #monsters = game.nearest_monsters(me.location, 1)

            # choose a monster to move to at random
            #monster_to_move_to = monsters[random.randint(0, len(monsters)-1)]

            # get the set of shortest paths to that monster
            #paths = game.shortest_paths(me.location, monster_to_move_to.location)
            #destination_node = paths[random.randint(0, len(paths)-1)][0]
        else:
            destination_node = me.destination
        opp_loc=game.get_opponent().location
        opp_path=game.shortest_paths(me.location, opp_loc)
        opp_stance=game.get_opponent().stance
        if (me.movement_counter - me.speed) == 1:
            if game.has_monster(me.destination) and (game.get_monster(me.destination).dead == False):
                chosen_stance=get_winning_stance(game.get_monster(me.destination).stance)
            # if there's a monster at my location, choose the stance that damages that monster
        if game.has_monster(me.location) and (game.get_monster(me.location).dead == False):
            # if there's a monster at my location, choose the stance that damages that monster
            chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
        elif len(opp_path[0])<=1 and opp_stance!="Invalid Stance" and (me.movement_counter - me.speed) > 1:
            chosen_stance=get_winning_stance(opp_stance)
        else:
            # otherwise, pick a random stance
            if (me.movement_counter - me.speed) > 1:
                chosen_stance = stances[random.randint(0, 2)]
        #if game.get_monster(0).dead == False:
            #health_time=40+game.get_turn_num()
        if  me.location==0 and game.get_monster(0).dead and me.movement_counter - me.speed <= game.get_monster(0).respawn_counter and game.get_monster(0).respawn_counter < 7:
            destination_node=0
        if game.get_turn_num()>160:
            early_flag=False
            mid_flag=True
    if mid_flag:
        path = [0, 1, 3, 2, 4, 13,12,11,10,0]
        if me.location == me.destination: # check if we have moved this turn
            destination_node=path[path_pointer]
            if path_pointer <len(path)-1:
                path_pointer+=1
            else:
                path_pointer=0
            # for i in monsters:
            #     if game.get_monster(i).dead == False:
            #         paths = game.shortest_paths(me.location, i)
            #         destination_node = paths[random.randint(0, len(paths)-1)][0]
            # get all living monsters closest to me
            #monsters = game.nearest_monsters(me.location, 1)

            # choose a monster to move to at random
            #monster_to_move_to = monsters[random.randint(0, len(monsters)-1)]

            # get the set of shortest paths to that monster
            #paths = game.shortest_paths(me.location, monster_to_move_to.location)
            #destination_node = paths[random.randint(0, len(paths)-1)][0]
        else:
            destination_node = me.destination
        opp_loc=game.get_opponent().location
        opp_path=game.shortest_paths(me.location, opp_loc)
        opp_stance=game.get_opponent().stance
        if (me.movement_counter - me.speed) == 1:
            if game.has_monster(me.destination) and (game.get_monster(me.destination).dead == False):
                chosen_stance=get_winning_stance(game.get_monster(me.destination).stance)
        if game.has_monster(me.location) and (game.get_monster(me.location).dead == False):
            # if there's a monster at my location, choose the stance that damages that monster
            chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
        elif len(opp_path[0])<=1 and opp_stance!="Invalid Stance" and (me.movement_counter - me.speed) > 1:
            chosen_stance=get_winning_stance(opp_stance)
        else:
            # otherwise, pick a random stance
            if (me.movement_counter - me.speed) > 1:
                chosen_stance = stances[random.randint(0, 2)]
        #if game.get_monster(0).dead == False:
            #health_time=40+game.get_turn_num()
        #if game.get_monster(0).dead and 5 == game.get_monster(0).respawn_counter:
            #destination_node=0
        if game.get_turn_num()>300:
            mid_flag=False
            late_flag=True
    if late_flag:
        destination_node=0;
        chosen_stance="Paper"
    #destination_node=0 #IMPORTANT DONT CHANGE
    # submit your decision for the turn (This function should be called exactly once per turn)
    if (game.get_turn_num()<7):
            destination_node=1
    game.submit_decision(destination_node, chosen_stance)
