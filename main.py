import time
from core.listr import final_li
from core.parsing import *
from core.opxls import *


if __name__ == '__main__':
    print('>>>>>>>>>> start parsing')
    start_ticks = time.time()
    file_path = './templ.xmind'
    json_result = get_xm_content_json(file_path)
    xm_root_topic = json_to_dict(json_result)
    all_result_list = []
    tc_list = []
    tc_full_list = []
    splitstr = '_'
    parse_root_topic(xm_root_topic, '', all_result_list, splitstr)
    print('total test case: ', len(all_result_list))

    final_list = final_li(
        all_result_list, tc_list, tc_full_list, splitstr)
    for item in final_list:

        print(item)
    print('>>>>>>>>>> stop parsing')
    print('creating workbook')

    print('writing template')
    # xls.write_tc_template()
    print('writing test case to workbook')
    print('saving')
    print('done')
    end_ticks = time.time()
    print('cost time：', end_ticks - start_ticks, ' ms')
