# re module 
import re
# json module 
import json
html = ''
dates = []
with open('res.html','r',encoding='utf-8') as f:
    html += f.read()
    f.close()
# 2013-06-23
pattern = re.compile(r"(\d{4}\-\d{2}\-\d{2})?(\d{1}\/\d{2}\/\d{4})?(\d{2}\.\d{2}\.\d{4})?")
matches = pattern.finditer(html)
for item in matches:
   if len(item.group()) > 0:
        if item.group() not in dates:
            print(item.group())
            dates.append(item.group())
with open("final_dates.json",'w',encoding='utf-8') as f:
    json.dump(dates,f,ensure_ascii=False,indent=4)
    f.close()
