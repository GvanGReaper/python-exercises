import functions #This file contains 2 functions that I decided to make in order to make the code in this file cleaner and easier to read.

file = open("two_cities_ascii.txt","r") #Here the program reads a text file and in the two for loops below it reads the lines one by one
first_char = True
sums = [0 , 0 , 0, 0, 0] 
""" This list contains 5 different sums and is used instead of using 5 different variables.The five sums are(in order):
    1.The sum of all 16 digit binary numbers
    2.The sum of all even numbers
    3.The sum of all numbers that can be perfectly divided by 3
    4.The sum of all numbers that can be perfectly divided by 5
    5.The sum of all numbers that can be perfectly divided by 7
"""
sixteen_digit_number = ""
for line in file:
    for letter in line:
        num = ord(letter) #here we get the ascii number of each character of the text
        string = ""


        while num != 1:                             #This part of the code turns the decimal ascii number that corresponds to each character
            string = str(num%2) + string            #and turns it into the corresponding 7 bit binary number
            num = num//2                            
        string = "1" + string                       
        while len(string) < 7:                      
            string = "0" + string                   

    
        if first_char == True:
            seven_bit_binary_file = open("seven_bit_binary_file.txt","w")       #This part of the code created a new text file with the name 
            string = string + " "                                               #"seven_bit_binary_file" where the 7 bit binary representation
            seven_bit_binary_file.write(string)                                 #of the original text can be seen
            first_char = False
        else:
            seven_bit_binary_file = open("seven_bit_binary_file.txt","a")
            string = string + " "
            seven_bit_binary_file.write(string)
        
        if len(sixteen_digit_number) < 16:                                                              #This part of the code takes the two first and
            sixteen_digit_number = sixteen_digit_number + string[0] + string[1] + string[5] + string[6] #last bits of every 7bit number that we have
        elif len(sixteen_digit_number) == 16:                                                           #and,since they are strings,concatenates them                                                                #until the new string's length is 16
            sums = functions.sixteen_bit_to_integer(sixteen_digit_number,sums)                          
            sixteen_digit_number = string[0] + string[1] + string[5] + string[6]
    
         
    seven_bit_binary_file.write(" \n")

seven_bit_binary_file.close()    
file.close()
functions.final_results(sums)
