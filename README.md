# Cash Register Model

This project implements a `CashRegister` class in Python, simulating basic cash register functionalities such as adding items, applying discounts, and voiding transactions. The model is designed to be extensible and easy to understand.

## Features

- **Add Items**: Incorporate items with their price and quantity into the register, updating the total and transaction history.
- **Apply Discounts**: Apply a percentage-based discount to the total price, with validation to ensure the discount is within a valid range (0-100%).
- **Void Transactions**: Revert the last transaction, adjusting the total and item list accordingly.
- **Transaction History**: Maintain a record of all transactions for auditing and operational purposes.

## Installation

No special installation is required beyond a standard Python 3 environment.

## Usage

To use the `CashRegister` class, simply import it into your Python script and instantiate an object. Below is an example demonstrating its core functionalities:

```python
from cash_register import CashRegister

# Initialize the cash register with an optional discount
register = CashRegister(discount=10) # 10% discount
print(f"Initial discount set to: {register.discount}%")

# Add items to the register
register.add_item("Laptop", 1200.00, 1)
register.add_item("Mouse", 25.00, 2)
print(f"Current items: {register.items}")
print(f"Current total: ${register.total:.2f}")

# Void the last transaction (Mouse)
register.void_last_transaction()
print(f"Total after void: ${register.total:.2f}")
print(f"Items after void: {register.items}")

# Add another item
register.add_item("Keyboard", 75.00, 1)
print(f"Current items: {register.items}")
print(f"Current total: ${register.total:.2f}")

# Apply the discount
register.apply_discount()
print(f"Total after discount: ${register.total:.2f}")
print(f"Items after discount: {register.items}")

# Attempt to set an invalid discount
register.discount = 120 # This will print "Not valid discount"
print(f"Discount after invalid attempt: {register.discount}%")
```

## Code

### `cash_register.py`

```python
class CashRegister:
    """
    A class to represent a cash register system.
    
    Attributes:
        discount (int): Percentage discount to apply (0-100).
        total (float): The current total price of items in the register.
        items (list): A list of item names added to the register.
        previous_transactions (list): A history of transaction objects.
    """

    def __init__(self, discount=0):
        # Initialize _discount to 0 and then use the setter for validation
        self._discount = 0 
        self.discount = discount  # Use setter for validation
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """The discount percentage (0-100)."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Sets the discount with validation, ensuring it's an integer between 0 and 100."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        """
        Adds an item to the cash register, updating the total and transaction history.
        
        Args:
            item (str): Name of the item.
            price (float): Price per unit.
            quantity (int): Number of units.
        """
        item_total = price * quantity
        self.total += item_total
        self.items.append(item)
        
        # Store transaction details including item, price, quantity, and total price for the item
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "total_price": item_total
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """
        Applies the stored discount percentage to the current total.
        
        This method also removes the last transaction from `previous_transactions`
        and the corresponding item from `items` as per requirements.
        If no transactions exist, it prints a message.
        """
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate the discount amount based on the current total
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Remove the last transaction record from the history
        last_transaction = self.previous_transactions.pop()
        
        # Remove the item associated with the last transaction from the items list
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])
            
        # The total is already updated by subtracting the discount_amount.

    def void_last_transaction(self):
        """
        Voids the most recent transaction, reversing its financial and item-list impact.
        
        If no transactions are present, it prints a message.
        """
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        # Retrieve and remove the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the total price of the voided item from the overall total
        self.total -= last_transaction["total_price"]
        
        # Remove the item from the current items list
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])
        
        print(f"Voided last transaction: {last_transaction["item"]}")
```

## Test Output

Below is a screenshot of the test script execution, demonstrating the functionality of the `CashRegister` class:

```
--- Testing CashRegister ---
Initialized with 20% discount. Current discount: 20%

Adding items...
Total: $9.00
Items: ['Apple', 'Milk']

Testing invalid discount (150)...
Not valid discount

Voiding last transaction (Milk)...
Voided last transaction: Milk
Total after void: $6.00
Items after void: ['Apple']

Added Bread. Total: $11.00

Applying 20% discount...
Total after discount: $8.80
Items after apply_discount (should have removed Bread): ['Apple']

Clearing transactions and testing empty discount apply...
There is no discount to apply.
```

## Author

Manus AI
