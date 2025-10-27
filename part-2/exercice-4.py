from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)
# map: transform every element
# f had exemple nmdou input wl output is the double of the input

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)
# filter: keep elements that satisfy a condition
# f had exemple we'll only keep the even numbers (a3dad zawjiya)

total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)
# reduce: combine all numbers into one number
# f had exemple we sum all the numbers together, we couldv'e did the sub or the multiplication too, lmohim ndirou something on a list of values and we'll get only one thing as the result, t'as bien capté?

result = reduce(
    lambda x, y: x + y,                    
    filter(
        lambda x: x > 10,                    
        map(lambda x: x * 2, numbers)        
    )
)
print("Final result:", result)
# hna drna everything at once, first thing we did is we doubled each number (using the map), ki tji tchouf we didn't store the result of the map in a variable, we just passed it directly to the filter
# then we filtered the doubled numbers to keep only those greater than 10, as you can see in line 23
# finally, we summed up the filtered numbers using reduce
