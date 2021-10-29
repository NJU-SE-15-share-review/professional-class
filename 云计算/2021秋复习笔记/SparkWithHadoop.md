# `Spark with Hadoop`

# `Hadoop`

## 概论

> - 面向数据存储和加工的平台
> - 定义好编程模型和接口
> - 用户编写Application，提交到平台：服务App vs. 运算App
> - 开源，面向数据分析
> - 不一定要在云上：分布式编程模型

### 问题

#### 存储

- 单机容量足够，各机器上的文件要求对外显示它们存于同一硬盘空间；

- 文件大小超出单机容量，要求利用多台机器存入后对外显示依旧为一个完整文件；

#### 计算

> 比如说数单词

#### 可靠性

应对宕机

> 网络开销、利用率、成本

### 分布式解决方案

#### 冗余存储与冗余计算

- 解决可靠性问题——不单纯靠额外增加设备的备份

- 将每台机器上存储的数据同时存于集群中的另一台机器上

- 将每台机器上数据的计算也同时在冗余数据的机器上计算

- `CMaster0`明确知道每一份数据都存储在多个地方

- `CMaster1`会要求存有待计算数据的机器都参与计算，并选择先结束的机器计算结果

冗余存储不仅提高了分布式存储的可靠性，也提高了分布式计算的可靠性。

> 分布式存储和分布式计算可以相互独立存在

#### 分布式存储（`Distributed File System, DFS`）

将多台机器硬盘以某种方式连接到一起

取机器`cSlave0`，`cSlave1`……和`cMaster0`，采用客户-服务器模式构建分布式存储集群。

让`cMaster0`管理`cSlave0`，`cSlave1`……。

##### 对内：客户-服务器模式

只要保证`store master`正常工作，我们很容易随意添加`store slave`，硬盘存储空间无限大。

##### 对外：统一存储空间，统一文件接口

整个集群就像是一台机器、一片云，硬盘显示为

统一存储空间，文件接口统一。

#### 分布式计算

> “移动计算比移动数据更划算”——`Google`论文

##### 计算的并行-`Map`

![image-20211015092645930](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015092645930.png)

##### 合并的并行-`Reduce`

![image-20211015092905250](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015092905250.png)

> 经过洗牌之后，合并的时候分布的文本某一个特定单词的计数都送到某一个节点上进行合并，不同单词之间的合并技术可以并行。

### `Hadoop`简介

#### 渊源

- `Apache`成立开源搜索引擎项目`Nutch`——但开发过程中无法有效地将计算任务分配到多台机器上；

- 前后`Google`陆续发表`GFS`、`MapReduce`、`BigTable`（谷歌三板斧）；

- `Apache`借鉴`GFS`和`MapReduce`，实现了自己的`NDFS`和`MapReduce`；

- 发现`Nutch`侧重搜索，而`NDFS`和`MapReduce`偏向通用基础架构，将`NDFS`和`MapReduce`移出；`Nutch`，成为独立开发项目，称为`Hadoop`；

`Hadoop 1.0` （1.X的统称）和 `Hadoop 2.0` （2.X的统称）架构差异较大。

#### 简介

> 可看作是`Google Cloud`的开源版本；但并不拘泥于复现`Google Cloud`的相关产品。
>
> | **Hadoop**          | Google              | 描述           |
> | ------------------- | ------------------- | -------------- |
> | `Hadoop  HDFS`      | `Google  GFS`       | 分布式文件系统 |
> | `Hadoop  MapReduce` | `Google  MapReduce` | 分布式计算     |
> | `HBase`             | `Google  BigTable`  | 分布式数据库   |
> | `ZooKeeper`         | `Google Chubby`     | 消息队列       |
> | `Pig`               | `Google  Sawzall`   | 脚本语言       |

通过调用程序库，可使用简单的编程模型处理分布在不同机器上的大规模数据。

采用客户-服务器模式，很容易从一台机器扩展至成千上万台机器，每台机器均能提供本地存储和本地计算。

##### `Hadoop 1.0`

- `Hadoop Common`：支持其他两个模块的公用组件

- `Hadoop DFS`（`HDFS`）：分布式文件系统

- `Hadoop MapReduce`：分布式计算框架

##### `Hadoop 2.0`

![image-20211015170805021](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015170805021.png)

- 分布式操作系统`Yarn`

- `ZooKeeper`：通用的分布式集群的数据管理者

  不仅仅只是为`Hadoop`服务！集群化思想

  - 统一命名服务
  - 配置管理
  - 集群管理

- `Hbase`：开源分布式数据库

  - 高可靠性

  - 高性能

  - 列存储

  - 可伸缩

  - 实时读写

  **逻辑模型**：用户对数据的组织形式

  `行键、列（<列族>:<限定符>）、时间戳；字节码，无类型`

  **物理模型**：在设备上具体存储形式

  将行按照列族分割存储；逻辑空值无存储

#### 应用领域

##### 构建大型分布式集群（存储+计算）

- 最直接的应用

- 构建大型分布式集群，提供海量存储和计算服务

- 类似产品中国移动“大云”、淘宝“云梯”

##### 数据仓库（存储）

