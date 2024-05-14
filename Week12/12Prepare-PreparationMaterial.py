# FINDING THE MAX OR MIN
numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # THis number is larger than the largest we had seen so far

        # So it is now th elargest we've seen
        largest_so_far = number

# Now after the loop we can display it:
print(f'The largest is: {largest_so_far}') # Output = 'The largest is: 85'


# KEEPING TRACK OF THE ITEM THAT IS THE MAX OR MIN
shopping_cart = [
    ['Chips', 2.99],
    ['Bread', 2.50],
    ['Milk', 3.19],
    ['Ice Cream', 6.99],
    ['Cheese', 5.99],
    ['Candy Bar', 0.99],
]

max_price = -1
max_product = '' # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f'The maximum price is: {max_price}') # Output = 'The maximum price is: 6.99'
print(f'The product with the maximum price is: {max_product}') # Output = 'The product with the maximum price is: Ice Cream'


# OTHER CODE WITH LOOPS AND FILES
'''
Keep in mind that you can use all of the other components you have learned throughout the semester in conjunction with files. 
For example, if you wanted to restrict your analysis of products to only those that had a price over a certain amount, or that 
had a name matching certain criteria, you can include an if statement in the middle of the loop that is iterating through the file.
'''