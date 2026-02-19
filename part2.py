from random import randint 
ranNum_list = [] 
# It is better to use a different variable name for the list than the loop counter 
# Generates a list of 5 random integers between 1 and 50 inclusive. 
for _ in range(10): # The underscore indicates that the loop counter variable is not used 
    ranNum_list.append(randint(1,50)) # Append to the list, not the loop counter 

print(ranNum_list)

# Define the number you want to find (e.g., 30, or get user input)
num_to_find = 30 # You can change this number

if **num_to_find** in **ranNum_list**:
    print("Number", **num_to_find**, "found in the list!")
else:
    print("Number", **num_to_find**, "not found in the list.")
