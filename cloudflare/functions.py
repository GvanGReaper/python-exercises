def hexadecimal_to_decimal(number):
    if number == "a":
        decimal_number = 10
    elif number == "b":
        decimal_number = 11
    elif number == "c":
        decimal_number = 12
    elif number == "d":
        decimal_number = 13
    elif number == "e":
        decimal_number = 14
    elif number == "f":
        decimal_number = 15
    else:
        decimal_number = int(number)
    
    return(decimal_number)