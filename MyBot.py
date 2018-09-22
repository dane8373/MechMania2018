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
mid_num=0
mid_path=[[0]]
# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

def check_monster(game, node):
    if (game.has_monster(node)):
        if (game.get_monster(node).dead == False):
            return True
    return False

def slay_monster(game, node):
    return get_winning_stance(game.get_monster(node).stance)
    
def next_to_spawn(dead_monsters, game, me):
            soonest=120
            next_monster=0
            for i in dead_monsters:
                if (game.get_monster(i).respawn_counter < soonest):
                    soonest = game.get_monster(i).respawn_counter < soonest
                    next_monster = i
            return game.shortest_paths(me.location, next_monster)

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
            if check_monster(game, me.destination):
                #
                #
                chosen_stance = slay_monster(game, me.destination)
                #
                #
                #chosen_stance=get_winning_stance(game.get_monster(me.destination).stance)
            # if there's a monster at my location, choose the stance that damages that monster
        if check_monster(game, me.location):
            # if there's a monster at my location, choose the stance that damages that monster
            #chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
            #
            #
            chosen_stance = slay_monster(game, me.location)
            #
            #
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
        if me.paper >=8 and game.get_turn_num()>125:
            early_flag=False
            mid_flag=True
            mid_num=0
            if (me.location==1 or me.location==3):
                mid_path = game.shortest_paths(me.location, 4)
            else:
                mid_path = game.shortest_paths(me.location, 0)

    if mid_flag:
        game.log(str(me.location))
        if me.location == 0:
            mid_num=0
            if game.get_monster(0).dead and me.movement_counter - me.speed <= game.get_monster(0).respawn_counter and game.get_monster(0).respawn_counter < 7:
                mid_path=[[0]]
            if game.get_monster(4).dead == False: # go to 4
                if game.get_monster(3).dead == False and me.speed<5: # go through 3
                    mid_path = game.shortest_paths(me.location, 3)
                else:
                    mid_path = game.shortest_paths(me.location, 4)
            elif game.get_monster(11).dead == False: #go to 11
                mid_path = game.shortest_paths(me.location, 11)
            elif game.get_monster(16).dead == False: #go to 16
                mid_path = game.shortest_paths(me.location, 16)
            else:
                mid_path = next_to_spawn([11,16, 4], game, me)
                #
                #

        if me.location == 3:
            mid_num=0
            if game.get_monster(0).dead==False or game.get_monster(0).respawn_counter < 15: # go to 0
                mid_path = game.shortest_paths(me.location, 0)
            else: #go to 4
                mid_path = game.shortest_paths(me.location, 4)

        if me.location == 4:
            mid_num=0
            if game.get_monster(0).dead==False or game.get_monster(0).respawn_counter < 15:
                mid_path = game.shortest_paths(me.location, 0)
            if game.get_monster(13).dead == False: #go to 13
                mid_path = game.shortest_paths(me.location, 13)
            elif me.rock >=4 and me.speed < 4 and game.get_monster(20).dead == False and game.get_monster(21).dead == False:
                mid_path = game.shortest_paths(me.location, 21)
            elif game.get_monster(11).dead == False: #go to 11
                mid_path = game.shortest_paths(me.location, 11)
            else: # go to 0
                mid_path = game.shortest_paths(me.location, 0)

        if me.location == 21:
            mid_num=0
            if game.get_monster(22).dead == False: #go to 22
                mid_path = game.shortest_paths(me.location, 22)
            elif game.get_monster(13).dead == False: #go to 13
                mid_path = game.shortest_paths(me.location, 13)
            else:
                mid_path = next_to_spawn([13,22], game, me)
                #
                #

        if me.location == 13:
            mid_num=0
            if game.get_monster(0).dead==False or game.get_monster(0).respawn_counter<15:
                mid_path = game.shortest_paths(me.location, 0)
            elif me.rock >=4 and me.speed <4 and game.get_monster(20).dead == False and game.get_monster(21).dead == False:
                mid_path = game.shortest_paths(me.location, 20)
            elif game.get_monster(16).dead == False: #go to 16
                mid_path = game.shortest_paths(me.location, 16)
            elif game.get_monster(11).dead == False: #go to 11
                mid_path = game.shortest_paths(me.location, 11)
            else:
                #
                #
                mid_path = next_to_spawn([11,16, 4], game, me)
                #
                #
        if me.location == 20:
            mid_num=0
            if game.get_monster(0).dead==False or game.get_monster(21).dead == False and me.speed < 4: #go to 21
                mid_path = game.shortest_paths(me.location, 21)
            else:
                mid_path = game.shortest_paths(me.location, 13)
            
        if me.location == 22:
            mid_num=0
            if  me.rock>=4 and game.get_monster(21).dead == False and me.speed < 4: #go to 21
                mid_path = game.shortest_paths(me.location, 21)
            if game.get_monster(16).dead == False: #go to 16
                mid_path = game.shortest_paths(me.location, 16)
            elif game.get_monster(11).dead == False: #go to 11
                mid_path = game.shortest_paths(me.location, 11)
            else:
                #
                #
                mid_path = next_to_spawn([11,16], game, me)
                #
                #
        if me.location == 16:
            mid_num=0
            if  game.get_monster(0).dead==False or game.get_monster(0).respawn_counter<15:
                mid_path = game.shortest_paths(me.location, 0)
            elif game.get_monster(15).dead == False: #go to 15
                mid_path = game.shortest_paths(me.location, 15)
            elif me.rock >=4 and me.speed <4 and game.get_monster(21).dead == False:
                mid_path = game.shortest_paths(me.location, 21)
            elif game.get_monster(13).dead == False: #go to 13
                mid_path = game.shortest_paths(me.location, 13)
            elif game.get_monster(11).dead == False: #go to 11
                mid_path = game.shortest_paths(me.location, 11)

        if me.location == 15:
            mid_num=0
            if me.rock >=4 and game.get_monster(17).dead == False: #go to 17 through 18
                mid_path = game.shortest_paths(me.location, 18)
            else:
                mid_path = game.shortest_paths(me.location, 16)

        if me.location == 18:
            mid_num=0
            mid_path = game.shortest_paths(me.location, 17)

        if me.location == 17:
            mid_num=0
            mid_path = game.shortest_paths(me.location, 16)

        if me.location == 11:
            mid_num=0
            if game.get_monster(0).respawn_counter<15:
                mid_path = game.shortest_paths(me.location, 0)
            elif me.rock >=4 and me.speed <4 and game.get_monster(21).dead == False:
                mid_path = game.shortest_paths(me.location, 21)
            elif game.get_monster(13).dead == False: #go to 13
                mid_path = game.shortest_paths(me.location, 13)
            elif game.get_monster(16).dead == False: #go to 16
                mid_path = game.shortest_paths(me.location, 16)
        # set the destination
        if (me.destination==me.location):
            destination_node = mid_path[0][mid_num]
            mid_num+=1
       # if mid_num>=len(mid_path[0]):
           # game.log(me.location)
        opp_loc=game.get_opponent().location
        opp_path=game.shortest_paths(me.location, opp_loc)
        opp_stance=game.get_opponent().stance
        if (me.movement_counter - me.speed) == 1:
            if check_monster(game, me.destination):
                #
                #
                chosen_stance = slay_monster(game, me.destination)
                #
                #
                #chosen_stance=get_winning_stance(game.get_monster(me.destination).stance)
        if check_monster(game, me.location):
            # if there's a monster at my location, choose the stance that damages that monster
            #
            #
            chosen_stance = slay_monster(game, me.location)
            #
            #
            #chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
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
        destination_node=0
        chosen_stance="Paper"
    #destination_node=0 #IMPORTANT DONT CHANGE
    # submit your decision for the turn (This function should be called exactly once per turn)
    if (game.get_turn_num()<7):
            destination_node=1
    game.submit_decision(destination_node, chosen_stance)
