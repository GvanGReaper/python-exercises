import random
p2wins = 0;
draws = 0;
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]


for game in range(1,101):    
    for i in xarti:
        for j in color:
            xartia.append([i,j])    
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        p2wins += 1
    else:

        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
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