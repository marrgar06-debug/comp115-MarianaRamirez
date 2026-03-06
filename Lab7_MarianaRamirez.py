""" 
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)
"""


def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

assert reverse_str("abcde") == "edcba"
assert reverse_str("apple") == "elppa"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("Abd") =="dbA"

"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)
"""

def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
            
    return count
    
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("COMP115") == 1
assert count_vowels("Abd") == 1 



"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)
"""
def remove_duplicates(s):
    """
    This function removes duplicate characters in a string s.
    E.g. 
    >>> remove_duplicates("apple")
    "aple"

    Parameters:
    - s (string): The input string from which duplicate characters are removed.

    Returns:
    - (string): A new string with duplicate characters removed,
    preserving the original order of characters.
    """
    result_s = ""
    
    for char in s:
        if char not in result_s:
            result_s += char
            
    return result_s

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile" 
assert remove_duplicates("pear") == "pear"




"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

"""
def find_index(s, t):
    """
    Finds the lowest index of character t in string s.

    E.g.,
    >>> find_index("Abd", 'b')
    1
    >>> find_index("Abdccc", 'c')
    3
    >>> find_index("Abd", 'w')
    -1

    Parameters:
    - s (string): The string to search through.
    - t (string): The single character to find.

    Returns:
    - (int): The lowest index of t in s, or -1 if t is not found.
    """
    for i in range(len(s)):
        if s[i] == t:
            return i
    return -1

assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')


def project_completion_day(day, days_to_completion):
    """

    Calculates the completion day of a project given the start day and duration.

    E.g.,
    >>> project_completion_day('Monday', 4)
    'Friday'
    >>> project_completion_day('Saturday', 2)
    'Monday'

    Parameters:
    - day (string): The current day of the week (e.g., 'Monday').
    - days_to_completion (int): The estimated number of days until completion.

    Returns:
    - (string): The day of the week the project will be completed.
    """
    
    start = days_week.index(day)
    
    completion = (start + days_to_completion) % 7
    
    return days_week[completion]
    
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'



"""
Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)

"""

def parse_log_line(line):
    """
    Parses a standardized log line into its components.
    
    Parameters:
    - line (str): A log line string.
    
    Returns:
    - tuple: (timestamp, level, module, message)
    """
    info = line.split()
    
    timestamp = info [0] + ' ' + info[1]
    
    level = info[2].strip('[]')
    
    module = info[3]
    
    message = ' '.join(info[4:])
    
    return (timestamp, level, module, message)


log_string = """
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
"""

parsed_logs_list = []

for line in log_string.split('\n'):
    parsed_tuple = parse_log_line
    parsed_logs_list.append(parsed_tuple)

assert parse_log_line('2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s') == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')
assert parse_log_line('2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)') == ('2024-03-05 14:32:18', 'WARNING', 'api.py', 'Slow query detected (2.3s)')
assert parse_log_line('2024-03-05 14:32:22 [INFO] server.py Server started on port 8000') == ('2024-03-05 14:32:22', 'INFO', 'server.py', 'Server started on port 8000')
assert parse_log_line('2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary') == ('2024-03-05 14:32:45', 'ERROR', 'database.py', 'Connection lost to primary')
