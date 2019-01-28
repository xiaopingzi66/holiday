
dict字典
定义：在Python中，字典是一系列键—值对 。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。


```python
#创建一个字典
fruit_colours={'lemon':'yellow','grape':'purple','watermelon':'green'}
#输出字典中的值
print(fruit_colours['lemon'])
```

    yellow
    

字典的相关方法
遍历字典



```python
#遍历字典中的所有键-值
fruit_colours={'lemon':'yellow','grape':'purple','watermelon':'green'}
for fruit,colour in fruit_colours.items():
    print(fruit.title()+"'s colour is "+ colour.title()+".")
```

    Lemon's colour is Yellow.
    Grape's colour is Purple.
    Watermelon's colour is Green.
    


```python
#遍历字典中的所有键
fruit_colours={'lemon':'yellow','grape':'purple','watermelon':'green'}
for fruit in fruit_colours.keys():
    print(fruit.title())
```

    Lemon
    Grape
    Watermelon
    


```python
#遍历字典中的所有值
fruit_colours={'lemon':'yellow','grape':'purple','watermelon':'green'}
for colour in fruit_colours.values():
    print(colour.title())

```

    Yellow
    Purple
    Green
    

嵌套
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套

set集合
定义：set是一个无序且不重复的元素集合。
集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。集合支持用in和not in操作符检查成员，由len()内建函数得到集合的基数(大小)， 用 for 循环迭代集合的成员。但是因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值。

set和dict一样，只是没有value，相当于dict的key集合，由于dict的key是不重复的，且key是不可变对象因此set也有如下特性：
1、不重复
2、元素为不可变对象


```python
#创建
#注意在创建空集合的时候只能使用s=set()，因为s={}创建的是空字典
s = set()
s = {11,22,33,44}
a=set('boy')
b=set(['y', 'b', 'o','o'])
c=set({"k1":'v1','k2':'v2'})
d={'k1','k2','k2'}
e={('k1', 'k2','k2')}
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
```

    {'o', 'b', 'y'} <class 'set'>
    {'y', 'b', 'o'} <class 'set'>
    {'k2', 'k1'} <class 'set'>
    {'k2', 'k1'} <class 'set'>
    {('k1', 'k2', 'k2')} <class 'set'>
    

相关方法


```python
#比较
se = {11, 22, 33}
be = {22, 55}
#找到se中存在，be中不存在的集合，返回新值
temp1 = se.difference(be)
print(temp1) #{33, 11}
print(se)    #{33, 11, 22} 

#找到se中存在，be中不存在的集合，覆盖掉se
temp2 = se.difference_update(be)
print(temp2)
print(se) 
```

    {33, 11}
    {33, 11, 22}
    None
    {33, 11}
    


```python
#删除
se = {11, 22, 33}
se.discard(11)
se.discard(44)  # 移除不存的元素不会报错
print(se)

se = {11, 22, 33}
se.remove(11)
se.remove(44)  # 移除不存的元素会报错
print(se)

se = {11, 22, 33}  # 移除末尾元素并把移除的元素赋给新值
temp = se.pop()
print(temp)  # 33
print(se) # {11, 22}
```


```python
#判断
se = {11, 22, 33}
be = {22}

print(se.isdisjoint(be))        #False，判断是否不存在交集（有交集False，无交集True）
print(se.issubset(be))          #False，判断se是否是be的子集合
print(se.issuperset(be))        #True，判断se是否是be的父集合
```


```python
#合并
se = {11, 22, 33}
be = {22}

temp1 = se.symmetric_difference(be)  # 合并不同项，并赋新值
print(temp1)
print(se)   

temp2 = se.symmetric_difference_update(be)  # 合并不同项，并更新自己
print(temp2)    
print(se)
```


```python
#取并集
se = {11, 22, 33}
be = {22,44,55}

temp=se.union(be)   #取并集，并赋新值
print(se)       #{33, 11, 22}
print(temp)     #{33, 22, 55, 11, 44}
```

file文件读取
对于新手而言，难以理解的部分
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
open(file, mode='r')
完整的语法格式为：open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

参数说明:
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用UTF-8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:       资料来源：http://www.runoob.com/python3/python3-file-methods.html


```python
#作业
f=open('C:/Users/Administrator/Desktop/homework.txt','r',encoding='utf-8')
line=f.read()
print(line)
print(type(line))
```

    python学习 咖喱 胡骞
    leetcode刷题 老表 陈焕森
    编程集训 孙超 小熊
    统计学 李奇峰 蓝昔
    ML项目实践 杨冰楠 孙涛
    高级算法梳理 于鸿飞 小雪
    基础算法梳理 sm1les 钱令武
    知乎小组 李严 黑桃
    学习群 咖喱 排骨
    
    <class 'str'>
    


```python
dict = {}
word=[]
a=len(line)
bag=0
key=''
str=''
value=[]
for i in range(a):                  
    if line[i].isspace():           
        b=len(word)                
        for j in range(b):         
            str = str+word[j]
        word.clear()               
        bag=+1                   
        if bag==1:                
            key=str                 
            str=''                  
        elif bag==2:               
            value.append(str)       
            str=''
        elif bag==3:               
            value.append(str)       
            dict[key] = value      
            key=''                  
            str=''
            value=[]
            bag=0
    else:                          
        word.append(line[i])
print (dict)
f.close()

#遍历字典
for key in dict:
    for i in range(2):
        for key2 in dict:
            for j in range(2):
                if dict[key][i]==dict[key2][j]:
                    cnt=1;
if cnt==1:
    print("有重复")
```

    {'python学习': ['咖喱', '胡骞'], 'leetcode刷题': ['老表', '陈焕森'], '编程集训': ['孙超', '小熊'], '统计学': ['李奇峰', '蓝昔'], 'ML项目实践': ['杨冰楠', '孙涛'], '高级算法梳理': ['于鸿飞', '小雪'], '基础算法梳理': ['sm1les', '钱令武'], '知乎小组': ['李严', '黑桃'], '学习群': ['咖喱', '排骨']}
    有重复
    


```python

```
