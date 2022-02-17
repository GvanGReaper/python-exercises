import random
p2wins = 0;
draws = 0;
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]



for game in range(1,101):   
    temp_array = [] 
    for i in xarti:
        for j in color:
            xartia.append([i,j])  
    ten_cards = [10,"J","Q","K"] # This is a list that contains the numbers of the cards that player 1 can draw as their first card
    p1_card_number = random.choices(ten_cards,weights= [1,1,1,1],k = 1) #This two lines of code randomly pick a random number and color
    card_color = random.choices(color,weights= [1,1,1,1],k = 1)         #for the first player's first card respectively
    p1_starting_card = p1_card_number + card_color
    

    card_color = random.choices(color,weights= [1,1,1,1],k = 1) #This is all the same as the code above except instead of choosing the card's number
    p2_card_number = random.randrange(1,10)                     #from ten_cards,it instead randomly picks one number from 1 to 9 
    temp_array.append(p2_card_number)
    p2_starting_card = temp_array + card_color
     

    xartia.remove(p1_starting_card)
    xartia.remove(p2_starting_card) #These lines of code remove the two randomly picked cards from the deck and then shuffle the remaining 50 cards
    random.shuffle(xartia)
    
    
    player1=[p1_starting_card]
    sum1= 0
    while sum1<16:
        sum1= 0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        p2wins += 1
    else:
        player2=[p2_starting_card]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum2>sum1:
            p2wins += 1
        elif sum2 == sum1:
            draws  += 1

print("P1 won " + str((100 - draws - p2wins)) + " times!")
print("P2 won " + str(p2wins) + " times!")
print("There were " + str(draws) + " draws!")
