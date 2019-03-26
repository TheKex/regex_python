import re
import timeit

bib_items = r"@(\w+)\{((.*\n)*?)\}"

test_r = r'(@\w+\{(.+\n)+?\})'
avg_time = 0

for i in range(10000):
    time_start = timeit.default_timer()

    f = open('biblio.bib', 'r', encoding='utf-8')

    data = f.read()

    parse_data = re.findall(test_r, data)
    avg_time += timeit.default_timer() - time_start
print(avg_time / 10000)
