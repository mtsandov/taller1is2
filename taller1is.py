

class Item:
    """Represents an item with a name, price, quantity, and category."""

    def __init__(self, name, price, qty):
        """Initializes the item with name, price, quantity, and default category."""
        self.name = name
        self.price = float(price) if isinstance(price, (int, float)) else 0.0
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def get_total(self):
        """Calculates the total price for the item."""
        return self.price * self.qty

    def get_most_prices(self):
        """Calculates a reduced price for the item."""
        return self.price * self.qty * 0.6


class ShoppingCart:
    """Represents a shopping cart containing multiple items and discount logic."""

    def __init__(self):
        """Initializes the shopping cart with default values."""
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Adds an item to the shopping cart."""
        self.items.append(item)

    def calculate_subtotal(self):
        """Calculates the subtotal for all items in the cart."""
        return sum(item.get_total() for item in self.items)

    def apply_discounts(self, subtotal, is_member, has_coupon):
        """Applies member and spending discounts ."""
        if is_member:
            subtotal -= subtotal * self.member_discount
        if subtotal > 100:
            subtotal -= self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Calculates the total cost"""
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member, has_coupon)
        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon:
            total -= total * self.coupon_discount

        return total


def main():
    """functionality of the ShoppingCart and Item classes."""
    cart = ShoppingCart()
    item1 = Item("Apple", 1.5, 10)
    item2 = Item("Banana", 0.5, 5)
    item3 = Item("Laptop", 1000, 1)
    item3.category = "electronics"

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    is_member = True
    has_coupon = True

    total = cart.calculate_total(is_member, has_coupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print(f"The total price is: ${total:.2f}")


if __name__ == "__main__":
    main()
