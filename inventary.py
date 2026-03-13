inventory = []

def add_item():
    i = True
    name = input("Hello, What's your name ?: ")
    print(f"\nWelcome {name} to the inventory system\n")
    print ("-----------------------------------------")

    

    while i:
            try:
                product = input("Enter the name of product: ")
                break
            except ValueError:
                print("Please, enter a valid product.")

    while i:
        try:
            quantity = int(input("Enter the quantities of items: "))
            break
        except ValueError:  
         print("Please enter a correct value ")

  
    while i:
            try:
                price =  float(input("Enter the price of items: "))
                break
            except ValueError:
                print("Please type the price with float")
    
   

    new_product = {
        "product": product,
        "quantity": quantity,
        "price": price
    }
    inventory.append(new_product)

add_item()