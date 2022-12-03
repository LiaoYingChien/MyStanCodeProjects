"""
File: anagram.py
Name: Norah Liao
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print("Welcome to stanCode ''Anagram Generator'' (or -1 to quit)")
    while True:
        s = input("Find anagrams for:")
        if s == '-1':
            break

        start = time.time()

        find_anagrams(s)

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    dic = []
    with open(FILE, "r") as f:
        for line in f:
            dic.append(line.strip())
    return dic


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dic = read_dictionary()
    print("Searching…")
    ans = find_anagrams_helper(s, [], dic, len(s), "", [])
    print(ans)


def find_anagrams_helper(str, current_lst, dic, str_len, current_word, ans_lst):
    if len(current_lst) == str_len:
        # search dic
        if current_word not in ans_lst and current_word in dic:
            ans_lst.append(current_word)
            print(f'Found: {current_word}')
            print("Searching…")
    # elif current_word != "" and len(current_lst) > 3 and has_prefix(current_word) is not True:
    #     pass
    else:
        for i in range(str_len):
            if i not in current_lst:
                # Choose
                current_word += str[i]
                current_lst.append(i)
                # if has_prefix(current_word) is not True:
                #     pass
                # else:
                # Explore
                find_anagrams_helper(str, current_lst, dic, str_len, current_word, ans_lst)
                # Un-choose
                current_word = current_word[:-1]
                current_lst.pop()

    return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    dic = read_dictionary()
    for i in range(len(dic)):
        if dic[i].startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
