import random
white_player_points = 0
black_player_points = 0
# note: files and ranks are the official chess terms for the vertical columns and the horizontal rows of the board respectively
for games in range(0,100):
    used_tiles = []
    for i in range(0,3):
        placed = False
        while placed == False:
            temp_file = random.randrange(1,9)
            temp_rank = random.randrange(1,9) 
            if i == 0: 
                pawn_type = "R" #"R" stands for the white Rook
                placed = True
                placement_info = [temp_file, temp_rank,pawn_type]
                used_tiles.extend(placement_info)
            elif i == 1:
                pawn_type = "B" # "B" stands for the white Bishop
                if temp_file != used_tiles[0] or temp_rank != used_tiles[1]:
                    placed = True
                    placement_info = [temp_file, temp_rank,pawn_type]
                    used_tiles.extend(placement_info)
            else:
                pawn_type = "Q" # "Q" stands for the black Queen
                if (temp_file != used_tiles[0] or temp_rank != used_tiles[1]) and (temp_file != used_tiles[3] or temp_rank != used_tiles[4]):
                    placed = True
                    placement_info = [temp_file, temp_rank,pawn_type]
                    used_tiles.extend(placement_info)
    """
    the following lines of code check whether the white player's rook is able to hit the black player's Queen while also making sure that the Bishop is not between the two
    it also gives the black player one point if the rook hits the Queen since the Queen can also attack in straight lines,and thus,automatically will also target the rook
    Now a short basic explanation of how this works:
    The used_tiles list always has 9 elements in it(with the index ranging from 0 to 8),the 9 elements can be divided into groups of three,with the first and second element
    of each group being the file and rank of the placed piece respectively,and the third being the type of piece("R" is always the 3rd element,"B" the 6th and "Q" the 9th)
    The following code then calculates wether the pieces shall be able to hit each other based on their coordinates and the game's rules.
    """
    # this code checks for straight line hits
    if (used_tiles[1] == used_tiles[7]): #checking if the Rook and the Queen are on the same rank
        if (used_tiles[1] == used_tiles[4]) and ((used_tiles[3] < used_tiles[0] and used_tiles[3] < used_tiles[6]) or (used_tiles[3] > used_tiles[0] and used_tiles[3] > used_tiles[6])):
            #this condition makes sure that if the Bishop is in the same rank as the Queen and the Rook,its not in the way of the rook hitting the Queen and vice versa
            if abs(used_tiles[3]-used_tiles[0])<abs(used_tiles[3]-used_tiles[6]):
                #this condition checks whether the Queen is between the Bishop and the Rook or not,awarding the black player the corresponding points
                white_player_points += 1
                black_player_points += 1 
            else:
                white_player_points += 1
                black_player_points += 2
        elif(used_tiles[1] != used_tiles[4]):
            #here the bishop is confirmed to not be in the way
            if(used_tiles[3] == used_tiles[6]):
                #checks wether the bishop is on the same file with the Queen while she is on the same rank as the rook
                white_player_points += 1
                black_player_points += 2
            else:
                white_player_points += 1
                black_player_points += 1
        else:
            #this is the case were the bishop is getting in the way
            black_player_points += 1
    elif (used_tiles[0] == used_tiles[6]):
        #the same but now the code is checking the files and not the ranks 
        if (used_tiles[0] == used_tiles[3]) and ((used_tiles[4] < used_tiles[1] and used_tiles[4] < used_tiles[7]) or (used_tiles[4] > used_tiles[1] and used_tiles[4] > used_tiles[7])):
            if abs(used_tiles[4]-used_tiles[1])<abs(used_tiles[4]-used_tiles[7]):
                white_player_points += 1
                black_player_points += 1 
            else:
                white_player_points += 1
                black_player_points += 2
        elif(used_tiles[0] != used_tiles[3]):
            if(used_tiles[4] == used_tiles[7]):
                #checks wether the bishop is on the same rank with the Queen while she is on the same file as the rook
                white_player_points += 1
                black_player_points += 2
            else:
                white_player_points += 1
                black_player_points += 1
        else:
            black_player_points += 1
    elif (used_tiles[0] != used_tiles[6]) and (used_tiles[6] == used_tiles[3]):
        #these last two conditions basically ensure that if the rook and the queen are not on the same file/rank but the Queen and Bishop are,the black player will receive one point 
        black_player_points += 1
    elif (used_tiles[1] != used_tiles[7]) and (used_tiles[7] == used_tiles[4]):
        black_player_points += 1



    """
    the following lines of code check for diagonnal hits
    """
    if (used_tiles[3]+used_tiles[4]) == (used_tiles[6]+used_tiles[7]):
        if (used_tiles[0]+used_tiles[1] == used_tiles[3]+used_tiles[4]) and ((used_tiles[0] > used_tiles[3] and used_tiles[0] > used_tiles[6])or(used_tiles[1] > used_tiles[4] and used_tiles[1] > used_tiles[7])):
            if abs(used_tiles[0]-used_tiles[3])<abs(used_tiles[0]-used_tiles[6]):
                white_player_points += 1
                black_player_points += 1
            else:
                white_player_points += 1
                black_player_points += 2
        elif(used_tiles[0]+used_tiles[1] != used_tiles[3]+used_tiles[4]):
            if((used_tiles[0]-used_tiles[1])==(used_tiles[6]-used_tiles[7])):
                white_player_points += 1
                black_player_points += 2
            else:
                white_player_points += 1
                black_player_points += 1
    elif (used_tiles[3] - used_tiles[4] == used_tiles[6] - used_tiles[7]):
        if (used_tiles[3] - used_tiles[4] == used_tiles[0] - used_tiles[1]) and ((used_tiles[0] < used_tiles[3] and used_tiles[0] < used_tiles[6])and(used_tiles[1] < used_tiles[4] and used_tiles[1] < used_tiles[7])):
            if abs(used_tiles[0] - used_tiles[3])< abs(used_tiles[0]-used_tiles[6]):
                white_player_points += 1
                black_player_points += 1
            else:
                white_player_points += 1
                black_player_points += 2
            # Here the if and the elif could have been done together but i decided not to do that for the shake of the code's readability.
        elif (used_tiles[3] - used_tiles[4] == used_tiles[0] - used_tiles[1]) and ((used_tiles[0] > used_tiles[3] and used_tiles[0] > used_tiles[6])and(used_tiles[1] > used_tiles[4] and used_tiles[1] > used_tiles[7])):
            if abs(used_tiles[0] - used_tiles[3])< abs(used_tiles[0]-used_tiles[6]):
                white_player_points += 1
                black_player_points += 1
            else:
                white_player_points += 1
                black_player_points += 2
        elif(used_tiles[3] - used_tiles[4] != used_tiles[0] - used_tiles[1]):
            if((used_tiles[0]+used_tiles[1])==(used_tiles[6]+used_tiles[7])):
                white_player_points += 1
                black_player_points += 2
            else:
                white_player_points += 1
                black_player_points += 1
    elif((used_tiles[3]+used_tiles[4])!=(used_tiles[6]+used_tiles[7])) and ((used_tiles[6]+used_tiles[7])==(used_tiles[0]+used_tiles[1])):
        black_player_points += 1
    elif((used_tiles[3]-used_tiles[4])!=(used_tiles[6]-used_tiles[7])) and ((used_tiles[6]-used_tiles[7])==(used_tiles[0]-used_tiles[1])):
        black_player_points += 1
        #these last two conditions check whether the rook can be attacked diagonally by the Queen but the bishop cant



print("White player's points:",white_player_points,"Black player's points:",black_player_points)