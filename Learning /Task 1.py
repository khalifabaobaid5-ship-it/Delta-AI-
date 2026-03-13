def is_long_word(word):
    return len(word)>10
input_words = ['cat', 'accomplishment', 'save', "bite"]

for input_word in input_words:
    # print(is_long_word(input_word))
    if is_long_word(input_word):
        print("This is a long word")
    else:
        print("Short")
# print(is_long_word("extraordinary"))
# print(is_long_word("cat"))
# print(is_long_word("accomplishment"))
# print(is_long_word("save"))