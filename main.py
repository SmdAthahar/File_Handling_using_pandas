import pandas as pd

# File names
SALES_FILE = "sales.txt"
REPORT_FILE = "sales_report.csv"


# Store the sales transactions in a Python list.
# Each inner list represents one sales transaction.

sales_data = [
    [101, "Laptop", 1, 65000, "Bangalore"],
    [102, "Mouse", 2, 1200, "Delhi"],
    [103, "Keyboard", 1, 2500, "Hyderabad"],
    [104, "Monitor", 2, 15000, "Chennai"],
    [105, "Headphones", 3, 1800, "Mumbai"],
    [106, "Laptop", 1, 62000, "Delhi"],
    [107, "Mouse", 5, 1100, "Bangalore"],
    [108, "Webcam", 2, 3200, "Pune"],
    [109, "Keyboard", 2, 2200, "Mumbai"],
    [110, "Monitor", 1, 14500, "Hyderabad"],
    [111, "USB Drive", 4, 700, "Chennai"],
    [112, "Laptop", 2, 64000, "Pune"],
    [113, "Headphones", 1, 2100, "Delhi"],
    [114, "Mouse", 3, 1250, "Hyderabad"],
    [115, "Webcam", 1, 3500, "Bangalore"],
    [116, "Monitor", 2, 15500, "Mumbai"],
    [117, "Keyboard", 3, 2400, "Chennai"],
    [118, "USB Drive", 6, 650, "Pune"],
    [119, "Laptop", 1, 67000, "Mumbai"],
    [120, "Headphones", 2, 1900, "Hyderabad"],
    [121, "Mouse", 1, 1300, "Chennai"],
    [122, "Monitor", 3, 14800, "Delhi"],
    [123, "Webcam", 2, 3300, "Mumbai"],
    [124, "Keyboard", 1, 2600, "Bangalore"],
    [125, "USB Drive", 5, 750, "Hyderabad"],
    [126, "Laptop", 1, 65500, "Chennai"],
    [127, "Headphones", 4, 1750, "Pune"],
    [128, "Mouse", 2, 1150, "Mumbai"],
    [129, "Monitor", 1, 15200, "Bangalore"],
    [130, "Webcam", 3, 3100, "Delhi"]
]

# Open the file in write mode.
# If the file does not exist, Python creates it.
# If it already exists, its previous contents are overwritten.

with open(SALES_FILE, "w", encoding="utf-8") as file:

    # Write the column headers into the text file.
    file.write("order_id,product,quantity,price,city\n")

    # Iterate through each transaction.
    for transaction in sales_data:

        # Convert the transaction values into strings
        # and join them using commas.
        line = ",".join(str(value) for value in transaction)

        # Write the transaction into the file.
        # \n moves the cursor to the next line.
        file.write(line + "\n")

print("STEP 1: sales.txt created with 30 transactions.")


# --------------------------------------------------
# STEP 2: Read the file using normal Python file handling
# --------------------------------------------------

print("\nSTEP 2: Reading sales.txt using normal Python file handling")

# Open the file in read mode.
with open(SALES_FILE, "r", encoding="utf-8") as file:

    # Read the entire file contents.
    file_contents = file.read()

    # Display the contents.
    print(file_contents)


# --------------------------------------------------
# STEP 3: Load the same file using Pandas
# --------------------------------------------------

print("STEP 3: Loading sales.txt using Pandas")

# read_csv() reads the comma-separated data
# and converts it into a Pandas DataFrame.
df = pd.read_csv(SALES_FILE)

# Display the DataFrame.
print("\nSales DataFrame:")
print(df)


# --------------------------------------------------
# STEP 4: Calculate revenue for each transaction
# --------------------------------------------------

# Revenue = Quantity * Price

# Create a new column called revenue.
# Pandas performs this calculation for every row.
df["revenue"] = df["quantity"] * df["price"]

print("\nSTEP 4: Revenue added to each order:")
print(df)


# --------------------------------------------------
# STEP 5: Calculate total revenue and average order value
# --------------------------------------------------

# sum() calculates the total revenue.
total_revenue = df["revenue"].sum()

# mean() calculates the average revenue per order.
average_order_value = df["revenue"].mean()

print("\nSTEP 5: Revenue Summary")

print(f"Total Revenue: Rs. {total_revenue:,.2f}")

print(f"Average Order Value: Rs. {average_order_value:,.2f}")


# --------------------------------------------------
# STEP 6: Find the highest-value and lowest-value orders
# --------------------------------------------------

# idxmax() returns the index of the row
# containing the highest revenue.
highest_order = df.loc[df["revenue"].idxmax()]

# idxmin() returns the index of the row
# containing the lowest revenue.
lowest_order = df.loc[df["revenue"].idxmin()]

print("\nSTEP 6: Highest-Value Order")
print(highest_order)

print("\nLowest-Value Order")
print(lowest_order)


# --------------------------------------------------
# STEP 7: Calculate revenue product-wise
# --------------------------------------------------

# groupby() groups all transactions by product.
# sum() calculates the total revenue for each product.
product_revenue = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSTEP 7: Revenue Product-wise")
print(product_revenue)


# --------------------------------------------------
# STEP 8: Calculate revenue city-wise
# --------------------------------------------------

# Group transactions by city
# and calculate the total revenue generated by each city.
city_revenue = (
    df.groupby("city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSTEP 8: Revenue City-wise")
print(city_revenue)


# --------------------------------------------------
# STEP 9: Save the processed data as a CSV file
# --------------------------------------------------

# to_csv() exports the DataFrame into a CSV file.
# index=False prevents Pandas from adding an extra index column.
df.to_csv(REPORT_FILE, index=False, encoding="utf-8")

print(f"\nSTEP 9: Processed sales report saved as {REPORT_FILE}")


# --------------------------------------------------
# PROJECT COMPLETED
# --------------------------------------------------

print("\nSales Analysis Project Completed Successfully!")