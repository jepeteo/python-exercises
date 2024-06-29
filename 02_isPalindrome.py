import re

def isPalindrome(text):
  checkText = ''.join([char for char in text.lower() if char.isalpha()])
  reversed = checkText[::-1]
  # print(checkText)
  # print(reversed)
  if checkText == reversed:
    return True
  else:
    return False

print(isPalindrome("Race Car")) # true
print(isPalindrome("Hello, World")) # false


# another solution
# checkText = ''.join(re.findall(r'[a-z]+', text.lower()))