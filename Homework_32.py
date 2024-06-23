import itertools


def all_variants(string):
    temp_list = []
    for i in range(1, len(string) + 1):
        temp_list.append(list(itertools.combinations(string, i)))
    for j in temp_list:
        for k in j:
            if ''.join(k) != 'ac':
                yield ''.join(k)


a = all_variants("abc")
for i in a:
    print(i)
