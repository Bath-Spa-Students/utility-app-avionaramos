# Vending Machine

print("""\n................................................................... Welcome to .............................................................................""")
print("""
      __      _______ ____  _   _          _  _____  __      ________ _   _ _____ _____ _   _  _____   __  __          _____ _    _ _____ _   _ ______ 
     /\ \    / /_   _/ __ \| \ | |   /\   ( )/ ____| \ \    / /  ____| \ | |  __ \_   _| \ | |/ ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
    /  \ \  / /  | || |  | |  \| |  /  \  |/| (___    \ \  / /| |__  |  \| | |  | || | |  \| | |  __  | \  / |  /  \ | |    | |__| | | | |  \| | |__   
   / /\ \ \/ /   | || |  | | . ` | / /\ \    \___ \    \ \/ / |  __| | . ` | |  | || | | . ` | | |_ | | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
  / ____ \  /   _| || |__| | |\  |/ ____ \   ____) |    \  /  | |____| |\  | |__| || |_| |\  | |__| | | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
 /_/    \_\/   |_____\____/|_| \_/_/    \_\ |_____/      \/   |______|_| \_|_____/_____|_| \_|\_____| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|""")

print(""""\n|$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
|$|                           |$| CATEGORY: BISCUITS                                    |$$$$$$$$$$$$$$$$$$$$|
|$|  =====  ..--''`  |~~``|   |$| Code: C1 | Name: Loacker   | Price: $1.00 | Stocks: 5 |$$|``````````````|$$|
|$|  |___|  \     |  :    |   |$| Code: C2 | Name: Glucose   | Price: $1.00 | Stocks: 3 |$$|              |$$|
|$|  /=__\  ./.__\   |/,__\   |$| Code: C3 | Name: Bounty    | Price: $2.50 | Stocks: 1 |$$|  Insert your |$$|
|$|  \__//   \__//    \__//   |$| Code: C4 | Name: Digestive | Price: $2.00 | Stocks: 2 |$$|   cash here  |$$|
|$|=====================================================================================|$$|  __________  |$$|
|$|`````````````````````````````````````````````````````````````````````````````````````|$$| |          | |$$|
|$|  =.._      +++     ////// |$| CATEGORY: SNACKS                                      |$$|  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻  |$$|
|$| \/  \     | |     \    \  |$| Code: F1 | Name: Lays      | Price: $2.50 | Stocks: 5 |$$|______________|$$|
|$| \___\     |_|     /___ /  |$| Code: F2 | Name: Doritos   | Price: $3.00 | Stocks: 7 |$|```````````````|$$|
|$| / __\\   /|_|\   // __\    |$| Code: F3 | Name: Cheetos   | Price: $1.50 | Stocks: 2 |$|  Card Payment |$$|
|$| \__//-   \|_//   -\__//   |$| Code: F4 | Name: Chezzy    | Price: $2.00 | Stocks: 4 |$|               |$$|
|$|=====================================================================================|$|               |$$|
|$|`````````````````````````````````````````````````````````````````````````````````````|$|    TAP HERE   |$$|
|$| ..--    ______   .--._.   |$| CATEGORY: COLD DRINKS                                 |$|_______________|$$|
|$| \   \   |    |   |    |   |$| Code: F1 | Name: Pepsi     | Price: $3.00 | Stocks: 2 |$|```````````````|$$|
|$|  \___\  : ___:   | ___|   |$| Code: F2 | Name: Coca-cola | Price: $3.50 | Stocks: 1 |$| ____________  |$$|
|$|  / __\  |/ __\   // __\   |$| Code: F3 | Name: Iced Tea  | Price: $2.50 | Stocks: 4 |$| |A1|A2|A3|A4| |$$|
|$|  \__//   \__//  /_\__//   |$| Code: F4 | Name: Water     | Price: $1.00 | Stocks: 6 |$| |C1|C2|C3|C4| |$$|
|$|=====================================================================================|$| |F1|F2|F3|F4| |$$|
|$|`````````````````````````````````````````````````````````````````````````````````````|$| |J1|J2|J3|J4| |$$|
|$|  =====  ..--''`  |~~``|   |$| CATEGORY: CHOCOLATE                                   |$| ````````````` |$$|     
|$|  |___|  \     |  :    |   |$| Code: J1 | Name: Kitkat    | Price: $3.00 | Stocks: 0 |$|[=============]|$$|                                                                                    
|$|  /=__\  ./.__\   |/,__\   |$| Code: J2 | Name: Reese     | Price: $1.50 | Stocks: 7 |$|    _   _      |$$|
|$|  \__//   \__//    \__//   |$| Code: J3 | Name: M&M       | Price: $2.00 | Stocks: 2 |$|   ||| ( )     |$$|
|$|                           |$| Code: J3 | Name: M&M       | Price: $2.00 | Stocks: 4 |$|   |||  `      |$$|                         
|$|=====================================================================================|$|    ~          |$$|
|$|`````````````````````````````````````````````````````````````````````````````````````|$|_______________|$$|      
|$|                                                                                     |$|               |$$|
|$|                                                                                     |$$$$$$$$$$$$$$$$$$$$|
|$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
|$||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$```````$$$$$$$$$|
|$|||||||||PUSH||||||||||||||||||||||||||||||||||||||||||||||||||||||$$$$$$$$$$$$$$\|||||/$$$$$$$$$$$$$$$$$$$|
|$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////////////////////
|___________________________________________________________________________________________________|CR98|___|""") 

