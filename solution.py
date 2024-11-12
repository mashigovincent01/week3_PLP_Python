

def calculate_discount(price, discount_percent):
    discount_percent = discount_percent / 100

    if discount_percent >= 0.2:
        return price * (1 - discount_percent)
    return price

original_price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage .eg 20%: "))

print(f"The final price is {calculate_discount(original_price, discount)}")
