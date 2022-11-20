word=str(input("enter the word:"))
print(word[::-1])
word=str(input("enter the word:"))
reverse_word=""
for i in word:
    reverse_word=i+reverse_word
print(reverse_word)