class VendingMachine:
    def __init__(self):
        self.menu = {
            'BISCUITS': { 'A1': {'name': 'Loacker',
                                'price': 1.00,
                                'stock': 5},
                          'A2': {'name': 'Glucose',
                                 'price': 1.00,
                                 'stock': 3},
                          'A3': {'name': 'Bounty',
                                 'price': 2.50,
                                 'stock': 1},
                          'A4': {'name': 'Digestive',
                                 'price': 2.00,
                                 'stock': 2}},
                                 
            'SNACKS': {'C1': {'name': 'Lays', 
                              'price': 2.50,
                                'stock': 5},
                       'C2': {'name': 'Doritos', 
                              'price': 3.00,
                                'stock': 7},
                       'C3': {'name': 'Cheetos', 
                              'price': 1.50, 
                              'stock': 2},
                       'C4': {'name': 'Cheezy', 
                              'price': 2.00, 
                              'stock': 4}},

            'COLD DRINKS': {'F1': {'name': 'Pepsi', 
                                   'price': 3.00, 
                                   'stock': 2},
                            'F2': {'name': 'Coca-cola',
                                    'price': 3.50, 
                                    'stock': 1},
                            'F3': {'name': 'Iced Tea', 
                                   'price': 2.50, 
                                   'stock': 4},
                            'F4': {'name': 'Water',
                                    'price': 1.00, 
                                    'stock': 6}},

            'CHOCOLATE': {'J1': {'name': 'Kitkat', 
                                 'price': 3.00,
                                   'stock': 0},
                          'J2': {'name': 'Reese', 
                                 'price': 1.50, 
                                 'stock': 7},
                          'J3': {'name': 'M&M', 
                                 'price': 2.00, 
                                 'stock': 2},
                          'J4': {'name': 'Break', 
                                 'price': 2.50,
                                  'stock': 4}},
        }

    def display_menu(self):
        #Display the vending machine menu.
        print("\nVENDING MACHINE MENU:")
        for category, items in self.menu.items():
            print(f"\n CATEGORY: {category}")
            for code, item in items.items():
                print(f"Code: {code} | Name: {item['name']} | Price: ${item['price']:.2f} | Stocks: {item['stock']}")

    def accept_money(self):
        #Accept money input from the user.
        while True:
            try:
                amount = float(input("\nPlease insert money (minimum of $5): $"))
                if amount >= 5:
                    return amount
                else:
                    print("Invalid amount. Kindly enter a minimum amount of $5.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def select_item(self):
        #Allow the user to select an item.
        while True:
            category = input("Kindly input the category code (such as 'SNACKS', 'COLD DRINKS', 'CHOCOLATE', 'BISCUITS'): ").upper()
            if category in self.menu:
                item_code = input(f"Enter the item code for {category}: ").upper()
                if item_code in self.menu[category]:
                    return category, item_code
                else:
                    print("Invalid item code. Please enter a valid code.")
            else:
                print("Invalid category. Please enter a valid category.")

    def dispense_item(self, category, item_code, amount_inserted):
        #Dispense the selected item if it's available.
        item = self.menu[category][item_code]
        if item['stock'] > 0 and amount_inserted >= item['price']:
            print(f"\n=============== PLEASE WAIT ===============")
            print(f"Dispensing {item['name']} ......")
            item['stock'] -= 1
            change = amount_inserted - item['price']
            print(f"\nYour change is ${change:.2f}")
        elif item['stock'] == 0:
            print(f"Sorry, {item['name']} is out of stock.")
        else:
            print("Insufficient funds. Please insert more money.")

    def suggest_purchase(self, category):
        #Suggest additional purchases based on the category.
        if category == 'COLD DRINKS':
            print("Consider adding a snack, chocolate, or biscuits to your purchase.")
        elif category == 'CHOCOLATE':
            print("Consider enhancing the item you purchased with some cold drinks, snack, or a biscuits.")
        elif category == 'SNACKS':
            print("Think about matching what you bought with some chocolate, cold drinks, or biscuits.")
        elif category == 'BISCUITS':
            print("Try combining your purchases with some chocolate, cold drinks, or snacks.")

    def vending_process(self):
        #Perform the vending process.
        self.display_menu()

        while True:
            amount_inserted = self.accept_money()
            category, item_code = self.select_item()
            self.dispense_item(category, item_code, amount_inserted)
            self.suggest_purchase(category)

            another_purchase = input("Would you like to make additional purchases? (yes/no): ").lower()
            if another_purchase != 'yes':
                print("""

 /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$ /$$   /$$       /$$     /$$ /$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$  /$$$$$$$        /$$   /$$  /$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$       
|__  $$__/| $$  | $$ /$$__  $$| $$$ | $$| $$  /$$/      |  $$   /$$//$$__  $$| $$  | $$      | $$_____//$$__  $$| $$__  $$      | $$  | $$ /$$__  $$|_  $$_/| $$$ | $$ /$$__  $$      
   | $$   | $$  | $$| $$  \ $$| $$$$| $$| $$ /$$/        \  $$ /$$/| $$  \ $$| $$  | $$      | $$     | $$  \ $$| $$  \ $$      | $$  | $$| $$  \__/  | $$  | $$$$| $$| $$  \__/      
   | $$   | $$$$$$$$| $$$$$$$$| $$ $$ $$| $$$$$/          \  $$$$/ | $$  | $$| $$  | $$      | $$$$$  | $$  | $$| $$$$$$$/      | $$  | $$|  $$$$$$   | $$  | $$ $$ $$| $$ /$$$$      
   | $$   | $$__  $$| $$__  $$| $$  $$$$| $$  $$           \  $$/  | $$  | $$| $$  | $$      | $$__/  | $$  | $$| $$__  $$      | $$  | $$ \____  $$  | $$  | $$  $$$$| $$|_  $$      
   | $$   | $$  | $$| $$  | $$| $$\  $$$| $$\  $$           | $$   | $$  | $$| $$  | $$      | $$     | $$  | $$| $$  \ $$      | $$  | $$ /$$  \ $$  | $$  | $$\  $$$| $$  \ $$      
   | $$   | $$  | $$| $$  | $$| $$ \  $$| $$ \  $$          | $$   |  $$$$$$/|  $$$$$$/      | $$     |  $$$$$$/| $$  | $$      |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/      
   |__/   |__/  |__/|__/  |__/|__/  \__/|__/  \__/          |__/    \______/  \______/       |__/      \______/ |__/  |__/       \______/  \______/ |______/|__/  \__/ \______/       
                                                                                                                                                                                      
        
         __      _______ ____  _   _          _  _____  __      ________ _   _ _____ _____ _   _  _____   __  __          _____ _    _ _____ _   _ ______ 
        /\ \    / /_   _/ __ \| \ | |   /\   ( )/ ____| \ \    / /  ____| \ | |  __ \_   _| \ | |/ ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
       /  \ \  / /  | || |  | |  \| |  /  \  |/| (___    \ \  / /| |__  |  \| | |  | || | |  \| | |  __  | \  / |  /  \ | |    | |__| | | | |  \| | |__   
      / /\ \ \/ /   | || |  | | . ` | / /\ \    \___ \    \ \/ / |  __| | . ` | |  | || | | . ` | | |_ | | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
     / ____ \  /   _| || |__| | |\  |/ ____ \   ____) |    \  /  | |____| |\  | |__| || |_| |\  | |__| | | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
    /_/    \_\/   |_____\____/|_| \_/_/    \_\ |_____/      \/   |______|_| \_|_____/_____|_| \_|\_____| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|                                                                                                                                                                  
 """)
                print("................................................................... SENDING YOU GOOD VIBES FOR A FANTASTIC DAY! ....................................................................\n")
                break

            
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.vending_process()


    





