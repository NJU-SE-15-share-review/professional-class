# CPU

> Powered by $YDJSIR$
>
> 下面的分类可能不是很严谨，只是把知识对照起来看

## CPU的结构和功能

1. 取指令、

2. 解释指令（译码）、

3. 取数据、

4. 处理数据、

5. 写数据

|                           粗略视图                           |                           详细视图                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![image-20210116205304843](CPU.assets/image-20210116205304843.png) | ![image-20210116205429157](CPU.assets/image-20210116205429157.png) |



# 运算器

> 只涉及课程中提到的内容

### ALU

> - Lecture04
>
> - Lecture05
>
> 考虑到这部分内容通常已经在机考中涉及，这里不作重点但仍会提及。

#### 1. 移位运算

##### 1.算数移位：

+ **符号位不变**, 左移相当于乘以 2, 右移相当于除以 2(左侧全补符号位).

##### 2. 逻辑移位:

+ **无符号数的移位**, 右移时永远在高位填 0.

##### 3. 循环移位

- 和它的名字一样

#### 2. 加法运算

##### 1. 全加器

   + $𝑆_𝑖=𝑋_𝑖⊕𝑌_𝑖⊕𝐶_{𝑖−1}$
   + $𝐶_𝑖=𝑋_𝑖𝐶_{𝑖−1}+𝑌_𝑖𝐶_{𝑖−1}+𝑋_𝑖𝑌_𝑖$

##### 2. Serial Carry Adder

   <iframe frameborder="0" style="width:150%;height:200%;" src="https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1#R7VpLc9owEP41HJvxS9g%2BJpC0h3amMxxKjipWsDrGYmwRIL%2B%2BMpZfWiAE%2FMAMF8ZaybL0fatvd20G5mix%2BR7hpf%2BLeSQYGJq3GZjjgWG4riF%2BE8M2NdjITA3ziHqpSS8ME%2FpBpFGT1hX1SFwZyBkLOF1WjTMWhmTGKzYcRWxdHfbGgupTl3hOgGEywwG0%2FqEe91OrY9iF%2FQehcz97sj50054FzgbLncQ%2B9ti6ZDKfB%2BYoYoynV4vNiAQJdhku6X0vB3rzhUUk5KfcYMslx3ybbY54Yq%2ByySLuszkLcfBcWJ8itgo9ksygiVYx5idjS2HUhfEf4XwricMrzoTJ54tA9pIN5VN5e3L9mlw%2FINkab0pd461spOtMFndwq9IUs1U0k6NsPQdVOCNhC8KjrRgTkQBz%2Bl6dC0u3mOfj8lt%2FMyqeYmjSgy1T8icdWM%2Fa2RQcR3PC5V0F%2FuKitIzCtGNlP0Ou3gVDV4U2UtA2GgPblmt7x8FKrvblEeC%2F9iknkyXebXstFK6KHY6Xqei80U3CgQTznUScbI7DCaHLHM6tQpA11yX5kSa%2FpDyOdhjrCkzHMDEAJtAjQ%2B8x0VXRmgU4julMOfCheOi03Cgd%2BaRZnPld6%2BuHPvWB425YAgvtASuzXeitw%2BEn2pCeGOCu0O3VifTm%2FN4EHI80wLJwX664ekDnYUK6oINEwpA4ORWB8lF2LKjnpYpEYvqB%2F%2B6mSphdJqve7QM9DdA4mUuIUJzqkV7PoRlqCoCaDU6NuccRVH0569S4PZJttOcMDS%2BU8lOBcrrJQNoVJNRMFqKfl4WAiUz7PMkSmo%2B3pWHyUF%2BoRehKY7BhdRaDHbNHanKpchxw9tYy7nQDV%2BiAutadA2owQYCFSd8SBAt1lyA4FkQ07D2iQ6c7QB0AKBTNok4JWZiA5OHY32mkfp72dVVlmE5NVUaLrzIc90sMHa8ktQcjT9Zey503VEoiJcHLg%2BCXS0k1etqNkezCSHF9JHdGKKqLUDVyNUioAQid9D%2F0q%2B8UEcylmgpULnzZMu0%2FoJaL9rt2G4jCXOq1%2F4gis0NEERTt6yk4ay8uDSWbOvELw6fzuKfJ%2BzmqDIvUe5jNaRjWFGbViZoMs%2Fad0MPVjlYToepETRIK69FJ%2BK3%2FYcmwrQqEezInq6moBAvI6U1Aah1w7xYwzV8qlpOnmwBVjemtgnrV%2F9qoPX%2FSVQc%2BM39S52kuf9I1WNbe423Og1FTvFUnajDe6hqsq%2B%2BM5kTUlRKrEzXKKKzrJ%2F3%2FRqKKXIuvnnQNflyf3gCih8qDViCFlfjrDUB6QkpaE6SiWfzhOZWJ4l%2Fj5vN%2F"></iframe>

+ 缺点: 速度慢.
+ 延时(OR AND $1ty$, XOR $3ty$)
  + $Cn: 2n \ ty$
  + $Sn: 2n+1 \ ty$

##### 3. Carry Look Ahead Adder

**注意**：这里的+均为“或”
$$
\begin{aligned}
𝐶_𝑖&=𝑋_𝑖𝐶_{𝑖−1}+𝑌_𝑖𝐶_{𝑖−1}+𝑋_𝑖𝑌_i\\
\\
C_1&=𝑋_1𝑌_1+(𝑋_1+𝑌_1)𝐶_0\\
𝐶_2&=𝑋_2𝑌_2+(𝑋_2+𝑌_2)𝑋_1𝑌_1+(𝑋_2+𝑌_2)(𝑋_1+𝑌_1)𝐶_0\\
𝐶_3&=𝑋_3𝑌_3+𝑋_3+𝑌_3𝑋_2𝑌_2+𝑋_3+𝑌_3𝑋_2+𝑌_2𝑋_1𝑌_1
+(𝑋_3+𝑌_3)(𝑋_2+𝑌_2)(𝑋_1+𝑌_1)𝐶_0\\
C_4 &=...
\end{aligned}
$$

可见,$Ci$ 仅与最初的X Y和 $C_0$有关.
令$𝑃_𝑖=𝑋_𝑖+𝑌_𝑖, 𝐺_𝑖=𝑋_𝑖𝑌_i$
则:
$$
\begin{aligned}
\\
𝐶_1&=𝐺_1+𝑃_1𝐶_0\\
𝐶_2&=𝐺_2+𝑃_2𝐺_1+𝑃_2𝑃_1𝐶_0\\
𝐶_3&=𝐺_3+𝑃_3𝐺_2+𝑃_3𝑃_2𝐺_1+𝑃_3𝑃_2𝑃_1𝐶_0\\
𝐶_4&=...
\end{aligned}
$$
总结得:$C_{i+1} = G_{i+1}+P_{i+1}C_i$, 超前进位加法器采用的是将低一位的逻辑代数代入高一位, 依此类推最终每一个进位输出仅考虑 $C_0, X_i, Y_i$几个信号, 于是所有的进位都能同时计算.

+   缺点:复杂
+   延时: $1 ty+ 2ty + 3 ty = 6 ty$

#### 4. Partial Carry Look Ahead Adder

   结合两者，比如说4个8位的Carry Look Ahead Adder组合成一个32位的加法器。

#### 5. 溢出判断

