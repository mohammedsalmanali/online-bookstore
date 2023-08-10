from book import Book
from user import User
from cart import Cart
from order import Order

def main():
    # Sample code to interact with the classes
    book1 = Book("Python Programming", "John Smith", 29.99)
    user = User("user123", "user@example.com")
    cart = Cart()  # Creating an instance of Cart
    cart.add_item(book1)
    
    payment_method = "Credit Card"  # Assume user selects a payment method
    order = Order(user, cart.items, payment_method)
    
    print(f"Total amount: ${cart.total()}")
    print(f"Order placed by: {order.user.username}")
    print(f"Payment method: {order.payment_method}")

if __name__ == "__main__":
    main()
