C++ 为什么选择OOP
---
OOP是Object Oriented Program

1. 潘敏学老师邮箱:mxp@nju.edu.cn
2. 不封装存在很大的安全隐患(数据暴露，可以被直接修改)
3. 不符合数据类型的定义,使用封装实现OOP

<!-- TOC -->

- [1. non-OO Solution 非面向对象的解决方案](#1-non-oo-solution-非面向对象的解决方案)
- [2. OO Solution 面向对象的解决方案](#2-oo-solution-面向对象的解决方案)
- [3. OOP 面向对象](#3-oop-面向对象)
- [4. OOP评价标准](#4-oop评价标准)
- [5. ENCAPSULATION(封装)](#5-encapsulation封装)
- [6. 对象类型的判断](#6-对象类型的判断)
  - [6.1. 方法一:运行时判断](#61-方法一运行时判断)
  - [6.2. 方法二:编译时判断](#62-方法二编译时判断)

<!-- /TOC -->

# 1. non-OO Solution 非面向对象的解决方案
```c++
//non-OO Solution
#include <stdio.h>
#define STACK_SIZE 00
struct Stack{
    int top;
    int buffer[STACK_SIZE];
};
//push和Stack是相关的，但是不是显式相关
bool push(Stack &s, int i){
    if(s.top == STACK_SIZE - 1) {
        printf("Stack is overflow.\n");
        return false;
    }else{
        s.top++;
        s.buffer[s.top] = i;
        return true;
    }
}
bool pop(Stack &s, int &i){
    if (s.top == -1){
        printf("Stack is empty.\n");
        return false;
    }else{
        i = s.buffer[s.top]; 
        s.top--;         
        return true;
    }
}
void main(){
    Stack st1, st2;
    st1.top = -1;//安全隐患
    st2.top = -1;//安全隐患
    int  x; 
    push(st1,12);  
    pop(st1,x);
    //可以直接操控其中的数据
    st1.buffer[2] = -1;//违背ADT
    st2.buffer[2]++;   //违背ADT
}
```

# 2. OO Solution 面向对象的解决方案
1. cfront:用来进行检查一些访问权限的问题。
```c++
#include <iostream.h>
#define STACK_SIZE 100
class Stack
{   private: 
        int top;
        int buffer[STACK_SIZE];
    public:
        Stack(){ top = -1; }//定义的构造方法
        bool push(int i);
        bool pop(int& i);
};
bool Stack::push(int i);{
    if (top == STACK_SIZE-1) {
        cout << "Stack is overflow.\n";
        return false;
    }else{
        top++;
        buffer[top] = i;
        return true;
    }
}
bool Stack::pop(int& i){
    if (top == -1) {
        cout << "Stack is empty.\n";
        return false;
    }else {
        i = buffer[top];           
        top--;
        return true;
    }
}
void main()
{    Stack st1,st2;
     int x;
     st1.push(12); 
     st1.pop(x);
     //st1.buffer[2] = -1无法操作
     //cfront用来检查
}
```
1. 实际上,程序存储的时候并没有发生变化

```c++
struct Stack{   
    int top;
    int buffer[STACK_SIZE];
};
//this是指向自己的指针
//对象的函数至少都持有一个this
bool push(Stack *const this,int i);{
    if (top == STACK_SIZE-1) {
        cout << "Stack is overflow.\n";
        return false;
    }else{
        top++;
        buffer[top] = i;
        return true;
    }
}
bool pop(Stack *const this,int& i){
    if (top == -1) {
        cout << "Stack is empty.\n";
        return false;
    }else {
        i = buffer[top];           
        top--;
        return true;
    }
}
void main(){   
    Stack st1, st2;
    st1.top = -1;
    st2.top = -1;
    int x;
    push(st1,12);
    pop(st1,x);
}
```

# 3. OOP 面向对象
1. Concepts 面向对象概念
    1. Program = Object<sub>1</sub> + Object<sub>2</sub> + ... + Object<sub>n</sub>
    2. 对象:数据 + 操作
    3. 信息:函数调用
    4. 类
2. Classify 分类
    1. Object-Oriented 面向对象
    2. Object-Based(Ada:基于对象的语言)
        + Without Inheritance


# 4. OOP评价标准
1. 高扩展性
2. 质量
    + 外部评价指标：正确性、效率、健壮性、可靠性、可用性、可重用性
    + 内部评价指标：可读性、可维护性、可移植性

# 5. ENCAPSULATION(封装)
具体到markdown文件中

# 6. 对象类型的判断

## 6.1. 方法一:运行时判断
1. 使用if..else
```c++
int i;
if(typeid(i) == typeid(int) )
    cout << "i is int" << endl ;
else
    cout << "i is not int" << endl ;
```

## 6.2. 方法二:编译时判断
```c++
template<class T>
void func(T t ){
    cout << "i is not int" << endl ;
}
template<> void func<int>(int i){//特化
    cout << "i is int" << endl ;
}
int i;
func(i)
```