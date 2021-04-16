# 1
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# 2
users_word = (input('Input your word:'))
users_word = users_word.lower()


def is_palindrome(word):
    if len(word) == 1 or len(word) == 0:
        return 0
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return 1


test = is_palindrome(users_word)
if test == 0:
    print("YES")
elif test == 1:
    print("NO")
