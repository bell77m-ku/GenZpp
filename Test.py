import random
from faker import Faker

def generate_word_list(num_words):
    fake = Faker()
    word_list = [fake.word() for _ in range(num_words)]
    return word_list

if __name__ == "__main__":
    num_words = int(input("Enter the number of words in the list: "))
    random_word_list = generate_word_list(num_words)
    print("Random Word List:")
    for word in random_word_list:
        print(word)
