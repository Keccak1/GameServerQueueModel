from abc import ABC, abstractmethod
from json import dumps

class GameElement(ABC):

    @abstractmethod
    def to_dict(self):
        pass

        


    



    
