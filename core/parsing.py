import zipfile
import json


def get_xm_content_json(xm_file_path):
    """
    读取文件 content.json 的内容
    @param xm_file_path: xmind 文件路径
    @return:
    """
    try:
        xm = zipfile.ZipFile(xm_file_path)
    except FileNotFoundError:
        print('找不到xm文件: ', xm_file_path)
        exit(404)
    except zipfile.BadZipFile:
        print('解析文件失败: ', xm_file_path)
        exit(500)
    else:
        xm_json = xm.read('content.json').decode('utf-8')
        # 取json字符串内容返回，去除多余的方括号 [ ]
        return xm_json[1:-1]


def json_to_dict(json_str):
    """
    json 字符串转 Python dict 对象
    @param json_str: json字符串
    @return:
    """
    dict_ob = json.loads(json_str)
    return dict_ob['rootTopic']


def parse_root_topic(root_topic, custom_title, result_list, splitstr):
    """
    递归遍历 rootTopic
    @param root_topic: rootTopic dict对象
    @param custom_title: 自定义开头内容
    @param result_list: 返回结果集 List
    @return:
    """
    custom_title = custom_title + splitstr + root_topic['title']
    # 三种解决 dict 取值时出现 KeyError 问题: 当 key 不存在时会报错，需要处理
    # 1 异常捕获
    # try:
    #     children = root_topic['children']
    # except BaseException as e:
    #     # print('叶子节点没有children属性')
    #     result_list.append(parent_title)
    # else:
    #     attached_list = children['attached']
    #     for children_dict in attached_list:
    #         parse_root_topic(children_dict, parent_title, result_list)

    # 2 给默认值
    # children = root_topic.get('children', 'none')
    # if children == 'none':
    #     result_list.append(parent_title)
    # else:
    #     attached_list = children['attached']
    #     for children_dict in attached_list:
    #         parse_root_topic(children_dict, parent_title, result_list)

    # 3 提前判断是否存在
    if 'children' in root_topic:
        children = root_topic['children']
        attached_list = children['attached']
        for children_dict in attached_list:
            parse_root_topic(children_dict, custom_title,
                             result_list, splitstr)
    else:
        result_list.append(custom_title)