存储半结构化业务数据，通过`Hive`、`Hbase`提供报表查询之类服务

##### 数据挖掘（计算）

- 大数据环境下的数据挖掘思路和算法没有太大变化

- 硬盘性能和内存大小带来的限制——通过分布式集群解决硬件限制

#### 部署方式

传统解压包（繁琐易错）和标准`Linux`部署方式（简单易用）

![image-20211015095217686](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015095217686.png)

> 注意下面均以`Hadoop 2.0`为基础

## 体系架构

### `Common`

其他模块的公共组件，定义程序员取得集群服务的编程接口，为其他模块提供共用API。

#### 作用

降低`Hadoop`设计的复杂性，减少其他模块间耦合性，增强`Hadoop`健壮性。

#### 功能

- 提供公用API和程序员编程接口（例如`Configuration`类）；
- 本地Hadoop库（例如压缩解压缩用的是`Hadoop`本地库）；
- 超级用户`superuser`；
- 服务级别认证；
- `HTTP`认证；

### `HDFS`

高容错、高扩展、高可靠，并提供服务访问接口，如API接口和管理员接口。

#### 体系架构

- 架构：`master`/`slave`；文件分块存储；`namenode`/`datanode`；
- 典型拓扑：一般/商用（`ZooKeeper`选举`ActiveNamenode`，`JourNalNode`两个`Namenode`交换数据）

![image-20211015153417530](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015153417530.png)

#### 内部特性

- 冗余备份、副本存放、副本选择、心跳检测

- 数据完整性检测、元数据磁盘失效

- 简单一致性模型、流式数据访问、客户端缓存

- 流水线复制、架构特征、超大规模数据集

#### 对外功能

- `Namenode`==高可靠性==：配置多个`NameNode`，一个失效时立即替换
- `HDFS`快照：当数据损坏时，支持回滚到正确的时间节点
- 元数据管理与恢复工具：通过命令`hdfs oiv`和`hdfs oev`管理修复`fsimage`和`edits`
- `HDFS`安全性：用户和文件级别安全认证、机器和服务级别安全认证
- `HDFS`配额功能：管理目录或文件配额大小
- `HDFS` C语言接口：使用C语言操作HDFS的接口
- `HDFS Short-Circuit`功能：客户端可以绕开`Datanode`直接读取本机数据，加快`Map`操作
- `WebHdfs`：==通过`Web`方式操作`HDFS`==（插、删、改、查）

### Yarn

管理计算机资源、提供用户和程序访问系统资源的API。

- 一个高层的集群管理框架；

- 根据需要的计算类型，定制`ApplicationMaster`；
- 根据需要的调度策略，扩展`Scheduler`

#### 架构

![image-20211015154235691](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015154235691.png)

#### 组件详解

1. `Client`：客户端，负责向集群提交作业。

2. `ResourceManager`：集群主进程，仲裁中心，负责集群资源管理和任务调度。

3. `Scheduler`：资源仲裁模块。==纯粹的资源仲裁中心==

4. `ApplicationManager`：选定，启动和==只==监管`ApplicationMaster`。

5. `NodeManager`：集群从进程，管理监视`Containers`，执行具体任务。

6. `Container`：==本机==资源集合体，如某`Container`为4个CPU，8GB内存。

7. `ApplicationMaster`：任务执行和监管中心。==负责任务整体执行==

#### 作业流程

1. 提交作业
2. 任务分配
3. 任务执行
4. 进度和状态更新
5. 任务完成

![image-20211015154901595](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015154901595.png)

#### 典型拓扑

![image-20211015155031593](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015155031593.png)

#### 核心问题：调度策略

`ResourceManager`的`Scheduler`模块支持插拔，通过配置文件，用户可以个性化指定其调度策略。

##### 自带策略1：容量调度算法`CapacityScheduler`

- 多用户多任务调度策略；
- 以队列为单位划分任务，以`Container`为单位分配资源；
- 按照配置好的资源配比为不同层级的用户分配最大可用资源；

##### 自带策略2：公平调度算法`FairScheduler`

- 多任务公平使用集群资源的可插拔式调度策略；
- 当资源能够满足所有任务时，则按需分配资源；
- 当资源受限时，会将正在执行的任务释放的资源分配给在等待资源的任务；
- 短任务在合理时间内完成；长任务不至于永远等待；

### MapReduce

编程范式。

`Yarn`中`ApplicationMaster`用来管理任务的执行，其能够管理的任务类型是固定的

通过定义不同类型的`ApplicationMaster`，可以实现管理不同类型的任务。可以将`MapReduce`看作一种类型的计算任务。提供对应的`ApplicationMaster`来管理`MapReduce`任务。

==`ApplicationMaster`和`Scheduler`都是可变的==。

![image-20211015164310161](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015164310161.png)

### 拓展

- 在`Hadoop`框架内定义新的计算任务——编程模板
- 跳出`Hadoop`的限制——==Spark==——定义更加通用的编程
- 安全机制——不同级别、不同场景的安全认证

## 访问接口

### Web

> 注意到新版本中`Hadoop`的都统一到9870端口了，下面那个表格的端口号要改

