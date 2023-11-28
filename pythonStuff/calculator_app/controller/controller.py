from model.model import Model
from view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def button_click(self, caption):
        result = self.model.calculate(caption)
        
        self.view.entry_variable.set(result)
    
    def main(self):
        self.view.main()
