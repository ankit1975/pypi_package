
class anki:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def show(self):
        return f"My Name is {self.name}"

    def money(self):
        return self.amount + 10
        