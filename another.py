#! /usr/bin/python
a = input();
b = input();
count = 0;
t = "";
t2 = [];
while True:
	t += a[count];
	count += 1;
	if count == len(a):
		break;
	if a[count] == b:
		count += 1;
		t2.append("{{checkuser|" + t + "}}");
		t = "";
		if count == len(a):
			break;
count = 0;
while True:
	print(t2[count]);
	count += 1;
	if count == len(t2):
		break;
input();

