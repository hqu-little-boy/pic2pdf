#!/usr/bin/python3
# coding=utf-8

# def sort_key(file_name):
#     prefix = '政宗君的复仇 '  # input("输入文件名前缀：")
#     suffix = '集'  # input("输入文件名后缀：")
#     file_key = float(file_name.split(prefix)[1].split(suffix)[0])
#     return file_key

import os

import fitz


# PATH = input()
def get_name(path, prefix, suffix, prefix_exist=True):  # 获取总文件夹中的每话文件夹，以绝对目录的列表返回
    names = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            names.append(name)
    if prefix_exist:  # 如果文件有前缀或后缀
        names.sort(key=lambda x: float((x.replace(prefix, "")).replace(suffix, "")))
    # names.sort(key=sort_key)
    # names.sort(key=lambda x: float(x.split('政宗君的复仇 ')[1].split('集')[0]))
    else:
        names.sort()
    return names


# print(get_name(PATH))
def get_files(path, name):  # 获取每话文件夹中的图片，以绝对目录的列表返回
    pictures = []
    new_path = os.path.join(path, name)
    for file_name in os.listdir(new_path):  # 对文件类型判断
        if not (file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".bmp")):
            continue
        else:
            pictures.append(os.path.join(new_path, file_name))
    pictures.sort()
    return pictures


# def make_pdf(pictures):


# def make_menu():
#     pass

# def make_one_pdf(name, pictures, out_path):  # 每话生成单个pdf
#     # out_path = "./漫画单个输出/"
#     if not os.path.exists(out_path):
#         os.mkdir(out_path)
#     with open(os.path.join(out_path, name + ".pdf"), "wb") as one_pdf:
#         one_pdf.write(img2pdf.convert(pictures))
# return one_pdf

def make_one_pdf(name, pictures, out_path):  # 每话生成单个pdf
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    pdf_one = fitz.open()
    for img in sorted(pictures):  # 读取图片，确保按文件名排序
        # print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        pdf_one.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists(os.path.join(out_path, name + ".pdf")):
        os.remove(os.path.join(out_path, name + ".pdf"))
    pdf_one.save(os.path.join(out_path, name + ".pdf"))  # 保存pdf文件
    pdf_one.close()


# def handle_path():
#     pass


def make_file(path, out_path, prefix, suffix, _bool=False):  # 汇总前面的函数
    # path = input()
    # path = "/home/zengwang/Downloads/新建文件夹/"
    names = get_name(path, prefix, suffix, _bool)
    for name in names:
        pictures = get_files(path, name)
        # print(pictures)
        make_one_pdf(name, pictures, out_path)
    # print(names)


def beep(duration=1, freq=440):  # 提示音，仅linux可用
    # second
    # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))


if __name__ == "__main__":
    variate_prefix = '政宗君的复仇 '  # input("请输入文件前缀：")
    variate_suffix = '集'  # '#input("请输入文件后缀：")
    variate_path = "/home/zeng/lanzouDownloads/《朋友借我》第130plus话/"
    variate_out_path = "./漫画单个输出/"
    make_file(variate_path, variate_out_path, variate_prefix, variate_suffix)
    beep()
