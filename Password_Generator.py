#Password Generator

import random

print("Welcome to Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

pass_lett = int(input("How many letter do you want in your password: "))
pass_sym = int(input("How many symbols would you like to have in your password: "))
pass_num = int(input("How many numbers would you like to have in your password: "))

p_lett = random.sample(letters, pass_lett)
p_sym = random.sample(symbols, pass_sym)
p_num = random.sample(numbers, pass_num)

pass_res = p_lett + p_sym + p_num
str_shuff = random.sample(pass_res, len(pass_res))
final_pass = ''.join(str_shuff)

print("Your password: ", final_pass)
