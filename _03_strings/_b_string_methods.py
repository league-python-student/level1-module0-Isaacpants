# Given Strings s1 and s2, return the longer String
def find_longer_string(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length > s2_length:
        return s1
    return s2


# If String s contains the word "underscores", change all of the spaces to underscores
def format_spaces(s1):
    s2 = s1.replace('_', ' ')
    return s2




# Return the name of the person whose LAST name would appear first if they were
# in alphabetical order.
# You cannot assume there are no extra spaces around the name, but you can
# assume there is only one space between the first and last name.
# Strings can be compared alphabetically using <, >. Be aware that capital letters
# come first alphabetically:
# "abc" < "abd"   # True
# "abc" < "abD"   # False
def line_leader(s1, s2, s3):

   pass

# Return the sum of all numerical digits in the String
def numeral_sum(s):
    s_list = list(s)
    for element in s_list:
        if(i)


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
