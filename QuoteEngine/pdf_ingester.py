from typing import List
import subprocess
import os
import random
from PyPDF2 import PdfFileReader
from .ingester_interface import IngesterInterface
from .quote_model import QuoteModel


class PDFIngester(IngesterInterface):
    allowed_extensions = ['pdf']


    def __repr__(self):
        return f'{self}'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')


        tmp = f'/tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        new_quote = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                _quote = QuoteModel(parsed[0], 
                              parsed[1])
                new_quote.append(_quote)

        file_ref.close()
        os.remove(tmp)
        return new_quote