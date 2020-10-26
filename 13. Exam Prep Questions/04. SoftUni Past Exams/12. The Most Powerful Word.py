import math

word_strength = 0
max_strength = 0
winner_word = ""

word = input()
while word != "End of words":

    for char in range(len(word)):
        word_strength += ord(word[char])

    if word[0] == 'a' or word[0] == 'A' or word[0] == 'e' or word[0] == 'E' or word[0] == 'i' or word[0] == 'I' or word[0] == 'o' or word[0] == 'O' or word[0] == 'u' or word[0] == 'U' or word[0] == 'y' or word[0] == 'Y':
        word_strength *= len(word)
    else:
        word_strength = math.floor(word_strength / len(word))

    if word_strength > max_strength:
        max_strength = word_strength
        winner_word = word

    word_strength = 0
    word = input()

print(f"The most powerful word is {winner_word} - {max_strength}")