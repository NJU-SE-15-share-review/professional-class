# 部署Spark

## 环境相关

本次实验中共使用了5台华为云ECS，其中1台作为`master`节点，3台作为`workers`节点，1台作为观察用的机器。（由于绑定外网相关设置复杂，我们组开了同一地域的一个虚拟机专门用于访问其他四台机器的网页）除了观察用的机器是`Windows Server 2012R2 64位简体中文版`以外，其他的机器使用的都是`Ubuntu Server 18.04`。剩余四台主机的主机名、内网IP与公网IP如下。

| 主机名       | 内网IP        | 外网IP | 作用       |
| ------------ | ------------- | ------ | ---------- |
| `ecs-master` | 192.168.0.142 |        | 主节点     |
| `ecs-d202`   | 192.168.0.17  |        | Worker节点 |
| `ecs-d203`   | 192.168.0.100 |        | Worker节点 |
| `ecs-d204`   | 192.168.0.102 |        | Worker节点 |

由于IP绑定的问题，通过外网直接访问时，需要主动将网页提供的URL中的内网IP替换为内网IP才可以正常访问。但是在专门准备的观察机器上访问则没有这个问题，因为可以内网直通。

## 工具相关

由于网络问题，此处涉及的所有安装文件都是本地下载后用`WinSCP`上传到既定位置的。相关操作按下不表。

华为云的`CloudShell`很方便，本次实验中所有的操作都在`CloudShell`上运行。

注意，==下面所有的配置均以只配置一个`worker节点`的情形为例==。因为后面扩大规模时是将它的镜像直接克隆两个，再修改`Spark`和`Hadoop`的配置文件中的列表以及`hosts`文件即可。

==最后展示的运算结果是三个`worker节点`均启用的情形==。

## 基础环境配置

### `所有节点`改host

```bash
vim /etc/hosts
```

此处默认走华为云内网（因为是同一个用户），也可以改为公网。

所有的节点都要添加`除了自己以外`的节点的IP地址和主机名。

改完就能用了。

以`主节点`为例。

```bash
127.0.0.1       localhost
192.168.0.102   ecs-d204 # 这里是内网IP

# The following lines are desirable for IPv6 capable hosts
::1     localhost       ip6-localhost   ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
127.0.1.1       localhost.vm    localhost
```

### `主节点`免密SSH

由于华为云上提供的都是Ubuntu的服务器版本，因此我们不需要再安装SSH客户端。

```bash
ssh-keygen -t rsa
ssh-copy-id -i /root/.ssh/id_rsa.pub ecs-master
ssh-copy-id -i /root/.ssh/id_rsa.pub ecs-d204
```

第一次连接时，系统会提示请输入对应主机密钥。

在主机上验证对所有这些worker的SSH免密连接。

## 环境搭建

### `主节点`安装Oracle JDK8

#### 解压

```bash
cd /usr
mkdir java
sudo tar -zxvf jdk_8u291_linux_x64.tar.gz
```

#### 添加环境变量

```bash
export JAVA_HOME=/usr/java/jdk1.8.0_291
export CLASSPATH=$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
```

方法不过是进文本编辑器后在末尾添加上面的文字。为避免重复，下面的部分只谈环境变量本身而不再提及编辑环境变量的过程。

```bash
vim /etc/profile		# 编辑配置文件
source /etc/profile		# 让这个配置文件生效
```

#### 测试JAVA环境

```bash
root@ecs-master:/usr/java# java -version
java version "1.8.0_291"
Java(TM) SE Runtime Environment (build 1.8.0_291-b10)
Java HotSpot(TM) 64-Bit Server VM (build 25.291-b10, mixed mode)
root@ecs-master:/usr/java# 
```

成功。

### `主节点`安装Scala

#### 安装

此处采取了官网`deb`包的安装方式。

```bash
apt-get install ./scala-2.12.15.deb
```

#### 测试Scala环境

```bash
root@ecs-master:/usr# scala
Welcome to Scala 2.12.15 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_291).
Type in expressions for evaluation. Or try :help.

scala> println("Hello, world")
Hello, world

scala> 
```

