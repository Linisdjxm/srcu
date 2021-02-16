#! /usr/bin/python
import platform;
import os;
list = [];
list2 = [];
x = 0
while True:
	a = input();
	if ((a == "END1") or (a == "END2") or (a == "END")):
		if (a == "END2"):
			x = 1
		break;
	list.append(a);
count = 0;
while True:
	if count > 9:
		list2.append("{{srcu|" + (list[count])[12:-2] + "|zh|w}}");
	else:
		list2.append(" |user name" + str(count + 1) + "        = " + (list[count])[12:-2]);
	count += 1;	
	if count > len(list) - 1:
		break;
sv = platform.system()
if sv == "Windows":
	os.system("cls");
else:
	os.system("clear");
count = 0;
if (x == 1):
	print("=== " + (list[0])[12:-2] + "@zh.wikipedia ===\n{{CU request\n |status          = <!--don't change this line-->\n |language code   = zh\n |project shortcut = w\n");
while True:
	print(list2[count]);
	count += 1;
	if(count > len(list) - 1):
		break;
if x == 1:
	print(" |discussion      = [[:w:zh:Wikipedia:元維基用戶查核請求#" + (list[0])[12:-2] + "]]\n |reason =\n}}");
