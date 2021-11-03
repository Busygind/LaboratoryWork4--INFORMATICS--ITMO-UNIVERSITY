import xmltodict
import json
import time

start_time = time.time()

xml_file = open('docs/xml_schedule.xml', 'r', encoding='UTF-8')
json_file = open('Additional_task1/json_schedule_2.json', 'w', encoding='UTF-8')

xml_content = xml_file.read()
dict = xmltodict.parse(xml_content, encoding='UTF-8')
print(json.dumps(dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')), file=json_file)

json_file.close()
xml_file.close()

time_file = open('docs/time.txt', 'a')
print('Десятикратное время выполнения программы, в которой использовались библиотеки для парсинга', file=time_file)
print("--- %s seconds ---" % ((time.time() - start_time)*10), file=time_file)
time_file.close()