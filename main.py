#! /usr/bin/python
import platform;
import os;
list = [];
list2 = [];
while True:
	a = input();
	if a == "END":
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
while True:
	print(list2[count]);
	count += 1;
	if(count > len(list) - 1):
		break;


		