| 服务        | Web地址                                 | 配置文件          | 配置参数                                  |
| ----------- | --------------------------------------- | ----------------- | ----------------------------------------- |
| `HDFS`      | `http://<NameNodeHostName>:50070`       | `hdfs-site.xml`   | `{dfs.namenode.http-address}`             |
| `Yarn`      | `http://<ResourceManagerHostName>:8088` | `yarn-site.xml`   | `{yarn.resourcemanager.webapp.address}  ` |
| `MapReduce` | `http://<JobHistoryHostName>:19888`     | `mapred-site.xml` | `{mapreduce.jobhistory.webapp.address}`   |

### 命令行

#### `HDFS`命令

- 以`tar`包方式部署时，其执行方式是`$HADOOP_HOME/bin/hdfs`
- 以完全模式部署时，使用HDFS用户执行`hdfs`即可

#### `Yarn`命令

- 以tar包方式部署时，其执行方式是`$HADOOP_HOME/bin/yarn`
- 以完全模式部署时，使用`Yarn`用户执行`yarn`即可

#### `Hadoop`命令

- 两种部署方式下分别为`$HADOOP_HOME/bin/Hadoop` 和 `hadoop`

#### 其他

- `sbin/`目录下的脚本

  ![image-20211015165528143](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015165528143.png)

- 启停服务/管理服务

### 开发接口

#### HDFS编程

- 实例化配置文件 `Configuration conf = new Configuration()`；
- 获取文件系统 `FileSystem hdfs = FileSystem.get(conf)`；
- 使用`hdfs`对象执行文件操作；

> https://hadoop.apache.org/docs/r2.6.4/api/org/apache/hadoop/conf/Configuration.html
>
> 通过configuration传参：`conf.set(key, value)`，`context.getConfiguration().getInt(key)`

#### Yarn编程

- 一套编程协议；
- `Client`负责提交任务，`ApplicationMaster`负责执行任务；
- Client中与RM通信；`ApplicationMaster`与RM通信；`ApplicationMaster`与NM通信
- 编写符合协议的`Client`和`ApplicationMaster`即可

#### 只需考虑MapReduce本身

`Hadoop`默认实现了`MapReduce`的`Client`和`ApplicationMaster`、`MRClientService`和`MRAppMaster`等。

`Yarn`处理`MR`程序时使用了各种默认的类。

# `Spark`

## 概论

### 简介

当今大数据领域最活跃、最热门的大数据计算处理框架

- 2009年——诞生于美国加州大学伯克利分校AMP实验室

- 2013年——`Spark`成为`Apache`基金项目

- 2014年——成为`Apache`基金顶级项目

一体化、多元化的大数据处理体系

- 批处理，`Batch Processing`

- 流处理，`Stream Processing`

- 即席查询，`Adhoc Query`

#### 开发包

`Spark SQL`、`Spark Streaming`、`Spark Mllib`、`Spark GraphX`……

![image-20211015173939819](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015173939819.png)

##### `Spark SQL`

- 前身是`Shark`：基于`Hive`的`Spark SQL`，代码量大、复杂，难优化和维护；

- 交互式查询、标准访问接口、兼容`Hive`；

- 专门用于处理结构化数据；

- 分布式`SQL`引擎；在`Spark`程序中调用`API`；

#### `Spark Streaming`

- 实时对大量数据进行快速处理，处理周期短；

- 对数据分段、定义了自动监听更新的框架、提供各种Spark计算函数；

##### `Spark GraphX`

- 以图为基础数据结构的算法实现和相关应用；

- 使用RDD存储图节点和边信息，提供各种计算函数；

##### `Spark MLlib`

- 为解决机器学习开发的库；

包括`分类`、`回归`、`聚类`和`协同过滤`等。

> 插曲，`Spark Mllib`的效率被基于`MPI`（`Message Passing Interface`）的机器学习吊打
>
> 可能的解释：https://zhuanlan.zhihu.com/p/81784947

`Spark`==专注于数据的计算==，而==数据的存储==在生产环境中往往还是由`Hadoop`分布式文件系统==HDFS==承担。

### 优势

#### 对比`Hadoop`

- 支持多种数据计算需求
  - 流式迭代的类MR计算
  - 图数据结构的计算

- 基于内存的计算范式，不用像`Hadoop`那样需要不停地写入硬盘（落盘）

> `Spark`曾经是一个`Hadoop`应用程序，但是`Spark`并不一定要依赖于`Hadoop`

#### 对比`MapReduce`

`Spark`是在`Hadoop`开创的分布式计算框架下对`MapReduce`编程范式进行扩展的一种更加通用的并行计算框架。

- 独立性更强

- 基于内存：`RDD`，速度更快；基于内存的计算快100x倍，基于硬盘的快10x倍

- 支持更多数据计算方法：`transformation`，`action`等

#### 整体优势

##### **易用**

  支持`Scala`、`Java`、`Python`和`R`等多种编程语言

##### **强大**

  支持`SQL`、`Streaming`、`Graph`和`Machine Learning`等多种应用场景

##### **通用**

  适用于自带的`Standalone`、`Mesos`、`Yarn`等多种不同分布式集群管理框架；

  适用多种不同数据存储方式（数据读取接口丰富）

