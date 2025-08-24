# Stock---management-my-first-repo
A simple stock management system for learning Git and GitHub . A stock management system to add, update and track products in inventory .  

##Features
-Adding
-Updating
-Deleting
-Watching product list 



import json, os
stock = []

## Loading file function
def load_S(path="Stock.json"):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read() or "[]")

## Saving file function
def save_S(path="Stock.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=2)

## Menu function
def menu():
    print("\n1. Adding product")
    print("2. Display product list")
    print("3. Delete a product")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

## Adding function
def add_p(pro_N, pro_Q):
    new_P = {"pro_N": pro_N, "pro_Q": pro_Q, "done": False}
    stock.append(new_P)
    save_S()
    print("Product added successfully!")

## Displaying product list function
def display():
    if not stock:
        print(" No products available.")
        return

    print("\nCurrent Products:")
    print("-" * 40)
    print(f"{'No.':<5}{'Name':<20}{'Quantity':<10}")
    print("-" * 40)
    for i, p in enumerate(stock, 1):
        print(f"{i:<5}{p['pro_N']:<20}{p['pro_Q']:<10}")
    print("-" * 40)

## Removing product from list
def delete(pro_N):
    for i, p in enumerate(stock):
        if p['pro_N'].lower() == pro_N.lower():
            del stock[i]
            save_S()
            print(f" The item : {pro_N} was deleted successfully.")
            return
    print(f" Product : {pro_N}  not found!")

## Main function
def main():
    global stock
    stock = load_S()
    while True:
        choice = menu()
        if choice == 1:
            pro_N = input("Enter product name: ").strip()
            pro_Q = int(input("Enter product quantity: "))
            add_p(pro_N, pro_Q)
        elif choice == 2:
            display()
        elif choice == 3:
            pro_N = input("Enter product name to delete: ").strip()
            delete(pro_N)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print(" Invalid choice!")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
