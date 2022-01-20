import json
from collections import OrderedDict

data = OrderedDict()
data['key'] = 'w91CC6XKX5C3vgOonc8ZN+udXJehNQLYRtMbpuDf8wWgPXPhrB25+2uoYanXzArao/m4Ldi7yNqgiQY4IuA7PQ=='
with open('protectKey/key.json','w',encoding='utf-8') as file:
    json.dump(data, file, indent='\t')