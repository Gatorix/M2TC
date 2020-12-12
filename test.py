# dt =
# def collect(dt, ls=[]):
#     for k in dt:
#         if k == 'collect':
#             ls.append(dt[k])
#         elif k == 'next':
#             if isinstance(dt[k], dict):
#                 return collect(dt[k], ls)
#             else:
#                 return ls


# # print(collect(dt))


# li = ["['title'],['总账-凭证列表']", "['children'],['attached'],[0],['title'],['新增凭证']", "['children'],['attached'],[0],['children'],['attached'],[0],['title'],['无需数据准备']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['录入1']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['结果1']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[1],['title'],['录入2']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[1],['children'],['attached'],[0],['title'],['结果2']",
#       "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[2],['title'],['录入3']", "['children'],['attached'],[0],['children'],['attached'],[0],['children'],['attached'],[2],['children'],['attached'],[0],['title'],['结果3']", "['children'],['attached'],[1],['title'],['删除凭证']", "['children'],['attached'],[1],['children'],['attached'],[0],['title'],['凭证001、凭证002']", "['children'],['attached'],[1],['children'],['attached'],[0],['children'],['attached'],[0],['title'],['删除']", "['children'],['attached'],[2],['title'],['分支主题 3']", "['children'],['attached'],[2],['titleUnedited'],[True]"]

# print(type(li[0]))
# print(li[0][1:-1])

li = ['q1', 'w1', 'e1']
str = ''


def merge_description(li, str=''):
    for i in range(len(li)):
        str = str+'_'+li[i]
    return str[1:]


str = merge_description(li)

print(str)
