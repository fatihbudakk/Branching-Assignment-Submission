# Package Express Shipping Calculator
# Created by: Maria Garcia
# Version: 3.0.0

# Print welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight
mass_input = float(input("Please enter the package weight:\n"))

# Weight limit check
if mass_input > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package measurements
measure_w = float(input("Please enter the package width:\n"))
measure_h = float(input("Please enter the package height:\n"))
measure_l = float(input("Please enter the package length:\n"))

# Calculate total measurements
total_measure = measure_w + measure_h + measure_l

# Size limit check
if total_measure > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Formula: (width * height * length * weight) / 100
cost_total = (measure_w * measure_h * measure_l * mass_input) / 100

# Display shipping cost
print(f"Your estimated total for shipping this package is: ${cost_total:.2f}")
print("Thank you!") 