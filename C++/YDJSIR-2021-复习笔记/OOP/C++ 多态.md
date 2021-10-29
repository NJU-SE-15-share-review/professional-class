多态
---
1. 通用概念:同一论域中一个元素可有多种解释。
2. 提高面向对象设计的语言灵活性
3. 程序设计语言:OO程序设计
4. 多态形式
   1. 函数重载:(静态多态)，和虚函数的动态多态不同(一名多用):函数重载包含操作符重载
   2. 类属多态:模板:template

<!-- TOC -->

- [1. 操作符重载](#1-操作符重载)
  - [1.1. 操作符 + 的重载](#11-操作符--的重载)
  - [1.2. 可以重载的操作符](#12-可以重载的操作符)
  - [1.3. 双目操作符的重载](#13-双目操作符的重载)
    - [1.3.1. 类成员函数(双目操作符)](#131-类成员函数双目操作符)
    - [1.3.2. 全局函数](#132-全局函数)
  - [1.4. 返回值总结](#14-返回值总结)
  - [1.5. 单目操作符的重载](#15-单目操作符的重载)
  - [1.6. 操作符 = 的重载](#16-操作符--的重载)
  - [1.7. 操作符 [] 的重载](#17-操作符--的重载)
  - [1.8. 多维数组 class Array2D](#18-多维数组-class-array2d)
    - [1.8.1. 多维数组的最终版本](#181-多维数组的最终版本)
  - [1.9. 操作符 () 的重载](#19-操作符--的重载)
    - [1.9.1. 函数调用](#191-函数调用)
    - [1.9.2. 操作符类型转换的重载](#192-操作符类型转换的重载)
  - [1.10. 操作符 -> 的重载](#110-操作符---的重载)
  - [1.11. 操作符 new 和 delete 的重载](#111-操作符-new-和-delete-的重载)
    - [1.11.1. 重载 new](#1111-重载-new)
    - [1.11.2. 重载 delete](#1112-重载-delete)
    - [1.11.3. new和delete考试](#1113-new和delete考试)
- [2. 模板 template](#2-模板-template)
  - [2.1. 模板](#21-模板)
  - [2.2. 类属函数 templat function](#22-类属函数-templat-function)
  - [2.3. 函数重载](#23-函数重载)
  - [2.4. 函数指针](#24-函数指针)
  - [2.5. 函数模板](#25-函数模板)
  - [2.6. 类模板](#26-类模板)
  - [2.7. 模板例子](#27-模板例子)
  - [2.8. C++中模板的完整定义通常出现在头文件中](#28-c中模板的完整定义通常出现在头文件中)
  - [2.9. Template MetaProgramming 元编程](#29-template-metaprogramming-元编程)
- [3. 参考](#3-参考)

<!-- /TOC -->

# 1. 操作符重载
1. 函数重载
    1. **名同、参数不同**，返回值不同没有用的:参数顺序、参数类型匹配(找到最佳匹配)
    2. 静态绑定
2. 歧义控制:
    1. 顺序:
    2. 最佳匹配:
       1. 原则一:这个匹配每一个参数不必其他的匹配更差
       2. 原则二:这个匹配有一个参数更精确匹配
    3. 整形提升:更好的，标准转换(标准转换都是一视同仁的)
    4. 窄转换?允许的，大->小
3. 操作符重载(变为一种函数)
    1. 动机:操作符语义
        + built_in 类型
        + 自定义数据类型
    2. 作用:
        1. 提高可读性
        2. 提供可扩充性
4. 重点记忆返回的变量

## 1.1. 操作符 + 的重载
1. 重载第一步
```c++
class Complex {
    double real, imag;
    public:
        Complex() {real = 0; imag = 0;}
        Complex(double r, double i) { real = r; imag = i; }
        Complex add(Complex& x);
};
Complex a(1,2),b(3,4),c;
c=a.add(b);//想要写成 a + b
//使用操作符重载
class Complex {
    double real, imag;
    public:
        Complex() { real = 0; imag = 0; }
        Complex(double r, double i) { real = r; imag = i; }
        Complex operator + (Complex& x) {  
            Complex temp;
            temp.real = real + x.real;
            temp.imag = imag + x.imag;
            return temp;
        }
};
Complex a(1,2),b(3,4),c;
c = a.operator + (b);

//进一步完成操作符重载
class Complex {
    double real, imag ;
    public :
        Complex() { real = 0 ; imag = 0 ; }
        Complex(double r, double i) {
            real = r;
            imag = i;
        }
        friend Complex operator+(Complex& c1 , Complex& c2);//这个是已经预定义好的，我们这样子写就是重载
};
//全局函数
Complex operator+ (Complex& c1 , Complex& c2 ) {//全局函数重载至少包含一个用户自定义类型
    Complex temp;
    temp.real = c1.real + c2.real;
    temp.imag = c1.imag + c2.imag;
    return temp;
}//一般返回临时变量

Complex a(1,2),b(3,4),c;
c = a + b;//自动进行翻译
```
2. 自增和自减的问题
```c++
class Counter {
    int value;
    public:
        Counter() { value = 0; }
        Counter& operator ++()//++a 左值
        {
            value ++;
            return *this;
        }
        Counter operator ++(int)//a++ 右值
        {
            Counter temp = *this;
            value++;
            return temp;
        }
}
```
3. 重载++函数:封装SAT的问题
   1. 返回值引用或者是值是有区别的

```c++
enum Day { SUN, MON, TUE, WED, THU, FRI, SAT};
Day& operator++(Day& d)
{  return d= (d==SAT)? SUN: Day(d+1); }
//重载重定向符号，用的很多,不能进成员函数重载
ostream& operator << (ostream& o, Day& d)
{	switch (d)
	{	case SUN: o << "SUN" << endl;break;//直接使用ostream中的<<
		case MON: o << "MON" << endl;break;
		case TUE: o << "TUE" << endl;break;
		case WED: o << "WED" << endl;break;
		case THU: o << "THU" << endl;break;
		case FRI: o << "FRI" << endl;break;
		case SAT: o << "SAT" << endl;break;
	}
	return o;//为什么要return ostream类型的变量:需要连续的使用可以链式调用，Cout << 1 << 2;
}
void main(){
    Day d = SAT;
    ++d;
    cout << d;
}
```

## 1.2. 可以重载的操作符
1. 不可以重载的操作符:`.`(成员访问操作符)、`.*`(成员指针访问运算符，如下)、`::`(域操作符)、`?:`(条件操作符)、`sizeof`:也不重载
   1. 原因:前两个为了防止类访问出现混乱
   2. ::后面是名称不是变量
   3. ?:条件运算符涉及到跳转，如果重载就影响了理解

```c++
class A
{   int x;
    public:
        A(int i):x(i){} 
        void f() {}
        void g() {}
};
void (A::*p_f)();//A类成员的函数指针

p_f= &A::f;
(a.*p_f)();
int a = 0;b = 0;
b?(a = 1):(b = 1);//a == b == 1
operator ?: (p,a = 1,b = 1)//均执行了
```

1. 重载基本原则:
    1. 方法:(大多数都支持，但是有的不支持)
        1. 类成员函数
        2. **带有类参数**的全局函数
    2. 遵循原有语法
        1. 单目/双目:一一对应
        2. 优先级
        3. 结合性
2. 永远不要重载&&和||:会造成极大的问题
    
## 1.3. 双目操作符的重载

### 1.3.1. 类成员函数(双目操作符)
1. 类成员函数:
    1. 格式:`<ret type>operator #(<arg>)`
    2. this: 隐含，必然是第一个参数
2. 使用:

```c++
<class name> a,b;
a # b;//a -> this
a.operator#(b)
```

### 1.3.2. 全局函数
1. 友元:`friend <ret type> operator #(<arg1>,<arg2>)`
2. 格式:`<ret type> operator #(<arg1>,<arg2>)`
3. 注意:`=`、`()`、`[]`、`->`不可以作为全局函数重载
    + 大体上来讲，C++ 一个类本身对这几个运算符就已经有了相应的解释了。
    + 如果将这四种符号进行友元全局重载，则会出现一些冲突
    + 下标和箭头运算符为什么？有保留调用顺序，我们希望能保留原来的顺序，而全局不能要求，而成员函数的this就可以解决这个问题
    + <a href = "https://blog.csdn.net/weixin_30781107/article/details/98147938">参考</a>
4. 全局函数作为补充:
   1. 单目运算符最好重载为类的成员函数
   2. 双目运算符最好重载为类的友元函数

```c++
class CL {
    int count;
    CL(int i){...}//10可以直接隐式类型转换
    public:
        friend CL operator +(int i, CL& a);
        friend CL operator +(CL& a, int i); 
};//支持隐式类型转换就行
//如果最左边不是类对象，则必须作为友元函数
```

5. 永远不要重载 && 和 ||:逻辑与和逻辑或
   1. 原因:短路，类似?:
   2. 虽然绝大多数都没有问题，但是如果有逻辑短路容易出现问题

```c++
char *p;
if ((p != 0) && (strlen(p) >10)) //利用了短路，一旦计算就没有短路行为了
if (expressin1 && expression2)
if (expression1.operator && (expression2))
if (operator && (expression1, expression2))
```
1. 返回类型的问题:如果没有&的时候，第一个return出现了对象拷贝，避免:临时变量不能返回拷贝
```c++
class Rational { 
	public:
		Rational(int,int);
            const Rational& operator *(const Rational& r) const;//const写不写都行，写了更好
	private:
		int n, d;	
};
// operator * 的函数体
return Rational(n * r.n, d * r.d);

Rational *result  = new Rational(n*r.n, d*r.d);
return *result;//返回引用的问题?
// w = x * y * z出现问题:出现内存泄露的问题

static Rational result;//声明为static
result.n = n * r.n;
result.d = d * r.d;
return result;//static是全局的，可以吗?不可以，同时出现两个的结果会出现问题
//if((a * b) == (c * d)) ->永真式
```

2. 操作符重载的哲理:尽量让事情有效率，但不是过度有效率(返回引用)
3. 结论:每次就是返回一个拷贝，而不是引用


## 1.4. 返回值总结
1. 加减乘除:就是拷贝，不是引用，效率不太高?为了解决这个问题:可以返回值优化，第一个return没有拷贝，直接返回的是一个对象(无拷贝)，先计算，最后生成一个对象返回。

## 1.5. 单目操作符的重载
1. 类成员函数:
    1. this:隐含
    2. 格式:`<ret type> operator#()`:this的隐含
2. 全局函数:
   1. `<ret type> operator#(<arg>)`
   2. 参数必须为自定义类型
3. 单目操作符在绝大多数情况下重载为类的成员函数
4. 15min没了
5. a++ 和 ++ a

```c++
class Counter{
    int value;
    public:
        Counter() { value = 0; }
        Counter& operator ++() // ++a
        {   value++;
            return *this;
        }
        Counter operator ++(int) //a++
        {   Counter temp=*this;//这里的int值是什么意义?区分两个函数，dummy argument，哑元变量
            value++;
            return temp;
        }
}
```

## 1.6. 操作符 = 的重载
1. 默认赋值操作符重载函数
2. 逐个成员赋值
3. 对含有对象成员的类，该定义是递归的
4. 赋值操作符的重载不可以被继承：因为拷贝构造，派生出来的类有一些新的部分
5. 返回引用类型:返回*this的引用，支持链式赋值
6. this引用应该是非常量引用，返回出来的是作为右值进行计算
   1. a = b = c:不要求非常量引用
   2. (a = b).f():要求非常量引用
7. 例一:
```c++
class A;
A a = b;//需要调用拷贝构造函数(更重要的是构造，在构造对象时候调用)
A a(b);
A a,b;
a = b;//需要调用
```
```c++
class A {
    int x,y ;
    char *p ;
    public :
        A(int i,int j,char *s):x(i),y(j){
            p = new char[strlen(s)+ 1 ];
            strcpy(p,s);//进行拷贝，最后留一个\0
        }
        virtual ~A(){
            delete[] p;
        }
        A& operator = (A& a) {
            //赋值
            x = a.x;
            y = a.y;
            delete []p;
            p = new char[strlen(a.p)+1];
            strcpy(p,a.p);
            return *this;//也会出现悬垂
        }//还有问题，就是赋值自身会出现问题
};
A a, b;
a = b;//调用自己的复制

//idle pointer，B被析构的时候会将p释放掉，导致p指向已经被释放掉的指针
//Memory leak,A申请的区域可能没有办法被释放
```

```c++
//更安全的拷贝，先new再delete
char *pOrig = p;
p = new char ...
strcpy();
delete pOrig;
return *this;
//自我赋值可以吗？可以，换了一块内存空间，没有内存泄露
```

1. 注意:避免自我赋值(因为是相同的内存地址)
   1. Sample: class string
   2. s = s
      1. `class {... A void f(A& a);...}`
      2. `void f (A& a1, A& a2)`
      3. `int f2(Derived &rd,Base& rb);`
   3. Object identity
      1. Content
      2. Same memory location
      3. Object identifier

```c++
if(this == &a)
    return *this;
delete p;//48min - 50min
```

```c++
class A{
    public:
        ObjectID identity() const;
}; 
A *p1,*p2; 
p1-> identity() == p2-> identity()
```

## 1.7. 操作符 [] 的重载
```c++
class string {
    char *p;
    public :
        string(char *p1){
            p = new char [strlen(p1)+ 1];
            strcpy(p,p1);//#pragma warning(disable:4996)来屏蔽问题
        }
        char& operator[](int i){
            return p[i];
        }
        const char operator[](int i) const{
            return p[i];
        }
        //可以用两个重载函数吗?是可以的
        virtual ~string() { delete[] p ; }
};
string s("aacd");
s[2] = 'b' ;
//第一个重载加上const可以使得const或者非const对象都可以调用
const string cs('const');
cout << cs[0];
const cs[0] = 'D';//const 版本不想被赋值(返回const的)，非const版本想要被赋值，之后再进行重载的时候就需要同时重载两个
```

## 1.8. 多维数组 class Array2D
![](img/18.png)
```c++
class Array2D{
    int n1, n2;
    int *p;
    public:
        Array2D(int l, int c):n1(l),n2(c){
            p = new int[n1*n2];
        }
        virtual ~Array2D() { delete[] p; }
};

int & Array2D::getElem(int i, int j) { ... }
//上面是实现高维数组
Array2D data(2,3);
data.getElem(1,2) = 0; 
//target -> data[1][2]
//想法:化解为两次调用
data.operator[](1)[2];//int *operator[](int i) 一次偏移一行，转化成Array1D
data.operator[](1).operator[](2) 

//问题:三维数组重载问题:重载一次降维一次，3D->2D等等，多个依次进行重载，重载之后返回对象
//代理对象:Array1D

class  Array1D{
    int *q;//一维降低到int *就行
    Array1D(int *p){ q = p; }
    int&  operator[](j){
        return q[j];
    }
}
```

### 1.8.1. 多维数组的最终版本
```c++
class Array2D{
    private:
        int *p;
        int num1, num2;
    public:
	    class Array1D{//Surrogate 多维，proxy class
            public:
                Array1D(int *p) { this->p = p; }
                int& operator[ ] (int index) { return p[index]; }
                const int operator[ ] (int index) const { return p[index]; }
	        private:
		        int *p;
        };
        Array2D(int n1, int n2) {
            p = new int[n1 * n2];
            num1 = n1;
            num2 = n2;
        }
        virtual ~Array2D() {
            delete [] p;
        }
        Array1D operator[](int index) {
            return p + index * num2;//return的值和int*相同，构造函数不能声明成显式构造函数。
        }
        //这里为什么是array1D?通过构造函数进行类型转换
        const Array1D operator[] (int index) const {
            return p+index*num2;
        }
};
```

## 1.9. 操作符 () 的重载
1. ()的意义
   1. 函数调用
   2. 类型转换操作符

### 1.9.1. 函数调用
```c++
class Func {
    double para;
    int lowerBound , upperBound ;
    public:
        double operator()(double,int,int);
};
Func f;
f(2.4, 0, 8);
class Array2D{
    int n1, n2;
    int *p;
    public:
        Array2D(int l, int c):n1(l),n2(c){
            p = new int[n1*n2];
        }
        virtual ~Array2D() {
            delete[] p;
        }
        int& operator()(int i, int j){
            return (p+i*n2)[j];//优化getElement
        }
};
```

### 1.9.2. 操作符类型转换的重载
1. 基本数据类型
2. 自定义类

```c++
class Rational {
    public: Rational(int n1, int n2) {
        n = n1;
        d = n2;
    }
    operator double() {//类型转换操作符，语法特殊
        return (double)n/d;
    }
    private:
        int n, d;
};
//减少混合计算中需要定义的操作符重载函数的数量
Rational r(1,2);
double x = r;
x = x + r;//避免的double 和 rational 的全局函数重载，会自动全部转换为double
```

```c++
//48min
ostream f("abc.txt");
if (f)
//重载  数值型：如 int
```

1. 问题:为什么禁止在类外禁止重载赋值操作符?
   1. 如果没有类内提供一个赋值操作符，则编译器会默认提供一个类内的复制操作符
   2. 查找操作符优先查找类内，之后查找全局，所以全局重载赋值操作符不可能被用到

## 1.10. 操作符 -> 的重载
1. ->为二元运算符，重载的时候按照一元操作符重载描述。
```c++
A a;
a->f();
a.operator->(f)
a.operator->()->f() //重载时按一元操作符重载描述,这时，a.operator->()返回一个指针(或者是已经重定义过->的对象)
```
2. 例子:画图板程序
```c++
class CPen {
    int m_color;
    int m_width;
    public:
        void setColor(int c){ m_color = c;}
        int getWidth(){ return m_width; }
};
class CPanel {
    CPen m_pen;
    int m_bkColor;
    public:
        CPen* getPen(){return &m_pen;}
        void setBkColor(int c){ m_bkColor =c;}
};
CPanel c;
c.getPen()->setColor(16);
//简单修改，可以返回一个对象内部对象的指针
class CPen {
    int m_color;
    int m_width;
    public:
        void setColor(int c){ m_color = c;}
        int getWidth(){return m_width; }
};
class CPanel {
    CPen m_pen;
    int m_bkColor;
    public:
        CPen* getPen(){return &m_pen;}
        void setBkColor(int c) { m_bkColor =c;}
};
CPanel c;
c->setColor(16);
//等价于
//c.operator->()->setColor(16);
//c.m_pen.setColor(16)
c->getWidth();
//等价于
//c.operator->()->getWidth();
//c.m_pen.getWidth()
CPanel *p=&c;
p->setBkColor(10);
```
3. Prevent memory Leak:需要符合compiler控制的生命周期
```c++
class A{
    public:
    void f();
    int g(double);
    void h(char);
};
void test(){
    A *p = new A;
    p->f();//如果出错可能会导致问题
    p->g(1.1);//返回值
    p->h('A');
    delete p;
}
//更好的管理A对象，不用在任何退出的地方写delete p
void test()
{
    AWrapper p(new A);
    p->f();//如果出错可能会导致问题
    p->g(1.1);//返回值
    p->h('A');
    delete p;
}
//须符合compiler控制的生命周期
class AWrapper{//不包含逻辑
    A* p;// ? T p; 支持多个类型
    public:
        AWrapper(A *p) { this->p = p;}
        ~AWrapper() { delete p;}
        A*operator->() { return p;}
};//RAII 资源获取及初始化
//函数返回，销毁局部指针的时候会直接删除
```

## 1.11. 操作符 new 和 delete 的重载
1. 频繁调用系统的存储管理，影响效率。
2. 程序自身管理内存，提高效率
3. 方法:
    1. 调用系统存储分配，申请一块较大的内存
    2. 针对该内存，自己管理存储分配、去配
    3. 通过重载new与delete来实现
    4. 重载的new与delete是静态成员(隐式的，不需要额外声明，不允许操作任何类的数据成员)
    5. 重载的new与delete遵循类的访问控制，可继承(注意派生类和继承类的大小问题，开始5min左右)
4. 我们想要对某些程序进行自己的资源管理的话，可以重载这两个操作符。
5. 有些我们重复新建销毁的，比如Restful的可以单独管理
6. new构造和返回指针
7. delete析构和释放内存
8. 可以重载成全局函数，也可以重载成类成员函数

### 1.11.1. 重载 new
1. `void *operator new (size_t size, s...)`
2. 名:operator new
3. 返回类型:void *
4. 第一个参数:size_t(unsigned int)
    + 系统自动计算对象的大小，并传值给size
5. 其他参数:可有可无
    + `A *p = new (...) A`，表示传给new的
6. new的重载可以有多种
7. 如果重载一个new，那么通过new动态创建该类的对象时将不再调用内置的(预定义的)new
8. 允许进行全局重载，但是不推荐使用全局重载

```c++
if(size != sizeof(base))
    return ::operator new (size);//调用全局标准库的new进行size的分配，标准库的new永远是可以使用的
operator new;
new A[10];
operator new [];
void * operator new (size_t size, void*)//是不可以被重载的，标准库版本
void * operator new (size_t size, ostream & log);//可以同时写入到日志
void * operator new (size_t size, void * pointer);//定位new，placement new，被调用的时候，在指针给定的地方的进行new(可能预先已经分配好的)，分配比较快，长时间运行不被打断(不会导致内存不足)
```

8. new也可以new在栈上
```c++
class A{};
char buf[sizeof(A)];
A* a = new(buf) A;//定位new，不用分配内存，直接使用buf指向的区域
```

### 1.11.2. 重载 delete
1. `void operator delete(void *,size_t size)`
2. 名：operator delete
3. 返回类型:void
4. 第一个参数:void *(必须)：被撤销对象的地址
5. 第二个参数:可有可无;如果有，则必须为size_t类型：被撤销对象的大小
6. delete 的重载只能有一个
7. 如果重载了delete，那么通过 delete 撤消对象时将不再调用内置的(预定义的)delete
8. 动态删除其父类的所有的。
9. 如果子类中有一个虚继承函数，则size_t大小会根据继承情况进行确定大小

### 1.11.3. new和delete考试
1. 主要考核集中在这些上面

# 2. 模板 template

## 2.1. 模板
1. 模板是一种**源代码复用**机制
2. 参数化模块:
    + 对程序模块(如:类、函数)加上**类型参数**
    + 对不同类型的数据实施相同的操作
3. 实例化:生成具体的函数/类
4. 模板定义了若干个类，需要显式实例化
5. 编译系统自动实例化函数模板：是否实例化模板的某个实例由使用点来决定；如果未使用到一个模板的某个实例，则编译系统不会生成相应实例是的代码。

## 2.2. 类属函数 templat function
1. 同一函数对不同类型的数据完成相同的操作
2. 宏实现:
    1. `#define max(a,b) ((a)>(b)?(a):(b))`
    2. 缺陷:
        1. 只能实现简单的功能
        2. 没有类型检查

## 2.3. 函数重载
```c++
int max(int,int);
double max(double,double);
A max(A,A) ;
```
1. 缺陷:
    1. 需要定义的重载函数太多
    2. 定义不全
2. 不可以只有返回值不同

## 2.4. 函数指针
```c++
void sort(void * , unsigned int, unsigned int, int (* cmp) (void *, void *) )
```
1. 缺陷:
    1. 需要定义额外参数
    2. 大量指针运算
    3. 实现起来复杂
    4. 可读性差
2. template更加结构清晰，实现简单

## 2.5. 函数模板
```c++
//int和double都可以使用，编译器编译的并不是之下的代码，而是T转化成具体代码，然后分别编译
template <typename T>
void sort(int A[], unsigned int num) {
    for(int i=1; i<num; i++)
        for (int j=0; j< num - i; j++) {
            if  (A[j] > A[j+1]) {
                T t = A[j];
                A[j] = A[j+1];
                A[j+1] = t;
            }
        }
}
class C {...}
C a[300];
sort(a, 300);//没有重载>
```
1. 必须重载操作符 >
2. 函数模板定义了一类重载的函数
3. 函数模板的实例化:
    1. **隐式实现**
    2. 根据具体模板函数调用
4. 函数模板的参数
    1. 可有多个类型参数，用逗号分隔
    2. 可带普通参数
        + **必须列在类型参数之后**
        + 调用时需显式实例化，使用默认参数值可以不显式实例化

```c++
template <class T1, class T2>
void f(T1 a, T2 b) {}
template <class T, int size>
void f(T a) {T temp[size];}
f<int,10>(1);
```

1. 函数模板与函数重载配合使用(编译器优先使用没有使用模板的函数)
```c++
template <class T> T max(T a, T b) {
    return a>b?a:b;
}
int x, y, z;
double l, m, n;
z = max(x,y);
l = max(m,n);
//为了解决max(x,m)我们使用函数重载更新
double max(int a, double b) {
    return a>b? a : b;
}
```

## 2.6. 类模板
1. 类定义带有类型参数，类属类需要显式实例化
2. 类模板中的静态成员属于实例化后的类
3. 类模板的实例化:创建对象时显式指定

```c++
class Stack {
    int buffer[100];
    public:
        void push(int x);
        int pop();
};
void Stack::push(int  x) {...}
int Stack::pop(){...}

Stack st1;

template <class T>
class Stack {
    T buffer[100];
    public:
        void push( T x);
        T pop();
};

template <class T>
void Stack <T> ::push(T x) {...}

template <class T>
T Stack <T> ::pop() {...}

//如下是显式实例化
Stack <int> st1;
Stack <double> st2;
```

## 2.7. 模板例子
```c++
template <class T, int size>
class Stack {
    T buffer[size];
    public:
        void push(T x);
        T pop();
};

template <class T, int size>
void Stack <T, size>::push(T x) {...}

template <class T, int size>
T Stack <T, size>::pop() {...}

Stack <int, 100 > st1 ;//上面改为template<class T = int,int size = 100>,这里可以改成stack<> st1用来显示实例化
Stack <double, 200 > st2 ;
```

1. 类型参数也可以给出初始值，模板类如果不按照从右往左指定默认值参数，会导致编译错误
2. 函数模板的默认值不一定是从右向左的，C++11之后函数模板才接受默认值参数。
3. 总而言之从右向左给出默认值总是没有问题的。

## 2.8. C++中模板的完整定义通常出现在头文件中
1. 如果在模块A中要使用模块B中定义的某模板的实例，而在B中未使用这个实例，则模板无法使用这个实例
2. 为什么C++中模板的完整定义常常出现在头文件中?

```c++
//file1.h
template <class T> class S {
    T a;
    public:
        void f();
};

//file1.cpp
#include "file1.h"
template <class T>
void S<T>::f(){...}

template <class T>
T max(T x, T y){return x>y?x:y;}
void main() {
    int a,b;
    max(a,b);//实例化函数模板
    S<int> x;
    x.f();
}

//file2.cpp
#include "file1.h"
extern double max(double,double);
void sub(){
    max(1.1,2.2);//error
    S<float> x;
    x.f();//error
}
//不能通过编译，为什么？file2.cpp找不到max定义，也找不到完整的S代码
```
- 解决方案:将file1.cpp中的代码放置到头文件中
- 连接器可以去掉多重定义

## 2.9. Template MetaProgramming 元编程
1. 元程序就是编写一些直接可以生成或者操作其他程序的程序，要在更高层次上。
2. 编写元程序就是元编程(两级编程)，在编译的时候就已经完成编程

```c++
template<int N>
class Fib
{
    public:
        enum { value = Fib<N - 1>::value + Fib<N - 2>::value };
};

//模板显式实例化
template<>  
class Fib<0>{
    public:
        enum { value = 1 };
};
template<>
class Fib<1>
{
    public:
        enum { value = 1 };
};
void main() {
    cout << Fib<8>::value << endl;// calculated at compile time
}
```

1. 元编程的特点
   1. 输入就是模板中的参数(int N)
   2. 返回值往往是enum、static、final等等
   3. 往往是只支持整数，但是浮点数也是可以的
2. 选择和循环语句如何操作?
   1. 选择可以通过特殊实例化实现:`class isTen<N==10>`:模板的特例化
   2. 递归的调用模板就提供了循环的能力
3. 模板元编程是图灵完备的
4. 不作为考核内容

# 3. 参考
1. <a href = "https://www.jianshu.com/p/38f17600f19a">C++泛型与多态(1)：基础篇</a>