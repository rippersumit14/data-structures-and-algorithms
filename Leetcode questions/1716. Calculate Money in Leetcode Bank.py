

#there are weeks
#On first monday $1 is made
#On second monday if it arises then $1 more than the previous monday


#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. On every subsequent Monday, 
he will put in $1 more than the previous Monday.

 
 After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. 
 Notice that on the 2nd Monday, Hercy only puts in $2.

 
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.'''

"""
Monday - 1
Tuesday - 2
Wednesday - 3
Thursday - 4
Friday - 5
Saturday - 6
Sunday - 7
"""

n = 10

Total_money = 0

Monday_money = 1 #Monday money
current_money = Monday_money #today's deposit
Day_count = 0 #The no. of days passed

for i in range(n):
    Total_money += current_money
    Day_count += 1
    if Day_count == 7:
        Monday_money += 1
        current_money = Monday_money
        Day_count = 0
    else:
        current_money += 1


print(Total_money)

#Time_complexity = O(n)
#Space_complexity = o(1)
























