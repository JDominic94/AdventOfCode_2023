import numpy as np
import re

def Part_1():
    # Open File
    with open("inputs/Day_1.txt") as f:
        input = f.read()
        
    # Func to filter out the ints
    get_numbers = lambda line: [num for num in line if num.isdigit()]
    
    # Func to combine first and last int
    complete_numbers = lambda line: int(get_numbers(line)[0] + get_numbers(line)[-1])
    
    # Open input and apply funcs to get a list of all nums
    numbers = [complete_numbers(line) for line in input.split("\n")]
    
    # Sum nums together
    result = sum(numbers)    
    return result


def Part_2():
    # Open File
    with open("inputs/Day_1.txt") as f:
        input = f.read()
    
    # Dict to swap strings, o1e instead of 1 to enable twone to be interpreted correclty to 21
    digit_dict = {
        "one": "o1e", 
        "two": "t2o", 
        "three": "t3e", 
        "four": "f4r", 
        "five": "f5e", 
        "six": "s6x", 
        "seven": "s7n", 
        "eight": "e8t", 
        "nine": "n9e"
        }

    # Replace strings with digts-string
    for k,v in digit_dict.items():
        input = re.sub(k,v,input)
    
    ### Same as Part 1 ###
    # Func to filter out the ints
    get_numbers = lambda line: [num for num in line if num.isdigit()]
    
    # Func to combine first and last int
    complete_numbers = lambda line: int(get_numbers(line)[0] + get_numbers(line)[-1])
    
    # Open input and apply funcs to get a list of all nums
    numbers = [complete_numbers(line) for line in input.split("\n")]
    
    # Sum nums together
    result = sum(numbers)    
    return result
    

# One liner
print(f"Day 1, Part 1: ", sum([int([num for num in line if num.isdigit()][0] + [num for num in line if num.isdigit()][-1]) for line in open("inputs/Day_1.txt").read().split("\n")]))
print("Day 1, Part 2: ", sum([int([num for num in line if num.isdigit()][0] + [num for num in line if num.isdigit()][-1]) for line in input.split("\n")] if ((input := open("inputs/Day_1.txt").read()) and ([input := re.sub(k,v,input) for k,v in {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}.items()])) else ["Merry Christmas"]))
