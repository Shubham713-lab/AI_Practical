# welcome message
print("Welcome to My First AI Robot")

# spots of Room
room = ['D', 'C', 'D', 'D', 'C']

# Before Cleaning the room
print("Room before Cleaning : ", room)

# function to clean the room
def clean_spot(spot):
    if spot == 'D':
        return 'C'
    else:
        return 'C'
    
# intialize cleaned Room
cleaned = 0

# loop to check Cleaned room 
for i in range(len(room)):
    if room[i] == 'D':
        room[i] = clean_spot(room[i])
        cleaned += 1

# output : 
print("Room after Cleaning : ", room)
print("Total Spot Cleaned : ", cleaned)

print()

# My Room
my_room = ['D', 'C', 'D', 'D', 'C', 'D', 'C']
print("My Room before Cleaning : ", my_room)

cleaned = 0

# loop to check Cleaned room 
for i in range(len(my_room)):
    if my_room[i] == 'D':
        my_room[i] = clean_spot(my_room[i])
        cleaned += 1

# output : 
print("My Room after Cleaning : ", my_room)
print("Total Spot Cleaned : ", cleaned)

print("Congrats! You have made your First AI Cleaning Robot.")