#### 改进之处的差异

> 复习课专门提了一下，不是很懂他意思

`Hadoop 2.0`对`Hadoop 1.0`的改进主要是引进了`Yarn`，在`Map-Reduce`的基础上又分出了`Master`和`Worker`，完善了任务管理分配调度方面；

`Spark`的改进则主要是为`Map-Reduce`增添了算子，丰富了`Map-Reduce`的功能与应用；

> 据说2021年考试到此为止

### 部署模式

#### Local模式

`Local`是方便初学者入门学习和测试用的部署模式

#### Cluster模式

Cluster是真正的集群模式

- `Standalone`集群管理器
- `Yarn`集群管理器
- `Mesos`集群管理器

### 提交模式

`Client`模式和`Cluster`模式

`Local`部署模式只支持`Client`提交模式。

真正的`Cluster`集群部署模式同时支持`Client`和`Cluster`提交模式。

#### Client提交模式

在`Worker`节点启动`Driver`程序运行应用程序，结果返回到`Client`端。

#### Cluster提交模式

在`Master`上启动`Driver`程序，结果不会返回给`Client`而是保存在`Master`上。

## 内核机制解析

![image-20211015193231739](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015193231739.png)

### `RDD`（`Resilient Distributed Datasets`）

`Spark`是建立在`RDD`(`Resilient Distributed Datasets`，弹性分布式数据集)之上的。

`RDD`是一个==容错的==、==并行的==逻辑数据结构，使得`Spark`可以用一致的方式处理大数据的不同应用场景。

#### 性质

`RDD`是高度受限的共享内存模型。

- `RDD`只能从外界接入或由其他`RDD`产生。
- 从父`RDD`到子`RDD`的过程可以构建一棵树（有向无环图，`Directed Acyclic Graph（DAG）`）。若子`RDD`出现问题，可以通过父`RDD`重新推演。

#### 特点

- 数据存储到内存和磁盘；

- 控制数据分区；

- 丰富的API操作数据；

#### 五大特性

- 分区列表：记录了数据块所在的分区位置；一个`RDD`对应的数据是切分为数据块存储在集群的不同节点上的。

- 依赖列表：记录了当前这个`RDD`依赖于哪些其它的`RDD`。

- 计算函数：用于计算`RDD`各个分区的值。

- **可选**：分区器，子类可以重新指定新的分区方式：`Hash`和`Range`。
- **可选**：计算各分区时优先的位置列表。例如从`HDFS`文件生成`RDD`时，`HDFS`文件所在位置就是对应生成的`RDD`分区所在位置的优先选择。

#### 两种算子

##### Transformation

| **Transformation操作**           | **说明**                                                     |
| -------------------------------- | ------------------------------------------------------------ |
| `map(func)`                      | 对源`RDD`中的每个元素调用`func`，生产新的元素，这些元素构成新的RDD并返回 |
| `flatMap(func)`                  | 与`map`类似，但是`func`的返回是多个成员                      |
| `filter(func)`                   | 对`RDD`成员进行过滤，成员调用`func`返回`True`的才保留，保留的构成新`RDD`返回 |
| `mapPartitions(func)`            | 和`map`类似，但是`func`作用于整个分区，类型是`Iterator<T>  => Iterator<T>` |
| `mapPartitionsWithIndex(func)`   | …                                                            |
| `union(otherDataset)`            | …                                                            |
| `reduceByKey(func, [numTasks])`  | 对`<key,  value>`结构的`RDD`聚合，相同`key`的`value`调用`reduce`，`func`是`(v,v)=>v` |
| `join(otherDataset, [numTasks])` | …                                                            |

##### Action

| **Action操作**             | **说明**                                                     |
| -------------------------- | ------------------------------------------------------------ |
| `reduce(func)`             | 对RDD成员使用`func`进行`reduce`，`func`接收两个值返回一个值；`reduce`只有一个返回值。`func`会并发执行 |
| `collect()`                | 将`RDD`读取到`Driver`程序里面，类型是`Array`，要求`RDD`不能太大 |
| `count()`                  | 返回`RDD`成员数量                                            |
| `first()`                  | 返回`RDD`第一个成员，等价于`take(1)`                         |
| `take(n)`                  | …                                                            |
| `saveAsTextFile(path)`     | 把`RDD`转换成文本内容并保存到指定的`path`路径下，可能有多个文件；`path`可以是本地文件系统路径，也可以是`HDFS`路径，转换方法是`RDD`成员的`toString`方法 |
| `saveAsSequenceFile(path)` | …                                                            |
| `foreach(func)`            | 对`RDD`的每个成员执行`func`方法，没有返回值                  |

#### 弹性的七个方面

##### 自动进行内存和磁盘存储的切换 `效率考虑`

优先内存，实在放不下则放到磁盘里。

##### 基于`Lineage`（血统）的高效容错机制 ==`效率考虑` `容错考虑`==

记录每一个数据分片的计算来源，便于快速恢复。

##### `Task`如果失败会自动进行特定次数的重试 ==`容错考虑`==

`TaskScheduler`获取一个`Stage`的`TaskSet`，运行它们；默认4次。

