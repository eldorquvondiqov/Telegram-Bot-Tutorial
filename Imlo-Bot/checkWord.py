from uzwords import words
from difflib import get_close_matches as gcm

# print(len(words))
# print(words[0])
# print(words[-1])
# print(words[7777])
# print(words[22222])


# print(gcm('тариҳ', words, n=10))
# print(gcm('муомала', words))


def checkWord(word, words=words):
    word = word.lower()
    matches = set(gcm(word, words))
    available = False #Bunday so'z mavjud emas

    if word in matches:
        available = True
        matches = word

    elif 'ҳ' in word:
        word = word.replace('ҳ', 'x')
        matches.update(gcm(word, words))
    
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(gcm(word, words))

    return {'available':available, 'matches':matches}

if __name__ == '__main__':
    print(checkWord('хато'))
    print(checkWord('олма'))
    print(checkWord('ҳато'))
