import turtle
import os  # For saving receipts
import winsound  # For sound effects (Windows only)

# Function to calculate the total price
def calculate_total_price(item_price, quantity=1, discount=0.0, tax_rate=0.18):
    """
    Calculates the total price for an item considering:
    - Item price
    - Quantity (default is 1)
    - Discount (default is 0.0, meaning no discount)
    - Tax rate (default is 18%)
    """
    price_after_discount = item_price * quantity * (1 - discount)
    total_price = price_after_discount * (1 + tax_rate)
    return total_price

# Function to save the receipt as a text file
def save_receipt_to_file(customer_name, item_name, item_price, quantity, discount, tax_rate, total_price):
    """
    Saves the receipt details to a text file.
    """
    filename = f"{customer_name}_receipt.txt"
    with open(filename, "w") as file:
        file.write("="*30 + "\n")
        file.write("Receipt\n")
        file.write("="*30 + "\n")
        file.write(f"Customer: {customer_name}\n")
        file.write(f"Item: {item_name}\n")
        file.write(f"Price per item: ${item_price:.2f}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Discount: {discount * 100:.1f}%\n")
        file.write(f"Tax rate: {tax_rate * 100:.1f}%\n")
        file.write(f"Total Price: ${total_price:.2f}\n")
        file.write("="*30 + "\n")
        file.write("Thank you for shopping with us!\n")
    print(f"\nReceipt has been saved as {filename}!")

# Function to draw a visual receipt using Turtle
def draw_receipt(customer_name, item_name, item_price, quantity, discount, tax_rate, total_price):
    """
    Draws a visual receipt using the turtle graphics module.
    """
    screen = turtle.Screen()
    screen.title("Receipt Animation")
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("blue")

    # Draw the border
    pen.penup()
    pen.goto(-200, 200)
    pen.pendown()
    for _ in range(2):
        pen.forward(400)
        pen.right(90)
        pen.forward(300)
        pen.right(90)

    # Add title
    pen.penup()
    pen.goto(-180, 180)
    pen.pendown()
    pen.write("Receipt", font=("Arial", 16, "bold"))

    # Add receipt details
    receipt_details = [
        f"Customer: {customer_name}",
        f"Item: {item_name}",
        f"Price per item: ${item_price:.2f}",
        f"Quantity: {quantity}",
        f"Discount: {discount * 100:.1f}%",
        f"Tax rate: {tax_rate * 100:.1f}%",
        f"Total Price: ${total_price:.2f}"
    ]
    y = 150
    for detail in receipt_details:
        pen.penup()
        pen.goto(-180, y)
        pen.pendown()
        pen.write(detail, font=("Arial", 12, "normal"))
        y -= 30

    # Thank-you message
    pen.penup()
    pen.goto(-180, y - 30)
    pen.pendown()
    pen.write("Thank you for shopping with us!", font=("Arial", 12, "italic"))

    pen.hideturtle()
    # Play a sound effect
    try:
        winsound.Beep(500, 200)  # Beep sound on Windows
    except:
        pass  # Ignore if sound is unsupported
    screen.mainloop()

# Function to display receipt
def display_receipt(customer_name, item_name, item_price, quantity=1, discount=0.0, tax_rate=0.18):
    """
    Displays a receipt, saves it to a file, and draws it using the Turtle module.
    """
    total_price = calculate_total_price(item_price, quantity, discount, tax_rate)
    print("="*30)
    print(f"Customer: {customer_name}")
    print(f"Item: {item_name}")
    print(f"Price per item: ${item_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Discount: {discount * 100:.1f}%")
    print(f"Tax rate: {tax_rate * 100:.1f}%")
    print(f"Total Price: ${total_price:.2f}")
    print("="*30)

    # Save receipt to file
    save_receipt_to_file(customer_name, item_name, item_price, quantity, discount, tax_rate, total_price)

    # Draw receipt
    draw_receipt(customer_name, item_name, item_price, quantity, discount, tax_rate, total_price)
    return total_price

# Main shopping process
def online_shopping():
    print("\nWelcome to the Online Shopping System!")
    customer_name = input("Enter your name: ")
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity (default is 1, press Enter to skip): ") or 1)

    # Get discount as percentage or decimal
    discount = float(input("Enter discount rate (default is 0, press Enter to skip, e.g., 10 for 10%): ") or 0.0)
    if discount > 1:  # Convert to decimal if user enters a percentage
        discount = discount / 100

    tax_rate = float(input("Enter tax rate (default is 18%, press Enter to skip): ") or 0.18)

    # Display the receipt
    display_receipt(customer_name, item_name, item_price, quantity, discount, tax_rate)

# Function to repeat shopping for multiple customers
def run_shopping_system():
    while True:
        online_shopping()
        again = input("\nWould you like to shop again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for shopping with us! Have a great day!")
            break

# Run the program
run_shopping_system()