一切正常。

### `主节点`安装并配置Hadoop

#### 解压

```bash
cd /usr/java
sudo tar -zxvf hadoop-3.2.2.tar.gz
```

#### 添加环境变量

```bash
export HADOOP_HOME=/usr/java/hadoop-3.2.2
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

#### 测试Hadoop环境

```bash
root@ecs-master:/usr/java# hadoop version
Hadoop 3.2.2
Source code repository Unknown -r 7a3bc90b05f257c8ace2f76d74264906f0f7a932
Compiled by hexiaoqiao on 2021-01-03T09:26Z
Compiled with protoc 2.5.0
From source with checksum 5a8f564f46624254b27f6a33126ff4
This command was run using /usr/java/hadoop-3.2.2/share/hadoop/common/hadoop-common-3.2.2.jar
root@ecs-master:/usr/java# 
```

可见Hadoop已经就绪了。

#### 配置`Hadoop`

##### 创建文件夹

```bash
mkdir tmp
mkdir hdfs
mkdir hdfs/name
mkdir hdfs/data
```

##### 配置节点列表

修改`$HADOOP_HOME/etc/hadoop/workers`，删除原先的`localhost`，改为所配置的`workers`的名字列表，并用换行符空开。

```bash
ecs-d204
```

##### 修改`Hadoop`的配置文件

###### `$HADOOP_HOME/etc/hadoop/hadoop-env.sh`

添加如下内容。

```bash
export HDFS_NAMENODE_USER="root"
export HDFS_DATANODE_USER="root"
export HDFS_SECONDARYNAMENODE_USER="root"
export YARN_RESOURCEMANAGER_USER="root"
export YARN_NODEMANAGER_USER="root"
```

修改如下内容。

```bash
# The java implementation to use. By default, this environment
# variable is REQUIRED on ALL platforms except OS X!
export JAVA_HOME=/usr/java/jdk1.8.0_291
```

> 取消注释 `export`那行并输入正确的`JAVA_HOME`的值。也可以直接用`${JAVA_HOME}`。

###### `$HADOOP_HOME/etc/hadoop/core-site.xml`

修改为如下内容。

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://ecs-master:9000</value>
    </property>
    <property>
        <name>io.file.buffer.size</name>
        <value>131072</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
		<value>/usr/java/hadoop-3.2.2/tmp</value>
    </property>
</configuration>
```

###### `$HADOOP_HOME/etc/hadoop/hdfs-site.xml`

修改为如下内容。

```xml
<configuration>
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>ecs-master:50090</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value >2</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/java/hadoop-3.2.2/hdfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/java/hadoop-3.2.2/hdfs/data</value>
    </property>
</configuration>
```

###### `$HADOOP_HOME/etc/hadoop/mapred-site.xml`

修改为如下内容。

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>ecs-master:10020</value>
    </property>
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>ecs-master:19888</value>
    </property>
</configuration>
```

###### `$HADOOP_HOME/etc/hadoop/yarn-site.xml`

修改为如下内容。

```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.resourcemanager.address</name>
        <value>ecs-master:8032</value>
    </property>
    <property>
        <name>yarn.resourcemanager.scheduler.address</name>
        <value>ecs-master:8030</value>
    </property>
    <property>
        <name>yarn.resourcemanager.resource-tracker.address</name>
        <value>ecs-master:8031</value>
    </property>
    <property>
        <name>yarn.resourcemanager.admin.address</name>
        <value>ecs-master:8033</value>
    </property>
    <property>
        <name>yarn.resourcemanager.webapp.address</name>
        <value>ecs-master:8088</value>
    </property>
