import re
from src.core.job.mapper import Mapper

class WordCountLongMapper(Mapper):
    def map(self, record, emit):
        cleaned_record = re.sub(r'[^\w\s]', '', str(record))
        
        for token in cleaned_record.lower().split():
            if token and len(token) > 5:
                emit(token, 1)