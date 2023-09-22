# def encode_sentence(input_sentence, key):
#     words = input_sentence.split()
#     encoded_words = []

#     for i, word in enumerate(words):
#         if i % 2 == 0:
#             # For words in even positions, reverse the word
#             encoded_word = word[::-1]
#         else:
#             # For words in odd positions, move each letter by the key positions
#             encoded_word = ''.join([chr(ord(letter) + key) for letter in word])

#         encoded_words.append(encoded_word)

#     encoded_sentence = ' '.join(encoded_words)
#     return encoded_sentence

# # Input sentence and key
# input_sentence = "I am the King"
# key = 2

# # Encode the sentence using the given key
# encoded_result = encode_sentence(input_sentence, key)

# print("Encoded Sentence:", encoded_result)


