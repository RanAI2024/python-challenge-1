# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []
menu = {
    "Fast Burgers" : {
        "Small Burger" : 1.99,
        "Medium Burger" : 2.99,
        "Large Burger" : 3.99,
        "add cheese" : 0.50
    },
    "Burger Specials" : {
        "Quick Burger" : 6.99,
        "Express Burger" : 6.99,
        "First Class" : 8.99,
        "Fastlane Special" : 9.99
    },

    "Fast Fries" : {
        "Small" : 0.99,
        "Medium" : 1.99,
        "Large" : 2.99
    },

    "Drinks" : {
        "Fountain Drink" : 1.99,
        "Can Soda" : 0.99,
        "Bottled Water" : 1.99
    }
}


# Launch the store and present a greeting to the customer
print("Welcome to Fastlane Burgers food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order?")
    menu_items = {}
    i = 1

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        menu_category = int(menu_category)
        # Check if the customer's input is a valid option
        if menu_category in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[menu_category]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            i = 1
            item_menu = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                item_spaces = " " * (24 - len(key))
                print(f"{i}      | {key}{item_spaces} | ${value}")
                item_menu[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1

            # 2. Ask customer to input menu item number
            menu_item_number = input("Please enter item number: ")

            # 3. Check if the customer typed a number
            if menu_item_number.isdigit():
                # Convert the menu selection to an integer
                menu_item_number = int(menu_item_number)

                # 4. Check if the menu selection is in the menu items
                if menu_item_number in item_menu.keys():
                    # Store the item name as a variable
                    menu_item_name = item_menu[menu_item_number]["Item name"]
                    menu_item_price = item_menu[menu_item_number]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input("Enter quantity: ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        print("Invalid input. Defaulting quantity to 1.")
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_item = {
                        "Item name": menu_item_name,
                        "Price": menu_item_price,
                        "Quantity": quantity
                    }
                    order_list.append(order_item)

                    # Ask the customer if they would like to order anything else
                    while True:
                        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ")
                        # 5. Check the customer's input
                        if keep_ordering.upper() == "N":
                            # Complete the order
                            place_order = False
                            # Since the customer decided to stop ordering, thank them for their order
                            print("Thank you for your order.")
                            break
                        elif keep_ordering.upper() == "Y":
                            break
                        else:
                            # Tell the customer to try again
                            print("Invalid input. Please enter 'Y' or 'N'.")
                else:
                    # Tell the customer they didn't select a menu option
                    print("Invalid item number selection.")
            else:
                # Tell the customer they didn't select a number
                print("Invalid input. Please enter a number.")
        else:
            # Tell the customer they didn't select a menu option
            print("Invalid menu selection.")
    else:
        # Tell the customer they didn't select a number
        print("Invalid input. Please enter a number.")

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                | Price  | Quantity")
print("-------------------------|--------|----------")

# 6. Loop through the items in the customer's order
total_cost = 0
for item in order_list:
    # 7. Store the dictionary items as variables
    menu_item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    item_spaces = " " * (24 - len(menu_item_name))
    price_spaces = " " * (6 - len(str(price)))

    # 9. Create space strings

    # 10. Print the item name, price, and quantity
    print(f"{menu_item_name}{item_spaces} | ${price}{price_spaces} | {quantity}")

    # 11. Calculate the cost of the order using list comprehension
    total_cost += price * quantity

print(f"\nThe total cost of your order is: ${total_cost:.2f}")

