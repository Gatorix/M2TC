import util
import json


def get_xmind_json(filename):
    if len(filename) == 0:
        print('当前路径未找到.xmind文件')
        util.exit_with_anykey()

    xm = util.load_xmind_file(filename)

    json = xm.read('content.json').decode('utf-8')

    return json[1:-1]


# def collect(dt, ls=[]):
#     for k in dt:
#         if k == 'title':
#             ls.append(dt[k])
#         elif k == 'children':
#             if isinstance(dt[k], dict):
#                 return collect(dt[k], ls)
#             else:
#                 return ls




tc_dict = json.loads(get_xmind_json('./test1.xmind'))

root_topic = tc_dict['rootTopic']

root_title = root_topic['title']

second_list = root_topic['children']['attached']

second_title = []

for i in range(len(second_list)):
    second_title.append(second_list[i]['title'])

print(root_title)
# print(len(root_topic))
print(second_title)

print(collect(tc_dict))