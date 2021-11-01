#Option Num = 2
#Parse from XML to JSON
#Понедельник

#Выполнил студент группы P3115 Бусыгин Дмитрий
def has_only_open_tag(str):
    return (str.find('<') != -1 and str.find('</') == -1)


def is_content_in_line(str):
    return str.find('<') != -1 and str.find('</') != -1 and str.find('</') != str.find('<')


def get_content(str):
    return str[str.find('>') + 1:str.find('</')]


def get_tag(str):
    return str[str.find('<') + 1:str.find('>')]


def find_repitable_tags(str):
    repitable_tags = {}
    for i in range(len(str)):
        tag_name = str[i][str[i].find('<') + 1:str[i].find('>')].strip()
        if str.count(str[i]) != 1 and '</' not in str[i]:
            if tag_name not in repitable_tags:
                repitable_tags[tag_name] = 1
            else:
                repitable_tags[tag_name] += 1
    return repitable_tags


xml_file = open('xml_schedule.xml', 'r', encoding='UTF-8')
xml_lines = xml_file.readlines()

json_file = open('json_schedule_1.json', 'w', encoding='UTF-8')
json_lines = []


tabs = 0 # переменная отвечающая за количество отступов в два пробела

json_lines.append('{') # задаем первую строку как открывающуюся фигурную скобку
tabs += 1              # добавляем отступ

repitable_tags = find_repitable_tags(xml_lines) #находим повторяющиеся теги
used_repitable_tags = [] #массив отвечающий за запоминание использованных повторяющихся тегов

for i in range(2, len(xml_lines)):
    s = xml_lines[i]
    final_line = '  ' * tabs
    #если строка содержит только открывающийся тег, то мы проверяем, является ли он повторяющимся
    #если является, то создаем массив из блоков, а если нет, то просто открываем '{', кроме того если повторяющийся
    #тег уже использовался то заменяем его на '{'
    if has_only_open_tag(s):
        tag_name = get_tag(s)
        if tag_name in repitable_tags and tag_name not in used_repitable_tags:
            json_line = '  ' * tabs + '"' + tag_name + '": [ \n'
            tabs += 1
            json_line += '  '*tabs + '{'
            used_repitable_tags.append(tag_name)
            repitable_tags[tag_name] -= 1
        elif tag_name in used_repitable_tags:
            json_line = '  ' * tabs + '{'
            repitable_tags[tag_name] -= 1
        else:
            json_line = '  ' * tabs + '"' + tag_name + '": {'
        tabs += 1

    #если строка содержит открывающийся и закрывающийся тег, значит в ней расположен контент, заменяем ее на обычную json строку
    #"tag": "text"
    elif is_content_in_line(s):
        tag_name = get_tag(s)
        content_line = get_content(s)
        json_line = '  ' * tabs + '"' + tag_name + '":' + ' "' + content_line.lstrip() + '"'
        #проверяем следующую строку, чтобы понять, нужно ли ставить запятую
        if has_only_open_tag(xml_lines[i+1]) or is_content_in_line(xml_lines[i+1]):
            json_line += ','

    #если тег закрывающий и он один то просто закрываем '}'
    #если тег закрывающий, но закрывает один из повторяющихся тегов, то закрываем его с запятой '},'
    #если тег закрывающий и последний среди повторяющихся тегов то закрываем массив ']'
    else:
        tag_name = s[s.find('/')+1:s.find('>')]
        tabs -= 1
        if tag_name in used_repitable_tags and repitable_tags[tag_name] == 0:
            json_line = '  ' * tabs + '} \n'
            tabs -= 1
            json_line += '  ' * tabs + ']'
        else:
            if tag_name in repitable_tags or (i != len(xml_lines) - 1 and (has_only_open_tag(xml_lines[i+1]) or is_content_in_line(xml_lines[i+1]))):
                json_line = '  ' * tabs + '},'
            else:
                json_line = '  ' * tabs + '}'
    json_lines.append(json_line)

#собираем в единое целое строки json
json_lines.append('}')
for elem in json_lines:
    json_file.write(elem + '\n')

#закрываем открытые файлы
json_file.close()
xml_file.close()