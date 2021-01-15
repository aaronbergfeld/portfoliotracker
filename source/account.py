class Account:
    def __init__(self, starting_capital, risk_per_trade):
        self.capital = starting_capital
        self.risk = risk_per_trade
        
    def enter_change(self, change_amount):
        self.capital += change_amount
    
    def set_value(self, new_value):
        self.capital = new_value
        
    def info(self):
        print(f"Capital: {self.capital}\n")