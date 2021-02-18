#! /usr/bin/python
import platform;
import os;
list = [];
list2 = [];
x = 0
while True:
	a = input();
	if ((a == "END1") or (a == "END2") or (a == "END") or(a == "END3")):
		if (a == "END2"):
			x = 1;
		if (a == "END3"):
			x = 2;
		break;
	list.append(a);
count = 0;
while True:
	if ((count > 9) or (x == 2)):
		list2.append("{{srcu|" + (list[count])[12:-2] + "|zh|w}}");
	else:
		list2.append(" |user name" + str(count + 1) + "		= " + (list[count])[12:-2]);
	count += 1;	
	if count > len(list) - 1:
		break;
sv = platform.system();
if sv == "Windows":
	os.system("cls");
else:
	os.system("clear");
count = 0;
if (x == 1):
	print("=== " + (list[0])[12:-2] + "@zh.wikipedia ===\n{{CU request\n |status		  = <!--don't change this line-->\n |language code   = zh\n |project shortcut = w\n");
if ((x != 1) and (x != 2)):
	while True:
		print(list2[count]);
		count += 1;
		if(count > len(list) - 1):
			break;
cx = 0;
if x == 2:
	while True:
		print("* ",end="");
		print(list2[cx]);
		cx += 1;
		if cx == len(list2):
			break;
if x == 1:
	#if(len(list) > 10):
	cx = 0;
	while True:
		print(list2[cx]);
		cx += 1;
		if(cx == 10 or cx == len(list2)):
			break;
	if(len(list) > 10):
		print(" |discussion	  = [[:w:zh:Wikipedia:元維基用戶查核請求#" + (list[0])[12:-2] + "]]\n |reason = More users: ");
		while True:
			print("*",end="");
			print(list2[cx]);
			cx += 1;
			if cx == len(list2):
				break;
		print("}}",end = "");
	else:
		print(" |discussion	  = [[:w:zh:Wikipedia:元維基用戶查核請求#" + (list[0])[12:-2] + "]]\n |reason =\n}}");
input();
