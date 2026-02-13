# Stores item names and their prices in a dictionary.
# Takes an item name as input from the user.
# Checks whether the item exists in the dictionary.
# If it exists, displays its price.
# Otherwise, displays "Item not available".

d = {
      "Fan" : "$200",
      "fridge" : "$300",
      "T.v" : "$400"
}

item_name = input("name of item is :")


if (item_name in d):
    print("Price of the item is :" , d[item_name])

else:
    print("Ieam not available")

                                            # secound method

def item ():

    if (item_name in d):
        print(f"ITEM price is : {d[item_name]}")
        return
    
    elif (item_name not in d):
        print(f"ITEM not found. ")

d = {"Fan" : "$200" , "fridge" : "$300" , "T.v" : "$400"}
item_name = input("Enter item name for their price :")
item ()
