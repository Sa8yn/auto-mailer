def word_replace():
    str = 'Hey, I\'m Vaibhav. Nice to meet youio.'
    print(str)
    word_to_replace = input('Enter the word to replace:')
    word_to_replace_with = input('Enter the word to replace with:')
    print(str.replace(word_to_replace, word_to_replace_with))
word_replace()