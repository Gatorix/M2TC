import xlwt



def write_header_line_trail_balance(sheet):
    header_line = ['功能路径', '功能点', '功能说明', '来源', '测试点', '用例级别', '用例责任人',
                   '适用版本', '能否实现自动化', '是否已完成', '自动化用例名', '执行人', '测试结果', '备注']
    for i in range(len(header_line)):
        sheet.write(0, i, header_line[i])


