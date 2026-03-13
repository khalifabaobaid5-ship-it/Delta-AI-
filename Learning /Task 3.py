def is_long_word(word):
    return len(word)>10
def contains_a(word):
    return "a" in word 
inputsentence = "the cat accomplished a big jump"
count = 0
for words in inputsentence.split(" "):
    print(words)
    if is_long_word(words) and contains_a(words): count = count +1
print(count)