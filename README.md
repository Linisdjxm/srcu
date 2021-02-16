Example:

In[1]:
```
{{checkuser|Example1}}
{{checkuser|Example2}}
{{checkuser|Example3}}
{{checkuser|Example4}}
END              
```

Output:
```
 |user name1        = Example1
 |user name2        = Example2
 |user name3        = Example3
 |user name4        = Example4
```
In[2]:
```
{{checkuser|Example1}}
{{checkuser|Example2}}
{{checkuser|Example3}}
{{checkuser|Example4}}
END1              
```
Output:
```
 |user name1        = Example1
 |user name2        = Example2
 |user name3        = Example3
 |user name4        = Example4
```
IN[3]:
```
{{checkuser|Example1}}
{{checkuser|Example2}}
{{checkuser|Example3}}
{{checkuser|Example4}}
END2              
```
Output:
```
=== Example1@zh.wikipedia ===
{{CU request
 |status          = <!--don't change this line-->
 |language code   = zh
 |project shortcut = w

 |user name1        = Example1
 |user name2        = Example2
 |user name3        = Example3
 |user name4        = Example4
 |discussion      = [[:w:zh:Wikipedia:元維基用戶查核請求#Example1]]
 |reason =
}}
```
