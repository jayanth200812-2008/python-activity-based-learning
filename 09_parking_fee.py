# Case Study 9: Smart Parking Fee Management
entry = int(input("Enter entry hour (0-23): "))
exit_hour = int(input("Enter exit hour (0-23): "))
vehicle = input("Vehicle type (two/four): ").lower()

if entry < 0 or entry > 23 or exit_hour < 0 or exit_hour > 23:
    print("Invalid time")
else:
    duration = exit_hour - entry
    if duration <= 0:
        duration = duration + 24
    if vehicle == "two":
        rate = 10
    elif vehicle == "four":
        rate = 20
    else:
        rate = 0
    if rate == 0:
        print("Invalid vehicle type")
    else:
        fee = duration * rate
        if fee > 200:
            fee = 200
        print("Parking duration:", duration, "hours")
        print("Parking fee: Rs.", fee)
