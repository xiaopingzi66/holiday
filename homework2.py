#!/usr/bin/env python
# coding: utf-8

# In[1]:


#我的名字列表里的人名全是颜色
names=["red","green","blue","yellow"]
print(names[0])


# In[2]:


names=["red","green","blue","yellow"]
print(names[-1])


# In[4]:


names=["red","green","blue","yellow"]
message="nice to meet you"+","+names[0]
print(message)


# In[5]:


#append()可以在列表末尾增加元素
names=["red","green","blue","yellow"]
print(names)

names.append("purple")
print(names)


# In[6]:


#insert()可在列表任意位置处增加元素
names=["red","green","blue","yellow"]
names.insert(0,"purple")
print(names)


# In[7]:


#del()可以删除列表中的元素，但需要知道元素的位置
#我要去除第一个元素
names=["red","green","blue","yellow"]
print(names)

del names[0]
print(names)


# In[9]:


#pop()一般用来删除列表末尾的元素，但也可以删除其余位置的元素
names=["red","green","blue","yellow"]
print(names)

popped_names=names.pop()
print(names)

popped_names=names.pop(0)
print(names)


# In[14]:


#打印出与字母顺序相反的顺序列表
names=["red","green","blue","yellow"]
names.sort(reverse=True)
print(names)


# In[22]:


#深浅拷贝
#在Python中对象的赋值其实就是对象的引用。当创建一个对象，把它赋值给另一个变量的时候，python并没有拷贝这个对象，只是拷贝了这个对象的引用而已。
#浅拷贝：拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。也就是，把对象复制一遍，但是该对象中引用的其他对象我不复制
#深拷贝：外围和内部元素都进行了拷贝对象本身，而不是引用。也就是，把对象复制一遍，并且该对象中引用的其他对象我也复制。
#浅拷贝
names=["red","green","blue","yellow"]
names2=names.copy()
names[2]="purple"
print(names)
print(names2)
#深拷贝
import copy
names=["red","green",["pink",],"blue","yellow"]
new_names = copy.deepcopy(names)
names[2][0]="purple"
print(names)
print(new_names)


# In[ ]:


#元组
#列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的。
#Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。
#元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
list=(1,2,"3",'4')#有无引号没关系，用逗号隔开就好。
list[0]=3  #这种修改是不被允许的
list=(5)   #元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
type(list) # 不加逗号，类型为整型
list=(5,)
type(list) # 加上逗号，类型为元组


# In[28]:


#作业
#将男女朋友"purple"加入第四位
family=["red","green","blue","yellow"]
family.insert(3,"purple")
print(family)


# In[29]:


#将男女朋友移除
family=["red","green","blue","yellow"]
family.insert(3,"purple")
print(family)

del family[3]
print(family)


# In[ ]:





# In[ ]:




