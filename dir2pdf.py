# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, re, pyText2pdf
from sys import argv
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def usage():
	print "Usage: %s <directory>" %(argv[0])
	exit(0)

def find(path,dir):
	for i in os.listdir(path)[::-1]:
		if os.path.isfile(path+"/%s"%i):
			file1.append(path+"/%s"%i)
		if os.path.isdir(path+"/%s"%i):
			dir.append(path+"/%s"%i)

def loop(directory,directory2):
	for i in directory:
		find(i,directory2)

def main_loop():
	i=0
	while True:
		directory2.append([])
		loop(directory2[i],directory2[i+1])
		if len(directory2[i+1]) == 0:
			break
		i+=1

def ingredients(list1):
	for i in list1:
		a = re.search("%s/+(.+)$"%argv[1],i)
		if a:
			subdirectory.append(a.groups(1)[0])

def text2pdf_f(i,arg1):
    i.parseArgs(arg1)
    i.Convert()

def getnumpages(c):
	for i in range(0,len(c)-1):
		a = PdfFileReader(open("%s/%s.pdf"%(argv[1],c[i]), "rb"))
		b = a.getNumPages()
		numpages.append(numpages[i]+b)

def merge_pdfs(c):
	merge = PdfFileMerger()

	for i in range(0,len(c)):
		a = open("%s/%s.pdf"%(argv[1],c[i]))
		merge.append(a)

	output = open("output.pdf", "wb")
	merge.write(output)

def clear_pdfs(list1):
	for i in list1:
		os.remove("%s/%s.pdf"%(argv[1],i))

def add_bookmark(list1,list2):
	output = PdfFileWriter()
	input1 = PdfFileReader(open('output.pdf', 'rb'))
	num = input1.getNumPages()
	for i in range(0,num):
		output.addPage(input1.getPage(i))

	for i in range(0,len(list1)):
		output.addBookmark(list1[i], list2[i])
	
	os.remove("output.pdf")
	pdf = open("output.pdf", "wb")
	output.write(pdf)

def make_pdfs():
	files = []
	file_types = {}

	for i in file1:
		a = re.search("%s/.+\.(.+)$"%argv[1],i)
		tmp = []
		if a:
			tmp.append(a.groups(1)[0])
			tmp.append(i)
			files.append(tmp)
			file_types[a.groups(1)[0]] = ""
		else:
			tmp.append("")
			tmp.append(i)
			files.append(tmp)

	for i in files:
		for k in non_plain_text_filetypes:
			if k == i[0]:
				file2.remove(i[1])
				break

	print "This directory contains this file types."
	for i in file_types.keys():
		print i
	print "and this program converts only plain text files. So non plain text files are ignored."
	raw_input("Plase any key to continue ... ")


	for i in range(0,len(file2)):
		to_pdf_ins.append(pyText2pdf.pyText2Pdf())
		arg_list = []
		arg_list.append("%s/pyText2pdf.py"%argv[1])
		arg_list.append("%s"%file2[i])
		text2pdf_f(to_pdf_ins[i],arg_list)
	print "\nFile merging is completed."


def main():
	global file1
	file1 = []
	global file2
	file2 = []
	global directory
	directory = []
	global directory2
	directory2 = []
	directory2.append([])
	global subdirectory
	subdirectory = []
	global	numpages
	numpages = [0,]
	global to_pdf_ins
	to_pdf_ins = []
	global non_plain_text_filetypes
	non_plain_text_filetypes = ["pdf","png","jpg","jpeg","pyc"]

	if not len(argv) == 2:
		usage()

	find(argv[1],directory)
	loop(directory,directory2[0])
	main_loop()
	file2 = file1

	make_pdfs()
	ingredients(file2)

	getnumpages(subdirectory)
	merge_pdfs(subdirectory)
	clear_pdfs(subdirectory)
	add_bookmark(subdirectory,numpages)

if __name__ == '__main__':
	main()
