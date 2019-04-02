import re

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






for i in bib_list:
    for j in i:
        print(j, '=', i[j])
    break;

