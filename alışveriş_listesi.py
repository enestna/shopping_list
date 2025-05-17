# SHOPPİNG LİST
mylist = {}

def add_product():
    product = input("Product name: ").strip()
    amount = int(input("Amount: "))
    if(product in mylist):
        mylist[product]+=amount
        print(f"{product} already had but amount uptaded to {mylist[product]}.")
    else: 
        mylist[product]=amount
        print(f"{product} added.")
def show_list():
    print("\nShopping List:")
    if not mylist:
        print("absent list")
    else:

       for product, amount in mylist.items():
         print(f"- {product}: {amount}")

def delete_product():
    product = input("Product to delete: ").strip()
    if product in mylist:
        del mylist[product]
        print(f"{product} deleted.")
    else:
        print("Product not found.")

while True:
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show list")
    print("3. Delete product")
    print("4. Exit")

    choice = input("Your choice: ").strip()

    if (choice == "1"):
        add_product()
    elif (choice == "2"):
        show_list()
    elif (choice == "3"):
        delete_product()
    elif (choice == "4"):
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
