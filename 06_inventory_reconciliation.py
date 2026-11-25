# Case Study 6: Warehouse Inventory Reconciliation
products = ["Pen", "Notebook", "Pencil"]
opening = [100, 80, 120]
received = [30, 20, 25]
dispatched = [90, 65, 100]
reported_closing = [40, 35, 45]

for i in range(len(products)):
    calculated = opening[i] + received[i] - dispatched[i]
    difference = reported_closing[i] - calculated
    print("\nProduct:", products[i])
    print("Calculated closing stock:", calculated)
    print("Reported closing stock:", reported_closing[i])
    if difference == 0:
        print("Status: Reconciled")
    else:
        print("Discrepancy:", difference)
    if calculated < 30:
        print("Replenishment required:", 50 - calculated)
    else:
        print("No replenishment required")
