# initializes the list to hold user's input
order_list = []
check = True

# creates the menu
menu_items = {
    1: {"Item": "Pizza", "Price": 9.00},
    2: {"Item": "Burger", "Price": 5.00},
    3: {"Item": "Hot Dog", "Price": 4.50},
    4: {"Item": "Fries", "Price": 2.50},
    5: {"Item": "Soft Drink", "Price": 3.75},
}

# creates a function in order to display the menu
def displayMenu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['Item']} - ${value['Price']:.2f}")

# this loop allows users to place their order
# this function will loop until the user decides not to order anything else
place_order = True
while place_order:
    displayMenu()
    # asks the user what the item number is of the item they want to order
    menu_selection = input("\nEnter the number of the item you'd like to order: ")

    # checks the input to make sure it is a number
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number. \n")
    else:
        # forces the input number to an integer
        menu_selection = int(menu_selection)

        # checks to make sure the user input is valid and if it isnt it restarts the loop
        if menu_selection not in menu_items:
            print("Error: Invalid selection. Please choose a valid item.\n")
        else:
            # extracts the name of the item
            item_name = menu_items[menu_selection]["Item"]

            # asks the user how many they want to order
            quantity = input(f"How many {item_name}s would you like? (default is 1): ")

            # checks to make sure that the input is a number
            # if the input is not the it will be set to 1 as stated above
            if not quantity.isdigit():
                quantity = 1
            else:
                quantity = int(quantity)

            # adds the order to the end of the list
            order_list.append({
                "Item Name": item_name,
                "Price": menu_items[menu_selection]["Price"],
                "Quantity": quantity
            })

            # a match case statement to continue ordering
            while check:
                action = input("Do you want to continue ordering? (y/n): ").lower()
                match action:
                    case 'y':
                        place_order = True
                        check = False
                    case 'n':
                        place_order = False
                        print("Thank you for your order!")
                        check = False
                    case _:
                        print("\nInvalid input. Please try again.\n")
            check = True
            
            # prints the receipt header
            print("\nItem Name                | Price  | Quantity")
            print("-------------------------|--------|----------")

            # prints the rest of the receipt
            for order in order_list:
                item_name = order["Item Name"]
                price = order["Price"]
                quantity = order["Quantity"]

                # calcs the correct number of spaces to make it look pretty
                spaces_item = " " * (25 - len(item_name))

                # prints the current item in proper formatting
                print(f"{item_name}{spaces_item}| ${price:.2f}  | {quantity}")
            print("\n")

# calcs & prints the final price
total_price = sum([order["Price"] * order["Quantity"] for order in order_list])
print(f"\nTotal Price: ${total_price:.2f}\n")
