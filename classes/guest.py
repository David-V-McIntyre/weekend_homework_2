class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def guest_pays_entry_fee(self, room):
        self.wallet -= room.entry_fee
        return self.wallet