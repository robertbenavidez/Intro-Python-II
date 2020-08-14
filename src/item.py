class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item: {self.name}\nDescription: {self.description}"

    def on_take(self):
        return f"You grabbed a {self.name}"

    def on_drop(self):
        return f"You dropped a {self.name}"
