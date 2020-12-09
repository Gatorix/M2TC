import util


filename = util.get_all_filepath('./')


def get_xmind_json(filename):
    if len(filename) == 0:
        print('当前路径未找到.xmind文件')
        util.exit_with_anykey()

    xm = util.load_xmind_file(filename)

    json = xm.read('content.json').decode('utf-8')

    return json


print(get_xmind_json(filename[0]))

