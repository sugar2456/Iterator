from abc import ABC, abstractmethod
from app.interface.iterator import Iterator

class Aggredate(ABC):
    @abstractmethod
    def iterator(self) -> Iterator:
        pass