##### `Stage`如果失败会自动进行特定次数的重试 ==`容错考虑`==

`DAGScheduler`调度`Stage`，`Stage`跟踪执行情况；默认4次。

##### `Checkpoint`和`Persist`（检查点和持久化）可主动或被动触发 ==`效率考虑` `容错考虑`==

用户能见的`RDD`可以==主动调用==，自动产生的中间RDD则可==配置==。

##### 数据调度弹性（`DAGScheduler`、`TaskScheduler`和资源管理无关）==`效率考虑`==

任务调度、数据分配和计算资源的管理解耦：Yarn管理Spark集群

##### 数据分片的高度弹性：合并分片和切分分片 ==`效率考虑`==

根据产生的分片（数据块）大小自动选择继续切分还是放到磁盘

#### 创建方式

- 通过已存在的数据集合创建（变量）
- 通过HDFS和本地文件系统创建`textFile(…)`
- 通过其他RDD转换（`transformation`操作）
- 从数据库读入

#### 宽窄依赖

![image-20211015204733278](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015204733278.png)

|                 窄依赖（`NarrowDependency`）                 |                宽依赖（`ShuffleDependency`）                 |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| ==父RDD==中的Partition==最多==被==子RDD==的==1个==Partition所使用 | ==一个====父RDD==的Partition会同时被==子RDD==的==多个==Partition所使用 |
|                       ==完全==并行执行                       | 需要==Shuffle后==才能对计算==并行化==；==Shuffle过程不能完全并行== |
| ![image-20211015205511434](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015205511434.png) | ![image-20211015205517567](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015205517567.png) |

#### 运算流程

![image-20211015213320153](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015213320153.png)


构造DAG，划分`Job`、`Stage`、`Task`，==遇到`Action`，才会提交`Job`==。

![image-20211015210017829](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211015210017829.png)

- `Transformation`：从持久化存储中通过*变换*（**`Transformations`**，如 *map* 或者 *filter*）将其载入内存，然后可以对 `RDD` 施加任何系统支持的一系列变换。它只是一个声明，不碰到Action运算不会进行。

- `Action`：将 `RDD` 重新持久化到外存中或者将控制权交还用户。
- `Application`：客户端的一次提交，可以看作一个主函数。
- `Job`：由`action`触发的一系列计算任务。
- `Stage`：把一个`job`按照宽依赖分割成若干阶段。
- `Task`：把`stage`根据RDD分区数进行区分。

> 参考链接：https://stackoverflow.com/questions/42263270/what-is-the-concept-of-application-job-stage-and-task-in-spark

#### 解决的具体问题

`Hadoop`不能基于内存共享数据，==反复读写磁盘==。因此，`Hadoop`的`MapReduce`对==迭代==式算法支持的效率不高，更别提图算法和机器学习算法了。

`Spark`适应于==在交互式数据挖掘工具中反复查询一个数据子集的==应用场景。

#### 缓存（`Cache`）

将RDD保存到内存（也可能在磁盘上），读写速度极快。

实现方式是在`Persist`持久化时将`Storgelevel`设置为`MEMORY_ONLY`

共12种`StorageLevel`；本质上和`Persist`没有区别，都是`Persist`方法，只是级别不同。

##### 作用

计算RDD完成后对其进行缓存，若整个计算失败，可以从缓存读取这个RDD，避免重新计算这个RDD，提升容错效率。

##### 适用场景

- 获取大量数据后；
- 进行一个非常长的计算链条，设置一些缓存点；
- 某个步骤计算非常耗时，步骤完成后对结果进行缓存；
- 进行`checkpoint`前也会缓存；

#### `Checkpoint`

将`RDD`持久化到`HDFS`，利用`HDFS`的容错能力降低`RDD`数据丢失的风险。

它会将`RDD`的依赖清空，如果`HDFS`也不能保证数据不丢失，则任务需要重新启动。

#### 四个层次的容错

- `Stage`输出失败，上层调度器`DAGScheduler`重试

- `Task`内部任务失败，底层`TaskScheduler`调度器重试

- 根据`RDD Lineage`血统重新计算
  - 对于宽依赖而言，如果结果的一个`Partition`出错，需要重新计算父`RDD`所有`Partition`
  - 对于窄依赖而言，如果结果的一个`Partition`出错，只需重新计算父RDD被丢失`Partition`依赖的那个`Partition`
  - `Cache`可看作时`Lineage`容错机制的效率提升机制，本身并无容错考虑，如果`Cache`丢失则仍需重新计算

- Checkpoint机制

### `Scheduler`

调度器，简洁清晰和高效。

- 输入：`Spark RDD`
- 输出：执行器`Executor`

![image-20211018141659263](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018141659263.png)

#### `Spark Driver`

是运行`Application`的`main`函数。

负责初始化`SparkContext`，它负责。

与集群通讯、资源申请、任务分配和监控等。

#### 流程

##### 初始化`SparkContext`

初始化了`TaskScheduler`，`SchedulerBackend`，`DAGScheduler`。

##### `RDD Transformation`操作 *`RDD.Transformation`==Lazy*

只记录RDD之间依赖关系，和操作类型，不具体调用`compute`方法。

