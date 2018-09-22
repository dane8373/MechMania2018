Position = 0 logic
    If monster 0 respawn < 5
        Stay and wait
    if monster 4 is alive
        if monster 3 is alive
            go to monster 3
        go to monster4
    else if monster 11 is alive
        go to monster 11
    else if monster 16 is alive
        go to monster 16

position 3 = logic
    go to monster 4

position = 4 logic
    if monster 0 respawn < 15
        go to 0
    if monster 13 is alive
        go to 13
    else if me.rock >=4 and 20 is alive and 21 is alive
        go to 21
    else if 11 is alive
        go to 11
    else go to 0

position = 21 logic
    if monster 22 is alive
        go to monster 22
    else if monster 13 is alive
        go to monster 13
    else
        go to monster 22

position = 13 logic
    if monster 0 respawn count<20
        go to 4
    else if monster 16 is alive
        go to monster 16
    else if monster 11 is alive
        go to monster 11

position = 22 logic
    if monster 16 is alive
        go to monster 16
    else if monster 11 is alive
        go to monster 11
    else go to monster 6

position = 16 logic
    if  monster 0 count<15
        got to position 0
    else if monster 15 is alive
        go to monster 15
    else if me.rock >= 4
        go to position 21
    else if monster 13 is alive
        go to monster 13
    else if monster 11 is alive
        go to monster 11

postion = 11 logic
    if monster 0 count<15
        got to position 0
    else if me.rock >= 4 and monster 21 is alive
        go to position 21
    else if monster 13 is alive
        go to monster 13
    else if monster 16 is alive
        go to monster 16


