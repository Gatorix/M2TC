import xlwt


def write_tc_template(sheet, tcname):

    style_merge = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中

    style_merge.alignment = al

    font_merge = xlwt.Font()
    font_merge.bold = True
    font_merge.height = 320

    style_merge.font = font_merge

    style_headline = xlwt.XFStyle()

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']

    style_headline.pattern = pattern

    sheet.write_merge(0, 0, 0, 13, '%s测试用例' % (tcname), style_merge)
    header_line = ['功能路径', '功能点', '功能说明', '来源', '测试点', '用例级别', '用例责任人',
                   '适用版本', '能否实现自动化', '是否已完成', '自动化用例名', '执行人', '测试结果', '备注']
    for i in range(len(header_line)):
        sheet.write(1, i, header_line[i], style_headline)

    each_width = [18, 12, 23, 10, 40, 10, 12,
                  10, 16, 12, 14, 10, 10, 10]
    for i in range(14):
        sheet.col(i).width = 256 * int(round(each_width[i], 0))

    sheet.row(0).set_style(xlwt.easyxf('font:height 480'))


# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('测试用例')

# write_tc_template(worksheet, 'test')

# workbook.save('./t.xls')
