
inventory=[]
n=int(input("ENTER THE NUMBER OF ASSETS: "))# here we need to enter the Count of the inventory 
for i in range(n):                     # the loop will work at the number of times we have entered the count of the inventory

    print("enter the asset details :")
    asset_id=input("ENTER THE ASSET ID:")
    asset_name=input("ENTER THE ASSET NAME:")
    quantity=int(input("ENTER THE ASSET QUANTITY  :"))
    brand=input("ENTER THE BRAND OF THE ASSET :")
    if quantity>0:        # the condition is if the quantity is >0 then the status will be available otherwise it will be out of stock
        status="available"
    else:
        status="out of stock"

    asset={
        "asset id":asset_id,"asset name":asset_name,"quantity":quantity,"brand":brand,"status":status}
    inventory.append(asset) # here we are appending the asset details to the inventory list


print(" Office Inventory details ")
for asset in inventory:
    print("--------------------")
    for key, value in asset.items():
        print(key ,":",value)