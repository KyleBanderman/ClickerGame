global id_counter
id_counter = 1

class UpgradeModel:
    def __init__(self, id, counter_amount, amount, purchase_cost = 0):
        self.id = id_counter
        id_counter += 1
        self.counter_amount = counter_amount
        self.amount = amount
        if self.amount == 0:
            self.purchase_cost = 10 ** id
        else:
            self.purchase_cost = purchase_cost
    
    def update_passive_increment():
        passive_increment += counter_amount

    def purchase_new_upgrade():
        amount += 1
        clicker_counter = clicker_counter - purchase_cost
        purchase_cost = purchase_cost * 1.2
        