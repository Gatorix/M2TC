# dt =
# def collect(dt, ls=[]):
#     for k in dt:
#         if k == 'collect':
#             ls.append(dt[k])
#         elif k == 'next':
#             if isinstance(dt[k], dict):
# #                 return collect(dt[k], ls)
# #             else:
# #                 return ls


# # # print(collect(dt))


# # li = ["['title'],['总账-凭证列表']", "['children'],['attached'],[0],['title'],['新增凭证']", "['children'],['attached'],[0],['children'],['attached'],[0],['title'],['无需数据准备']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['录入1']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['结果1']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[1],['title'],['录入2']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[1],['children'],['attached'],[0],['title'],['结果2']",
# #       "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[2],['title'],['录入3']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[2],['children'],['attached'],[0],['title'],['结果3']", "['children'],['attached'],[1],['title'],['删除凭证']", "['children'],['attached'],[1],['children'],['attached'],[0],['title'],['凭证001、凭证002']", "['children'],['attached'],[1],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['删除']", "['children'],['attached'],[2],['title'],['分支主题 3']", "['children'],['attached'],[2],['titleUnedited'],[True]"]

# # print(type(li[0]))
# # print(li[0][1:-1])

# li = ['q1', 'w1', 'e1']
# str = ''


# def merge_description(li, str=''):
#     for i in range(len(li)):
#         str = str+'_'+li[i]
#     return str[1:]


# str = merge_description(li)

# print(str)
import xlwt
from core.opxls import *


def get_vaild_index(all_list, vaild_list_index):
    for i in range(len(all_list)):
        if all_list[i] == all_list[i-1] and i != 0:
            pass
        else:
            vaild_list_index.append(
                all_list.index(all_list[i]))
    return vaild_list_index


li = [['中心主题', 'a1', 'b1', '需求文档', 'c1', 'd1', 'e1', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', 'b1', '需求文档', 'c1', 'd2', 'e2', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', 'b1_c2', '需求文档', 'd3', 'e3', 'f1', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', 'b1_c2', '需求文档', 'd3', 'e4', 'f2', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', 'b1_c2', '需求文档', 'd3', 'e5', 'f3', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', 'b1_c2', '需求文档', 'd3', 'e6', 'f4', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', '', '需求文档', 'b2', 'c3', 'd4', '0级', 'caosheng', 'v3.0'], [
    '中心主题', 'a1', '', '需求文档', 'b2', 'c4', 'd5', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a1', '', '需求文档', 'b2', 'c5', 'd6', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a2', '', '需求文档', '子主题 3', 'b3', 'c6', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a2', '', '需求文档', '子主题 3', 'b4', 'c7', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a3', 'b5_c8_d7', '需求文档', 'e7', 'f5', 'g1', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a3', 'b5_c8_d7', '需求文档', 'e7', 'f6', 'g2', '0级', 'caosheng', 'v3.0'], ['中心主题', 'a3', 'b5_c8_d7', '需求文档', 'e7', 'f7', 'g3', '0级', 'caosheng', 'v3.0']]
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


workbook, worksheet = create_sheet()

write_tc_template(worksheet, '%s ' % (li[0][0]))

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

for i in range(len(tc_input_li)):
    worksheet.write(i+2, 3, tc_source_li[i])
    worksheet.write(i+2, 4, tc_input_li[i])
    worksheet.write(i+2, 5, tc_output_li[i])
    worksheet.write(i+2, 6, tc_level_li[i])
    worksheet.write(i+2, 7, tc_tester_li[i])
    worksheet.write(i+2, 8, tc_version_li[i])

vaild_tc_funcpath_li = []
vaild_tc_point_li = []
vaild_tc_description_li = []

vaild_tc_funcpath_li = get_vaild_index(tc_funcpath_li, vaild_tc_funcpath_li)
vaild_tc_point_li = get_vaild_index(tc_point_li, vaild_tc_point_li)
vaild_tc_description_li = get_vaild_index(
    tc_description_li, vaild_tc_description_li)

print(vaild_tc_funcpath_li)
print(vaild_tc_point_li)
print(vaild_tc_description_li)


worksheet.write_merge(2, len(tc_funcpath_li)+1, 0, 0,
                      tc_funcpath_li[vaild_tc_point_li[0]])
# TODO 合并写入功能点
# TODO 合并写入功能说明，按来源的空行合并
# TODO 合并前置条件
save_workbook(workbook, '%s.xls' % ('./test22'))
