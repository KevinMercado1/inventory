inventory = []

# Here I put a greeting to the user

name = input("Hello, What's your name ?: ")
print(f"\nWelcome {name} to the inventory system!\n")
print ("-----------------------------------------")

# Here is the principal def for running all the program.

def add_item():
    # I added a variable "i", for controlling the while loop
    i = True
    product = input("Enter the name of product: ")
    while i:
        try:
            quantity = int(input(f"Enter the quantities of items: "))
            if quantity > 0:

                break
        except ValueError:  
         print("Please enter a correct value ")

  # Here I placed a while loop to iterate through the price and ensure it is greater than 0.
    while i:
            try:
                price =  float(input(f"Enter the price of items: "))
                if price > 0:

                 break
            except ValueError:
                print("Please type the price with float")
    
    # In this part call a varible "total_cost", for implement the result between Quantity and price.
    # I added a dictionary inside a list.
    total_cost = quantity * price

    new_product = {
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": total_cost
    }
    inventory.append(new_product)

# I put a varible ask for a while loop and control it.
ask = True

while ask:

# I added 'add_item' to call the entire function inside the while loop
    add_item()
    op = input("Do you want to add more items? (y/n): ").lower()
    if op != "y":
        ask = False

print("\n\nFinal of inventory: ")
print("-------------------------------")

total_sum = 0

#Finally a for loop to call the items and inventory and thus calculate the total of the etire inventory.

for items in inventory:
    print( f"product: {items['product']}, "
        f"quantity: {items['quantity']}, "
        f"price: {items['price']:.2f}, "
        f"total: {items['total']:.2f}")
    total_sum += items['total']

print(f"\nHere your voucher: {total_sum:.2f}")
print("-------------------------------")

#That's all, Thanks you for reading and understanding it.