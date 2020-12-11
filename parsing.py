import util
import json


def get_xmind_json(filename):
    if len(filename) == 0:
        print('当前路径未找到.xmind文件')
        util.exit_with_anykey()

    xm = util.load_xmind_file(filename)

    json = xm.read('content.json').decode('utf-8')

    return json[1:-1]


def collect(dt, ls=[]):
    for k in dt:
        if k == 'title':
            print(dt[k])
            ls.append(dt[k])
        elif k == 'children':
            for i in dt[k]['attached']:
                if isinstance(dt[k], list):
                    print(dt[k])
                    return collect(dt[k], ls)
                else:
                    return ls


tc_dict = json.loads(get_xmind_json('./test1.xmind'))

root_topic = tc_dict['rootTopic']

# root_title = root_topic['title']

# second_list = root_topic['children']['attached']

# second_title = []

# for i in range(len(second_list)):
#     second_title.append(second_list[i]['title'])

# print(root_title)
# # print(len(root_topic))
# print(second_title)

# print(collect(root_topic))



def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list


    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            # 传入数据的value值是列表或者元组，则调用_get_value
            _get_value(key, value, tmp_list)

    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            # 传入数据的value值是字典，则调用get_target_value
            get_target_value(key, val_, tmp_list)
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身


print(get_target_value('title', root_topic, []))


