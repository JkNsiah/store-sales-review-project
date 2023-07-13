products = ["Sankofa Foods", "James Town Coffee", "Bioko Chocolate", "Blue Skies Ice Cream",
           "Fair Afric Chocolate", "Kawa Maka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# calculate the total price average for all products
total_prices = sum(prices)
average_price = total_prices /len(products)
print("The total price average for all product is: $", average_price)

# Create a new price list that reduces the old prices by $ 5
new_price = [price - 5 for price in prices]
print("The new price list is:", new_price)

# Calculate the total revenue generated from the products
total_revenue = sum(price * customers for price, customers in zip(prices, last_week))
print("The total revenue generated for the products is:", total_revenue)

# Calculated the average daily revenue generated from the products
average_daily_revenue = (total_revenue / 7)  # assuming 7 is a number of days in a week
print("The average daily revenue generated from the products is:", average_daily_revenue)

# Based on the new prices, which products are less than $ 30
products_less_than_thirty_dollars = [product for product, price in zip(products, new_price) if price < 30]
print("Products less than $30:", products_less_than_thirty_dollars)