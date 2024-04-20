def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_sentence = ' '.join(words[word] if word in words else word for word in sentence.split())
    return translated_sentence

print(translate("el gato esta en la casa"))
