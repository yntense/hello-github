# -*- coding:utf-8 -*-
names=['boy ming',"girl chen",'boy cai']
for name in names:
	print("Hello "+name.title()+","+"good moring!");
	
print(names[0]);
print(names[-1]);

names[0]='boy chen'
print(names)

#���һ������
names.append('girl hu')
print(names);

#ɾ��һ������
del names[0]
print(names)

#����һ������
names.insert(2,'girl wang');
print(names)

#ɾ�����һ������
message=names.pop(-1)
print(names)
print(message)
print("Hello "+name.title()+","+"good moring!")
print("will be deleted :"+message);

#����ֵ��ɾ��Ԫ��
names.remove('girl wang')
print(names)

name ='boy cai'
names.remove(name)
print(names)

guests=['A','B','C']
print(guests)
print(guests[0].title()+" will be not coming")
guests[0]='D'
for guest in guests:#��סð��
	print("welcome to my party "+guest)
	
print("I find a bigger place so,")
guests.insert(0,'E')
num= len(guests)
guests.insert((int)(num/2),'F')
guests.append('G')
for guest in guests:
	print("welcome to my party "+guest)
print("sorry, because the dest is limited, I only invite two guest:")
for guest in guests[2:]:
	name=guests.pop()
	print("sorry "+name+" will not come ")
print(guests)
del guests[0]
del guests[0]
print(guests)

#���ӵ��б�
cars=["bwm","ans","h"]
print(cars)
cars.sort ()
print(cars)
cars.sort(reverse=True)
print(cars)

#��ʱ�Ե�����
print(sorted(cars))
print(cars)

#���õ���
cars.reverse();
print("\n");
print(cars)
lenth=len(cars)
print(str(lenth))