</configuration>
```

运行如下命令使得更改生效。

```bash
hadoop namenode -format
```

运行时会问你要不要初始化HDFS，此处选择Y。

### `主节点`配置Spark

#### 解压

```bash
cd /usr/java
sudo tar -zxvf hadoop-3.2.2.tar.gz
```

#### 添加环境变量

```bash
export SPARK_HOME=/usr/java/spark-3.0.3-bin-hadoop3.2/
export PATH=$PATH:$SPARK_HOME/bin
```

#### 测试Spark环境

```bash
root@ecs-master:/usr# spark-shell
21/10/15 23:59:50 WARN Utils: Your hostname, ecs-master resolves to a loopback address: 127.0.1.1; using 192.168.0.142 instead (on interface eth0)
21/10/15 23:59:50 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
21/10/15 23:59:51 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://192.168.0.142:4040
Spark context available as 'sc' (master = local[*], app id = local-1634313599435).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.3
      /_/
         
Using Scala version 2.12.10 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_291)
Type in expressions to have them evaluated.
Type :help for more information.

scala> println("Hello, world!")
Hello, world!

scala> 
```

由此可见，Spark环境已经正常。

#### 配置`Spark`环境

##### `$SPARK_HOME/conf/spark-env.sh`

```bash
cd $SPARK_HOME/conf
cp spark-env.sh.template spark-env.sh
```

添加如下内容。

```bash
export JAVA_HOME=/usr/java/jdk1.8.0_291
export HADOOP_HOME=/usr/java/hadoop-3.2.2
export SPARK_WORKER_MEMORY=2g
export HADOOP_CONF_DIR=/usr/java/hadoop-3.2.2/etc/Hadoop
export SPARK_MASTER_IP=192.168.0.142 # 个人测试这个地方用ecs-master就是不行，所以直接写IP了。
export SPARK_MASTER_PORT=7077
# export SPARK_LOCAL_IP=127.0.0.1 # 这一行不要设置
```

##### `$SPARK_HOME/conf/slaves`

修改为如下内容。这个地方实质上就是把你的worker列表加入其中。模仿时请注意对应修改。

```bash
ecs-d204
```

## 分发配置

### `主节点`分发配置环境与环境

对==每一个==`worker节点`进行如下操作。以对`ecs-d204`的操作为例。

```bash
scp -r /usr/java root@ecs-d204:/usr
scp -r /etc/profile root@ecs-d204:/etc/profile
```

而后在==每一个==`worker节点`中运行如下命令。

````bash
source /etc/profile
````

## 启动集群

### 启动`Hadoop`

在`主节点`上，启动`Hadoop`集群。

```bash
cd $HADOOP_HOME/sbin
./start-all.sh
```

如果没有任何错误，应看到如下信息。

```bash
root@ecs-master:/usr/java/hadoop-3.2.2/sbin# ./start-all.shStarting namenodes on [ecs-master]
Starting datanodes
Starting secondary namenodes [ecs-master]
Starting resourcemanager
Starting nodemanagers
root@ecs-master:/usr/java/hadoop-3.2.2/sbin#
```

在`主节点`上，输入`jps`命令，观察是否有`SecondaryNameNode`，`ResourceManager`和`namenode`。

```bash
root@ecs-master:/usr/java/hadoop-3.2.2/sbin# jps
9089 Jps
8777 ResourceManager
8539 SecondaryNameNode
8236 NameNode
926 WrapperSimpleApp
```

成功。

在`worker节点`中，输入`jps`命令，观察是否有`NodeManager`，`DataNode`。

```bash
root@ecs-d204:/usr/java/hadoop-3.2.2/sbin# jps
4432 DataNode
4594 NodeManager
4708 Jps
936 WrapperSimpleApp
```

成功。

### 启动`Spark`

在`主节点`，启动Spark集群。

```bash
cd $SPARK_HOME/sbin
./start-all.sh
```

得到如下输出。

```bash
root@ecs-master:/usr/java/spark-3.0.3-bin-hadoop3.2/sbin# ./start-all.shstarting org.apache.spark.deploy.master.Master, logging to /usr/java/spark-3.0.3-bin-hadoop3.2//logs/spark-root-org.apache.spark.deploy.master.Master-1-ecs-master.out
ecs-d204: starting org.apache.spark.deploy.worker.Worker, logging to /usr/java/spark-3.0.3-bin-hadoop3.2/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-ecs-d204.out
ecs-master: starting org.apache.spark.deploy.worker.Worker, logging to /usr/java/spark-3.0.3-bin-hadoop3.2/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-ecs-master.out
```

在`主节点`，输入`jps`命令。得到的结果比启动`Hadoop`后增加了`Master`和`Worker`。

在`worker`节点，输入`jps`命令，得到的结果比启动`Hadoop`后增加了`Worker`。

### 测试：计算Pi

#### 输入

在`主节点`，运行如下命令。

```bash
$SPARK_HOME/bin/run-example SparkPi 10
```

确保他能跑不报错后，用`spark-summit`实现正式的能在网页上显示的提交。

```bash
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi --deploy-mode cluster  --name spark-pi --master spark://192.168.0.142:7077 /usr/java/spark-3.0.3-bin-hadoop3.2/examples/jars/spark-examples_2.12-3.0.3.jar
```

#### 命令行输出

运行后得到如下输出。

```bash
root@ecs-master:/usr/java/hadoop-3.2.2/sbin# $SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi --deploy-mode cluster  --name spark-pi --master spark://192.168.0.142:7077 /usr/java/spark-3.0.3-bin-hadoop3.2/examples/jars/spark-examples_2.12-3.0.3.jar
21/10/17 20:25:07 WARN Utils: Your hostname, ecs-master resolves to a loopback address: 127.0.1.1; using 192.168.0.142 instead (on interface eth0)
21/10/17 20:25:07 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
log4j:WARN No appenders could be found for logger (org.apache.hadoop.util.NativeCodeLoader).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
21/10/17 20:25:07 INFO SecurityManager: Changing view acls to: root
21/10/17 20:25:07 INFO SecurityManager: Changing modify acls to: root
21/10/17 20:25:07 INFO SecurityManager: Changing view acls groups to: 
21/10/17 20:25:07 INFO SecurityManager: Changing modify acls groups to: 
21/10/17 20:25:07 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(root); groups with view permissions: Set(); users  with modify permissions: Set(root); groups with modify permissions: Set()
21/10/17 20:25:08 INFO Utils: Successfully started service 'driverClient' on port 36051.
21/10/17 20:25:08 INFO TransportClientFactory: Successfully created connection to /192.168.0.142:7077 after 51 ms (0 ms spent in bootstraps)
21/10/17 20:25:08 INFO ClientEndpoint: Driver successfully submitted as driver-20211017202508-0000
21/10/17 20:25:08 INFO ClientEndpoint: ... waiting before polling master for driver state
21/10/17 20:25:13 INFO ClientEndpoint: ... polling master for driver state
21/10/17 20:25:13 INFO ClientEndpoint: State of driver-20211017202508-0000 is RUNNING
21/10/17 20:25:13 INFO ClientEndpoint: Driver running on 192.168.0.100:45823 (worker-20211017202501-192.168.0.100-45823)
21/10/17 20:25:13 INFO ShutdownHookManager: Shutdown hook called
21/10/17 20:25:13 INFO ShutdownHookManager: Deleting directory /tmp/spark-d5da4c1e-e685-4512-b9ac-ded68ae44883
```

#### `master`网页端输出

![image-20211017203727702](https://oss.ydjsir.com.cn/GitPages/initSpark/image-20211017203727702.png)

> 图中我们可以看到我们的三个节点和三个节点加起来的内存（每个节点提供2GB内存）
>
> 刚刚的一次会对应一个Application，且其已经完成。

![image-20211017204007859](https://oss.ydjsir.com.cn/GitPages/initSpark/image-20211017204007859.png)

> 图中可以看到三个执行者都返回了结果，并使用了不同的核心数量。

#### `driver`详情页

![image-20211017204208916](https://oss.ydjsir.com.cn/GitPages/initSpark/image-20211017204208916.png)

> 点击`Finished Executors`的`stdout`，我们便可看到π的结果。

![image-20211017204444515](https://oss.ydjsir.com.cn/GitPages/initSpark/image-20211017204444515.png)

经过测试，在本地通过公网向集群提交计算任务是可行的。运行截图如下。

![image-20211017232101672](https://oss.ydjsir.com.cn/GitPages/initSpark/image-20211017232101672.png)

