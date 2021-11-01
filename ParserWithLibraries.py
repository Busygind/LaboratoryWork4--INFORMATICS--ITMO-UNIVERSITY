import xmltodict
import json

xml_file = open('xml_schedule.xml', 'r', encoding='UTF-8')
json_file = open('json_schedule_2.json', 'w', encoding='UTF-8')

xml_content = xml_file.read()
dict = xmltodict.parse(xml_content, encoding='UTF-8')
print(json.dumps(dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')), file=json_file)
