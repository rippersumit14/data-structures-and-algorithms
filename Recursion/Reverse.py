#reverse
#Write a recursive function called reverse which accepts a string and returns a new string in reverse.
#Examples

#reverse('python') # 'nohtyp'
#reverse('appmillers') # 'srellimppa'

def reverse(s):
    assert isinstance(s, str), "Must be a string"

    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


print(reverse("sumit"))

#Time Complexity  = O(n²)
#Space Complexity = O(n²) as new string is created in every recursive call
