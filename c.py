#! /usr/bin/python
a = input();
count = 0;
la = 0;
b = [];
t = "";
while True:
    t += a[count];
    if a[count] == "}":
        if count + 1 == len(a):
            b.append(t);
            t = "";
        else:
            if a[count + 1] != "}":
                b.append(t);
                t = "";
    count += 1;
    if count == len(a):
        break;
count = 0;
while True:
    print(b[count]);
    count += 1;
    if count == len(b):
        break;
input();
