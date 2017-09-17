message='hello "Python" world!'
print(message);
message="hello ‘Python’ world!it will be good!"
print(message);
message="hello ‘Python’ world!it will be good!"
print(message.title());#字符串的每个单词的首字母以大写的形式出现

message="hello ‘Python’ world!it will be good!"
print(message.upper());#字符串的每个单词以大写的形式出现

message="hello ‘Python’ world!it will be good!"
print(message.lower());#字符串的每个单词以小写的形式出现
#拼接字符串
class_in="15电信1"#class是一个关键字
name="cai"
full=class_in+" "+name
print(full);

message="Hello"+" "+full.title()+"!"

print(message);

#用制表符来添加空白
print("\t"+message);

#用换行符来添加空白
print("\n"+message);

#删除字符串的结尾的空白行
message="hello ‘Python’ world!it will be good!  "
print(message.rstrip());

print(message+"!");#短暂删除

message=message.rstrip();
print(message+"!");#永久删除

#删除字符串的前后的空白行
message="  hello ‘Python’ world!it will be good!  "
print(message.strip());
print(message);

#删除字符串的开头的空白行
message="  hello ‘Python’ world!it will be good!  "
print(message.lstrip());
print(message);

name="boy ming"
print(name.upper());
print(name.lower());
print(name.title());

message="would you like to learn some Python today?"
print("Hello "+name+","+message);

famous_person="Abert Einstein"
say="A perspn who never made a mistake never tried anything new"
message=famous_person+' once said,"'+say+'"'
print(message)

name="\tboy ming "
print(name.lstrip());
print(name.rstrip());
print(name.strip());

print(3+3);
print(2*3);
print(8-2);
print(12/2);
num=3+3;
print("I like "+str(num));
import this 







