#! /usr/bin/python
a = input();
b = input();
c = input();
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
		if c != "2":
			t2.append("{{checkuser|" + t + "}}");
		else:
			t2.append("*{{srcu|" + t + "|zh|w}}");
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

