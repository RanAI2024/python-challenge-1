# Menue Dictionary
menue = {
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

for key, value in menue.items():
    print(f"{key}: {value}")

print("Welcome to Fastlane Burgers food truck.")


s = 1
menu_items = {}
    
for key in menue.keys():
        print(f"{s}: {key}")   
        menu_items[s] = key
        s += 1
menu_category = input("Type menu number: ")

if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            
            print(f"You selected {menu_category_name}")
            print(f"What {menu_category_name} item would you like to order?")

            s = 1
            menu_items = {}

            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            ## This whole for loop retrieves the menu one item at a time
            ## and prints it with a number for selection
            for key, value in menue[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{s}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[s] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        s += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{s}      | {key}{item_spaces} | ${value}")
                    menu_items[s] = {
                        "Item name": key,
                        "Price": value
                    }
                    s += 1