import time
from core.listr import *
from core.parsing import *
from core.opxls import *
from core.util import *


if __name__ == '__main__':

    print(" ____    ____   _____   _________    ______  ")
    print("|_   \  /   _| / ___ `.|  _   _  | .' ___  | ")
    print("  |   \/   |  |_/___) ||_/ | | \_|/ .'   \_| ")
    print("  | |\  /| |   .'____.'    | |    | |        ")
    print(" _| |_\/_| |_ / /_____    _| |_   \ `.___.'\ ")
    print("|_____||_____||_______|  |_____|   `.____ .' ")
    print("===============ver 0.0.5-beta================\n")

    while True:
        xmpath = input('>>> Enter .xmind file path: ')
        if len(get_all_filepath(xmpath)) == 0:
            print('>>> None .xmind file in this path')
        else:
            print('>>> Found %s .xmind files: %s' %
                  (len(get_all_filepath(xmpath)), get_all_filepath(xmpath)))
            break
    print('---------------------------------------------')
    start_ticks = time.time()
    for xmfile in get_all_filepath(xmpath):
        file_path = xmfile
        print('>>> Reading %s...' % (file_path))
        json_result = get_xm_content_json(file_path)
        xm_root_topic = json_to_dict(json_result)
        all_result_list = []
        tc_list = []
        tc_full_list = []
        splitstr = '-->'
        print('>>> Parsing content.json...')
        parse_root_topic(xm_root_topic, '', all_result_list, splitstr)
        print('>>> Total Routes: %s' % (len(all_result_list)))
        final_list = final_li(all_result_list, splitstr, tc_list, tc_full_list)
        # for item in final_list:
        #     print(item)
        print('>>> Valid Testcases: %s' % (len(final_list)))
        if len(final_list)==0:
            print('>>> None valid Testcases...')
            print('---------------------------------------------')
        else:
            print('>>> Creating workbook...')
            workbook, worksheet = create_sheet()
            print('>>> Writing template...')
            write_tc_template(worksheet, '%s ' % (final_list[0][0]))
            print('>>> Writing test case to workbook...')
            write_cell(final_list, worksheet)
            print('>>> Saving...')
            save_workbook(workbook, '%s.xls' % (xmfile[:-6]))
            print('>>> Done')
            print('---------------------------------------------')
    print('>>> All done')
    end_ticks = time.time()
    print('>>> Time spend: %ss' % round((end_ticks-start_ticks), 4))

    exit_with_anykey()
