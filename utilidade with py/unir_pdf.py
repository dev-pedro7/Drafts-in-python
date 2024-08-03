import PyPDF2
import os

merge = PyPDF2.PdfMerger()
lista_pdf = os.listdir('arquivos_pdf')
lista_pdf.sort()
print(lista_pdf)

for arquivo in lista_pdf:
    if '.pdf' in arquivo:
        merge.append(f'arquivos_pdf/{arquivo}')
merge.write('junção.pdf')        