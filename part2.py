from random import randint

# 1. Generate a list of 10 random integers between 1 and 50 inclusive.
ranNum_list = []
for _ in range(10):
    ranNum_list.append(randint(1,50))

print("Generated List:", ranNum_list)

# 2. Define the number you want to find
num_to_find = 30
print("Searching for:", num_to_find)

# 3. Initialize counter and tracking variable
comparisons = 0
found = False

# 4. Perform linear search with comparison counter
for num in ranNum_list: # Changed '_________' to 'num'
    comparisons += 1 # Increment for each comparison
    
    if num == num_to_find: # Changed '_________' to 'num'
        found = True
        break

# 5. Output results
print("Comparisons made:", comparisons)
if found:
    print("Number", num_to_find, "found in the list!")
else:
    print("Number", num_to_find, "not found in the list.")

print("testing")