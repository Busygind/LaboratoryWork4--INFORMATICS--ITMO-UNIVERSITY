import xml.etree.ElementTree as ET
import pandas as pd



cols = ["День", "Время и недели", "Место проведения", "Название и преподаватель", "Формат занятия"]
rows = []

# Parsing the XML file
xml_text = ET.parse('docs/xml_schedule.xml')
root = xml_text.getroot()
for schedule in root:
    for day in schedule.findall("day"):
        for lessons in day.findall("lessons"):
            for lesson in lessons.findall("lesson"):
                if (lesson):
                    short_day = lesson.find("short-name-of-day").text
                    time = lesson.find("time-and-weeks").text
                    room = lesson.find("room").text
                    name = lesson.find("name-and-teacher").text
                    format = lesson.find("lesson-format").text

                    rows.append({"День": short_day,
                                 "Время и недели": time,
                                 "Место проведения": room,
                                 "Название и преподаватель": name,
                                 "Формат занятия": format})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('Additional_task4/csv_schedule.csv')