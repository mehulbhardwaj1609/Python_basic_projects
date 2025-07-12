from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = []
n = int(input("Enter the number of PDF files to merge: "))

for i in range(n):
    name = input(f"Enter the name of PDF file {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")    
merger.close()    



