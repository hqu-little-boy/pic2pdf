import glob
import fitz
import os


def pic2pdf(pdf_name, pic_floder):
    doc = fitz.open()
    for img in sorted(glob.glob(os.path.join(pic_floder, "*.jpg"))):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档

    # 修订PDF文件名
    if pdf_name.endswith(".pdf"):
        pdf_name += ".pdf"

    # 保存在图片文件夹下
    save_pdf_path = os.path.join(pic_floder, pdf_name)
    if os.path.exists(save_pdf_path):
        os.remove(save_pdf_path)

    doc.save(save_pdf_path)  # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    pic2pdf("软件需求分析报告模板(完整版).pdf", "home/zengwang/Pictures/1730850-[Dschinghis Khan no Tamanegi wa Ore no Yome (Taniguchi-san)] Kimi -Jeanne d'Arc- ni Naru 2.0 (FateGrand Order) [Chinese] [黎欧x新桥月白日语社] [Digital]")