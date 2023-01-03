
def count_characters(name):
    count = 0
    for i in name:
        count  += 1
    return count


name = input("enter your name: ")
print(count_characters(name))
