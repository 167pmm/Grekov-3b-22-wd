def letter_count(str):
    result = {}
    for i in str:
        count = 0
        for j in str:
            if i == j:
                count += 1
            else:
                continue
        result[i] = count
    return result


print(letter_count("Hello world dddd"))