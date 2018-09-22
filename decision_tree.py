 if mid_flag:
    if me.location == 0 :
        mid_num=0
        if me.movement_counter - me.speed <= game.get_monster(0).respawn_counter and game.get_monster(0).respawn_counter < 7:
            mid_path=[0]
        if game.get_monster(4).dead == False: # go to 4
            if game.get_monster(3).dead == False: # go through 3
                mid_path = game.shortest_paths(me.location, 3)
        elif game.get_monster(11).dead == False: #go to 11
            mid_path = game.shortest_paths(me.location, 11)
        elif game.get_monster(16).dead == False: #go to 16
            mid_path = game.shortest_paths(me.location, 11)
        else:
            dead_monsters = [11,16,4]
            soonest=120
            next_monster=0
            for i in dead_monsters:
                if (game.get_moster(i).respawn_counter<soonest):
                    soonest=game.get_moster(i).respawn_counter<soonest
                    next_monster=i
            mid_path = game.shortest_paths(me.location, next_monster)

    if me.location == 3:
        mid_num=0
        if game.get_monster(0).respawn_counter < 15: # go to 0
            mid_path = game.shortest_paths(me.location, 0)
        else #go to 4
            mid_path = game.shortest_paths(me.location, 4)

    if me.location == 4:
        mid_num=0
        if game.get_monster(0).respawn_counter < 15:
            mid_path = game.shortest_paths(me.location, 0)
        if game.get_monster(13).dead == False: #go to 13
            mid_path = game.shortest_paths(me.location, 13)
        elif me.rock >=4 and me.speed <4 and game.get_monster(20).dead == False and and game.get_monster(21).dead == False:
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
            dead_monsters = [13, 22]
            soonest=120
            next_monster=0
            for i in dead_monsters:
                if (game.get_moster(i).respawn_counter<soonest):
                    soonest=game.get_moster(i).respawn_counter<soonest
                    next_monster=i
            mid_path = game.shortest_paths(me.location, next_monster)

    if me.location == 13:
        mid_num=0
        if game.get_monster(0).respawn_counter<20:
            mid_path = game.shortest_paths(me.location, 0)
        elif me.rock >=4 and me.speed <4 and game.get_monster(20).dead == False and and game.get_monster(21).dead == False:
            mid_path = game.shortest_paths(me.location, 21)
        elif game.get_monster(16).dead == False: #go to 16
            mid_path = game.shortest_paths(me.location, 16)
        elif game.get_monster(11).dead == False: #go to 11
            mid_path = game.shortest_paths(me.location, 11)
        else:
            dead_monsters = [11,16,4]
            soonest=120
            next_monster=0
            for i in dead_monsters:
                if (game.get_moster(i).respawn_counter<soonest):
                    soonest=game.get_moster(i).respawn_counter<soonest
                    next_monster=i
            mid_path = game.shortest_paths(me.location, next_monster)

    if me.location == 22:
        mid_num=0
        if game.get_monster(16).dead == False: #go to 16
            mid_path = game.shortest_paths(me.location, 16)
        elif game.get_monster(11).dead == False: #go to 11
            mid_path = game.shortest_paths(me.location, 11)
        else:
            dead_monsters = [11,16]
            soonest=120
            next_monster=0
            for i in dead_monsters:
                if (game.get_moster(i).respawn_counter<soonest):
                    soonest=game.get_moster(i).respawn_counter<soonest
                    next_monster=i
            mid_path = game.shortest_paths(me.location, next_monster)
            

    if me.location == 16:
        mid_num=0
        if  game.get_monster(0).respawn_counter<15
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

    if me.location == 11
        mid_num=0
        if game.get_monster(0).respawn_counter<15
            mid_path = game.shortest_paths(me.location, 0)
        elif me.rock >=4 and me.speed <4 and game.get_monster(21).dead == False:
            mid_path = game.shortest_paths(me.location, 21)
        elif game.get_monster(13).dead == False: #go to 13
            mid_path = game.shortest_paths(me.location, 13)
        elif game.get_monster(16).dead == False: #go to 16
            mid_path = game.shortest_paths(me.location, 16)


