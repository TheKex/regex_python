import re


def parse_authors(_str):
    return _str.replace(',', '').replace(' and', ',')


FORMAT_DICT = {
    'Author': '{Author}',
    'Title': ' {Title}',
    'Journal': ' // {Journal}',
    'Year': ' .-  {Year}',
    'Publisher': ' {Publisher}',
    'Address': ' {Address}',
    'Pages': ' .- p  {Pages}',
    'Volume': ' .- vol. {Volume}'
}

bib_parse_exp = r"@(?P<type>\w+)\{(?P<id>[\w.:]+),\n(?P<content>(.*\n*)+?)\}"
content_parse_exp = r"\s+(?P<key>\w+)\s+=\s\{(?P<value>.*)\}"

f = open('biblio.bib', 'r', encoding='utf-8')
data = f.read()
parse_data = re.finditer(bib_parse_exp, data)

bib_list = list()

for item in parse_data:
    tmp = dict()
    tmp['type'] = item['type']
    tmp['id'] = item['id']
    tmp_parse = re.finditer(content_parse_exp, item.group('content'))
    for i in tmp_parse:
        tmp[i['key']] = i['value']
    bib_list.append(tmp)

tmp1 = bib_list[0]
print(tmp1)
tmp_str = ''
for i in FORMAT_DICT:
    if tmp1.get(i):
        tmp_str += FORMAT_DICT[i]
print(tmp_str.format(**tmp1))



#
#
# for i in bib_list:
#     for j in i:
#         if j == 'Author':
#             print(j, '=', parse_authors(i[j]))
#         else:
#             print(j, '=', i[j])
