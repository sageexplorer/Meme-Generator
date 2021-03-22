from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

class IngesterInterface(ABC):
    """ This is the abstract base class """

    allowed_extensions = []

    @classmethod 
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod 
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:    
        pass 





