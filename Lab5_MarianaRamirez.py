"""
Lab 5 - Functions and Lists 
(100 marks in total, including 7 exercises)

Author:  <Mariana Ramirez>
Due Date: This Friday (Feb. 6) 5pm.

"""
#Exercise 1 (10 marks)

def convert_american_dollars(american_dollars):
    canadian_dollars = american_dollars * 1.34
    return round(canadian_dollars, 2)
    

assert convert_american_dollars(1) == 1.34
assert convert_american_dollars(100) == 134
assert convert_american_dollars(100.05) == 134.07


'''
Exercise 2 (10 marks)
'''

days_week = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]
def back_day_from_trip(day_today, days_trip):
   day_back = (day_today + days_trip) %7
   return days_week[day_back]


assert back_day_from_trip(3, 5) == "Tuesday"
assert back_day_from_trip(1, 2) == "Thursday"
assert back_day_from_trip(1, 7) == "Tuesday"

'''
Exercise 3 (10 marks) - From interactive textbook 10.31.4
'''

def average(nums):
    total = 0
    for num in nums:
        total += num
    return round (total/ len(nums), 2)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 4]) == 2.5
assert average([2, 9, 2]) == 4.33





"""
Exercise 4 (10 marks) - From interactive textbook 10.31.6

"""

# Function implementation
def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num ** 2
    return round (total, 2) 


assert sum_of_squares([2, 3, 4]) == 29
assert sum_of_squares([2, 4]) == 20
assert sum_of_squares([]) == 0


"""
Exercise 5 (20 marks)

"""

# Function implementation 
def add_number(nums, k):
    for i in range (len(nums)):
        nums[i]+= k
    return nums
    

assert add_number([2, 4, 1], 5) == [7, 9, 6]
assert add_number([7, 8], -5) == [2, 3]


"""
Exercise 6 (20 marks) 

"""

# Function implementation
def squares(nums):
    total = []
    for num in nums: 
        total.append(num ** 2)
    return total


assert squares([2, 3, 4]) == [4, 9, 16]
assert squares([2, 4]) == [4, 16]
assert squares([5, 6, 7]) == [25, 36, 49]
assert squares([]) == []


"""
Exercise 7 (20 marks) 

"""

# Function implementation 
def repeat_elements(nums):
    total = []
    for num in nums: 
        total.append(num)
        total.append(num)
    return total



assert repeat_elements([1, 2, 3, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]
assert repeat_elements([2, 7, 8]) == [2, 2, 7, 7, 8, 8]
assert squares([]) == []




"""
Congratulations on finishing your lab5. This is a big move!
Now upload to your GitHub repository, and paste your GitHub link on e-learn.
"""
