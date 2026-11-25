# Case Study 1: Progressive Electricity Billing
units = int(input("Enter electricity units consumed: "))
if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00
    fixed_charge = 50
    total = bill + fixed_charge
    print("Energy charge: Rs.", round(bill, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Total bill: Rs.", round(total, 2))
