# 1) Run the code in the markdown and write a comment about what happens.






# 2) Try to print(sorted(my_list2)) and print(my_list2.sort()). Is there a difference? What do you observe?
my_list2 = [1,4,10,9,8,300,20,21,21,46,52]






# 3) Let's say you wanted to sort your list but in reverse order.  To do this, you can put reverse=True inside the parentheses (for either sort() or sorted().
# Try it below, and then print your reverse  sorted list!
my_list3 = [1,4,10,9,8,300,20,21,21,46,52]






# 4) But Mr. Custance, to this  point all I've been sorting are lists with integer values inside. How does .sort() and  sorted() organize string values?
# Sort the following list, print it and comment on how it was sorted:
word_list = ["pizza", "frog", "lemon", "lemon", "computer", "water bottle", "lamp", "table", "radio", "speaker"]





# 5) Do the same  for the following list:
word_list2 = ["lamb", "lap", "lalalala", "laaaa", "larynx", "laguardia", "laproscopy", "lad"]






# 6) How does the .sort() method and sorted function deal with lists that have multiple data types? Create a list that has integers, strings and floats. Sort and print, and then comment on the results.







# 7) Let's say you wanted to sort a list based purely on length of characters. You can  define a function that returns the length of an item, and then use
# that as the key for your sort. For example:
'''
def len_func(a):
  return(len(a))

length_list = ["aaaaaaa", "aaaaa", "aaa", "a", "aaaaaaaaaaaaaaa", "aa", "aaaaaaaaaa", "", "aaaaaaaaaaaaaaaaaaa", "aaaaa", "aaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "   ", "bcbcbdhbb", "dibvibfv", "a"]
'''

#Uncomment the code above, and sort it using either sort() or sorted(). When you do,  in the parentheses include key = len_func. This makes the key based on the function you've defined
#Print your new list below







# 8) Print the list from the  previous  question, but in reverse length order.







# 9) Can .sort() and sorted() be used to sort the chracters in a string? Try it below and comment.






###Bonus###



# 1) Write a program that populates an empty list with 100 random numbers between a minumum and maximum of your choice. Then, sort your new list from smallest to biggest and print your newly sorted list.








