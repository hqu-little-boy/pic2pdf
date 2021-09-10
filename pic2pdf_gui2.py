#!/usr/bin/python3
# coding=utf-8
import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
import pic2pdf_one
import pic2pdf_merge


class pic2pdf_TK_gui():
    def __init__(self):
        root = tkinter.Tk()
        root.title = "pic2pdf"
        root.geometry("480x640")
        self._bool = False
        self.pic_address_sign = tkinter.Label(root, text="图片总文件夹：")
        self.pic_address_sign.grid(row=0, column=0, sticky=tkinter.W)
        # self.pic_address_sign
        self.pic_address = tkinter.Entry(root)
        self.pic_address.grid(row=0, column=1, columnspan=1, sticky=tkinter.W)
        self.pic_address_btn = tkinter.Button(root, text="选择文件夹")
        self.pic_address_btn.grid(row=0, column=2, sticky=tkinter.W)
        self.pic_address_btn.bind("<Button-1>",
                                  func=self.handler_adaptor(self.print_pic_address, label=self.pic_address))
        self.out_one_pdf_sign = tkinter.Label(root, text="单个pdf输出文件夹：")
        self.out_one_pdf_sign.grid(row=1, column=0, sticky=tkinter.W)
        self.out_one_pdf = tkinter.Entry(root)
        self.out_one_pdf.grid(row=1, column=1, columnspan=1, sticky=tkinter.W)
        self.out_one_btn = tkinter.Button(root, text="选择文件夹")
        self.out_one_btn.bind("<Button-1>", func=self.handler_adaptor(self.print_pic_address, label=self.out_one_pdf))
        self.out_one_btn.grid(row=1, column=2, sticky=tkinter.W)
        #
        self.out_pdf_sign = tkinter.Label(root, text="pdf输出文件名：")
        self.out_pdf_sign.grid(row=2, column=0, sticky=tkinter.W)
        self.out_pdf = tkinter.Entry(root)
        self.out_pdf.grid(row=2, column=1, columnspan=1, sticky=tkinter.W)
        self.prefix_and_suffix_exist = tkinter.Checkbutton(root, text="是否存在前缀", command=self.bool_change)
        self.prefix_and_suffix_exist.grid(row=7, column=0)
        self.prefix_sign = tkinter.Label(root, text="文件前缀：")
        self.prefix_sign.grid(row=3, column=0, sticky=tkinter.W)
        self.prefix = tkinter.Entry(root)
        self.prefix.grid(row=3, column=1, columnspan=1, sticky=tkinter.W)

        self.suffix_sign = tkinter.Label(root, text="文件后缀：")
        self.suffix_sign.grid(row=4, column=0, sticky=tkinter.W)
        self.suffix = tkinter.Entry(root)
        self.suffix.grid(row=4, column=1, columnspan=1, sticky=tkinter.W)
        self.pic2pdf_progressbar = tkinter.ttk.Progressbar(root, mode="indeterminate", maximum=100,
                                                           orient=tkinter.HORIZONTAL)
        self.pic2pdf_progressbar.grid(row=6, column=0)

        self.start_pic2pdf_btn = tkinter.Button(root, text="开始")
        self.start_pic2pdf_btn.bind("<Button-1>", func=self.start_pic2pdf)
        self.start_pic2pdf_btn.grid(row=5, column=2, sticky=tkinter.E)

        root.mainloop()

    def print_pic_address(self, event, label):
        label.delete(0, tkinter.END)
        dir_name = tkinter.filedialog.askdirectory()
        label.insert(0, dir_name)

    def handler_adaptor(self, fun, **kwds):
        """事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧"""
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)
    def bool_change(self):
        self._bool = -self._bool

    def start_pic2pdf(self,event):
        self.pic2pdf_progressbar.start()
        self.pic_address_path = str(self.pic_address.get())
        self.out_one_pdf_path = str(self.out_one_pdf.get())  # + "/"
        # pic2pdf_one.make_file(path, out_path)
        # variate_in_path = out_one_pdf_path
        self.variate_output = str(self.out_pdf.get()) + ".pdf"
        # variate_out_path = "./"
        self.variate_prefix = str(self.prefix.get())
        self.variate_suffix = str(self.suffix.get())
        pic2pdf_one.make_file(self.pic_address_path, self.out_one_pdf_path, self.variate_prefix, self.variate_suffix,
                              self._bool)
        pic2pdf_merge.make_file(self.out_one_pdf_path, self.variate_output, self.variate_prefix, self.variate_suffix,
                                self._bool)
        # print("\a")
        pic2pdf_one.beep()
        self.pic2pdf_progressbar.stop()
        tkinter.messagebox.showinfo(message="pdf文件输出完成")

if __name__ == "__main__":
    GUI = pic2pdf_TK_gui()
    # GUI.geometry("480x640")
    # GUI.mainloop()
