def merge_description(li, str=''):
    for i in range(len(li)):
        str = str+'_'+li[i]
    return str[1:]


def final_li(all_result_list, tc_list, tc_full_list, splitstr):
    for item in all_result_list:
        tc_list.append(item[1:])

    #  TODO 需要对节点数进行判断，除前两级节点外，每条路线应至少包含三个节点，丢弃不符合条件的路线

    for i in tc_list:
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
        tc_preconditions = i.split(splitstr)[-3]
        # input
        tc_input = i.split(splitstr)[-2]
        # output
        tc_output = i.split(splitstr)[-1]
        # 用例级别
        tc_level = '0级'
        # 用例责任人
        tc_tester = ''

        tmpli.append(tc_funcpath[0])
        tmpli.append(tc_point[0])
        tmpli.append(merge_description(tc_description))
        tmpli.append(tc_source)
        tmpli.append(tc_preconditions)
        tmpli.append(tc_input)
        tmpli.append(tc_output)
        tmpli.append(tc_level)
        tmpli.append(tc_tester)

        tc_full_list.append(tmpli)

    return tc_full_list
