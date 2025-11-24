import re
from src.core.job.mapper import Mapper

class WordCountCleanMapper(Mapper):
    def map(self, record, emit):
        cleaned_record = re.sub(r'[^\w\s]', '', str(record))
        
        for token in cleaned_record.lower().split():
            if token:
                emit(token, 1)