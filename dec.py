# write a function that checks if a variable passed is a palindrome or not 
# what a palindrome is/not 
# input
# output
# l = [1, 2, 3]
# s = "test string"
# l[::]
def is_palindrome(string):
  if type(string) != str:
    return False
  string = string.upper()
  string_1 = ''
  # list comprehension
  for char in string:
    if char.isalnum():
      string_1 += char
  reversed_string = string_1[::-1]
  if reversed_string == string_1:
    return True
  return False
print(is_palindrome("1A Toyota's a Toyota1"))



