import xlwt


def write_tc_template(sheet, tcname):

    style_merge = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style_merge.alignment = al

    font_merge = xlwt.Font()
    font_merge.name='宋体'
    font_merge.bold = True
    font_merge.height = 320
    style_merge.font = font_merge

    style_headline = xlwt.XFStyle()

    al_headline = xlwt.Alignment()
    al_headline.horz = 0x02      # 设置水平居中
    al_headline.vert = 0x01      # 设置垂直居中

    style_headline.alignment = al_headline

    font_headline = xlwt.Font()
    font_headline.name='宋体'
    font_headline.bold = True

    style_headline.font = font_headline

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['ice_blue']

    style_headline.pattern = pattern

    sheet.write_merge(0, 0, 0, 14, '%s测试用例' % (tcname), style_merge)

    header_line = ['功能路径', '功能点', '功能说明', '来源', '', '', '用例级别', '用例责任人',
                   '适用版本', '能否实现自动化', '是否已完成', '自动化用例名', '执行人', '测试结果', '备注']

    for i in range(len(header_line)):
        sheet.write(1, i, header_line[i], style_headline)
    sheet.write_merge(1, 1, 4, 5, '测试点', style_headline)
    each_width = [18, 12, 23, 10, 20, 20, 10, 12,
                  10, 16, 12, 14, 10, 10, 10]
    for i in range(14):
        sheet.col(i).width = 256 * int(round(each_width[i], 0))

    sheet.row(0).set_style(xlwt.easyxf('font:height 480'))
    sheet.row(1).set_style(xlwt.easyxf('font:height 250'))
    

def create_sheet():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('testcase', cell_overwrite_ok=True)
    return workbook, worksheet


def save_workbook(workbook, savepath):
    workbook.save(savepath)


workbook, worksheet = create_sheet()
write_tc_template(worksheet, 'test')

save_workbook(workbook, './eee.xls')