+ $C_n\oplus C_{n-1} =1$, 即符号位进位与最高有效位进位不同时,发生溢出.
+ $𝑋_𝑛 𝑌_𝑛 \overline{𝑆_𝑛}+\overline{𝑋_𝑛𝑌_𝑛}𝑆_𝑛=1$,则溢出,与上面等价.

#### 3. 减法运算

减法运算大致与加法相同,只需要将减数`取反加一`然后按加法算即可, **注意加一的操作是令 $C_0 = 1$**。

#### 4. 乘法运算

##### 1. 无符号整数乘法

通过**加法和移位实现**,与竖式乘法极其类似,但是计算机很难像人类那样一次性把各位乘的结果一次性相加,因此采用部分积的方式:
例:$0111\times0110$

| <font color=#FF0000>部分积</font> |              乘数               |       得到当前行的操作       |
| :-------------------------------: | :-----------------------------: | :--------------------------: |
|  <font color=#FF0000>0000</font>  |              0110               | 部分积+乘数末位$\times 0111$ |
|  <font color=#FF0000>0000</font>  | <font color=#FF0000>0</font>011 |             右移             |
|  <font color=#FF0000>0111</font>  | <font color=#FF0000>0</font>011 | 部分积+乘数末位$\times 0111$ |
|  <font color=#FF0000>0011</font>  | <font color=#FF0000>10</font>01 |             右移             |
|  <font color=#FF0000>1010</font>  | <font color=#FF0000>10</font>01 | 部分积+乘数末位$\times 0111$ |
|  <font color=#FF0000>0101</font>  | <font color=#FF0000>010</font>0 |             右移             |
|  <font color=#FF0000>0101</font>  | <font color=#FF0000>010</font>0 | 部分积+乘数末位$\times 0111$ |
|  <font color=#FF0000>0010</font>  | <font color=#FF0000>1010</font> |             右移             |

+ 乘数末位决定被乘数是否加到部分积,然后部分积和乘数均**右移**,部分积低位保存到乘数高位.
+ **被乘数只与部分积高位相加**

原理:
$$\begin{aligned}
XY &= XY_nY_{n-1}...Y_2Y_1\\&=X(Y_n\times2^{n-1}+Y_n\times2^{n-2}+...+Y_2\times2^1+Y_1\times2^0)\\&=2^n(XY_n\times2^{-1}+XY_{n-1}\times2^{-2}+...+XY_1\times2^{-n})\\
&=2^nP_{n},其中P_{n} = 2^{-1}\times(XY_{n}+P_{n-1}),n\gt1.\end{aligned}$$

##### 2. 补码整数乘法

根据上面无符号整数的原理, 可以将二进制补码整数相乘变形如下:

$$\begin{aligned}XY& = XY_nY_{n-1}...Y_2Y_1\\&=X(-Y_n\times2^{n-1}+Y_n\times2^{n-2}+...+Y_2\times2^1+Y_1\times2^0)\\&=2^nX((Y_{n-1}-Y_n)\times2^{-1}+(Y_{n-2}-Y_{n-1})\times2^{-2}+...+(Y_0-Y_1)\times2^{-n})\\&
=2^nP_{n},其中Y_0=0,P_{n} = 2^{-1}\times(X(Y_{n-1}-Y_{n})+P_{n-1}),n\gt1.\end{aligned}$$

形式上还原了,只是每次乘的**不是乘数的末位数**, 且注意是**算数右移**,需要补符号位,
例: $-7\times-6 = 42,即 1001\times1010=00101010$

| <font color=#FF0000>部分积</font> |               乘数               |       得到当前行的操作        |
| :-------------------------------: | :------------------------------: | :---------------------------: |
|  <font color=#FF0000>0000</font>  | 1010<font color=#0000FF>0</font> | 部分积+$(Y_0-Y_1)\times 1001$ |
|  <font color=#FF0000>0000</font>  | <font color=#FF0000>0</font>1010 |             右移              |
|  <font color=#FF0000>0111</font>  | <font color=#FF0000>0</font>1010 | 部分积+$(Y_1-Y_2)\times 1001$ |
|  <font color=#FF0000>0011</font>  | <font color=#FF0000>10</font>101 |             右移              |
|  <font color=#FF0000>1100</font>  | <font color=#FF0000>10</font>101 | 部分积+$(Y_2-Y_3)\times 1001$ |
|  <font color=#FF0000>1110</font>  | <font color=#FF0000>010</font>10 |             右移              |
|  <font color=#FF0000>0101</font>  | <font color=#FF0000>010</font>10 | 部分积+$(Y_3-Y_4)\times 1001$ |
|  <font color=#FF0000>0010</font>  | <font color=#FF0000>1010</font>1 |             右移              |

#### 5. 除法运算

##### 1. unsigned

1.人的计算:除数右移, 2n位

+ 竖式计算:
  <img src="https://i0.hdslb.com/bfs/article/8216b980b855f3139a28932f6883a053a6e04f1f.png" style="zoom:50%;" />

|   余数   |   <font color=#0000FF>除数</font>   |               商                |
| :------: | :---------------------------------: | :-----------------------------: |
| 00000111 | <font color=#0000FF>00110000</font> |              0000               |
| 00000111 | 0<font color=#0000FF>0011000</font> |              0000               |
| 00000111 | 0<font color=#0000FF>0011000</font> | 000<font color=#FF0000>0</font> |
| 00000111 | 00<font color=#0000FF>001100</font> | 000<font color=#FF0000>0</font> |
| 00000111 | 00<font color=#0000FF>001100</font> | 00<font color=#FF0000>00</font> |
| 00000111 | 000<font color=#0000FF>00110</font> | 00<font color=#FF0000>00</font> |
| 00000001 | 000<font color=#0000FF>00110</font> | 0<font color=#FF0000>001</font> |
| 00000001 | 0000<font color=#0000FF>0011</font> | 0<font color=#FF0000>001</font> |
| 00000001 | 0000<font color=#0000FF>0011</font> | <font color=#FF0000>0010</font> |





2. 计算机的计算: **余数左移**, n位

| <font color=#0000FF>余数</font> |               <font color=#FF0000>商</font>                | 除数 |
| :-----------------------------: | :--------------------------------------------------------: | :--: |
| <font color=#0000FF>0000</font> |              <font color=#0000FF>0111</font>               | 0011 |
| <font color=#0000FF>0000</font> |               <font color=#0000FF>111</font>               | 0011 |
| <font color=#0000FF>0000</font> | <font color=#0000FF>111</font><font color=#FF0000>0</font> | 0011 |
| <font color=#0000FF>0001</font> | <font color=#0000FF>11</font><font color=#FF0000>0</font>  | 0011 |
| <font color=#0000FF>0001</font> | <font color=#0000FF>11</font><font color=#FF0000>00</font> | 0011 |
| <font color=#0000FF>0011</font> | <font color=#0000FF>1</font><font color=#FF0000>00</font>  | 0011 |
| <font color=#0000FF>0000</font> | <font color=#0000FF>1</font><font color=#FF0000>001</font> | 0011 |
| <font color=#0000FF>0001</font> |               <font color=#FF0000>001</font>               | 0011 |
| <font color=#0000FF>0001</font> |              <font color=#FF0000>0010</font>               | 0011 |

##### 2. 带有符号的除法

+ 如何判断余数(的绝对值)是否大于除数(的绝对值)?
  + 同号则减, 异号则加. 与结果符号相同的那个数绝对值大

