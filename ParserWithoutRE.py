#Option Num = 2
#Parse from XML to JSON
#Понедельник

#Выполнил студент группы P3115 Бусыгин Дмитрий

xml_file = open('main_task.xml', 'r', encoding='UTF-8')
json_file = open('json_schedule.json', 'w', encoding='UTF-8')
print('{', file=json_file)
for string in xml_file:
    text = xml_file.read()
    print(text)
    for elem in text:
        if elem == '<':

print('  ', file=json_file)