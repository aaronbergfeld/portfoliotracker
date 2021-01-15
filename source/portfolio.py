from source.position import Position

class Portfolio:
    def __init__(self, portfolio = {}):
        self.portfolio = portfolio
        
    def add_position(self, pos: Position):
        self.portfolio[pos.ticker] = pos
        
    def close_position(self, symbol, close_price, shares_bought):
        stock = self.portfolio[symbol]
        if not stock:
            print("This is not in your portfolio")
        elif stock.closed:
            print("Position Has Already Been Closed")
        else:
            roi = (close_price - stock.buy_price) * shares_bought
            stock.account.enter_change(roi)
            self.portfolio.pop(symbol)
            stock.closed = True
        
    def __repr__(self):
        for key in self.portfolio.keys():
            print(self.portfolio[key])
        return ""