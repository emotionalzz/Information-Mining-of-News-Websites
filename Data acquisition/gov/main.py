from openpyxl import WorkBook
#创建工作簿,同时页建一个sheet
wb = WorkBook()
#调用得到的sheet,并命名为test1
ws = wb.active
#active返回的是一个列表

ws.title = 'test1'

#插入数据
ws.append([...])

#保存工作簿,在当前目录下文件名为test1.xlsx
wb.save('test1.xlsx')