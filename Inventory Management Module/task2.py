# Laptop Management System
new_laptops = []
# ADD LAPTOP DETAILS
n = int(input("Enter number of laptops: "))
for i in range(n):
    print("\nEnter Laptop Details")
    laptop_id = input("Enter Laptop ID: ")
    brand = input("Enter Brand: ")
    RAM = input("Enter RAM: ")
    Storage = input("Enter Storage: ")
    Status = input("Enter Status: ")
    laptop = {"Laptop ID": laptop_id,"Brand": brand,"RAM":RAM,"Storage":Storage,"Status":Status}
    new_laptops.append(laptop)
# UPDATE CONFIGURATION
for laptop in new_laptops:
    print("\nUpdate Laptop Configuration")
    new_RAM= input("Enter New RAM: ")
    laptop["RAM"] = new_RAM
    new_Storage = input("Enter New Storage:")
    laptop["Storage"] = new_Storage
# MODIFY ALLOCATION STATUS
for laptop in new_laptops:
    print("\nModify  Status")
    new_Status = input("Enter New  Status: ")
    laptop["Status"] = new_Status
# DISPLAY UPDATED RECORDS
print("\nUPDATED LAPTOP RECORDS")
for laptop in new_laptops:
    print("-------------------")
    for key, value in laptop.items():
        print(key, ":", value)
# BRAND-WISE LAPTOP REPORT
print("\nBRAND-WISE LAPTOP REPORT")
for laptop in new_laptops:
    print("-------------------")
    print("Brand :", laptop["Brand"])
    print("RAM :", laptop["RAM"])
    print("Storage :", laptop["Storage"])
    print("Status :", laptop["Status"])