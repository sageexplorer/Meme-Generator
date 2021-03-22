from typing import List
import pandas

from .ingester_interface import IngesterInterface
from .quote_model import QuoteModel

class CSVImporter(IngesterInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
   
        new_quote = []
        df = pandas.read_csv(path, header=0)
  
        for index, row in df.iterrows():
            _quote = QuoteModel(row['body'], row['author'])
            new_quote.append(_quote)

        return new_quote