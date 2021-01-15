from source.account import *

class Position:
    pass

class Long(Position):
    def __init__(self, ticker, account:Account, buy_price, stop_loss):
        self.ticker = ticker
        self.closed = False
        self.buy_price = buy_price
        self.stop_loss = stop_loss
        self.account = account
        
        self.R = self.buy_price - self.stop_loss  
        self.profit_target = 2*self.R + self.buy_price
        self.reward =  self.profit_target - self.buy_price
        
        self.share_amt = self.account.capital*self.account.risk/self.R
        self.profit2loss = self.reward/self.R
        
        self.position_size = self.share_amt*self.buy_price
        self.potential_profit = self.reward*self.share_amt
    
    def __repr__(self):
        print(f"ticker: {self.ticker}\n\nbuy price: {self.buy_price}\nstop loss: {self.stop_loss}\nprofit target: {self.profit_target}\n\namount of shares: {self.share_amt}\nposition size: {self.position_size}\n\nrisk: {self.R}\nreward: {self.reward}\nprofit/risk: {self.profit2loss}\n\n")
        return ""