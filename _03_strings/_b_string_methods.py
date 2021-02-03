# Given Strings s1 and s2, return the longer String
def find_longer_string(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length > s2_length:
        return s1
    return s2


# If String s contains the word "underscores", change all of the spaces to underscores
def format_spaces(s):

    if "underscores" in s:
        s = s.replace(' ', '_')

    return s



# Return the name of the person whose LAST name would appear first if they were
# in alphabetical order.
# You cannot assume there are no extra spaces around the name, but you can
# assume there is only one space between the first and last name.
# Strings can be compared alphabetically using <, >. Be aware that capital letters
# come first alphabetically:
# "abc" < "abd"   # True
# "abc" < "abD"   # False
def line_leader(s1, s2, s3):
    s1_lower = s1.lower()
    s2_lower = s2.lower()
    s3_lower = s3.lower()
    s1list = list(s1_lower)
    s2list = list(s2_lower)
    s3list = list(s3_lower)
    space_num1 = 1
    space_num2 = 1
    space_num3 = 1
    first = 'hello'
    for i, element in enumerate(s1list):
        if s1list[i] == ' ':
            space_num1 = i
            break
    s1_last = s1_lower[space_num1+1:len(s1_lower)]

    for i, element in enumerate(s2list):
        if s2list[i] == ' ':
            space_num2 = i
            break
    s2_last = s2_lower[space_num2+1:len(s2_lower)]

    for i, element in enumerate(s3list):
        if s3list[i] == ' ':
            space_num3 = i
            break

    s3_last = s3_lower[space_num3+1:len(s3_lower)]

    if (s1_last<s2_last) and (s1_last<s3_last):
        return s1
    elif(s2_last<s1_last) and (s2_last<s3_last):
        return s2
    elif(s3_last<s1_last) and (s3_last<s2_last):
        print('got to s3')
        return s3

    return first



# Return the sum of all numerical digits in the String
def numeral_sum(s):
    new_str = ""
    s_list = list(s)
    for element in s_list:
        if(s_list[element].isdigit()):
            new_str+=s_list[element]
    return new_str


# Return the number of times String substring appears in String s
def substring_count(s, substring):
    s1 = s.count(substring)

    return str(s1)



# Return the number of words in Strings that end with String substring
# You can assume there are no punctuation marks between words
def words_ends_with_substring(s, substring):
    pass


# Given String s, return the number of characters between the first occurrence
# of String substring and the final occurrence
# You can assume that substring will appear at least twice
def distance(s, substring):
    pass


# Return true if String s is a palindrome
# palindromes are words or phrases are read the same forward as backward.
# HINT: ignore/remove all punctuation and spaces in the String
def palindrome(s):
    pass
