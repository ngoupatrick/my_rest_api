class WelcomeModel:
    def __init__(self):
        self.message = "Hello World!"
        self.state = False
        self.number = 10
        self.float = 1.76
        self.resultat = 0.0

    def produit(self, quotient):
        self.resultat = self.number*self.float*quotient