##### 触发点：Action操作 *`RDD.action`触发`SparkContext`的`runJob`*

调用`runJob`，触发`DAGScheduler`调用`submitJob`。

![image-20211018142148221](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018142148221.png)

![image-20211018142232497](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018142232497.png)

##### `DAGScheduler`构建`Stage`

在`createStage`时从最后一个`Stage`开始递归构建`Stage`，并根据`dependency`类型划分`Stage`。

![image-20211018142405321](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018142405321.png)

##### `DAGScheduler`构建`Stage`

在提交`Stage`时从最后一个`Stage`开始回溯直到没有前序`Stage`的第一个`Stage`，执行`submitMissingTask`。

构建好`TaskSet`，计算每一个`Task`最佳位置，将`TaskSet`提交给`TaskScheduler`。

![image-20211018142641421](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018142641421.png)

##### `TaskScheduler`针对每一个`TaskSet`细粒度调度和执行

- 根据`Task`位置和执行器信息分配`Task`到`Executor`。

- 通过`SchedulerBackend`将执行命令发送到`Executor`上开始执行。

- 通过`SchedulerBackend`获得执行器相关信息。

![image-20211018142836729](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018142836729.png)

> 注意图中的两个调度算法。先来先服务和公平调度。
>
> 要先知道执行器的相关信息才能发送执行，因此要看Driver、Master、Work如何通信！

### `Executor`

#### 创建`Executor`

- 首先`Application`要向`Master`注册——==由`SchedulerBackend`通过`AppClient`的子类`ClientEndpoint`完成==；

- `Master`回复注册成功，并将`Application`发送到满足条件的`Worker`上，在`Work`上启动`Executor`；

- 通过`Worker`的`RpcEndpoint`向`Worker`发送启动`Executor`请求；

- `Worker`收到请求后启动`ExecutorRunner`，并通知`Master Executor`的相关信息；

- 此时本质上是启动了负责帮`Executor`和`Driver`通信的`Backend`：`ExecutorBackend`；

- `ExecutorBackend`直接向Driver注册`Worker`让它准备启动的`Executor`；

- 收到`Driver`确认后，`Executor`正式新建；

  ==是`Executor`主动联系`Driver`，让`SchedulerBackend`了解到所有`Executor`的信息，再让`TaskScheduler`根据`Executor`情况分配`Task`到`Executor`==

#### `Executor`资源分配

- `Driver`启动的时候从`spark-submit`收集对`executor`的需求，并在向`Master`注册时发送过去；
- 具体可以参考如何从提交程序收集需求，并一直传递给`Master`，再给`Worker`；
- `ExecutorRunner`从`Worker`那里得到这些参数，并在根据参数启动`ExecutorBackend` `JVM`进程；

#### `Executor`启动

- 在`ExecutorBackend`向`Driver`注册后，收到确认时的操作就是创建`Executor`；
- 此时`TaskScheduler`根据`Executor`情况安排好`TaskSet`调度，`Executor`也启动好了；

#### 通过`DriverEndpoint`向`ExecutorBackend`发送执行`Task`的消息

![image-20211018144030533](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018144030533.png)

#### `ExecutorBackend`收到`LaunchTask`通知后

- 调用`Executor`的`launchTask`方法；
- 内部创建`TaskRuner`，用线程池执行`TaskRunner`，调用`run`方法；

- - 反序列化出`Task`
  - 调用`Task`的`run`方法

### `Storage`

#### 通信层

`Master-Slave`结构，传输控制和状态信息。

`BlockManager`, `BlockManagerMaster`, `BlockManagerMasterEndpoint`, `BlockManagerSlaveEndpoint`。

#### 存储层

负责将数据存储到内存、磁盘或堆外内存中，为数据在远程节点生成副本。

`DiskStore`, `MemoryStore`。

![image-20211018144317048](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018144317048.png)

![image-20211018144453854](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211018144453854.png)

### `Shuffle`

#### 【1】RDD创建过程

构建`RDD`时确定好与父RDD之间的依赖关系，如果是`ShuffleDependency`，会向`ShuffleManager`注册，获取`Handle`，用来保存父RDD的相关信息。

#### 【2】`RDD`计算过程

在实际计算时，`runTask`会调用`RDD compute`方法，其中根据`dependency`获取`reader`读取用来计算`RDD`的输入数据，也就是之前`shuffle`操作写入的数据。

#### 【3】`Task`结束处理

当`runTask`完成计算后，获取子`RDD`之间的依赖关系，如果是`shuffle`依赖则同样通过`dependency`和`ShuffleManager`获得`Handle`，进而获得`writer`。

#### 可插拔的`Shuffle`框架

•`ShuffleDependency`，`ShuffleManager`，`ShuffleHandle`

•`ShuffleReader`，`ShuffleWriter`

•`ShuffleMapTask`，`ResultTask`

#### 拓展

`Shuffle`前后必不可少地需要网络I/O，因此通过数据序列化方法和压缩技术进行效率优化。

> Spark中序列化方法和压缩算法的配置

##### `Spark 1.0`：基于`Hash`的`Shuffle`机制

每一个`Mapper`阶段的`Task`都会为`Reduce`阶段的每一个`Task`生成1个文件，==M*R==个。

