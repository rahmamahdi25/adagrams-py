from random import randint

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2,
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2,
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
    'Y': 2, 'Z': 1
}

SCORES = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, 
    "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
    }

def draw_letters():
    available_list = []

    for letter, quantity in LETTER_POOL.items():
        for _ in range(quantity):
            available_list.append(letter)

    hand = []
    hand_length = 10

    for _ in range(hand_length):
        current_len = len(available_list)
        random_index = randint(0, current_len - 1)
        letter = available_list.pop(random_index)
        hand.append(letter)
         
    return hand

def uses_available_letters(word, letter_bank):
    copy_list = letter_bank.copy()

    for letter in word.upper():
        if letter in copy_list:
            copy_list.remove(letter)
        else:
            return False

    return True

def score_word(word):
    total_score = 0

    for letter in word.upper():
        total_score += SCORES[letter]

    word_length = len(word)

    if 7 <= word_length <= 10:
        total_score += 8

    return total_score

def get_highest_word_score(word_list):
    highest_word = word_list[0]
    highest_score = score_word(highest_word)

    for word in word_list:
        score = score_word(word)

        if score > highest_score:
            highest_word = word
            highest_score = score

        elif score == highest_score:
            if len(word) == 10 and len(highest_word) != 10:
                highest_word = word
            elif len(highest_word) != 10 and len(word) < len(highest_word):
                highest_word = word

    return (highest_word, highest_score)