<table style="border-collapse:collapse;margin-left:52.305pt" cellspacing="0"><tbody><tr style="height:29pt"><td style="width:94pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt" rowspan="2"><p class="s116" style="padding-top: 2pt;padding-left: 6pt;padding-right: 5pt;text-indent: 0pt;line-height: 22pt;text-align: center;">remainder</p><p class="s116" style="padding-left: 6pt;padding-right: 5pt;text-indent: 0pt;line-height: 22pt;text-align: center;">sign</p></td><td style="width:74pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt" rowspan="2"><p class="s116" style="padding-top: 2pt;padding-left: 10pt;padding-right: 9pt;text-indent: 0pt;line-height: 22pt;text-align: center;">Divisor</p><p class="s116" style="padding-left: 10pt;padding-right: 9pt;text-indent: 0pt;line-height: 22pt;text-align: center;">sign</p></td><td style="width:211pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt" colspan="2"><p class="s116" style="padding-top: 2pt;padding-left: 62pt;text-indent: 0pt;text-align: left;">Subtraction</p></td><td style="width:216pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt" colspan="2"><p class="s116" style="padding-top: 2pt;padding-left: 74pt;padding-right: 73pt;text-indent: 0pt;text-align: center;">Addition</p></td></tr><tr style="height:29pt"><td style="width:106pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s116" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s116" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td><td style="width:111pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s116" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s116" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td></tr><tr style="height:29pt"><td style="width:94pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:74pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:106pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Enough</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Not enough</p></td><td style="width:111pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 11pt;padding-right: 10pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td></tr><tr style="height:29pt"><td style="width:94pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:74pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td><td style="width:106pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:111pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 11pt;padding-right: 10pt;text-indent: 0pt;text-align: center;">Enough</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Not enough</p></td></tr><tr style="height:29pt"><td style="width:94pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td><td style="width:74pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">0</p></td><td style="width:106pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:111pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 11pt;padding-right: 10pt;text-indent: 0pt;text-align: center;">Not enough</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Enough</p></td></tr><tr style="height:29pt"><td style="width:94pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td><td style="width:74pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;text-indent: 0pt;text-align: center;">1</p></td><td style="width:106pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Not enough</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">Enough</p></td><td style="width:111pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 11pt;padding-right: 10pt;text-indent: 0pt;text-align: center;">----</p></td><td style="width:105pt;border-top-style:solid;border-top-width:1pt;border-left-style:solid;border-left-width:1pt;border-bottom-style:solid;border-bottom-width:1pt;border-right-style:solid;border-right-width:1pt"><p class="s117" style="padding-top: 2pt;padding-left: 8pt;padding-right: 7pt;text-indent: 0pt;text-align: center;">----</p></td></tr></tbody></table>

<img src="https://i0.hdslb.com/bfs/article/aadda87e9086a37cb714b2970fa7596c0721f939.png" width = "30%" />

1. **恢复余数法** 在下面的步骤中,余数和除数的和是存储在余数寄存器里面的,判断完成后,还要恢复原来的余数(即减去余数).之前的不带符号位除法**也都是恢复余数法**,只是没有表示出来.

   | <font color=#0000FF>余数</font> |               <font color=#FF0000>商</font>                | 除数 |        得到本步操作        |
   | :-----------------------------: | :--------------------------------------------------------: | :--: | :------------------------: |
   | <font color=#0000FF>1111</font> |              <font color=#0000FF>1001</font>               | 0011 |             -              |
   | <font color=#0000FF>1111</font> |               <font color=#0000FF>001</font>               | 0011 |            左移            |
   | <font color=#0000FF>1111</font> | <font color=#0000FF>001</font><font color=#FF0000>0</font> | 0011 | 1111+0011 =0010,not enough |
   | <font color=#0000FF>1110</font> | <font color=#0000FF>01</font><font color=#FF0000>0</font>  | 0011 |            左移            |
   | <font color=#0000FF>1110</font> | <font color=#0000FF>01</font><font color=#FF0000>00</font> | 0011 | 1110+0011=0001, not enough |
   | <font color=#0000FF>1100</font> | <font color=#0000FF>1</font><font color=#FF0000>00</font>  | 0011 |            左移            |
   | <font color=#0000FF>1111</font> | <font color=#0000FF>1</font><font color=#FF0000>001</font> | 0011 |   1100+0011=1111, enough   |
   | <font color=#0000FF>1111</font> |               <font color=#FF0000>001</font>               | 0011 |            左移            |
   | <font color=#0000FF>1111</font> |              <font color=#FF0000>0010</font>               | 0011 | 1111+0011=0010,not enough  |

   **最后,结果取 <font color=#FF0000>0010</font> 的补码整数 <font color=#FF0000>1110 </font>为最终结果.**

   + 缺点:Problem: recover remainder is high cost
   + 解决方案:使用不恢复余数法(加减相消法)

2. 加减相消法.

   + 规则 
     + 将被除数符号拓展 n 位后存储在余数和商寄存器.
     + 如果被除数与除数符号相同, 作减法; 若符号位不同, 作加法.
       + 若新的**余数与除数符号相同, 上商 1**; 否则上商 0.
     + 新的余数(指左移前的余数)与除数符号位相同, 则 $R_{i+1}= 2R_i-Y$, 即`余数=余数<<1-除数`;否则$R_{i+1}= 2R_i+Y$
   + 商的修正:
     + **商左移一位. 若被除数和除数异号(即商为负), 商加一**
     + 若余数与被除数符号不同:
       + 若被除数和除数同号,余数加除数 
       + 若被除数和除数异号,余数减除数
     + 注意：若做完如上修正后，余数为除数相反数，需要将余数置为0，同时商减一
   + 示例:
     <img src="https://i0.hdslb.com/bfs/article/35ad64b739a0dbd5d9908dcf33a496f7bd10bac0.png" >

#### BCD 码

+ 每 4 位二进制数表示十进制的一位数

+ 加法:由于真值的进位是 10,而 BCD 码的进位是 16,所以在真值产生进位的时候需加 6 强制进位.

+ 减法:类似于补码减法. BCD"补码"与原码相加得 9.若结果是负数("补码"表示),需转化成负号+原码的形式.
  $𝑁1−𝑁2=𝑁1+(10^𝑛−𝑁2)$
  **计算补码**

  “Invert” 每一位, 并在最后一位加一(注意：这里的位指的是整个NBCD数的最后一位！)
  **“Invert” NBCD数位**

  - 反转每一位,并加上 “1010”
  - 加上“0110”, 并反转每一位



### FPU

> - Lecture06

#### 浮点数的加减运算

$X=X_S \times 2^{X_E},Y=Y_S \times 2^{Y_E}$

+ 步骤
  1. 检查是否为零
  2. 阶码对齐,尾数移位
  3. 对尾数加或减
  4. 标准化结果
  5. 溢出判断

