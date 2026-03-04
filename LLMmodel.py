from abc import ABC, abstractmethod
class LLMODEL(ABC):
    @abstractmethod
    def genera(self,prompt):
        pass
