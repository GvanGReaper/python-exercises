import requests
import functions
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
num_of_char = 0
temp_string = data["randomness"]
hexadecimal_numbers = []
temp = ""
#the code below takes the randomly generated string and takes it apart,filling a list with 2 digit numbers of the hexadecimal system
for char in temp_string:
    if num_of_char < 2:
        temp = temp + char
        num_of_char += 1
    else:
        hexadecimal_numbers.append(temp)
        temp = char
        num_of_char = 1


kino_numbers = []
for hexadecimal_number in hexadecimal_numbers:
    first_number_decimal = functions.hexadecimal_to_decimal(hexadecimal_number[0])
    second_number_decimal = functions.hexadecimal_to_decimal(hexadecimal_number[1])
    kino_numbers.append(((first_number_decimal*16)+(second_number_decimal))%80)
    for number in kino_numbers:
        while kino_numbers.count(number) > 1:
            kino_numbers.remove(number)



k = requests.get("https://api.opap.gr/draws/v3.0/1100/last-result-and-active")
data = k.json()

winning_numbers = (data["last"]["winningNumbers"]["list"])
total_winners = 0
for number in kino_numbers:
    if winning_numbers.count(number) > 0:
        total_winners += 1
        

print("The number of winning numbers according to Kino's last winners list is: ",total_winners)