
inventory=[]
asset_id=[101,102,103,104,105]
asset_name=["laptop","mouse","keyboard","monitor","printer"]
quantity=[10,20,15,5,8]
brand=["dell","logitech","asus","samsung","hp"]

for i in range(len(asset_id)):
    if quantity[i]>0:        # the condition is if the quantity is >0 then the status will be available otherwise it will be out of stock
        status="available"
    else:
        status="out of stock"

    asset={
        "asset id":asset_id[i],"asset name":asset_name[i],"quantity":quantity[i],"brand":brand[i],"status":status}
    inventory.append(asset) # here we are appending the asset details to the inventory list


print(" Office Inventory details ")
for asset in inventory:
    print("--------------------")
    for key, value in asset.items():
        print(key ,":",value)