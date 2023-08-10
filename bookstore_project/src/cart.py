class Cart:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cart, cls).__new__(cls)
            cls._instance.items = []  # Initialize items list here
        return cls._instance

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)
