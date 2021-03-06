import getpass
import re


def merge_description(li, str=''):
    for i in range(len(li)):
        str = str+'_'+li[i]
    return str[1:]


def final_li(all_result_list, splitstr, tc_list, tc_full_list):
    for item in all_result_list:
        tc_list.append(item[len(splitstr):])
    none_preconditioncode = []
    for i in tc_list:
        if len(i.split(splitstr)) < 5:
            print('>>> Dump: %s\n      Reason: Route too short' % (i))
        elif '#' in i:
            print('>>> Dump: %s\n      Reason: Manually Abandoned' % (i))
        else:
            tmpli = []

            # 功能路径
            tc_funcpath = i.split(splitstr)[:1]
            # 功能点
            tc_point = i.split(splitstr)[1:2]
            # 功能说明
            tc_description = i.split(splitstr)[2:-3]
            # 来源
            tc_source = '需求文档'
            # 前置条件
            try:
                tc_preconditions = i.split(splitstr)[-3]
            except IndexError as e:
                print(e)
            # 匹配单个大写或小写字母、一个或两个数字、一个字母和一个数字组合、一个数字和字母组合
            if re.match('^[a-zA-Z]{1}$|^[0-9]{1,2}$|^[a-zA-z]{1}[0-9]{1}$|^[0-9]{1}[a-zA-z]{1}$', i.split(splitstr)[-3]):
                if len(i.split(splitstr)[-3]) < 2:
                    tc_preconditions = '%s0数据准备：无' % (i.split(splitstr)[-3])
                else:
                    tc_preconditions = '%s数据准备：无' % (i.split(splitstr)[-3])
            # elif i.split(splitstr)[-3] == '无':
            #     tc_preconditions = '数据准备：无'
            else:
                tc_preconditions = '数据准备：%s' % (i.split(splitstr)[-3])
            # input
            tc_input = 'input: %s' % (i.split(splitstr)[-2])
            # output
            tc_output = 'output: %s' % (i.split(splitstr)[-1])
            # 用例级别
            # TODO 获取脑图中的用例级别
            tc_level = '0级'
            # 用例责任人
            tc_tester = getpass.getuser()
            # 适用版本
            tc_version = 'v3.0'

            tmpli.append(tc_funcpath[0])
            tmpli.append(tc_point[0])
            tmpli.append(merge_description(tc_description))
            tmpli.append(tc_source)
            tmpli.append(tc_preconditions)
            tmpli.append(tc_input)
            tmpli.append(tc_output)
            tmpli.append(tc_level)
            tmpli.append(tc_tester)
            tmpli.append(tc_version)

            tc_full_list.append(tmpli)

    return tc_full_list
