# Laptop Management System
new_laptops = []
# Add Laptop Details
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
# Updated Configuration
for laptop in new_laptops:
    print("\nUpdate Laptop Configuration")
    new_RAM= input("Enter New RAM: ")
    laptop["RAM"] = new_RAM
    new_Storage = input("Enter New Storage:")
    laptop["Storage"] = new_Storage
# Modify Allocation Status
for laptop in new_laptops:
    print("\nModify  Status")
    new_Status = input("Enter New  Status: ")
    laptop["Status"] = new_Status
# Display Updated records
for laptop in new_laptops:
    print("-------------------")
    print("Laptop ID :", laptop["Laptop ID"])
    print("Brand     :", laptop["Brand"])
    print("RAM       :", laptop["RAM"])
    print("Storage   :", laptop["Storage"])
    print("Status    :", laptop["Status"])
# Brand-Wise Laptop Report
print("Brand-Wise Laptop Report:")
brands = []
for laptop in new_laptops:
    if laptop["Brand"] not in brands:
        brands.append(laptop["Brand"])
for brand in brands:
    print("Brand :", brand)
    for laptop in new_laptops:
        if laptop["Brand"] == brand:
            print("Laptop ID :", laptop["Laptop ID"])
            print("RAM       :", laptop["RAM"])
            print("Storage   :", laptop["Storage"])
            print("Status    :", laptop["Status"])
