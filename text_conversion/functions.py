def sixteen_bit_to_integer(sixteen_bit_number,sums): #This function takes the 16 bit binary numbers and turns them into decimal numbers
    power = 15                                       #It then does the corresponding calculations and updates the sums table
    number = 0
    sums[0] += 1
    for digit in sixteen_bit_number:
        digit = int(digit)
        number = number + digit*(2**power)
        power -= 1


    if number%2 ==0:
        sums[1] += 1
    if number%3 == 0:
        sums[2] += 1
    if number%5 == 0:
        sums[3] += 1
    if number%7 == 0:
        sums[4] += 1
    
    return(sums)
    

#This function calculates the percentages and prints the results
def final_results(sums):
    percentage = []
    for x in range(1,5):
        percentage.append((sums[x]/sums[0])*100)
    
    print("The percentage of even numbers is: ",percentage[0])
    print("The percentage of numbers that can perfectly be divided by 3 is: ",percentage[1])
    print("The percentage of numbers that can perfectly be divided by 5 is: ",percentage[2])
    print("The percentage of numbers that can perfectly be divided by 7 is: ",percentage[3])