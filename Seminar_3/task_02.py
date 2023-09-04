# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр
# символов. За основу возьмите любую статью из википедии или из
# документации к языку.

import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = '''The programming language Python was conceived in the late 1980s,
[1] and its implementation was started in December 1989[2] by Guido van
Rossum at CWI in the Netherlands as a successor to ABC capable of 
exception handling and interfacing with the Amoeba operating system.[3]
Van Rossum is Python's principal author, and his continuing central
role in deciding the direction of Python is reflected in the title
given to him by the Python community, Benevolent Dictator for Life
(BDFL).[4][5] (However, Van Rossum stepped down as leader on
July 12, 2018.[6]). Python was named after the BBC TV show Monty
Python's Flying Circus.[7] Python 2.0 was released on October 16, 2000,
with many major new features, including a cycle-detecting garbage
collector (in addition to reference counting) for memory management and
support for Unicode. However, the most important change was to the
development process itself, with a shift to a more transparent and
community-backed process.[8] Python 3.0, a major, backwards-incompatible
release, was released on December 3, 2008[9] after a long period
of testing. Many of its major features have also been backported
to the backwards-compatible, though now-unsupported, 
Python 2.6 and 2.7.[10]'''


print(top_10_words(text))