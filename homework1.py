# -*- coding: utf-8 -*-
#     1.环境搭建
#         anaconda环境配置
#         解释器
#     ---------------------------
#     2.python初体验
#         print and input
print("hello world!")
a=input("input:")
input:请输入
#     ---------------------------
#     3.python基础讲解
#         python变量特性+命名规则
变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头
变量名不能包含空格，但可使用下划线来分隔其中的单词
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词
变量名应既简短又具有描述性，慎用小写字母l和大写字母O
#         注释方法
用“#”表示注释
多行注释用三个单（双）引号
#         python中“：”作用
在分支语句和循环语句中表示换行，在切片中表示步长
#         学会使用dir( )及和help( )
dir():查看一下要使用模块的功能列表
help( )：实际使用过程中的帮助函数
#         import使用
import:导入模块或者包的关键词
#         pep8介绍
python的编码规范
#     ---------------------------
#     4.python数值基本知识
#         python中数值类型，int，float，bool，e记法等
int:输出输入数的整数，无关正负
float:输出小数
bool:布尔值
    True 正确的
    False 错误的
#         算数运算符
+：整数型是加法运算，字符串是合并运算
-：整数型是减法运算
*：整数型是乘法运算，字符串是重复运算
/：整数型除法运算只保留整数，浮点数除法保留浮点数
%：整数型除法取余数运算
**：整数型幂运算
#         逻辑运算符
 and,or,not
#         成员运算符
 in,not in
#         身份运算符
 is,not is
#         运算符优先级
#     ---------------------------
#     5.string字符串
#         定义及基本操作（+，*，读取方式）
 字符串 就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号
#         字符串相关方法
 修改字符串的大小写;合并（拼接）字符串;使用制表符或换行符来添加空白;删除空白
#         字符串格式化问题
 %d：格式化整数
 %s：格式化字符串
 %c：格式化字符及其ASCII码
 %e：格式化科学记数法浮点数
#     ------------------------------------------------------------------------------------
#     【作业】
#         学习代码分享，200-300行要求。
#         作业：要求用户依次输入姓名，性别，年龄，并对用户信息进行输出格式如下：您的姓名是：***，
#          您的性别是：***，您是***年出生的。
name=input("请输入您的姓名")
gender=input("请输入您的性别")
age=input("请输入您的出生年份")
print("您的姓名是：%s，您的性别是%s，您是%d年出生的"%(name,gender,age))
#     ------------------------------------------------------------------------------------
