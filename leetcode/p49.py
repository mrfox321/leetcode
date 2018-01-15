def primes():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    hashmap = {}
    for index,char in enumerate(alphabet):
        hashmap[char] = primes[index]
    return hashmap

def wordMap(word,hashmap):
    count = 1
    for char in word:
        count *= hashmap[char]
    return count

def groupMap(strings):
    hashmap = primes()
    group = {}
    for word in strings:
        maps = wordMap(word,hashmap)
        if maps in group:
            group[maps].append(word)
        else:
            group[maps] = [word]

    list_of_groups = [value for value in group.itervalues()]
    return list_of_groups

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

print groupMap(strings)
