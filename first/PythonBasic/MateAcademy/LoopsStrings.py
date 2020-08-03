import math


def same_name(name1, name2):
    if name1 == name2:
        return True
    return False


def max_number(name1, name2, name3):
    if name1 > name2 and name1 > name3:
        return name1
    if name2 > name1 and name2 > name3:
        return name2
    if name3 > name1 and name3 > name2:
        return name3
    return "it's Tie"


def append_sum(list):
    for i in range(3):
        list.append(list[-1] + list[-2])

    print(list)


def combine_sort(list1, list2):
    return sorted(list1 + list2)


def every_three_nums(start):
    list = [start]
    count = math.floor((100 - start) / 3)
    for i in range(count):
        start = start + 3
        list.append(start)
    return list


def delete_starting_evens(lst):
    count = None
    for i in lst:
        if i % 2 != 0:
            count = lst.index(i)
            break
    if count is None:
        return "list is empty"
    return lst[count:]


def unique_english_letters(word):
    return len(set(word))


def count_char_x(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
    return count


def count_multi_char_x(string, substring):
    return string.count(substring)


def substring_between_letters(word, start, end):
    if (not word.__contains__(start)) or (not word.__contains__(end)):
        return word
    return word[word.index(start) + 1:word.index(end)]


def x_length_words(sent, count):
    return all(len(i) >= count for i in sent.split())


# print(same_name("Colby", "Colbu"))
# print(max_number(3, 3, 3))
# print(combine_sort([1, 3, 7], [2, 4, 5]))
# print(every_three_nums(25))
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(unique_english_letters("mississippi"))
# print(count_char_x("mississippi", 'm'))
# print(count_multi_char_x("mississippi", 'iss'))
# print(substring_between_letters("apple", "p", "e"))
print(x_length_words("I likes apples", 2))
