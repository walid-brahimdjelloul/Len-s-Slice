# Your code below:
## To keep track of the kinds of pizzas you sell, create a list called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

## To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

## Count the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)

## Find the length of the toppings lis
num_pizzas = len(toppings)

## Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas]
print('We sell '+ str(num_pizzas)+ ' different kinds of pizza!')

## Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

## Note: You don’t need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

## Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).

pizza_and_prices.sort()

## Store the first element of pizza_and_prices
cheapest_pizza = pizza_and_prices[0]

## A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
priciest_pizza = pizza_and_prices[-1]

## It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our
pizza_and_prices.pop(-1)

## Add the new peppers pizza topping to our list pizza_and_prices.
pizza_and_prices.insert(4, [2.5, 'peppers'])

## Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
