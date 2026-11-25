# Case Study 4: Retail Billing with Discount Rules
count = int(input("Number of products: "))
subtotal = 0
for i in range(count):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    if price < 0 or quantity < 0:
        print("Invalid item; ignored")
    else:
        subtotal = subtotal + price * quantity

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05
else:
    discount = 0

taxable = subtotal - discount
tax = taxable * 0.05
total = taxable + tax
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Tax: Rs.", round(tax, 2))
print("Final amount: Rs.", round(total, 2))
