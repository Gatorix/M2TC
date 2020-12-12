import os
import sys


def exit_with_anykey_win():
    import msvcrt
    print("按任意键退出...")
    ord(msvcrt.getch())
    os._exit(1)


def exit_with_anykey_mac(msg):

    import termios
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()

    # 获取标准输入(终端)的设置
    old_ttyinfo = termios.tcgetattr(fd)

    # 配置终端
    new_ttyinfo = old_ttyinfo[:]

    # 使用非规范模式(索引3是c_lflag 也就是本地模式)
    new_ttyinfo[3] &= ~termios.ICANON
    # 关闭回显(输入不会被显示)
    new_ttyinfo[3] &= ~termios.ECHO

    # 输出信息
    sys.stdout.write(msg)
    sys.stdout.flush()
    # 使设置生效
    termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    # 从终端读取
    os.read(fd, 7)

    # 还原终端设置
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)


def exit_with_anykey():
    if sys.platform == 'win32':
        exit_with_anykey_win()
    else:
        exit_with_anykey_mac("按任意键退出...")
        sys.exit(0)


# def load_xmind_file(filename):
#     try:
#         xm = zipfile.ZipFile(filename)
#     except zipfile.BadZipFile as e:
#         print('无法解析文件: '+filename)
#         exit_with_anykey()
#     return xm


def get_all_filepath(folder):
    # 获取指定路径下的所有.xmind文件
    file_path = []
    for fpathe, dirs, fs in os.walk(folder):
        for f in fs:
            if '.DS_Store' in os.path.join(fpathe, f):
                pass
            elif os.path.join(fpathe, f)[-6:] != '.xmind':
                pass
            else:
                file_path.append(os.path.join(fpathe, f))
    return file_path
