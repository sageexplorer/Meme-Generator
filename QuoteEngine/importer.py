from .ingester_interface import IngesterInterface
from .text_ingester import TextIngester
from .docx_ingester import DocxImporter
from .csv_ingetser import CSVImporter
from .pdf_ingester import PDFIngester
from .quote_model import QuoteModel
from typing import List




class Ingester(IngesterInterface):
    """ This class determines the file type, and calls the appropriate helper class """
    importers = [TextIngester, DocxImporter, CSVImporter, PDFIngester]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
            