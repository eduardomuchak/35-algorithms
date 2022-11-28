def anagram(word, start, end):
    if start < end:
        pivot = limited_anagram(word, start, end)
        anagram(word, start, pivot - 1)
        anagram(word, pivot + 1, end)


def limited_anagram(word, start, end):
    anagram = word[end]
    limit = start - 1

    for i in range(start, end):
        if word[i] <= anagram:
            limit += 1
            word[limit], word[i] = word[i], word[limit]

    word[limit + 1], word[end] = word[end], word[limit + 1]
    return limit + 1


def is_anagram(first_string, second_string):
    first_word = first_string.lower()
    second_word = second_string.lower()

    first_list = list(first_word)
    second_list = list(second_word)

    anagram(first_list, 0, len(first_list) - 1)
    anagram(second_list, 0, len(second_list) - 1)

    first_sorted = "".join(first_list)
    second_sorted = "".join(second_list)

    if not first_sorted or not second_sorted:
        return (first_sorted, second_sorted, False)

    return (first_sorted, second_sorted, first_sorted == second_sorted)
