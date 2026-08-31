prices = [7,6,4,3,1]

#Given an array price
#prices[i] is the price of a given stock on the ith day

#Want to maximize the profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

#Return the maximum profit
#if no profit then return 0

#[7,1,5,3,6,4]
min_price_index = 0 #This will store the min price index
min_price = min(prices)

for i in range(len(prices)):
    if prices[i] == min_price:
        min_price_index = i#Stores the index of the min price
#now min_price contains the most minimum price
array_after_the_min_price = []

for i in range(min_price_index, len(prices)):
    array_after_the_min_price.append(prices[i]) #[1,5,3,6,4]

#Creating the max_price variable
max_price = 0
for i in range(len(array_after_the_min_price)):
    if array_after_the_min_price[i] > max_price:
        max_price = array_after_the_min_price[i]

print(array_after_the_min_price)
print(max_price)


final_answer = max_price - min_price
if max_price == 0:
    print("0")
else:
    print(final_answer)



