#!#!/usr/bin/python3
# coding=utf-8
import os
import shutil
import PyPDF2
import pic2pdf_one
import sys

if not sys.warnoptions:  # https://blog.csdn.net/m0_51713294/article/details/112783367
    import warnings

    warnings.simplefilter("ignore")


def remove_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def handle_pdf(in_path, prefix, suffix, prefix_exist=False):  # 处理之前生成的单个pdf
    pdf_comics = []
    for pdf_comic in os.listdir(in_path):
        if not pdf_comic.endswith(".pdf"):
            continue
        else:
            pdf_comics.append(pdf_comic)
    if prefix_exist:
        pdf_comics.sort(key=lambda x: float((x.replace(prefix, "")).replace(suffix + ".pdf", "")))
    # prefix = input("请输入PDF文件前缀：")
    # suffix = input("请输入PDF文件后缀：")
    else:
        pdf_comics.sort()
    # pdf_comics.sort(key=lambda x: float(x.split('政宗君的复仇 ')[1].split('C')[0]))
    return pdf_comics


def merge_pdfs(pdf_comics, in_path):  # 将他们合并
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_comic in pdf_comics:
        pdf_reader = PyPDF2.PdfFileReader(os.path.join(in_path, pdf_comic))
        bookmark_page = pdf_writer.getNumPages()
        # pdf_writer.addBookmark(pdf_comic,Bookmark_page)
        for page in range(pdf_reader.getNumPages()):
            # 把每张PDF页面加入到这个可读取对象中
            pdf_writer.addPage(pdf_reader.getPage(page, ))
        # print(Bookmark_page)
        pdf_writer.addBookmark(pdf_comic, bookmark_page)

    return pdf_writer


def output_pdf(pdf_writer, output):
    # 把这个已合并了的PDF文档存储起来
    # if not os.path.exists(out_path):
    #     os.mkdir(out_path)
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def make_file(in_path, output, prefix, suffix, _bool=False):
    pdf_comics = handle_pdf(in_path, prefix, suffix, _bool)
    pdf_writer = merge_pdfs(pdf_comics, in_path)
    output_pdf(pdf_writer, output)
    remove_folder("./漫画单个输出/")


if __name__ == "__main__":
    variate_path = "/home/zeng/lanzouDownloads/辉夜大_想让我告白"
    variate_out_path = "./漫画单个输出/"
    # pic2pdf_one.make_file(path, out_path)

    variate_in_path = variate_out_path
    variate_output = "辉夜大_想让我告白.pdf"
    # variate_out_path = "./"

    variate_prefix = ' '  # input("请输入PDF文件前缀：")
    variate_suffix = ''  # input("请输入PDF文件后缀：")
    pic2pdf_one.make_file(variate_path, variate_out_path, variate_prefix, variate_suffix)
    make_file(variate_in_path, variate_output, variate_prefix, variate_suffix, False)
    # pic2pdf_one.beep()
