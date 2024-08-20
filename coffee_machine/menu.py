class MenuItem:
    """
    Models the menu item i-e coffee, espresso, latte. These items will be created from this class.
    """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "milk" : milk,
            "coffee" : coffee
        }
        pass