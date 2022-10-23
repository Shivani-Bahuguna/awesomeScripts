import PyPDF2

pdf_path = "./sample.pdf"

pdfFileObj=open(pdf_path,'rb') 

pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
 
num = pdfReader.numPages
for i in range(num):
	pageObj=pdfReader.getPage(i) 
	text=pageObj.extractText()
	file1=open(pdf_path[:-4]+".txt","a")
	file1.writelines(text)
	file1.writelines("\n\n")