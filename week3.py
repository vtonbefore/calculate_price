def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price
# Prompt the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
