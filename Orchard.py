# Orchard
# Problem Description
# Orchards are a piece of enclosed land planted with different fruit trees in an orderly manner.

# Ashok and Anand are friends. On a fine day they went to an orchard where lemon and mango trees are planted in rows. The owner planted these trees in rows but in random order. Some trees have plenty of fruits and some other plants didn't gave good yield. While they are walking through the rows, both of them selected a row of trees. The trees in the row are represented by M and L which represents mango and lemon respectively. After selecting the rows, they both argued for sometime over the number of fruits. Then they saw Akhil walking towards them. They asked Akhil to declare which row holds more number of fruits. Akhil understood that guessing the row with maximum number of fruits will be quite difficult. So he asked each of them to select any three trees from the row such that no two adjacent trees should be of same type and whoever have maximum possibilities for selecting the trees will be considered as winners. Refer to the example section for better understanding.

# Given two strings denoting the trees in the selected rows, find who is the winner. If the input string is invalid, print "Invalid input" and if no one wins, print "Draw".

# Constraints
# 1 <= len(str) <= 10^5

# Input
# First line consists of the string denoting trees in Ashok's row.

# Second line consists of the string denoting trees in Anand's row.

# Output
# Print the name of the winner in a single line. If it's a draw match, print "Draw". Incase of invalid inputs, print "Invalid input".

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# MMLMLLM

# LMLLLMLM

# Output

# Anand

# Explanation-

# Ashok's possibilities are (1,3,4), (2,3,4), (3,4,6), (4,6,7), (1,3,7), (3,4,5), (1,5,7), (2,6,7), (2,3,7), (2,5,7), (4,6,7), (1,6,7) i.e., 12 possibilities.

# Anand's possibilities are (2,3,6), (1,2,3), (1,6,7), (1,2,4), (3,6,7), (2,3,8), (1,2,5), (2,4,6), (4,6,7), (1,2,7), (2,4,8), (5,6,7), (2,5,6), (2,7,8), (2,5,8), (6,7,8) i.e., 16 possibilities. Hence he wins.

# Example 2

# Input

# MLLM

# LMLL

# Output

# Draw

# Explanation-

# Ashok's possibilities are (1,3,4), (1,2,4) i.e., 2 possibilities.

# Anand's possibilities are (1,2,4), (1,2,3) i.e., 2 possibilities.

# So no one wins thus we print "Draw".









#Code
def count_valid_combinations(trees):
    n = len(trees)
    count = 0

    last_type = None
    current_count = 0

    for i in range(n):
        if trees[i] == last_type:
            current_count = 0
        current_count += 1

        if i >= 2:
            if trees[i] != trees[i - 1]:
                count += (current_count - 1) * (i - 1)

        last_type = trees[i]

    return count

def determine_winner(row_ashok, row_anand):
    if any(char not in "ML" for char in row_ashok) or any(char not in "ML" for char in row_anand):
        return "Invalid input"

    count_ashok = count_valid_combinations(row_ashok)
    count_anand = count_valid_combinations(row_anand)

    if count_ashok > count_anand:
        return "Ashok"
    elif count_anand > count_ashok:
        return "Anand"
    else:
        return "Draw"

row_ashok = input().strip()
row_anand = input().strip()

print(determine_winner(row_ashok, row_anand))