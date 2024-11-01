#Write a program to count the occurrences of an element in a list.
def count_occurrences(my_list,element):
    """"Count the occurrences of the element from  the list."""
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    return count

user_list = [1,3,7,1,2,3,1]
user_element = 1
occurrences = count_occurrences(user_list,user_element)
print(f"\nThe element {user_element} occures {occurrences} times in the list.")
