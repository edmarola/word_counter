def count_word(word: str, word_list: list) -> int:
    head, *tail = word_list
    value = int(head == word) # 1 if appear and 0 if it does not.
    last_item = len(tail) == 0
    return value if last_item else value + count_word(word, tail)

def analyze_sentence(sentence: str) -> list:
    sentence = ''.join(c.lower() for c in sentence if c.isalpha() or c == ' ') # Filter only letters and transform to lower.
    word_list = sentence.split()
    output = [] # [{'word': 'foo', 'counter': 2}]
    for w in word_list:
        if w not in [o['word'] for o in output]:
            output.append({
                'word': w,
                'counter': count_word(w, word_list)
            })

    return output

if __name__ == '__main__':
    # sentence = 'hola como como estas'
    # sentence = 'hola hola como                 estas hola como      como      estas     estas hola   hola como   como      '
    sentence = 'Hi how are      things? how are you?. Are you a developer?   I am  also a  developer'
    # sentence = '  h'
    # sentence = '.1.1. . .1.1. .1. 1.1 ..1 ¡¡  $%$b bb·bbbbb % b ·b /bb%b&/b(%&g/$"·%·aa$&·&$1231 '

    output = analyze_sentence(sentence)

    print(f"Sentence: {sentence} \n")
    for o in output:
        print(f"Word: {o['word']}, appears: {o['counter']} times.")