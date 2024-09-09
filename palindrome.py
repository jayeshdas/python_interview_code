def is_palindrome(word):
    reverse_word=word[::-1]
    return word==reverse_word


word="madama"
if is_palindrome(word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
