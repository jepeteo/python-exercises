import secrets

def load_wordlist(filename):
    wordlist={}
    with open(filename, 'r') as f:
        for line in f:
            key, word = line.strip().split()
            wordlist[key] = word
    return wordlist

def generate_diceware_number():
    return ''.join(str(secrets.randbelow(6) + 1) for _ in range(5))

def generate_diceware_phrase(word_count, wordlist):
    return ''.join(wordlist[generate_diceware_number()] for _ in range(word_count))

wordlist = load_wordlist("diceware_wordlist.txt")
word_count = int(input("Enter the number of words you want for your password: "))
phrase = generate_diceware_phrase(word_count, wordlist)
print(f'Your password / passphrase is:\n {phrase}')

