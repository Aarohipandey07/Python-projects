# Food item aur unke rates
menu = {
    "Pizza": 200,
    "Burger": 100,
    "Pasta": 150,
    "Sandwich": 80,
    "Fries": 50
}

# Function to display menu
def display_menu():
    print("\nMenu: ")
    for item, price in menu.items():
        print(f"{item} : {price}/-")

# Function to take order from customer
def take_order():
    total_bill = 0
    
    while True:
        display_menu()
        order = input("Type 'exit' to finish\nYour order please: ").capitalize()
        
        if order.lower() == "exit":
            print(f"Total bill: Rs {total_bill}")
            print("Thank you! Visit again.")
            break
        
        if order in menu:
            qty = int(input("Kitna chahiye?: "))
            item_total = menu[order] * qty
            total_bill += item_total
            
            print(f"Aapka order: {order} x {qty} = Rs {item_total}")
        else:
            print("Maaf kijiye, yeh item menu mein nahi hai.")

# Start taking orders
take_order()
