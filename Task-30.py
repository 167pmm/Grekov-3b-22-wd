def letter_count(str):
    vowels = "аеёиоуыэюя"
    vowels_count = 0
    consonants_count = 0
    for index in str:
        if index.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    return [vowels_count, consonants_count]


print(letter_count('ПрИвет МиР'))