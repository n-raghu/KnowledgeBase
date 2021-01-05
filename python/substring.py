in_str = 'abaaaaaabbcbcbacbababababababababababababcccbbbaaa'
'abaaabaaab cca bcbcbbcbccccb accaacaca ab'


def get_next_pair(start_point, in_str=in_str):
    nuset = set()
    for element in in_str[start_point:]:
        if element in nuset:
            continue
        elif len(nuset) == 2:
            return nuset
        else:
            nuset.add(element)
    return nuset


all_substr_pairs = []
start_point = 0
check_set = get_next_pair(0)

for idx, element in enumerate(in_str):
    if element in check_set:
        continue
    else:
        all_substr_pairs.append(in_str[start_point:idx])
        start_point = idx
        check_set = get_next_pair(start_point)

all_substr_pairs.append(in_str[start_point:])
print(all_substr_pairs)
print(max(all_substr_pairs, key=len))
