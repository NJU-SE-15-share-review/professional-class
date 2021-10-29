友元函数
---
1. 类外部不能访问该类的 private 成员
    1. 通过该类的 public 方法
    2. 会降低对 private 成员的访问效率，缺乏灵活性:如果使用public方法使用这些成员则是实行调用函数，降低调用效率，消耗时间
    3. 例：矩阵类(Matrix)、向量类(Vector)和全局函数(multiply)，全局函数实现矩阵和向量相乘
    4. 隐藏细节、保持一致性
2. 友元是数据保护和访问效率的折衷方案
3. 友元可以访问private和protected的成员

<!-- TOC -->

- [1. Example:Matrix 和 Vector](#1-examplematrix-和-vector)
- [2. 友元的分类](#2-友元的分类)
  - [2.1. 友元函数](#21-友元函数)
  - [2.2. 友元类](#22-友元类)
  - [2.3. 友元类成员函数](#23-友元类成员函数)
- [3. 友元函数分类实例](#3-友元函数分类实例)
- [4. 友元函数声明](#4-友元函数声明)
- [5. 友元函数作用](#5-友元函数作用)
- [6. 声明两个类互为友元](#6-声明两个类互为友元)
- [7. 封装原则](#7-封装原则)
- [8. 友元和protected](#8-友元和protected)

<!-- /TOC -->

# 1. Example:Matrix 和 Vector
```c++
//Matrix
class Matrix{
    int *p_data;//逻辑二维，一维存储
    int lin,col;
    public:
        Matrix(int l, int c){
            lin = l;
            col = c;
            p_data = new int[lin*col];
        }
        ~Matrix(){
            delete []p_data;
        }
        int &element(int i, int j){
            return *(p_data+i*col+j);//指针类型的偏移是根据指针指向对象的类型
        }
        void dimension(int &l, int &c){
            l = lin;
            c = col;
        }
        void display(){
            int *p=p_data; 
            for (int i=0; i<lin; i++){
                for (int j=0; j<col; j++){
                    cout << *p << ' ';
                    p++;
                }
                cout << endl;
            }
        };
};
//Vector
class Vector{
    int *p_data;
    int num;
    public:
        Vector(int n){
            num = n;
            p_data = new int[num];
        }
        ~Vector(){
            delete []p_data;
        }
        int &element(int i)
        {  return p_data[i]; }
        void dimension(int &n)
        { n = num; }
        void display(){
            int *p=p_data;
            for (int i=0; i<num; i++,p++)
                cout << *p << ' ';
            cout << endl;
        }
};
//实现 矩阵和一个向量进行计算，效率比较
void multiply(Matrix &m, Vector &v, Vector &r){ 
    int lin, col;
    m.dimension(lin,col);
    for (int i=0; i<lin; i++){
        r.element(i) = 0;
        for (int j=0; j<col; j++)
            r.element(i) += m.element(i,j)*v.element(j);//这里的调用效率会比较低
    }
}

void main(){
    Matrix m(10,5);
    Vector v(5);
    Vector r(10);
    multiply(m,v,r);
    m.display();
    v.display();
    r.display();
}
```

# 2. 友元的分类

## 2.1. 友元函数
1. 一个全局函数是一个类的友元，如果在这之前没有声明也是可以进行声明友元函数。

## 2.2. 友元类
1. 一个类是另一个类的友元
2. class关键字可以省略
3. 第一种情况:friend class B:
   1. 编译器会寻找有没有类B
   2. 如果没有则会引入一个B
4. 第二种情况:friend B
   1. 省略关键字的时候不会引入B，如果没有B会报错模板类
   2. 但是这种形式常用于模板类(T或者typedef的时候来写)

## 2.3. 友元类成员函数
1. 在完整的类的声明完成之前是不能够被声明的。

# 3. 友元函数分类实例
```c++
void func() ;
class B;//这种情况下B不是必须的
class C{
	void f();
};   
class A{
	friend void func();//友元函数
	friend class B;    //友元类:B中的每一个函数都可以访问A的成员函数
	friend void C::f();//友元类成员函数
};
```

# 4. 友元函数声明
1. 友元函数在之前可以没有声明
2. 友元函数如果之前还没有声明过，则当做已经声明了
3. 但是友元类函数在完整的类声明出现前不能声明友元函数。
4. 为什么友元函数和友元类成员函数的声明要求是不一样的？
   1. 数据的一致性:避免对应类里面没有这个函数(也就是C的完整定义必须有)
   2. 成员函数依赖于类

# 5. 友元函数作用
1. 作用
    1. 提高程序设计灵活性
    2. 数据保护和对数据的存取效率之间的一个折中方案
2. 友元不具有传递性:
   1. 不能说A是B的友元，B是C的友元就可以得出A是C的友元
   2. 友元必须显式声明

```c++
class Matrix{
 	friend void multiply(Matrix &m, Vector &v, Vector &r);
};
class Vector{
 	friend void multiply(Matrix &m, Vector &v, Vector &r);
};
```

1. 上面这段代码可以编译吗？(循环依赖)
   1. 不可以编译的，要在前面先声明Vector
   2. 使用变量前必须要先声明
   3. Matrix里面如果去掉Vector中的引用？会出现内存分配问题(不知道如何拷贝，而引用大小是相同的)
2. 解决方案:不完全声明:`class vector;`


# 6. 声明两个类互为友元
```c++
class A{
    int a;
    public:
        friend class B;
    void show(B &b){
        std::cout << b.b;//这里可以吗？不行，不知道B中有b
    }
}
class B{
    int b;
    public:
        friend class A;
        void show(A &a){
            std::cout << a.a;//这里是可以的
        }
}
void A::show (B &b){//只能在这里面实现
    std::cout << b.b;
}
```
1. 互为友元的两个类声明时是否需要**前置声明**
    1. 如果A和B不在一个命名空间不能通过编译
    2. 如果A和B在一个命名空间的话可以没有前置声明

# 7. 封装原则
1. 避免将data member放在公开接口中(使用get和set方法)
   1. 尽量将get和set成员更加完备化
   2. 遵循迪米特法则(最小知识原则):尽量让别的类对当前类的依赖最小

```c++
class AccessLevels {
    public:
        int getReadOnly const { return readOnly; }
        void setReadWrite(int value) { readWrite = value; }
        int getReadWrite() { return readWrite; }
        void setWriteOnly(int value) { writeOnly = value; }
    private:
        int noAccess;
        int readOnly;
        int readWrite;
        int writeOnly;
};
```
2. 努力让接口完满 (complete) 且最小化

# 8. 友元和protected
```c++
class Base{
    protected :
        int prot_mem;// protected 成员
};
class Sneaky : public Base {//36min
    friend void clobber(Sneaky&);//能访问Sneaky::prot_mem 
    friend void clobber(Base&);//不能访问Base::prot_mem，对外不可见
    int j;// j 默认是private 

    void clobber(Sneaky &s) {
        s.j = s.prot_mem = 0;
    }//正确：clobber 能访问Sneaky对象的 private和protected成员 
    void clobber(Base &b) {
        b.prot_mem = 0;
    }//错误:clobber 不能访问Base的 protected 成员
}
```
1. 继承过程中的友元传递:友元不具有传递性，不可以访问任意基类的
