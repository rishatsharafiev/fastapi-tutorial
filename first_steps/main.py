from typing import Mapping, Set


def f(my_mapping: Mapping[int, str]) -> Set[str]:
    return set(my_mapping.values())


a = f({3: "yes", 4: "no"})
print(a)

for i in range(5):  # this comment has too many spaces
    print(i)
    if True:
        pass
