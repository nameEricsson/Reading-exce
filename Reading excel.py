# как считывать данные с таблицы exсel

import openpyxl # подключаем библиотеку, заранее установив ее в настройках

book = openpyxl.open('проект.xlsx', read_only=True)

sheet = book.active #active значит берется первый лист

#sheet_2 = book.worksheets[2] #чтобы считывать второй лист в excel

#cells = sheet['A1':'B6']    создаем кортеж в него записываем  диапазон ячеек которые хотим вывести
#for appliances, cost in cells:
#   print(appliances.value, cost.value)


print(sheet['B2'].value) #можно считывать через номер столбца в excel
print(sheet[2][0].value) #можно считывать при помощи индексов где [строчка] [столбец]

for row in range(1, sheet.max_row + 1): #max_row означает что будет идти до конца по строкам
    appliances = sheet[row][0].value
    cost = sheet[row][1].value
    print(row, appliances, cost)