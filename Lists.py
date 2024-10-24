#place to store multiple items -> list
#do try to keep numbers to numbers, string to string, etc.
#every element on the list is offset by one. n-1

List=["milk", "eggs", "brownies", "bread", "water"]
print(f"List before: {List}")
#we want to keep the list items the same order to avoid confusion
List.append("apples!!!")
print(f"List after: {List}")
#to do that, use append to add to the end of the list.
#but if we want to remove something, we do:
List.remove("apple")
print(f"Removed apple from the list :()")
#to add use .append, to remove use .remove

#List.pop(position) to remove element in certain position
#print(f"your list is {len(List)} long") -> len() can give the number of things in a list when used with list, if there's a word (word=word), it can give how many letters on a spring.

