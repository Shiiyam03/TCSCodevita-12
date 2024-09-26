# WeaponBoxes
# Problem Description
# In the border of India, there is a military camp where soldiers stay. The soldiers need weapons during the wars and some weapons are made in India while the others are imported from other countries. One day many boxes of weapons arrived from different countries. These boxes have different numbers assigned to it. These numbers denotes the weight of the boxes. Larger the number on the box, the more will be the weapons inside it. All these boxes are arranged in a line starting from the camp. One day the commander wanted to test the weapons in all the boxes one by one. But he wanted to prioritize the boxes with more weight because when he open that box, the number of weapons will be more. So he will followed the below steps.

# He will carry this process in cycles. In each cycle, he will select the first N boxes. From those, every time he will pick the first two boxes and compare them and send the box with lower weight to the end of the line.
# At last one box will remain from those N boxes, then the cycle is said to be complete.
# He halts this process when the same box remains un-shifted to the end of the line in K consecutive cycles.
# For shifting these boxes, he hired labors and they will charge an amount which is equal to the sum of weights of all those boxes except those which are having triangular number weights.
# Given an array consisting of weights of all the boxes, two integers N and K, print the amount of money that the commander have to give to workers.

# Constraints
# 1 <= weight of each box <= 10^5

# 1 <= number of boxes <= 10^4

# 1 <= N,K <= 10^3

# All the elements in the array are distinct.

# Input
# First line consists of an array denoting the weight of all the boxes.

# Second line consists of two space separated integers N and K, denoting the number of boxes he selects in each cycle and number of times a box should remain un-shifted to halt the process.

# Output
# Print the amount of money that the commander have to give to workers.

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# 7 3 6 9 10 2 4 11 5 12 17 1

# 3 2

# Output

# 22

# Example 2

# Input

# 6 2 8 14 5 1 3

# 2 2

# Output

# 15





#Code
def is_triangular(num):
    m = 0
    triangular_number = 0
    while triangular_number < num:
        m += 1
        triangular_number = m * (m + 1) // 2
    return triangular_number == num

def triangular_numbers_set(max_weight):

    triangulars = set()
    m = 1
    while True:
        t_num = m * (m + 1) // 2
        if t_num > max_weight:
            break
        triangulars.add(t_num)
        m += 1
    return triangulars

def calculate_labor_cost(box_weights, N, K):
    max_weight = 100000
    triangulars = triangular_numbers_set(max_weight)
    
    queue = box_weights[:]
    consecutive_unshifted_count = {weight: 0 for weight in queue}
    labor_cost = 0

    while True:
        if len(queue) < N:
            selected_boxes = queue
        else:
            selected_boxes = queue[:N]

        if len(selected_boxes) == 1:
            break

        temp_queue = []
        for i in range(0, len(selected_boxes), 2):
            if i + 1 < len(selected_boxes):

                box1 = selected_boxes[i]
                box2 = selected_boxes[i + 1]
                if box1 < box2:
                    temp_queue.append(box1)
                    temp_queue.append(box2)
                    
                    if box2 not in triangulars:
                        labor_cost += box2
                    consecutive_unshifted_count[box2] += 1
                    consecutive_unshifted_count[box1] = 0
                else:
                    temp_queue.append(box2)
                    temp_queue.append(box1)

                    if box1 not in triangulars:
                        labor_cost += box1
                    consecutive_unshifted_count[box1] += 1
                    consecutive_unshifted_count[box2] = 0
            else:
                temp_queue.append(selected_boxes[i])
                consecutive_unshifted_count[selected_boxes[i]] += 1

        queue = temp_queue

        if any(count >= K for count in consecutive_unshifted_count.values()):
            break

    return labor_cost

box_weights = list(map(int, input().split()))
N, K = map(int, input().split())

print(calculate_labor_cost(box_weights, N, K))