1. 对阶

   1. 求阶差
      $\Delta E=\begin{cases}
        =0,已经对齐\\
      \ne0,\begin{cases}大的向小的对齐:减小较r大的阶码,同时扩大其尾数\\小的向大的对齐:增大较小的阶码,同时减小其尾数 \end{cases} \\
      \end{cases}$
      在计算机中,尾数左移可能会使最高位数据丢j失,故采用小阶向大阶对齐
      ![浮点数加减](https://i0.hdslb.com/bfs/article/deb6114c1afee838908c5071612f84f69a0fa8d0.jpg)

    <center>浮点数加减的过程</center>

##### 一些溢出情况

###### 1. Exponent overflow

  + 一个正的指数超出了指数的最大值(即127)
  + 指定为$-\infty 或 +\infty$

###### 2. Exponent underflow

  + 一个负的指数小于了指数的最小值(即-126)
  + 指定为0.

###### 3. Significand overflow

  + 同号的两个数字相加时,在最重要的位上产生了进位.
  + 在realignment时修正

###### 4. Significand underflow

  + 在对齐尾数的时候, 数据可能从尾数的最右端流失
  + 需要某种形式的四舍五入

##### 原码加减法(用于尾数的加减)

+ 如果两个操作数符号相同,做加法,否则做减法.

  + 加法:
    + 若最高位产生了进位,溢出
    + 符号同加数
  + 减法:加第二个数的补数
    + 若最高位产生进位,结果正确(符号等同于被减数)
    + 若没有进位,应该取结果的补数,最终结果与被减数相反.
      注意:此处可以是认定为没有符号位的补码在做计算,所以最终结果需要进行修正.(因为正数补码是它自身,负数补码是其反码加一) 
      ![浮点数运算源码加减法](https://i0.hdslb.com/bfs/article/baa713a920ac0acf967f9b22dda0cc73973d0598.png)

  更通俗的说法:最终算A+B的时候(无论是一开始就是A+B还是减法转化而来).如A,B同号,尾数是正常相加;若A,B异号,尾数为$A_S+[B_S]_补$

##### 浮点数加减法举例

+ 减法
  0.5-(-0.4375)=0.5+0.4375=0.9375
  0.5&emsp;&emsp;&emsp;<font color=RED>0</font>&emsp;<font color=BLUE>01111110</font>&emsp;<font color=GREEN>00000000000000000000000</font>
  -0.4375&emsp;<font color=RED>1</font>&emsp;<font color=BLUE>01111101</font>&emsp;<font color=GREEN>11000000000000000000000</font>
  &ensp;0.4375&emsp;<font color=RED>0</font>&emsp;<font color=BLUE>01111101</font>&emsp;<font color=GREEN>11000000000000000000000</font>
  <font color = BLUE>01111110-01111101=01111110+10000011=00000001</font>
  则前者阶码比后者大,后者向前者对齐(后者阶码加1,尾数右移一位,此处尾数包含隐藏位，即橙色位).减法经处理后,两个操作数同号,尾数做正常加法

  <center>&emsp;<font color=#FF8500>1</font>&emsp;<font color=GREEN>0000...00</font></center>
  <center>+&ensp;<font color = GREEN>0</font>&emsp;<font color=#FF8500>1</font><font color=GREEN>110...00</font></center>
  <center>——————————</center>
  <center><font color=#FF8500>&emsp;1</font>&emsp;<font color=GREEN>1110...00</font></center>

  加法计算没有进位，则结果正确，为

<center><font color=RED>1</font>&emsp;<font color=BLUE>01111101</font>&emsp;<font color=GREEN>11000000000000000000000</font></center>

+ 加法
  0.5+(-0.4375)=0.0625
  0.5&emsp;&emsp;&emsp;<font color=RED>0</font>&emsp;<font color=BLUE>01111110</font>&emsp;<font color=GREEN>00000000000000000000000</font>
  -0.4375&emsp;<font color=RED>1</font>&emsp;<font color=BLUE>01111101</font>&emsp;<font color=GREEN>11000000000000000000000</font>

  <font color = BLUE>01111110-01111101=01111110+10000011=00000001</font>
  则前者阶码比后者大,后者向前者对齐(后者阶码加1,尾数右移一位,此处尾数包含隐藏位，即橙色位).两个操作数异号,尾数加法做加后者补数.

  <center>&emsp;<font color=#FF8500>1</font>&emsp;<font color=GREEN>0000...00</font></center>
  <center>+&ensp;<font color = GREEN>1</font>&emsp;<font color=#FF8500>0</font><font color=GREEN>010...00</font></center>
  <center>——————————</center>
  <center><font color = RED>1</font><font color=#FF8500>&ensp;0</font>&emsp;<font color=GREEN>0010...00</font></center>

  符号相异产生进位,结果正确,与第一个操作数符号相同.经规格化后:

  <center><font color=RED>1</font>&emsp;<font color=BLUE>01111011</font>&emsp;<font color=GREEN>00000000000000000000000</font></center>

#### 浮点数乘法

![浮点数乘](https://i0.hdslb.com/bfs/article/16896fbb58f26550525aedbf82281f8eec4abede.jpg)

+ 步骤
  + 如果任何一个操作数为0,返回0.
  + 指数相加时需要减去偏差值,因为阶码用移码表示.
  + 尾数相乘.
  + 结果规格化并舍入.(可能造成指数溢出).

#### 浮点数除法

![浮点数除法](https://i0.hdslb.com/bfs/article/2489c91543786aa46bdfc31c6d4f6b1851450557.jpg)

+ 步骤
  + 除数为0,报错或设为无穷.
  + 被除数为0,设为0.
  + 被除数的阶码和除数的阶码做差,并加回偏差值.
  + 尾数相除.
  + 结果标准化并舍入.

**注意**:**和无符号整数除法不同**:浮点数除法给被除数后面填零存入余数和商寄存器,而整数是高位填零.

### 保护位

为了提高精度,在计算时每个数字都存在保护位,暂时储存着计算后(比如右移)后的超出低位的数据,到最后再将他们规约掉。（绝对值下取整/绝对值上取整/下取整/上取整）

### Transformer

> YDJSIR不清楚这是否是一个真正的物理单元，这里仅仅是提供一个逻辑上的概念。
>
> 当然即使真的是一个真正的物理单元，他也绝不像软院特色PA那么简单。
>
> 这部分内容在HW01里面应该展现得淋漓尽致了
>
> - Lecture03



# 寄存器

> - Lecture 15
>
> 注意到下面的这些寄存器的名字和X86中他们的名字并不完全相同！

## 寄存器的分类

### 用户可见寄存器

##### 1. 通用寄存器

可被程序猿指派各种用途。

> X86中的通用寄存器如下：
>
> ###### 数据寄存器
>
> `EAX` (Accumulator)：累加寄存器，也称之为累加器；**通用**
>
> `EBX` (Base)：基地址寄存器；**通用**
>
> `ECX` (Count)：计数器寄存器；**通用**
>
> `EDX` (Data)：数据寄存器；**通用**
>
> 不带E的是16位的，现在的X86_64又有别的解决方案但此处不展开。下面同理。

##### 2. 数据寄存器

仅可用于保持数据而不能用于操作数地址的计算。

##### 3. 地址寄存器

自身有某些通用性，或是专用于某种具体的寻址方式。

> ###### 指针寄存器
>
> `ESP` (Stack Pointer)：堆栈指针寄存器；**通用**
>
> `EBP` (Base Pointer)：基指针寄存器；**通用**
>
> ###### 变址寄存器
>
> `ESI` (Source Index)：源变址寄存器；**通用**
>
> `EDI` (Destination Index)：目的变址寄存器；**通用**
>
> ###### 段寄存器
>
> `ECS` (Code Segment)：代码段寄存器；
>
> `EDS` (Data Segment)：数据段寄存器；
>
> `ESS` (Stack Segment)：堆栈段寄存器；
>
> `EES` (Extra Segment)：附加段寄存器；

##### 4. 条件码寄存器

存放条件码，可用作程序分支的依据（如正，负，零，进位，溢出等）

### 用户不可见寄存器（大多数情况下）

##### 控制寄存器

控制CPU操作时用到的寄存器，其中`MAR`， `MDR`， `IR`为用户不可见，`PC`为用户可见寄存器。

##### 2. 控制和状态寄存器

##### 状态寄存器

存放条件码，至少部分用户可见。

CPU硬件设置这些条件位作为操作的结果。

例如：一个算数运算可能产生正的、负的、零或者溢出的结果。除结果本身寄存于寄存器或存储器外，一个条件代码亦同时被设置。这些代码被后面的条件转移指令所测试。

条件代码位被收集到一个或者多个寄存器当中，一般，它们构成控制寄存器的一部分。通常，机**器指令允许这些位以隐含引用的方式独处**，但是它们不能被程序猿更改。

> X86中的`Eflag`寄存器就是一个状态寄存器
>
> <img src="CPU.assets/v2-2b6dbe964630ba5a93a6f5fc999b5a66_r.jpg" alt="preview" style="zoom:67%;" />

##### PSW寄存器

存放程序状态字（程序状态字是在中断服务程序调用过程中，为了正确返回断点，需要保存程序现场，将一些存放软硬件状态的寄存器整合为一个大的寄存器，叫做程序状态字）普遍包括下列字段或标志：

- 符号：容纳最后算数运算结果的符号位
- 零： 当结果是零时被置位
- 进位：若操作导致最高位有向上的进位（加法）或结尾（减法）时被置位。
- 等于：若逻辑比较的结果是相等，则置位。
- 溢出：用于指示算数溢出。
- 中断允许/禁止： 用于允许或者禁止中断
- 监督：指出CPU是执行在监督模式下还是在用户模式中。某些特权的指令只能在监督模式下执行，某些存储器区域也只能在监督模式中被访问。

##### **一些其他的有关状态和控制的寄存器：**

1. 一个指向存储器快（如，进程控制块）的指针，此块含有另外的状态信息。

2. 使用向量式中断的机器中，可能提供一个有中断向量寄存器。

3. 若堆栈用于实现某些功能，则需要有一个系统堆栈指针。

4. 一个页表指针用于虚拟存储器系统。

5. /O操作控制方面也可能需要寄存器

### 其他相关概念

#### 1.段指针  

在具有分段寻址的机器中，一个段寄存器保持着该段的基地址。可有多个**段寄存器**。

#### 2.变址寄存器   

这些被用于变址寻址，并可能是自动变址的。

#### 3.堆栈指针

若有用户可见的堆栈寻址方式，则一般是堆栈在存储器中，而CPU内有一专用的寄存器指向栈顶。这允许隐含寻址，即`push`, `pop`和其他堆栈指令不需要显式的含有堆栈操作数。

## 设计出发点

> #### 到底该使用完全通用的寄存器，还是指定各寄存器的用途。

对指定寄存器的使用，一个操作数指定器所引用的寄存器类型通常能隐含在操作码中，操作数指定器必须做的只是证实这一组指定寄存器中的某一个将被使用，而不是所有寄存器中的某一个，于是节省了位数，但是，这又限制了程序猿的灵活性。

##### **寄存器数量**

寄存器过多，要求操作数指定器的位数会变多。

寄存器过少，导致更多的存储器访问。

##### 寄存器长度

寄存器的长度至少要能保存最长的地址。数据寄存器赢能保存大多数数据类型的值，某些机器允许两个相邻的寄存器作为一个寄存器来保存两倍长度的值。

## **设计考虑**

#### 操作系统支持。

某些类型的控制信息是专门为操作系统使用的。若CPU设计者对将要使用的操作系统有基本的了解，则寄存器组织可被扩展，而为此操作系统定制。

#### 控制信息在寄存器和存储器之间的分配。

普遍是将存储器最前面的几百或者几千字用于控制目的。设计者必须裁定多少控制信息应在寄存器中，多少应在存储器中。通常要在成本和速度之间进行权衡考虑。



# 指令集

## 指令集与指令执行过程

> - Lecture14

### 机器指令特征

CPU 的操作由它所执行的指令确定, 这些指令被称为**机器指令**. CPU 能执行的各种不同指令的集合称为 CPU 的**指令集**

#### 指令周期

指令周期: 指单条指令所需的处理过程

+ 取指令: 每次从内存中取一条指令
+ 执行指令: 执行每条指令

只有关机时, 程序执行才会停止, 或者遇到致命错误或者停止计算机的指令(hlt).

![](CPU.assets/e0b030becf80bf0525dff71c910c7fd93f851e23.jpg)

指令周期状态图:

![](CPU.assets/fc3cf8430f22ca3143d4b55650b07d2f47769ebb.jpg)

#### 带有中断的指令周期

带有中断的指令周期:

![](CPU.assets/e359c98a128d51005b90238847730a9b415ed433.jpg)

带有中断的指令周期状态图:

![](CPU.assets/5ee92d9d51c48e12f4947cd45c4c03b9e5cf9a63.jpg)



#### 机器指令要素

+ **操作码:**指定要执行的操作 

+ **源操作数引用:**操作会涉及一个或多个源操作数， 这是操作所需的输入

+ **结果操作数引用:**该操作可能产生一个结果

+ **下一指令引用:**它告诉处理器这条指令执行完成后到哪儿去取下一条指令

#### 指令表示

+ 每条指令都由一个位序列表示
+ 指令格式:指令被划分为字段，对应于指令的要素
+ 对于大多数指令集，使用一种以上的格式

![](CPU.assets/aaf8ff21d23a6df8b0e9fecc9049d71436d4f6a8.jpg)

+ 符号表示:帮助程序员和教科书的读者处理指令
+ 操作码用缩写表示，称为助记符
+ ADD: ADD, SUB: subtract, MUL: multiply, DIV: divide，
+ LOAD:从内存加载数据，STOR:将数据存储到内存
+ 操作数也用符号表示
+ 用寄存器名或内存地址替换操作数

#### 指令类型

+ **数据处理**:算数和逻辑指令
+ **数据存储**: 存储器指令
+ **数据传送:**I/O指令
+ **控制:** 测试和分支(branch)能力

### 操作类型

+ Data transfer
+ Arithmetic
+ Logical
+ Conversion
+ I/O
+ System control
+ Transfer of control

### 操作数类型

+ 地址
+ 数字
+ 字符
+ 逻辑(布尔)量

### **大端小端**

如图，把12345678（16进制）存进地址184

#### 左为大端法，右为小端法。

##### X86和ARM都是小端！读取的时候要小心！

![img](CPU.assets/clip_image001.png)

 

##  指令集:寻址方式和指令格式

#### 基本概念的定义

+ `A`: 指令中地址字段的内容
+ `R`: 指向寄存器的指令字段的内容
+ `EA`: 被访问未知的实际(有效)地址
+ `(X)`: 存储器位置 X 或者寄存器 X 的内容

### 立即寻址 (Immediate Addressing)

##### 操作数存在于指令中

$$操作数 = A$$

**应用:** 定义和使用常数, 或者设置变量的初始值.

**优点**: 获取操作书不需要访问存储器, 只获取指令

**缺点**: 数字的大小被限制为地址字段的大小

![](CPU.assets/5cf337a0b87f1d66a6e01b116b723b19c6838e0b.jpg)

### 直接寻址 (Direct Addressing)

#### 地址字段包含着操作数的有效地址, 早期计算机常见

$$
EA = A
$$

**优点**: 只有一次存储器访问, 不需要进行专门计算

**缺点**: 只能提供有限的地址空间

<img src="CPU.assets/8ff6aaf8a8134196fe5e560e0b8b8105b51e453a.jpg" style="zoom:50%;" />

### 间接寻址(Indirect Addressing)

#### 指令中地址字段只是一个存储器字地址, 而这个地址保存着操作数的全长度地址

$$
EA = (A)
$$

**优点**: 扩大了寻址空间

**缺点**: 需要访问两次内存来获取操作数

**评价**: 一次能够引用的不同地址数存在限制

<img src="CPU.assets/9657b9ecdc5d20d12fa932315c15466aeb8862e8.jpg" style="zoom:50%;" />

#### 寄存器寻址 (Register Addressing)

类似直接寻址, 地址字段指的时寄存器而不是一个主存地址.

$$
EA = R
$$



**优点**: 指令中只需要一个很小的地址字段用来指向寄存器, 不需要访问内存

**缺点**: 寻址空间极其有限

**注意**: 只有寄存器得到了有效的使用才有意义

<img src="CPU.assets/3a7e86bcb49b1a1a6f7ab1bc5ca207ea2b73731c.jpg" style="zoom:50%;" />

#### 寄存器间接寻址(Register Indirect Addressing)

地址的字段指向一个寄存器

$$
EA = (R)
$$


优点: 扩大了寻址空间, 比间接寻址少访问一次主存

劣势: ?

<img src="CPU.assets/36de30ca257d4106306ec9e3a890b5685f3c61a9.jpg" style="zoom:50%;" />

### 偏移寻址(Displacement Addressing)

结合直接寻址和间接寻址

$$
EA = (R) + A
$$


指令中有两条地址字段, 其中至少一个是显性的. 其中一个地址字段(val = A) 被直接使用, 另一个地址字段指向寄存器. 寄存器的内容加上 A 产生有效地址.

#### 1.**相对寻址**

隐式引用的寄存器时程序计数器`PC`, 即当前 PC 的值 (为现执行指令的下一条指令的地址), 加上地址字段的值(A, 通常为补码整数), 得到有效地址

$$
EA = (PC) + A
$$

**优点**: 利用了程序局部性的概念, 并在指令中保存了地址位.

**用途**: 子程序跳转?

#### 2.**基址寄存器寻址**

引用的寄存器含有一个主存地址, 地址字段含有一个相对于那个地址的偏移量(usually unsigned)

可以是显式引用, 也可以是隐式引用

$$
EA = (R) +A
$$

#### 3.**变址**

地址字段引用一个主存地址, 被引用的寄存器对于那个地址有一个正的偏移量

$$
EA = A+(R)
$$

用法: 高效完成重复操作, 将值 A 存入指令的地址字段, 选取一个寄存器作为变址寄存器, 初始化为0, 每次操作之后, 变址寄存器加1

扩展:结合间接寻址和变址:

+ 后变址: 间接寻址之后变址

  $$
  EA = (A) + (R)
  $$

+ 前变址: 变址在间接寻址之前

  $$
  EA = (A+(R))
  $$

### 栈寻址

栈指针维护在寄存器中, 所以对内存栈位置的访问实际上是一种寄存器间接寻址方式.

注意: 与栈相关的是一个指针, 它的值可能是栈顶地址或者第三个元素的地址(前两个可能已经进入寄存器)

> 特别适合程序多重调用的情况。另一种情况是将返回地址放在寄存器里面。DLX里面已经提到。

> ### X86实例
>
> ![image-20210117155904254](CPU.assets/image-20210117155904254.png)

### 指令格式

指令格式通过它的各个构成部分来定义指令的位安排。一个指令格式必须包括一个操作码，以及隐式或者显示的、零个或多个操作数。

学会指令集的计算（容量）和防止二义性的措施（通过不同的前x位字符做区分，操作码放前面，参数放后面）。

#### 指令长度

权衡考虑：强有力的指令清单与必须要节省空间。

但是有时候和处理器字长对齐也是一件好事。

#### 位的分配

对于一个给定的指令场地，很清楚在操作码数目和寻址能力之间有一个权衡考虑的问题，越多的操作码意味着操作码字段要更多的位，这就减少了寻址可用的位数。

采取变长的操作码：有一个最小操作码长度，但是对于某些操作码，可使用指令附加位的方法来指定附加的操作。

> X86正是如此

#### 影响因素

1. 寻址方式的数目

2. 操作数数目

3. 寄存器与存储器比较

4. 寄存器组的数目

5. 地址范围

6. 地址粒度

### 中断

有了中断，处理器可以在进行 I/O 操作时执行其他指令。提供中断主要是为了提高效率，因为大部分外设的速度都比处理器慢得多，假如没有中断，每次 I/O 操作后处理器都会进入空闲状态直到外设跟上进度。

+ 默认开，但是在执行一些特殊的不能中断的任务的时候会中断；

+ 程序可以在执行指令的时候执行另一条指令

  <iframe frameborder="0" style="width:100%;height:280px;" src="https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1#R3VjLcpswFP0abTO8H0uwcbtoZzqTRZOlYlRQByNGyLGdr68EEkKGpHk4dpJMJiMdriR07rmPANzFZv%2BNwqb8SXJUAcfK98BdAsfxHZf%2FFcChB1wn7oGC4ryHbA1c4wckQUuiW5yj1jBkhFQMNya4JnWN1szAIKVkZ5r9IZV5agMLNAGu17Caor9xzsoejZxQ498RLkp1sh3I%2B22gMpY3aUuYk90IcjPgLighrB9t9gtUCe4UL%2F261SNPhxejqGbPWRCo92AHdTmU87vKKaGsJAWpYZVpNKVkW%2BdI7GDxmbb5QUjDQZuDfxFjB%2Bk4uGWEQyXbVPIp2mN2Mxrfiq2ufDlb7uXO3eSgJjWjh5vxZLRKTPWybqbW9fcTl3qUIgm1ZEvX0sr3pKwgLZA084PBQVzYiGwQP4fbUFRBhu%2FN%2FaGUWDHYaS%2FwgXTEvFPU4few2spdQeaDdAEiSwySEETpxG%2FaK4LWXYkZum5gd6Edj0LTA%2FIARBnaP83L9L4yaCMpnZ2OAFvJuhypX0nsLYwE9uS6H1Smr5RbMCO38FxyC2blFq1AHIDMA2kk5CYHXIABiJcgscUg4pIMu0cpSLwnJGm9ryTVAqXJS0jU%2BeISDWckGp1JosFUW2ckVxN6O%2Bbz5OS%2BgUi59BfB%2FBQdD74ZD%2F6RzntfykXaGwml8DAya4RB%2B%2Fgxnu3NHbN62VtpKfTna2EMhDxLK%2BFFWpoP5XfPdq%2Fi8Y%2FB95Al%2FyODV3CvkoRRSniZiEXPkkWiavCSMVM4ArgR5aC%2Ba5uBzAsWEtc3FX3WQuJ%2BIv2%2BtQA8L0PY9vskrsAzz3Fflrjc0yaunsxJ8CSu6rpWIPG7wUJElBiEILFkZ5YsOyQQg0uHjx9fsA%2FzZ1icMCT6W%2F5rd0kpE0%2BPOeO3ZyYxsMJFzcdrzgKiHBAc4TWsEvlgg%2FO8j0bU4gd4120lGJc65Pv6KfCXYi8egG0fi6fi3DI5j6ecBzOUO6egfO4fiCnlXKxBR3k3Tab98mejfNL3ROejfK7Qzqk8tkESyaTBE8hnp%2Fw4s9hnVPl8ej7ubb4c5Z51OcrjGcqHLxO%2BqIvpV6R80v%2B8G%2BV8qj829z2L%2FmLvZv8A"></iframe>


### 处理中断处理

+ 顺序处理
+ 根据优先级决定优先处理的指令

> 关于外部设备对中断的处理方面，详情请看`IO.md`。



# 控制器

> - Lecture16

## 微操作

执行程序的时候，计算机操作由一序列指令周期组成，每周期执行一条极其指令。每个指令周期又能看做是由几个更小的单位组成。一种通常的方法是分解成取指、间址、执行和中断，只有取指周期和执行周期总是必有的。

事实上，这每个较小的周期又由一串涉及到CPU寄存器操作的更小的步骤组成，人们将这些步骤称位**微操作**。

![img](CPU.assets/clip_image002.jpg)

### 两个简单原则

1.时间流动的顺序必须是恰当的。

2.必须避免冲突。不要试图在一个时间单位内取读、写同意寄存器，否则结果不可预料。

## 数据流

![image-20210116214912860](CPU.assets/image-20210116214912860.png)

#### **取指周期**

**T1:  MAR<- PC**

**T2:  PC<-PC+1**

​          **MBR <- Memory**

**T3:  IR<- MBR**

`PC+1`也可以在T3执行。

![image-20210116215019057](CPU.assets/image-20210116215019057.png)

#### **间址周期**

**T1 ： MAR <- (IR(地址））**

**T2：MBR <- Memory**

**T3 :  IR <- (MBR(地址））**

![image-20210116215225007](CPU.assets/image-20210116215225007.png)

#### **中断周期**

**T1 : MBR <- (PC)**

**T2 : MAR <- SAVE_ADDRESS(** **保存当前指令与存储器的地址）**

​         **PC<-**目标指令地址(子程序地址）

**T3：Memory <- (MBR)**

![image-20210116215256198](CPU.assets/image-20210116215256198.png)

#### **执行周期**

**ADD R1 X:**

T1：MAR <- (IR(地址））

**T2 : MBR <- Memory**

**T3 : R1 <- (R1)+(MBR)**

## 指令流水线

#### **流水线策略**

一个产品经过几个制作步骤。通过把制作过程安排在一条装配线上，产品能在各个阶段同时被加工，这种过程被称为流水处理。

事实上，指令的指令也是可以被分成几个步骤的。

 

### **二分法：取指令和执行指令。**

在一条指令执行期间，有主存未被存取的时间。这个时间能用于取下一条指令，从而取址过程与当前指令的执行并行工作，可有效提高CPU工作效率。

![image-20210116223628910](CPU.assets/image-20210116223628910.png)

#### **可能的问题**

1. 执行的时间一般要长于取时间。于是，取指阶段可能必须等待一定的时间才能排空它的缓冲器。

2. 条件转移指令使得待取的下一条指令的地址是未知的。于是，取指阶段必须等待它由执行阶段得到下一条指令地址。而在取下一条指令时执行阶段又可能必须等待。

### 六分法

> 这里只做课堂教学示意用，事实上现实中何止分六部分！
>
> **第二代**Pentium 4北木核心（Northwoog）就已经使用了20级流水线了！
>
> 但是，并不是流水线层级越多效率越高的。原因如下：
>
> 1. 每个阶段都有涉及缓冲器间移动数据和各种准备和传送命令的花销
> 2. 处理逻辑会变得更加复杂
>
> |                                                              |                                                              |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | ![image-20210116224002785](CPU.assets/image-20210116224002785.png) | ![image-20210116221555546](CPU.assets/image-20210116221555546.png) |
>
> 
>
>   ![image-20210116224012046](CPU.assets/image-20210116224012046.png)

![image-20210116223643405](CPU.assets/image-20210116223643405.png)

##### 取指令（FI） 

读下一个预期的指令到缓冲器

##### 译码指令（DI）

确定操作码和操作数指定器

##### 计算操作数（CO）

计算每个源操作数的有效地址，这可能涉及到偏移、寄存器间接、间接或其他形式的地址计算。

##### 取操作数（FO）

由存储器取每个操作数。寄存器中的操作数不需要取

##### 执行指令（EI）

完成指定的操作。若有指定的目标操作数位置，则将结果写入此位置

##### 写操作数（WO）

将结果存入存储器。

### 问题

1. 不是所有的指令都可以被分为6个阶段

2. 不是所有的阶段都可以并行处理（如同时需要对内存进行存取）

3. 6个阶段所需要的时间不等价，可能会有一定的等待

4. 条件转移会导致一些指令的作废

5. 中断

### 性能

$T_i$ = 流水第i段的电路延迟时间

$T_m$= 最大段延迟（通过延时最长段的延迟）

$k$ = 指令流水线段数

$d$ = 锁存延时 （数据和信号送到下一段所需要的锁存接收时间）（课上好像没讲）

$$
T= max[Ti]+d = T_m+d
$$

通常情况下，延迟d等于时钟脉冲的宽度切$Tm>>d$。

假设现在有n条指令在进行，无转移发生。那么执行所有n条指令所需要的时间是：

$$
T_{k,n} = [k+(n-1)]T
$$

所以说流水线的加速比是
$$
S_k = \frac{T_{1, n}}{T_{k_n}} = \frac{n k t}{[k + (n - 1)]t} = \frac{n}{1 + \frac{n - 1}{k}}
$$


### 冒险（Hazard）

在一些情况下指令流水会堵塞，后面的指令不能被正确地按照预读取的方法执行。

#### 结构冒险

###### 原因：同一个设备被不同的指令使用

一个设备在一个指令中只被使用一次。

##### 解决方法

使用多个不同的设备。

#### 数据冒险

##### 原因：指令需要的数据还未产生

#####  解决方法

###### a)   嵌入无操作指令

| 插入NOP（软件）                                              | 插入“气泡”（硬件）                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20210116224140356](CPU.assets/image-20210116224140356.png) | ![image-20210116224209801](CPU.assets/image-20210116224209801.png) |

想想都知道这样有多么低效！

###### b)   暂停当前指令执行，直到数据产生

效率更低了……

###### c)   转发/绕过

<img src="CPU.assets/image-20210116224336542.png" alt="image-20210116224336542" style="zoom:80%;" />

前半个周期你用，后半个周期我用，就是这么自信

###### d)   调整指令顺序

编译器优化着力点之一。当然也有可能是硬件实现的。

|                                                              |                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20210116224507764](CPU.assets/image-20210116224507764.png) | ![image-20210116224539196](CPU.assets/image-20210116224539196.png) | ![image-20210116224549526](CPU.assets/image-20210116224549526.png) |

#### 控制冒险

指令执行顺序被改变导致预先执行的部分无效。

##### 原因

##### a)   转移指令：条件转移，循环…

|                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20210116223707592](CPU.assets/image-20210116223707592.png) | ![image-20210116223916599](CPU.assets/image-20210116223916599.png) |

###### b)   中断

<img src="CPU.assets/image-20210116223831189.png" alt="image-20210116223831189" style="zoom:80%;" />

###### c)   异常

###### d)   调用/返回

##### 处理方法

###### a)   多指令流

复制流水线的初始部分，并允许流水线同时取条件分支的两条指令，使用两个指令流。

###### b)   预取转移目标

识别出一个条件转移指令时，除了取此转移指令之后的指令外，转移目标处的指令也被取来。

###### c)   循环缓冲器

在流水线指令取阶段维护一个小的但极高速的存储器，含有n条最近取来的顺序指令。

###### d)   延迟转移

自动重排程序中的指令，以致一条转移指令出现在实际所要求的位置之后。

###### e)   分支预测：

​        i.     猜测绝不发生

​        ii.     猜测总是发生

​       iii.     依操作码预测：根据转移指令的操作码进行判定。处理器假定对某些条件转移指令的操作码将总是发生转移，对另外一些总是不发生。

​       iv.     发生和不发生切换

​        v.     转移历史表

> 作业中有一道很典型的题目（HW5的第10题），建议参考。
>
> ![image-20210116224751992](CPU.assets/image-20210116224751992.png)

## CPU控制的功能需求

通过把CPU的操作分解到它的最基础级，就能严格地定义控制器必定引起什么发生。于是，就可以定义控制器的功能需求，即控制器必须完成的功能。这些功能需求的定义是设计和实现控制器的基础。

### 3个步骤

#### **1.**定义CPU的基本元素

CPU的基本功能元素：ALU、寄存器、内部数据路径、外部数据路径、控制器。

#### 2.描述CPU完成的微操作

所有的微操作可按如下分类。

· 在寄存器之间传送数据

· 将数据由寄存器传送到外部界面（如系统总线)

· 将数据由外部界面传送到寄存器。

· 以寄存器作为输入、输出、完成算数或逻辑运算。

#### 3.确定为使微操作完成，控制器必须具备的功能。

##### 控制器的两个基本任务：

1. 排序：根据正被执行的程序，控制器使CPU以适当的顺序按步通过一串微操作

2. 执行：控制器使得每个微操作得以完成。

### 输入和输出控制器的一般模型

![img](CPU.assets/clip_image006.jpg)

#### 输入

##### 时钟 

控制器要每个时钟脉冲完成一个（或一组同时）的微操作。这有时被称为处理器周期时间或时钟周期时间。

##### 指令寄存器 

当前指令的操作码用于确定在执行周期内完成何种微操作

##### 标志 

控制器需要一些标志来确定CPU的状态和前面ALU操作的结局。

##### 来自控制总线的控制信号  

系统总线的控制线部分向控制器提供，如中断信号和认可信号这样的控制信号。

#### 输出

##### CPU内的控制信号    

1. 用于寄存器和他者之间传输数据

2. 用于启动指定的ALU功能

##### 到控制总线的控制信号 

1. 对存储器的控制信号

2. 到I/O模块的控制信号。

#### **三类控制信号**

- 启动ALU功能
- 控制数据路径
- 外部系统总线上的或者其他外部接口上的。

##### **例子：取指周期**

1. 传送PC的数据到MAR

启动控制信号打开PC与MAR之间的逻辑门。

2. 由存储器读一个字装入MBR并增量PC

A) 一个控制信号打开逻辑门，以便允许MAR的内容传送到地址总线

B) 一个存储器读控制信号送到控制总线

C) 一个允许数据总线上内容被存入MBR的开门信号

D) 对PC内容+1并返存PC逻辑的控制信号

接着，控制器发出打开MBR和IR之间门的控制信号。

#### **控制信号**

##### 1. 数据路径

##### 2.ALU

##### 3.系统总线

|                                      |                                      |
| ------------------------------------ | ------------------------------------ |
| ![img](CPU.assets/clip_image007.png) | ![img](CPU.assets/clip_image008.png) |

#### 控制器的最小性

控制器是整个计算机运行的引擎，它只需要知道将被执行的指令和算数、逻辑运算结果的性质（如 正负、溢出）。它不需要知道正在被处理的数据或者得到的实际结果具体是什么。并且，它控制人和事情只是以少量的送到CPU内的和送到系统总线上的控制信号来实现。

 

![img](CPU.assets/clip_image009.png) 

##### 处理器内部组织

- 使用一个CPU内部总线，ALU和所有CPU寄存器都链接到单一的内部总线上。

- 为将数据由各寄存器移到此总线上或者从此总线移出，提供了门和控制信号。

T1： MAR <- (IR(地址））

T2 : MBR <- Memory

T3 : Y<-(MBR)

T4: Z <- (AC)+(Y)

T5: AC <- (Z)



#### **两种控制器实现方式**

##### 硬连线实现

以硬连线实现，控制器本质上是一个组合电路。它的输入逻辑信号转换成一组输出逻辑信号，即控制信号。

##### 微程序实现



#### **关键输入**

**指令寄存器、时钟、标志、控制信号。**

其中，在标志和控制总线信号情况中，一般是每个位都有某种意义。然而另外两个输入对于控制器不是直接使用的。

##### 指令寄存器

a)   为简化控制其逻辑，应使每一操作码有一个唯一的逻辑输入。

b)   译码器完成这个功能，译码器有n位二进制输入和2^n个二进制输出。每一个都能激活唯一的输出。

c)   控制器的译码器更加复杂，要考虑到变长的操作码。

##### 时钟

A) 时钟脉冲周期要足够长，以允许信号能够沿着数据路径传播和通过CPU电路。

B) 控制器在一个指令周期以不同的时间单位发送不同的控制信号

C) 使用一个计数器作为控制器的输入，以不同的控制信号做T1.T2等等

