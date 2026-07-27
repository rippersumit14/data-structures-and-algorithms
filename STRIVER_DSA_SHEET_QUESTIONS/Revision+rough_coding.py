s = "abcde"


goal = "cdeab"

for i in range(len(s)):
    s = s[1:] + s[0]

    if s == goal: #Checks each time
        print("true")
    else:
        print("false")

