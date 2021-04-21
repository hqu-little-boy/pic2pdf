#!/usr/bin/python3
# coding=utf-8
import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
import pic2pdf_one
import pic2pdf_merge

global pic2pdf_TK_gui, pic_address_sign, pic_address, pic_address_btn, out_one_pdf_sign, \
    out_one_pdf, out_one_btn, out_pdf_sign, out_pdf, prefix_and_suffix_exist, pic2pdf_progressbar, \
    tart_pic2pdf_btn, prefix, prefix_sign, suffix, suffix_sign, _bool, start_pic2pdf_btn


# def open_dir_func():
#     dir_name = tkinter.filedialog.askdirectory()
#     return dir_name

# def my_paste(event):
#     pass
#
def open_dir_func(lei):
    lei.delete(0, tkinter.END)
    dir_name = tkinter.filedialog.askdirectory()
    lei.insert(0, dir_name)


def print_pic_address(event):
    global pic_address
    open_dir_func(pic_address)


def print_out_one_pdf(event):
    global out_one_pdf
    open_dir_func(out_one_pdf)


def bool_change():
    global _bool
    _bool = -_bool


def start_pic2pdf(event):
    global pic2pdf_progressbar, out_pdf, prefix_sign, prefix, suffix_sign, suffix, _bool
    pic2pdf_progressbar.start()
    pic_address_path = str(pic_address.get())
    out_one_pdf_path = str(out_one_pdf.get())  # + "/"
    # pic2pdf_one.make_file(path, out_path)
    # variate_in_path = out_one_pdf_path
    variate_output = str(out_pdf.get()) + ".pdf"
    # variate_out_path = "./"
    variate_prefix = str(prefix.get())
    variate_suffix = str(suffix.get())
    pic2pdf_one.make_file(pic_address_path, out_one_pdf_path, variate_prefix, variate_suffix, _bool)
    pic2pdf_merge.make_file(out_one_pdf_path, variate_output, variate_prefix, variate_suffix, _bool)
    # print("\a")
    pic2pdf_one.beep()
    pic2pdf_progressbar.stop()
    tkinter.messagebox.showinfo(message="pdf文件输出完成")


def prefix_and_suffix():
    global pic2pdf_TK_gui, prefix_sign, prefix, suffix_sign, suffix
    prefix_sign = tkinter.Label(pic2pdf_TK_gui, text="文件前缀：")
    prefix_sign.grid(row=3, column=0, sticky=tkinter.W)
    prefix = tkinter.Entry(pic2pdf_TK_gui)
    prefix.grid(row=3, column=1, columnspan=1, sticky=tkinter.W)

    suffix_sign = tkinter.Label(pic2pdf_TK_gui, text="文件后缀：")
    suffix_sign.grid(row=4, column=0, sticky=tkinter.W)
    suffix = tkinter.Entry(pic2pdf_TK_gui)
    suffix.grid(row=4, column=1, columnspan=1, sticky=tkinter.W)


def prefix_suffix_exist():
    global pic2pdf_TK_gui
    prefix_and_suffix()


# def print_out_pdf(event):
#     open_dir_func(out_pdf)
def GUI():
    global pic2pdf_TK_gui, pic_address_sign, pic_address, pic_address_btn, out_one_pdf_sign, \
        out_one_pdf, out_one_btn, out_pdf_sign, out_pdf, prefix_and_suffix_exist, pic2pdf_progressbar, \
        start_pic2pdf_btn, prefix_sign, prefix, suffix_sign, suffix, _bool
    _bool = False
    pic2pdf_TK_gui = tkinter.Tk()
    pic2pdf_TK_gui.title("pic2pdf")
    pic2pdf_TK_gui.geometry("480x640")
    # pic2pdf_TK_gui.bind_class("Entry","<Control-V>",my_paste)
    pic_address_sign = tkinter.Label(pic2pdf_TK_gui, text="图片总文件夹：")
    # pic_address_sign.pack(side = tkinter.LEFT,anchor = tkinter.N)
    pic_address_sign.grid(row=0, column=0, sticky=tkinter.W)
    pic_address = tkinter.Entry(pic2pdf_TK_gui)
    # pic_address.pack(side = tkinter.TOP)
    pic_address.grid(row=0, column=1, columnspan=1, sticky=tkinter.W)
    pic_address_btn = tkinter.Button(pic2pdf_TK_gui, text="选择文件夹")
    pic_address_btn.bind("<Button-1>", print_pic_address)
    # get_dir_btn.pack(side = tkinter.RIGHT,anchor = tkinter.N)
    # get_dir_btn.pack()
    pic_address_btn.grid(row=0, column=2, sticky=tkinter.W)

    out_one_pdf_sign = tkinter.Label(pic2pdf_TK_gui, text="单个pdf输出文件夹：")
    out_one_pdf_sign.grid(row=1, column=0, sticky=tkinter.W)
    out_one_pdf = tkinter.Entry(pic2pdf_TK_gui)
    out_one_pdf.grid(row=1, column=1, columnspan=1, sticky=tkinter.W)
    out_one_btn = tkinter.Button(pic2pdf_TK_gui, text="选择文件夹")
    out_one_btn.bind("<Button-1>", print_out_one_pdf)
    out_one_btn.grid(row=1, column=2, sticky=tkinter.W)
    #
    out_pdf_sign = tkinter.Label(pic2pdf_TK_gui, text="pdf输出文件名：")
    out_pdf_sign.grid(row=2, column=0, sticky=tkinter.W)
    out_pdf = tkinter.Entry(pic2pdf_TK_gui)
    out_pdf.grid(row=2, column=1, columnspan=1, sticky=tkinter.W)
    # out_pdf_btn = tkinter.Button(pic2pdf_TK_gui, text="选择文件夹")
    # out_pdf_btn.bind("<Button-1>", print_out_pdf)
    # out_pdf_btn.grid(row=2, column=2, sticky=tkinter.W)
    prefix_and_suffix_exist = tkinter.Checkbutton(pic2pdf_TK_gui, text="是否存在前缀", command=bool_change)
    prefix_and_suffix_exist.grid(row=7, column=0)
    prefix_and_suffix()
    pic2pdf_progressbar = tkinter.ttk.Progressbar(pic2pdf_TK_gui, mode="indeterminate", maximum=100,
                                                  orient=tkinter.HORIZONTAL)
    pic2pdf_progressbar.grid(row=6, column=0)

    start_pic2pdf_btn = tkinter.Button(pic2pdf_TK_gui, text="开始")
    start_pic2pdf_btn.bind("<Button-1>", start_pic2pdf)
    start_pic2pdf_btn.grid(row=5, column=2, sticky=tkinter.E)
    # make_file(variate_in_path, variate_output,variate_prefix,variate_suffix)
    pic2pdf_TK_gui.mainloop()


if __name__ == "__main__":
    GUI()
