import xlwt
import re
from collections import Counter
from core.util import exit_with_anykey


def write_tc_template(sheet, tcname):

    style_merge = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style_merge.alignment = al

    font_merge = xlwt.Font()
    font_merge.name = '宋体'
    font_merge.bold = True
    font_merge.height = 320
    style_merge.font = font_merge

    style_headline = xlwt.XFStyle()

    al_headline = xlwt.Alignment()
    al_headline.horz = 0x02      # 设置水平居中
    al_headline.vert = 0x01      # 设置垂直居中

    style_headline.alignment = al_headline

    font_headline = xlwt.Font()
    font_headline.name = '宋体'
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
    each_width = [18, 12, 23, 10, 40, 40, 10, 12,
                  10, 16, 12, 14, 10, 10, 10]
    for i in range(14):
        sheet.col(i).width = 256 * int(round(each_width[i], 0))

    sheet.row(0).set_style(xlwt.easyxf('font:height 480'))
    sheet.row(1).set_style(xlwt.easyxf('font:height 420'))


def create_sheet():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('testcase', cell_overwrite_ok=True)
    return workbook, worksheet


def save_workbook(workbook, savepath):
    try:
        workbook.save(savepath)
    except PermissionError as e:
        print('>>> File save failed, close .xls file and retry...')
        print('      %s' % (e))


def get_vaild_index(all_list, vaild_list_index):
    for i in range(len(all_list)):
        if all_list[i] == all_list[i-1] and i != 0:
            pass
        else:
            vaild_list_index.append(
                all_list.index(all_list[i]))
    return vaild_list_index


def write_merge_cell(worksheet, vaild_index_list, li, col, style, start_r=[], end_r=[]):

    start_r = vaild_index_list
    end_r = vaild_index_list[1:]
    end_r.append(len(li))

    for i in range(len(vaild_index_list)):
        if len(vaild_index_list) == 1:
            worksheet.write_merge(2, len(li)+1, col, col,
                                  li[vaild_index_list[0]], style)
        else:
            # try:
            worksheet.write_merge(2+start_r[i], 1+end_r[i], col, col,
                                  li[vaild_index_list[i]], style)
            # except AssertionError as e:
            #     print('>>> Abord!\n      Reason: Write merge cell failed.')
            #     exit_with_anykey()


