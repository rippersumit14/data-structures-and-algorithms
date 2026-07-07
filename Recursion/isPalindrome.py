def isPalindrome(stringo):
    # Input validation
    assert isinstance(stringo, str), "It must be a string"

    # Base Case
    # Empty string or single character is always a palindrome
    if len(stringo) <= 1:
        return True

    # If first and last characters are different
    if stringo[0] != stringo[-1]:
        return False

    # Recursive Case
    # Check the remaining middle part of the string
    return isPalindrome(stringo[1:-1])


print(isPalindrome("awesome"))                  # False
print(isPalindrome("foobar"))                   # False
print(isPalindrome("tacocat"))                  # True
print(isPalindrome("amanaplanacanalpanama"))    # True
print(isPalindrome("amanaplanacanalpandemonium"))  # False