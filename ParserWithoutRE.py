#Option Num = 2
#Parse from XML to JSON
#Понедельник

#Выполнил студент группы P3115 Бусыгин Дмитрий

xml_file = open('xml_schedule.xml', 'r', encoding='UTF-8')
xml_lines = xml_file.readlines()

json_file = open('json_schedule_1.json', 'w', encoding='UTF-8')
json_lines = []
print('{', file=json_file)

tabs = 0
tag_names = []
content = []

for i in range(2, len(xml_lines)):
    s = xml_lines[i]
    if s.find('<') == s.find('</'):
        tabs -= 1
    tag_names.append('  ' * tabs + '"' + s[s.find('<')+1:s.find('>')] + '": ')

    if s[s.find('>')+1:s.find('</')] != '':
        content.append('"' + s[s.find('>') + 1:s.find('</')] + '"')
        if xml_lines[i+1].lstrip()[0:2] != '</':
            content[-1] += ','
    elif s.find('<') != -1 and s.find('</') == -1:
        tag_names[-1] += '{'
        content.append(' ')
    elif s.find('<') == s.find('</'):
        tag_names[-1] = '  ' * tabs + '}'
        content.append(' ')
    if '</' not in s:
        tabs += 1

json_text = ''
for i in range(len(tag_names)):
    json_text += tag_names[i] + content[i] + '\n'
    print(tag_names[i] + content[i], file=json_file)

for string in json_text:

print(json_text)

json_file.close()
xml_file.close()