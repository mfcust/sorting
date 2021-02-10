# sorting

In this assignment, you'll learn all about sorting things! There are very helpful functions/methods that python has built in for sorting things like lists.  For example, let's say you had a list like the one below:
```
my_list = [1,4,10,9,8,300,20,21,21,46,52]
```
I like my list, but I want it to be ordered from the smallest number to the biggest number from left to right. I have two options I can choose from to accomplish this task. First, I can use the .sort() method on my list.  This method fundamentally changes my original list by switching the location of the numbers. Here's what it looks like below:
```
my_list.sort()
print(my_list)
```
I would use this method if I don't care about my original list, and just want the sorted one. This method works faster then the next one.

If instead I want to preserve the integrity of the orginial my_list, but still want to  generate  a new list of sorted values, I can use the sorted() function like so:
```
new_list = sorted(my_list)
print(new_list)
```

Navigate to your Python file to test these out, and to learn more about sorting!
