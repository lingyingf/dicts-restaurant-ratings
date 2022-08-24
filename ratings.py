"""Restaurant rating lister."""

# put your code here

# import scores.txt
# create a function that intake the file
# # have te user input res name and res score
# create a loop that reads each line of the file
# strip the right space and split the lines into list
# create a new_dictonary
# sort new_dic to turn the key into list
# # append the dic by user input
# create a loop get the resta.. name
# in the print, get the rating by referring to the new_dic
# print(f"{Big Bean Shack} is rated at {3}.")


# make variables to intake users input for any three actions
# if "s", print original
# if "a", input_restaurant and rating
# if "q", break

# create the dic in the beginning of function
# assign_res = choic() on the sorted dic
# print("assign_res" and its rating)
# new_rating = input("New rating?")
# update the assign_res rating

import random


data = open("scores.txt")



def create_dictionary(data):
    new_dictionary = {}

    for line in data:
        list_per_line = line.rstrip().split(":")
        restaurant = list_per_line[0]
        rating = list_per_line[1]
        new_dictionary[restaurant] = rating
    
    assign_res_random = random.choice(sorted(new_dictionary)) 
    print(f"{assign_res_random} is rated at {new_dictionary[assign_res_random]}.")
    
    input_new_rating = input("New update??")
    new_dictionary[assign_res_random] = input_new_rating

    input_action = input("What u wanna do?")

    if input_action.lower() == "q":
        quit()
    
    elif input_action.lower() == "a":
        input_restaurant = input("What's the restaurant name?").upper()

        while True:
            input_score = input("What's its score?")
            if 1 <= int(input_score) <=5:
                new_dictionary = {}

                for line in data:
                    list_per_line = line.rstrip().split(":")
                    restaurant = list_per_line[0]
                    rating = list_per_line[1]
                    new_dictionary[restaurant] = rating
                
                new_dictionary[input_restaurant] = input_score

                list_of_sorted_res = sorted(new_dictionary)

                for restaurant_sorted in list_of_sorted_res:
                    print(f"{restaurant_sorted} is rated at {new_dictionary[restaurant_sorted]}.")
                break
            
            else:
                print("invalid input, try again")

    elif input_action.lower() == "s":
        
        # new_dictionary = {}

        # for line in data:
        #     list_per_line = line.rstrip().split(":")
        #     restaurant = list_per_line[0]
        #     rating = list_per_line[1]
        #     new_dictionary[restaurant] = rating

        list_of_sorted_res = sorted(new_dictionary)

        for restaurant_sorted in list_of_sorted_res:
            print(f"{restaurant_sorted} is rated at {new_dictionary[restaurant_sorted]}.")
        
            
            
create_dictionary(data)
