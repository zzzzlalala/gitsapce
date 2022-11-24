import os
import shutil


def update_control(filePath, control_characters, all_extend):
    files = os.listdir(filePath)
    for file in files:
        oldpath = os.path.join(filePath, file)
        file_name, file_extend = os.path.splitext(file)
        for file_extend in all_extend:
            for i in control_characters:
                new_name = file_name  +file_extend + i  # 在文件名的最后加上
                # new_name = file_name + file_extend + i  # 在文件后缀名的最后加上
                newpath = os.path.join(filePath, new_name)
                shutil.copy(oldpath, newpath)


if __name__ == '__main__':
    # 这是你需要修改文件的路径地址
    # 在路径下放一个.txt 文件运行，根据i的位置确定控制字符的放置位置
    # 路径下会生成57个文件 1 + (1pdf+4word+4xls+5ppt) * 4 , 老版本扫描会扫出56个文件
    filePath = r"E:\workspace\others\zzpython\rename_test\raname_testC"
    control_characters = ['\u200e', '\u200f', '\u202d', '\u202e']

    doc_name = ['.doc', '.docx', '.docm', '.doct']
    xls_name = ['.xls', '.xlsx', '.xlsm', '.xlst']
    ppt_name = ['.ppt', '.pptx', '.pptm', '.potx', '.potm']
    pdf_name = ['.pdf']
    all_new_name = doc_name + xls_name + ppt_name + pdf_name

    old_name = ['.txt', '.db', '.ini', '.pdf']
    zip_name = ['.7z', '.rar', '.zip']
    pic_name = ['.bmp', '.jpg', '.png', '.tif', '.gif']
    mp3_name = ['.mp3', '.wav', '.wma']
    mp4_name = ['.mp4', '.3gp', '.mv4', '.mpg', '.swf', '.avi', '.wmv']

    all_old_name = old_name + zip_name + pic_name + mp4_name + mp3_name

    # update_extend(filePath,doc_name,ppt_name)
    # update_extend(filePath,doc_name,xls_name)
    update_control(filePath, control_characters, all_old_name)
    print([i for i in os.listdir(filePath)])
    print(len([i for i in os.listdir(filePath)]))