合并机制：每一个执行单位为`Reduce`阶段每一个`Task`生成==1个==文件。

##### `Spark 1.1`：基于`Sort`的`Shuffle`机制

每一个`Mapper`阶段的`Task`生成两个文件：索引和数据文件，`Reduce`阶段通过索引读取。

##### `Spark 1.4`：钨丝计划——优化内存管理模型

直接使用==二进制数据==，而不是`Java`对象；避免序列化和反序列化开销。

## 部署实验

详情参见 https://ydjsir.com.cn/2021/10/17/initSpark/。

## "实践"

> 参考：https://spark.apache.org/docs/2.1.1/programming-guide.html
>
> 不考不细讲，嗯，就这样。

### 基础

#### 从数据源到RDD

- `parallelize()` （把一个普通的collection变成支持分布式的）
- `textFile(path)`
- `hadoopFile(path)`
- `sequenceFile(path)`
- `objectFile(path)`
- `binaryFiles(path)`
- ……

#### 从RDD到目标数据

•`saveAsTextFile(path)`

•`saveAsSequenceFile(path)`

•`saveAsObjectFile(path)`

•`saveAsHadoopFile(path)`

•……

#### 二次排序

- 指在==归约（`reduce`）阶段==对==某个键关联的值==排序；
- ==`Map`阶段==可以对`<key, value>`对按照键的值进行排序，但是归约器不会自动对键值对按照值排序；但是有时候需要：将成绩按照班级==归约后排序==；店铺产品销量排序等

##### 例：按照`name`（第一标准）和`time`（第二标准）对`value`排序

![image-20211021093117197](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021093117197.png)

归约只能做到按照`name`把值区分开，但是分好后再对`value`按照`time`排序时，需要进行二次排序。

##### 方案1：在内存中实现排序，只借助`Map-Reduce`框架进行分组

组内直接在内存中调用排序函数。

- 创建`SparkContext`对象；连接到`Spark master`；读取原始数据；
- 构建<键,值>对;
- 按照键分组：`groupByKey`；
- 对每个组对应的新的value(是一个列表)进行排序操作；

不具备伸缩性，单个服务器的内存又成为瓶颈。

##### 方案2.1：利用框架实现值排序

自定义Key + `sortByKey()`：组合键。

- 自定义组合键：`<<name, time>, value>`；
- 调用`sortByKey`时会用`<name, time>`排序，因此要比较`<name, time>`大小；
- 在自定义`Key`中定义好`compare`方法；
- 按照自定义Key格式实现`mapToPair`
- 最后调用`sortByKey()`

##### 方案2.2：使用组合键 + `groupByKey()`

![image-20211021094415780](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021094415780.png)

#### `TOP N`列表

##### 基本思路

在每一个`Partition`内取本地的`Top N`；将所有本地`Top N`合并，再取全局`Top N`。

###### 使用`mapPartitions()`

- 对`RDD`的每一个`Partition`进行操作；
- 输入是整个`Partition`的数据，每一个`Task`对应处理一个`Partition`；
- 结果`RDD`与输入`RDD`有相同个数的`Partition`；
- 结果`RDD`的每一个`Partition`就是局部`Top N`；

###### 对保存所有局部`Top N`的`RDD`进行`action`操作

- 用`collect`方法将局部`Top N`存放到`list`中
- 遍历`list`，选出全局`Top N`

###### 使用框架的`reduce`操作

定义两两合并的规则。

##### 一种可行的解

- 使用框架的`takeOrdered(N, DefineComparator)`
- 支持自定义`Comparator`
- 得到`JavaPairRDD`后，直接使用`takeOrdered`获得全局`Top N`

### `Spark SQL`

Spark SQL是`Spark Core`上的一个模块，所有`SQL`操作被`Catalyst`翻译成类似普通`Spark`程序一样的代码，被`Spark Core`调度执行，过程也有`Job`、`Stage`和`Task`概念。

它是根据待处理数据和待执行计算的结构信息，做了额外优化。

#### `Spark Catalyst`

- 解析、优化`Spark SQL`语句，最终生成`Java`字节码；
- 使用核心数据结构-树-存储`SQL`语句；
- 使用基础概念-规则-对`SQL`语句对应的计算进行优化；

![image-20211021100418147](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021100418147.png)

| 实际用例                                                     | Catalyst                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20211021100100958](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021100100958.png) | ![image-20211021100111405](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021100111405.png) |

#### 使用途径

##### 使用`SQL`语句进行数据查询

- `Spark SQL`可以读取`Hive`上的数据；
- 可以在程序中执行`SQL`查询，结果以`dataset/dataframe`形式返回；
- 通过命令行使用`SQL`命令；

##### 在程序中使用`Dataset API`

- `Dataset`也是分布式数据集合，具有与`RDD`一样的优点，还根据`Spark SQL`引擎的特性进行了优化；
- 可以从`JVM`中的对象构建并使用类似`RDD`可用的`Transformation`操作；

##### `Dataframe`：也是一种`Dataset`，数据有列的概念，类似关系型数据库的“表”概念。

- 比`Dataset`更加丰富的操作；
- 多种来源：结构化数据文件，`Hive表`，外部数据库，`RDD`；

