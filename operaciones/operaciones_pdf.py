from abc import ABC, abstractmethod

class OperationPDF(ABC):
    @abstractmethod
    def ejecutar(self):
        pass