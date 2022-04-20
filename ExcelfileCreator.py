#1 python3

import os, json, openpyxl, pyperclip
os.chdir(os.path.realpath(__file__).replace('ExcelfileCreator.py', ''))

input = json.load(open(os.path.join('TriviaDeath2', 'content', 'TDFinalRound.jet'), 'r', encoding='utf-8'))
output = {}
files = {}
for i in range(len(input['content'])):
    data = json.load(open(os.path.join('TriviaDeath2', 'content', 'TDFinalRound', str(input['content'][i]["id"]), 'data.jet'), 'r', encoding='utf-8'))
    output[data['fields'][1]['v']] = input['content'][i]["text"]
    data['fields'][1]['s'] = input['content'][i]["text"]
    print(data)
    data2 = open(os.path.join('TriviaDeath2', 'content', 'TDFinalRound', str(input['content'][i]["id"]), 'data.jet'), 'w', encoding='utf-8')
    json.dump(data, data2)





    
    
# wb = openpyxl.load_workbook(r'.\audioScript.xlsx')
# sheet = wb['Tabelle1']
# count = 1
# for k, v in output.items():
#     sheet['A' + str(count)] = str(k)
#     sheet['C' + str(count)] = v
#     count += 1
# wb.save('newTexts1.xlsx')


