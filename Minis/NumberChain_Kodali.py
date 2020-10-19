# variable 
user = 'yes'

# starting number
start = 0

# while the user wants to keep going

while user == 'yes': 
    user_number = input("How many numbers? ")
    # loop 
    for x in range(start, int(user_number) + start):
        print (x)
    start = start + int(user_number)
    
    user = input("Would you like to keep going? yes or no. ")

    
