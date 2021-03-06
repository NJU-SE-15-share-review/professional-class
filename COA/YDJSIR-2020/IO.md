# IO

> Powered by $YDJSIR$
>
> - Lecture17
> 

## Peripheral Device：外部设备

### 外部环境←→外部设备←→计算机

### 人类可读

> 显示器、打印机

### 机器可读

> 硬盘、磁带

### 通信

> 本课程不涉及

### 为什么不直接把外部I/O设备连接到总线

1.设备种类繁多，相应的操作方法繁多

2.很多I/O设备的数据传递很慢，如果连接到总线，会拖慢处理器或者主存的速度。

3.很多I/O设备的数据传递太快，使得主存或者处理器没有办法处理。

4.外部设备可能会使用不同的数据格式，不同的字长。

## I/O模块

位于外部设备与总线之间（桥梁作用）

![img](IO.assets/clip_image002.png)

### 同I/O模块的交互途径

#### 1. 控制信号

#### 2.状态信号

两者连在控制逻辑上。

#### 3.数据交换

缓冲区（8-16位）

#### 控制与计时

1. CPU与外部设备以一种非预期的方式进行交互。

2. 一些资源得到共享。

#### I/O模块与处理器之间的通信

1. 解码
2. 数据交换
3. 状态报告
4. 地址识别

#### I/O模块与外部设备之间的通信

1. 命令状态
2. 数据交换

数据缓冲以及纠错

#### I/O模块的其他称呼

I/O通道 I/O处理器 I/O控制器 设备控制器

### IO操作

![img](IO.assets/clip_image002-1610709626276.png)

#### 两种寻址方式

**存储映射式寻址**：存储单元和I/O设备有单一的地址空间，处理器把I/O模块的状态、数据寄存器看成存储单元一样对待，并使用相同机器指令存取存储器和I/O设备。

**分离式寻址：**地址空间与存储器是分离的。总线既有存储器读线和写线，又有输入和输出命令线。

### 编程式IO与中断驱动式IO

| 编程式IO                                                     | 中断驱动式IO                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![img](IO.assets/clip_image001.png)                          | ![img](IO.assets/clip_image001-1610709862598.png)            |
| 1.发送一个命令到I/O模块<br/>2.I/O模块完成被请求的动作，<br/>然后再I/O状态寄存器中的某位进行设置<br/>此过程中处理器不停地检查I/O模块<br/>的状态，<br/>I/O模块不会向CPU发送中断请求,<br/>所以此过程中CPU一直处于忙状态<br/>3.准备就绪后，处理器从I/O模块<br/>读取字，并向存储器写入字。 | 处理器发出一条命令，<br/>继续处理下一条指令，<br/>直到I/O模块完成操作后，<br/>中断CPU<br/>**从I/O模块视角看：**<br/>1. 收到读的命令<br/>读的数据到寄存器<br/>2. 引发中断<br/>3. 等到CPU响应中断<br/>4. 将数据传送到数据总线上<br/>**从CPU视角看：**<br/>1. 发送命令<br/>2. 做其他事情<br/>3. 在某个指令周期结尾判断是否有中断<br/>4. 保存环境相应中断<br/>5. 获取数据并写入内存<br/>6. 恢复环境 |

##### 处理方式

1. 加线（IO设备太多加不完的，始终得回到下面那三种）
2. 轮询（慢）
3. 菊花链
4. 总线仲裁

##### 优先级

> 多线：多处理器处理
>
> 轮询：轮询顺序
>
> 菊花链：先后
>
> 总线仲裁：优先级

###### 响应优先级

终端一起过来的时候先处理谁

###### 处理优先级

屏蔽字：由处理优先级决定

它可以屏蔽自己以及优先级比自己低的中断，但是面对处理优先级比自己更高的终端，哪怕正在处理一个响应优先级更高的终端，CPU也得乖乖地让出来优先处理新来的中断。

![img](IO.assets/clip_image002-1610710757014.png)

### DMA

 I/O模块与主存直接进行数据交换 不需要CPU参与。

|                      全过程                       |                       展开                        |
| :-----------------------------------------------: | :-----------------------------------------------: |
| ![img](IO.assets/clip_image001-1610710886249.png) | ![img](IO.assets/clip_image001-1610710879341.png) |

CPU想要读或者写数据块的时候，发送一个命令给DMA模块，包括以下信息

a)   是请求读还是写，使用处理器和DMA模块之间的读或者写控制线；

b)   所涉及的I/O设备地址，经数据线通知；

c)   读或写存储器中的起始单元地址，经数据线通知并被DMA模块存入它的地址寄存器中；

读或写的字数，经数据线通知并被DMA模块存入他的数据计数寄存器中。

#### 处理和CPU的抢占总线问题

为了传输数据给存储器或者从存储器中取出数据，DMA需要占用控制总线，因此只有在CPU不需要总线或者强制CPU暂时挂起操作的时候才能使用总线。

| 终止CPU                                                      | 周期窃取法                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![img](IO.assets/clip_image002-1610711077195.png)            | ![img](IO.assets/clip_image002-1610711111554.png)            |
| **优点**：方便控制<br/>**缺点：**影响CPU正常工作，没有办法使得主存得到充分利用。<br/>*适合高速I/O设备* | **优点**：使得CPU与内存得到充分利用，即使得到I/O请求<br/>**缺点：** DMA需要每次申请<br/>*适合周期较长的I/O* |

| Alternate访问                                     |      |
| ------------------------------------------------- | ---- |
| ![img](IO.assets/clip_image002-1610711487486.png) |   优点：CPU既没有停止也没有等待，DMA不需要请求总线<br/>适合： CPU的处理周期大于 存储器的处理周期。 |

#### 连接方式

##### 单总线

###### 独立DMA

a)   所有模块共享一条系统总线

b)   DMA模块使用编程式I/O来交换数据

c)   廉价但是效率低

###### 继承DMA与I/O

a）除了系统总线之外，DMA模块与一个或者更多的I/O设备之间有通道

b）减少总线周期

##### 多总线


