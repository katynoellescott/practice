#create program to add something to shopping list, check to see if already exists
shopping_list = ["burritos","guacamole","cheese"]

#function to input item into list
def input_item():
    new_item = raw_input("What would you like to add to the shopping list? ")
    return new_item.lower()

#function to check if item already in list
def check_item(new):
    if new in shopping_list:
        return True
    else:
        return False

#function to add item to list
def add_item(added_item):
    shopping_list.append(added_item)


#main function: input, check, add if not in list, repeat if in list
def main():
    new_item = input_item()
    check = check_item(new_item)
    if check == True:
        print "That's already on the list."
        main()
    else:
        add_item(new_item)
        print "%s has been added to the list." % new_item
        shopping_list.sort()
        print shopping_list


if __name__ == '__main__':
    main()