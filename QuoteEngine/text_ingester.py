from typing import List
import subprocess
import os
import random
import pdb
from .ingester_interface import IngesterInterface
from .quote_model import QuoteModel

class TextIngester(IngesterInterface):
    allowed_extensions = ['txt']


    def __repr__(self):
        return f'{self}'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        file_ref = open(path, "r")
        new_quote = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                _quote = QuoteModel(parsed[0], 
                              (parsed[1]))
                          
                new_quote.append(_quote)
        file_ref.close()
        #os.remove(tmp)
        return new_quote 

        # git log --after="2018-05-07 00:00" --before="2018-05-07 23:59"

 # which release did it go out?

#  (tag: release399)