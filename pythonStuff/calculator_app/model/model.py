class Model:
    def __init__(self):
        self.value = ""
        self.operator = ""
        self.previous_value = ""
    
    def calculate(self, caption):
        if caption == "C":
            self.value = ""
            self.previous_value = ""
            self.operator = ""
        
        elif caption == "+/-":
            self.value = str(int(self.value) * (-1))
        
        elif caption == "%":
            pass
        
        elif caption == "=":
            value = self._evaluate()
            
            if ".0" in str(value):
                value = int(value)
            
            self.value = str(value)
        
        elif caption == ".":
            if not caption in self.value:
                self.value += caption
        
        elif isinstance(caption, int):
            self.value += str(caption)
        
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ""
        
        return self.value
    
    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)