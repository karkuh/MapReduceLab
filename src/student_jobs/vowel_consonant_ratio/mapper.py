import re
from src.core.job.mapper import Mapper

VOWELS_UA = "аеєиіїоуюя"
CONSONANTS_UA = "бвгґджзйклмнпрстфхцчшщ"

VOWELS_EN = "aeiouy"
CONSONANTS_EN = "bcdfghjklmnpqrstvwxyz"

ALL_VOWELS = VOWELS_UA + VOWELS_EN
ALL_CONSONANTS = CONSONANTS_UA + CONSONANTS_EN

class VowelConsonantRatioMapper(Mapper):
    def map(self, record, emit):
        cleaned_record = re.sub(r'[^\w\s]', '', str(record))
        
        for token in cleaned_record.lower().split():
            if not token:
                continue
                
            vowels_count = 0
            consonants_count = 0
            
            for char in token:
                if char in ALL_VOWELS:
                    vowels_count += 1
                elif char in ALL_CONSONANTS:
                    consonants_count += 1
            
            if vowels_count > 0 or consonants_count > 0:
                emit(len(token), (vowels_count, consonants_count))