![img](CPU.assets/clip_image010.png)

##  ICC

1.取指、间址和中断周期都各有一个序列，而对于执行周期则是每一操作码有一个序列。

为完善此模型，需要将微操作序列连接在一起。我们假设一个2位的新寄存器，叫做指令周期代码(ICC)，此ICC定义了CPU处于周期哪一部分的状态。

|  00  |  01  |  10  |  11  |
| :--: | :--: | :--: | :--: |
| 取指 | 间址 | 执行 | 中断 |

![img](CPU.assets/clip_image004.jpg)

 **控制器逻辑**

为每个控制信号得到一个布尔表达式。

PQ=00 取指周期

PQ=01 间址周期

PQ=10 执行周期

PQ=11 中断周期

C5控制的是使得外部数据总线上的数据被读入MBR

![img](CPU.assets/clip_image011.png)

即控制信号仅仅在取指和间址周期的第二个时间单位有效。

当然这个表示还不完整。 ![img](CPU.assets/clip_image013.jpg)

## IO模块

> 在`IO.md`里展开

## MMU

> 在`Memory&Cache`里展开

# 性能评估

> - Lecture01

### CPU - 性能

#### 衡量 CPU 性能的依据

$$
CPI =\frac{ \sum_{i=1}^n(CPI_i\times I_i)}{I_C},I_C = \sum_{i=1}^n I_i,
$$

$$
I_i 为某种指令的条数, CPI_i为某种指令的时钟周期数, I_C 为总的指令数,
$$

$$
则 CPI 为每条指令的平均时钟周期数,
$$

$$
T = I_C \times CPI \times t, t 为时钟周期,
$$

![image-20210116220321145](CPU.assets/image-20210116220321145.png)

$$
IPS(每秒钟总指令数) = \frac{f}{CPI} = \frac{I_C}{T} ,对应有MIPS，要 \times 10^{-6}
$$

$$
MIPS\ = \frac {I_c}{T \times 10^6 } = \frac {f}{ CPI \times 10^6 } 
$$



RAM - 容量与速度……

IO - 容量与速度……

BUS - 速度……

 ……

### 主要目标

CPU速度的提升