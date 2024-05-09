from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass
    
class Kucing(Hewan):
    def suara(self):
        print("Meow")
        
class Anjing(Hewan):
    def suara(self):
        print("Woof")
        
kucing = Kucing()
kucing.suara()  # output: Meow

anjing = Anjing()
anjing.suara()  # output: Woof

