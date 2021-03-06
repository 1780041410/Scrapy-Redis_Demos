############## 正则表达式匹配单个字符 ##############

import re

# 1.匹配某个字符串
# text = "hello"
# ret = re.match('he',text)
# print(ret)
# print(type(ret))
# print(ret.group())

# 2.点：匹配任意的字符
# text = "hello"
# ret = re.match('.',text)   #只能匹配一个字符，不能匹配换行符
# print(ret.group())

# 3. \d：匹配任意的数字(0-9)
# text = "1"
# ret = re.match('\d',text)
# print(ret.group())

# 4. \D：匹配任意的非数字
# text = "+"
# ret = re.match('\D',text)
# print(ret.group())

# 5. \s：匹配空白字符(\n换行符、\t制表符、\r、空格)
# text = "\n"
# ret = re.match('\s',text)
# print(ret.group())

# 6. \w：匹配的是a-z和A-Z，以及数字和下划线
# text = "A"
# ret = re.match('\w',text)
# print(ret.group())

# 7. \W：匹配的正好与\w相反
# text = "+"
# ret = re.match('\W',text)
# print(ret.group())

# 8. []组合的方式，只要满足中括号中的字符，就可以匹配
text = "0736-88888888 Changde"
ret = re.match('[\d\-]+',text)   #此处+意思为，匹配一个或多个满足前面条件的字符
print(ret.group())

# 8.1 中括号的形式代替\d
# text = "09"
# ret = re.match('[0-9]',text)
# print(ret.group())

# 8.2 中括号的形式代替\D
# text = "a"
# ret = re.match('[^0-9]',text)
# print(ret.group())

# 8.3 中括号的形式代替\w
# text = "_"
# ret = re.match('[a-zA-Z0-9_]',text)
# print(ret.group())

# 8.3 中括号的形式代替\W
# text = "+"
# ret = re.match('[^a-zA-Z0-9_]',text)
# print(ret.group())


############## 正则表达式匹配多个字符 ##############

# 9. 星号*：可以匹配0或者任意多个字符
# text = "0731"
# ret = re.match('\d*',text)
# print(ret.group())

# 10. 加号+：匹配1个或多个字符
# text = "ab+cd"
# ret = re.match('\w+',text)
# print(ret.group())

# 11. 问号？：匹配一个或者0个（要么没有，要么只有一个1）
# text = "+abcd"
# ret = re.match('\w?',text)
# print(ret.group())

# 12. {m}：匹配m个字符
# text = "abcde"
# ret = re.match('\w{3}',text)
# print(ret.group())

# 13. {m,n}：匹配m-n个字符
# text = "abcde"
# ret = re.match('\w{1,4}',text)
# print(ret.group())


############## 正则表达式匹配字符小案例 ##############

# 14.验证手机号码：
text = "13850523695"
ret = re.match('1[345678]\d{9}',text)
print(ret.group())

# 15.验证邮箱：
text = "zjg_901206@gmail.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
print(ret.group())

# 16.验证URL：
text = "https://github.com/"
ret = re.match('(http|https|ftp)://[^\s]+',text)
print(ret.group())

# 17.验证身份证：
text = "43072419941109021X"
print(len(text))
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())

# 18. ^ (脱字号)：表示以…开始
text = "hello"
ret = re.match('^h',text)
# ret = re.search('o', text)
print(ret.group())

# 19. $:表示以…结尾
text = "xxxxxxx@126.com"
ret = re.match('\w+@126.com$',text)
print(ret.group())

# 20. |：匹配多个表达式或字符串
text = "ftp"
ret = re.match('(http|https|ftp)$',text)
print(ret.group())

# 21. 贪婪模式与非贪婪模式：
text = "0123456"
ret = re.match('\d+',text)    # 贪婪模式
ret = re.match('\d+?',text)   # 非贪婪模式
print(ret.group())

text = "<h1>标题</h1>"
ret = re.match('<.+>',text)    # 贪婪模式
ret = re.match('<.+?>',text)   # 非贪婪模式
print(ret.group())

# 22. 匹配0-100之间的数字
text = "100"
ret = re.match('([1-9]\d?)$|100$',text)
print(ret.group())
