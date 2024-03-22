# Define countries eligible for discount
eligible_countries = ["egypt", "palestine", "syria", "yemen", "ksa", "usa", "bahrain", "england"]

# Prompt user for their country
country = input("What is Your Country? ").strip().lower()

# Set price and discount values
price = 100
discount = 30

# Check if the entered country is eligible for discount
if country in eligible_countries:
    # Apply discount and print the updated price
    discounted_price = price - discount
    print(f"Your Country is Eligible for a Discount. The Price After Discount is ${discounted_price}")
else:
    # Print the original price if the country is not eligible for discount
    print(f"Your Country is Not Eligible for a Discount. The Price is ${price}")