### `Spark Streaming`

> 这几张图检索一下就会发现来自于Spark官方文档

#### `Structured Streaming`

`Structured Streaming`基于`Spark SQL engine`。 

在动态变化的数据集上实现流式计算就像在静态数据集上做计算一样方便。

![image-20211021101018873](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021101018873.png)

#### 对`DataFrames/DataSets`进行多种操作

##### 基本操作

- `select`, `projection`, `aggregation`, `groupBy`, `groupByKey`, `filter`……
- 创建数据表，并使用SQL操作
- 判断是否是流

##### `Window Operations on Event Time`

![image-20211021101455071](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021101455071.png)

5分钟统计一次，10分钟是一个窗口。统计的不仅仅是从开始时间点到数据截止时的总出现次数，而是这10分钟的窗口期内出现的次数。

##### `Handling Late Data and Watermarking`

![image-20211021101806557](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021101806557.png)

迟一点不要紧，一样可以更新在表格里面。但是等待不是没有限度的，在那个`watermark`线以下的就直接`ignore`了。

![image-20211021101912017](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021101912017.png)

###### 启动计算

当定义好最后一个`DataFrames`或`DataSets`，就剩下启动流计算了。

**输出的细节**: 数据格式和位置等.

**输出模式**：每一次计算之后哪些数据被写入，包括`Append`模式，`Complete`模式和`Update`模式.

**应用名称**: 可选的，为该结构化流计算命名，是唯一的.

**触发时间间隔**: 可选的，定义每一次计算的触发时间间隔. 如果不设置，则在上一次计算结束后立即启动. 如果上一次计算太久导致错过设置的触发时间，系统不会等待下一个时间间隔，而是上一个任务结束就启动计算。

**检查点存储位置**: 应该是一个和HDFS兼容的高容错文件系统目录。

**内置的可写入输出**：`File sink`, `Kafka sink`, `Foreach sink`, `Console sink`, `Memory sink`。 

#### `Streaming`

实现可扩展、高吞吐、高容错的实时数据流处理。

![image-20211021102348551](https://oss.ydjsir.com.cn/GitPages/SparkWithHadoop/image-20211021102348551.png)

##### 部署条件

集群要求，JAR要求，配置要求，检查点配置，重启配置，日志配置，流配置等等。

- 执行监控
- 性能优化
- 降低数据处理时间（数据接收并行化、数据处理并行化、数据序列化、任务数量控制）
- 巧妙设置时间间隔
- 内存优化
- 容错

如何对已经部署的应用进行更新？

- 数据写入多个地方，同时启动更新应用；
- 停止旧应用再启动新应用；

##### 需要注意的地方

- 一旦一个流计算过程在`Context`中启动后，这个`Context`不可以再新建新的流计算过程；
- 一旦`Context`停止后，不可以被重新启动——只能重新提交`Application`；
- 一个`JVM`一次只能运行一个`StreamingContext`；
- `StreamingContext`的`stop`方法也会停止`SparkContext`，除非指定不停止`SparkContext`；
- `SparkContext`如果不停止，可以用于重复建立新的`StreamingContext`；

### `Spark GraphX`

图计算：以图为数据结构基础的相关算法及应用。

#### `GraphX`提供的`API`

- 图生成。
- 图数据访问：查询顶点数、边数；计算某个点的入度、出度等。
- 图算法：遍历顶点、边；计算连通性；计算最大子图；计算最短路径；图合并等。

#### `GraphX`的实现

- 核心是`Graph`数据结构，表示有向多重图；
- 两个顶点间允许存在多条边，表示不同含义；
- `Graph`由顶点`RDD`和边`RDD`组成；
- `Graph`的分布式存储方式；

#### 细节

##### 图生成

- 读入存储关系信息的文件，构造`EdgeRDD：eRDD = sc.textFile()`；
- 从`Edge RDD`构造`Graph：graph = Grapth.fromEdges(eRDD)`；

##### 基本接口

- 获取边数：`numEdges`；获取节点数：`numVertices`；
- 获取入度、出度：`inDegrees`, `outDegrees`；
- 结构操作：`reverse`，`subgraph`, `mask` ；

##### 关联类操作

- 将一个图和一个`RDD`通过顶点`ID`关联起来，使图获得`RDD`信息；
- `joinVertices`；
- `outerJoinVertices`； 

##### 聚合类操作

- 分布式遍历所有的边，执行自定义的`sendMsg`函数；
- 在节点上执行`mergeMsg`函数；

### `Spark MLlib`

Spark为机器学习问题开发的库。支持分类、回归、聚类和协同过滤等。

#### 基础数据类型

- 向量
- 带标注的向量：用于监督学习
- 模型：训练算法的输出

#### 主要的库

- `mllib.classification`:分类算法，二分类、多分类、逻辑回归、朴素贝叶斯、SVM等；
- `mllib.cluster`：聚类，`K-Means`、`LDA`等；
- `mllib.recommendation`：使用协同过滤的方法做推荐；
- `mllib.tree`：决策树、随机森林等算法；

#### 其它常用库

`mllib.evaluation`：算法效果衡量方法。