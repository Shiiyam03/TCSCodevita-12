# GoodString
# Problem Description
# A picnic to a famous museum is being planned in a school for class VI. When they reached the spot, the students started quarreling among themselves in the queue. So the teacher came up with an idea of "good string" which is explained below.

# Good String is provided as input. All letters in this string are good letters. Good letters need to be used in further computations as explained below.

# The teacher asked all the students to convert their names into good names with the help of good string. While converting, they have to calculate the distance. Based on that, she will arrange the students in a queue.

# For converting a name into good name, for each letter i in the name, select the nearest letter from the good name. Distance is calculated as the differences between the ASCII values of i and selected good letter. If there are two letters which are equidistant from i, select the letter which is nearest to the previously used good letter. In that case, distance will be the difference of ASCII value of previously used good letter and selected letter. If i is already present in the good string then no need to change it. Initially, previous good letter will be the first letter of good string. Calculate the total distance of the given name.

# Given the name of the student who is confused of implementing this task. Help him to calculate the total distance for his name.

# Note: Letters from good string can be reused any number of times.

# Constraints
# 1 <= len(good string) <= 100

# 1 <= len(name) <= 10^4

# Good string will consist of lower, upper case alphabets,digits and symbols.

# Name will consist of only space,lower and upper case alphabets.

# Characters are case sensitive.

# The ASCII values for all the characters in the good string and name will be between 32 to 126 (both inclusive).

# Input
# First line consists of good string.

# Second line consists of the name of the student who is confused to implement the task.

# Output
# Print the total distance for that name.

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# (@HR*i{kcQl

# Vyom

# Output

# 10

# Example 2

# Input

# 6*K4AQf]gpi

# Nainika

# Output

# 33







#Code
def calculate_total_distance(good_string, name):
    good_chars = list(good_string)
    total_distance = 0
    prev_good_char = good_chars[0]
    
    for char in name:
        if char in good_chars:
            prev_good_char = char
            continue
        
        min_distance = float('inf')
        nearest_good_char = None
        
        for good_char in good_chars:
            distance = abs(ord(char) - ord(good_char))
            
            if distance < min_distance:
                min_distance = distance
                nearest_good_char = good_char
            elif distance == min_distance:

                if abs(ord(good_char) - ord(prev_good_char)) < abs(ord(nearest_good_char) - ord(prev_good_char)):
                    nearest_good_char = good_char

        total_distance += min_distance

        prev_good_char = nearest_good_char
    
    return total_distance

good_string = input().strip()
name = input().strip()

print(calculate_total_distance(good_string, name))