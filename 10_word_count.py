import re
import collections

def count_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word  in all_words]
        print(f'The total words of this file are: {len(all_words)}')
        
        word_counts = collections.Counter(all_words)
        
        print('\n --- --- --- --- \n Top 20 Words\n')
        for word in word_counts.most_common(20):
            print(f'{word[0]} \t {word[1]}')
            
count_words("shakespear.txt")