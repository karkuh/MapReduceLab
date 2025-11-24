from src.core.job.reducer import Reducer

class VowelConsonantRatioReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0
        
        for v_count, c_count in values:
            total_vowels += v_count
            total_consonants += c_count
            
        total_chars = total_vowels + total_consonants
        
        if total_chars == 0:
            emit(key, "0.0% голосних, 0.0% приголосних")
            return
            
        vowel_percent = (total_vowels / total_chars) * 100
        consonant_percent = (total_consonants / total_chars) * 100
        
        result_string = f"{vowel_percent:.1f}% голосних, {consonant_percent:.1f}% приголосних"
        
        emit(key, result_string)