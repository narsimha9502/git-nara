# Example code for a simple grocery application CLI

inventory = {
    'apple': {'price': 1.00, 'quantity': 10},
    'banana': {'price': 0.50, 'quantity': 15},
    'orange': {'price': 0.75, 'quantity': 8},
    'grape': {'price': 1.00, 'quantity': 5}
}

cart = {}

#addinng cart
def add_to_cart(item, quantity):
    if item in inventory and inventory[item]['quantity'] >= quantity:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        inventory[item]['quantity'] -= quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Sorry, that item is either not available or we don't have enough stock.")
# adding view cart
def view_cart():
    total_price = 0
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, quantity in cart.items():
            price = inventory[item]['price']
            item_total = price * quantity
            total_price += item_total
            print(f"{item}: {quantity} x ${price} = ${item_total}")
        print(f"Total: ${total_price}")
# main function
def main():
    while True:
        print("\n=== Grocery Store ===")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ").strip().lower()
            quantity = int(input("Enter quantity: "))
            add_to_cart(item, quantity)
        elif choice == '2':
            view_cart()
        elif choice == '3':
            # Implement checkout logic 
            print("Checkout functionality not implemented yet.")
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
class Name:
    def __init__(javatpoint):
        javajavatpoint = 'java'
        name1=Name("ABC")
        name2=name1