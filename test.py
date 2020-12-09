import os
def get_all_filepath(folder):
    # 获取指定路径下的所有.ass文件
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

print(get_all_filepath('/Users/caosheng/Documents/M2TC'))