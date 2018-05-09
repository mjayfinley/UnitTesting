class Palindrome:
    def __init__(self):
        self.word = []

    def isPalindrome(self,word):
        self.word = self.word.append(word)
        reverse_word = word[::-1]
        if word == reverse_word:
            print("Palindrome")
        else:
            print("Not Palindrome")

test_word = Palindrome()

test_word.isPalindrome('racecar')

#for index in range(len(letters)-1,-1,-1):
#    reversed_word += word[index]
#if word == reversed_word:
#   print("PALINDROME")
#else:
#   print("NOT PALINDROME")