def write_cell(li, worksheet):
    tc_funcpath_li = []
    tc_point_li = []
    tc_description_li = []
    tc_source_li = []
    tc_preconditions_li = []
    tc_input_li = []
    tc_output_li = []
    tc_level_li = []
    tc_tester_li = []
    tc_version_li = []

    for x in range(len(li)):
        for y in range(1):
            tc_funcpath_li.append(li[x][0])
            tc_point_li.append(li[x][1])
            tc_description_li.append(li[x][2])
            tc_source_li.append(li[x][3])
            tc_preconditions_li.append(li[x][4])
            tc_input_li.append(li[x][5])
            tc_output_li.append(li[x][6])
            tc_level_li.append(li[x][7])
            tc_tester_li.append(li[x][8])
            tc_version_li.append(li[x][9])

    vaild_tc_preconditions_index = []

    vaild_tc_preconditions_index = get_vaild_index(
        tc_preconditions_li, vaild_tc_preconditions_index)

    for i in range(len(vaild_tc_preconditions_index)):
        tc_funcpath_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_funcpath_li[vaild_tc_preconditions_index[i]+i])
        tc_point_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_point_li[vaild_tc_preconditions_index[i]+i])
        tc_description_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_description_li[vaild_tc_preconditions_index[i]+i])
        tc_source_li.insert(
            vaild_tc_preconditions_index[i]+i, '')
        tc_input_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_preconditions_li[vaild_tc_preconditions_index[i]])
        tc_output_li.insert(
            vaild_tc_preconditions_index[i]+i, '')
        tc_level_li.insert(
            vaild_tc_preconditions_index[i]+i, '')
        tc_tester_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_tester_li[vaild_tc_preconditions_index[i]+i])
        tc_version_li.insert(
            vaild_tc_preconditions_index[i]+i, tc_version_li[vaild_tc_preconditions_index[i]+i])
    # 合并行单元格样式
    style_mergerow = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

    al_mergerow = xlwt.Alignment()
    al_mergerow.horz = 0x02      # 设置水平居中
    al_mergerow.vert = 0x01      # 设置垂直居中
    style_mergerow.alignment = al_mergerow
    style_mergerow.alignment.wrap = 1

    font_mergerow = xlwt.Font()
    font_mergerow.name = '宋体'
    style_mergerow.font = font_mergerow
    # 普通单元格样式
    style_normal_cell = xlwt.XFStyle()

    al_normal_cell = xlwt.Alignment()
    # al_mergecol.horz = 0x02      # 设置水平居中
    al_normal_cell.vert = 0x01      # 设置垂直居中
    style_normal_cell.alignment = al_normal_cell
    style_normal_cell.alignment.wrap = 1

    font_normal_cell = xlwt.Font()
    font_normal_cell.name = '宋体'
    style_normal_cell.font = font_normal_cell
    # 合并列单元格样式
    style_mergecol = xlwt.XFStyle()

    al_mergecol = xlwt.Alignment()
    al_mergecol.horz = 0x02      # 设置水平居中
    al_mergecol.vert = 0x01      # 设置垂直居中
    style_mergecol.alignment = al_mergecol
    style_mergecol.alignment.wrap = 1

    font_mergecol = xlwt.Font()
    font_mergecol.name = '宋体'
    # font_mergecol.bold=True
    style_mergecol.font = font_mergecol

    pattern_mergecol = xlwt.Pattern()
    pattern_mergecol.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern_mergecol.pattern_fore_colour = xlwt.Style.colour_map['gray25']

    style_mergecol.pattern = pattern_mergecol

    for i in range(len(tc_input_li)):
        worksheet.write(i+2, 3, tc_source_li[i], style_normal_cell)
        worksheet.write(i+2, 4, tc_input_li[i], style_normal_cell)
        worksheet.write(i+2, 5, tc_output_li[i], style_normal_cell)
        worksheet.write(i+2, 6, tc_level_li[i], style_normal_cell)
        worksheet.write(i+2, 7, tc_tester_li[i], style_normal_cell)
        worksheet.write(i+2, 8, tc_version_li[i], style_normal_cell)

    vaild_tc_funcpath_index = []
    vaild_tc_point_index = []
    vaild_tc_description_index = []

    vaild_tc_funcpath_index = get_vaild_index(
        tc_funcpath_li, vaild_tc_funcpath_index)
    vaild_tc_point_index = get_vaild_index(tc_point_li, vaild_tc_point_index)
    vaild_tc_description_index = get_vaild_index(
        tc_description_li, vaild_tc_description_index)

    try:
        write_merge_cell(worksheet, vaild_tc_funcpath_index,
                         tc_funcpath_li, 0, style_mergerow)
    except AssertionError:
        print('>>> Abord!\n      Reason: There may be repetitions in "tc_funcpath".')
        # check_repetition(tc_funcpath_li, vaild_tc_funcpath_index)
        exit_with_anykey()

    # TODO 优化提示，显示出有多少个重复元素，分别是什么。根据下标，创建一个新列表，对列表元素进行排查
    try:
        write_merge_cell(worksheet, vaild_tc_point_index,
                         tc_point_li, 1, style_mergerow)
    except AssertionError:
        print('>>> Abord!\n      Reason: There may be repetitions in "tc_point".')
        # check_repetition(tc_point_li, vaild_tc_point_index)
        # print(vaild_tc_point_index)
        # print(tc_point_li)
        exit_with_anykey()

    try:
        write_merge_cell(worksheet, vaild_tc_description_index,
                         tc_description_li, 2, style_mergerow)
    except AssertionError:
        print('>>> Abord!\n      Reason: There may be repetitions in "tc_description".')
        # print(check_repetition(tc_description_li, vaild_tc_description_index))
        exit_with_anykey()

    for i in range(len(vaild_tc_preconditions_index)):

        if re.match('^[a-zA-Z]{1}$|^[0-9]{1,2}$|^[a-zA-z]{1}[0-9]{1}$|^[0-9]{1}[a-zA-z]{1}$', tc_preconditions_li[vaild_tc_preconditions_index[i]][:2]):
            # TODO 如果使用了重复的标识，增加提示，可能会导致输出excel格式混乱，显示具体哪个标识重复
            worksheet.write_merge(2+vaild_tc_preconditions_index[i]+i, 2+vaild_tc_preconditions_index[i] +
                                  i, 4, 5, tc_preconditions_li[vaild_tc_preconditions_index[i]][2:], style_mergecol)
        else:
            worksheet.write_merge(2+vaild_tc_preconditions_index[i]+i, 2+vaild_tc_preconditions_index[i] +
                                  i, 4, 5, tc_preconditions_li[vaild_tc_preconditions_index[i]], style_mergecol)
    for i in range(len(tc_preconditions_li)+len(vaild_tc_preconditions_index)):
        worksheet.row(2+i).set_style(xlwt.easyxf('font:height 400'))


# def check_repetition(li, index):
#     reptition_li = []

#     for i, v in enumerate(li):
#         if i in index:
#             reptition_li.append(v)
#     print(reptition_li)
#     a=['dd','ff','gg','hh','dd']
#     b = dict(Counter(a))
#     print([key for key, value in b.items()if value > 1])  # 只展示重复元素

