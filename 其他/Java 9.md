# What's new in Java 9

没有博客所以只能发到空间了

Java 9疯狂跳票之后终于在2017.9.24出了，因为引入了源于Jigsaw的模块化系统，这个版本可谓是一次伤筋动骨的调整。不过除了模块化还有哪些改变呢？不妨一起来看一看

源网页在<http://openjdk.java.net/projects/jdk9/>。按JEP的顺序简单提炼了下每一条中的信息，附带一点个人观点。

#### JEP 102: 进程API升级

* `java.lang.Process`和`java.lang.ProcessHandle`类
* 支持所有进程相关的操作，开始、终止、查看PID、获取父子进程等等。
* 支持异步API如`CompletableFuture`，线程的异步技巧应该都可以用在进程上
* _中规中矩_

#### JEP 110: HTTP/2 客户端

* `HttpURLConnection` API将被取代，新的API支持了 HTTP/2 和 WebSocket
* 目标是满足绝大部分的应用场景，而不是把所有功能全部支持
* 允许以异步方式执行，当然还是用`CompletableFuture`
* 支持认证机制。不过刚开始时仅支持Basic
* 支持HTTPS/TLS
* JDK 9中这是一个incubator模块，未来可能会持续发生改变。JDK10中会加入`java.net`
* 性能目标是不低于Jetty，Netty等包含的HTTP客户端


* _很棒_

#### JEP 143: 改进的竞争性锁

* 全面提升object monitor的性能，包括monitor enter/exit，Object.notify/notifyAll
* 仅针对java monitor的性能，VM内部的锁不属于提案的范围
* _很棒，但并不能拯救傻逼设计_

#### JEP 158: 统一的JVM日志

* 通过一大堆命令行选项来定制日志格式啊重定向啊什么的，还可以通过jcmd jmx之类的来搞，**Java API暂时没有，以后可能会有**
* _注意是给VM打log的_

#### JEP 165: Compiler控制

* 运行时控制JIT compiler(C1, C2)
* _我想大概大部分人很难用到_

#### JEP 193: 变量句柄

* 类似于方法句柄
* 变量句柄是一个变量的类型化的引用(就像C++里的引用一样)，提供受限制的**直接**访问**某一内存地址**的机制，支持在这个变量上的操作，比如读写和CAS等等，这将取代`sun.misc.Unsafe`类和`java.util.concurrent.atomic`
* 现在支持的变量类型有实例域，静态域和数组成员，以后可能会加入其它的
* array view，即例如将byte[]当作long[]来访问(就像char c[100], long* lptr = (long*)c这样)，以及访问堆外内存(通过ByteBuffer)等。
* 支持内存屏障级别的设置
* 和MethodHandle的互操作性
* _Exciting! 进一步提高了Java的动态性_


#### JEP 197: 分段代码缓存

* 把JVM的代码区分成了三个部分，对不同区的代码采取不同的优化策略
* _JVM相关的，也是一般人碰不上的，具体自行搜索_


#### JEP 199: 智能Compiler

* sjavac编译器，javac的wrapper，提供了
  * 更智能的增量编译
  * 并行编译
  * 重用编译器实例（我理解为跑一个编译器进程在后台，以client-server的方式调用进行编译）
* 对于庞大的代码量比较有用

#### JEP 200: 模块化JDK

* 模块化之一(下一个是JEP 201)。定义了JDK模块化的结构。


* 由JCP管理的标准模块以`java.`开头

* 仅包含于JDK的模块以`jdk.`开头

* 如果一个模块中的类型，它的public或protected成员（变量或方法）使用了其他模块中的类型，那么，通过依赖传递(`requires transitive`)，前者则向第三方授权了对后者的默许可读性(implied readability)。（就是A引用了B，那么C用了A的同时也能用B了）

* 标准模块可以同时包含标准API包和非标准API包。如果标准模块开放/暴露(export)一个标准API包，那么这个开放可以可选地进行验证(may be qualified)；如果开放一个非标准API，那这个开放必须被验证(must be qualified)。无论如何，如果标准模块开放了一个带验证(qualification)的包，那么这个开放必须是JDK模块的自己。如果标准模块是一个Java SE的模块，那么它不能开放任何非SE的API，至少不能在没有验证的情况下开放。

* 标准模块可能会依赖于非标准模块，这中情况下它不能授权对后者的默许可读性。如果是一个SE模块，那么它不能授权对非SE模块的默许可读性

* 非标准模块不能开放任何标准API包。它可以授权对标准模块的默许可读性

* ![](https://bugs.openjdk.java.net/secure/attachment/72525/jdk.png)

  慢慢看吧

  * 黄色表示标准SE模块，蓝色是非SE模块
  * 模块间的线表示依赖关系，实线表示同时授权了可读性，虚线表示没有授权
  * 最下面试`java.base`，所有其他的模块全部依赖它
  * 最上面是`java.se.ee`，这是一个聚合模块，聚合了所有SE的模块以及一部分与EE有交叉的模块，但是本身没有添加新的内容。而`java.se`聚合了所有SE的模块但是没有EE的。
  * 非标准模块包含debug和服务性工具，比如jcmd啊jconsole啊，开发工具比如javadoc啊xml.bind啊，还有服务提供者，比如scripting.nashorn啊crypto.ec啊。
  * `java.smartcardio`是标准模块但不是SE模块

* _挺好的。反正JDK模块都是划分好的，用就是了_

#### JEP 201: 模块化JDK代码

* 模块化之二(下一个是JEP 200)。把JDK代码模块化，便于编译
* _没我们啥事儿_

#### JEP 211: 去除了import带来的的deprecation警告

* 如题，就是你import一个@Deprecated的类或者静态方法的时候不会警告了（就是只import但是没用的话，用了还是要警告的）
* _反正本来就没什么用_

#### JEP 212: 解决Lint和Doclint警告

* 把JDK代码里原来有的警告给解决了
* _原来大佬们也不看warning的_

#### JEP 213: Project Coin的改进

* Project Coin就是JDK 7的那一系列改进的统称，这个JEP是对这些改进的进一步优化。这也是Java 9语法层面的改变。
* `@SafeVarargs`允许用在私有实例方法上了
* 允许在`try-with-resource`的初始化部分是用effectivly-final的变量了，意思就是不在需要直接在try(...)里面直接new出来Closeable，可以拿个effectively-final的变量放进去了（这个提案在Project Coin提出时已经来不及加进标准里了，所以现在才加（所以为什么不在Java 8加呢，非要等同一个JEP的其他部分全部完成才行吗））
* 可以把可表示的匿名类放在<>里面了。我一时想不到可表示的匿名类是什么样的，等我想到了更一下这边……
* 下划线不再是合法的变量名了！
* 私有非abstract接口方法！让你不用把一堆代码全都塞到default方法里。接口和抽象类越来越像了
* _就这么多，是不是觉得很没诚意_




#### JEP 214: 移除一些过期的GC方式组合

* ```
  DefNew + CMS       : -XX:-UseParNewGC -XX:+UseConcMarkSweepGC
  ParNew + SerialOld : -XX:+UseParNewGC
  ParNew + iCMS      : -Xincgc
  ParNew + iCMS      : -XX:+CMSIncrementalMode -XX:+UseConcMarkSweepGC
  DefNew + iCMS      : -XX:+CMSIncrementalMode -XX:+UseConcMarkSweepGC -XX:-UseParNewGC
  CMS foreground     : -XX:+UseCMSCompactAtFullCollection
  CMS foreground     : -XX:+CMSFullGCsBeforeCompaction
  CMS foreground     : -XX:+UseCMSCollectionPassing
  ```

  上面这些GC方式被移除了

* _CMS过气啦！_



#### JEP 215: javac的层叠属性(Tired Attribution for javac)

* 编译相关，新的类型推导方式，用于确定调用方法的哪一个重载版本
* _超出知识范围了，不明觉厉……_



#### JEP 216: 正确处理import 语句

* 修复了特定的import顺序导致不能通过编译的问题
* _这……这怎么是个JEP，不是issue吗_



#### JEP 217: 注解管道2.0

* 重新设计javac里的注解处理，可以把注解加在更多奇怪的地方了，比如

  ```java
  Function<String, String> fss = (@Anno @Anno String s) -> s;
  ```

* javadoc中的注解也有升级，不过是在另一个地方

* _可以有更多骚操作了_



#### JEP 219: DTLS

* 实现了数据包传输层安全(Datagram Transport Layer Security)，就是UDP的TLS
* 然后提供了一些API，具体请参见官方文档
* _挺好_



#### JEP 220: 运行时模块映像 

* 模块化之三(下一个是JEP 261)。

* 旧的映像结构（其实就是JRE和JDK的目录结构）自己去复习。新的映像结构中，JDK简单的在JRE的结构的基础上加了一些开发工具，运行时映像的部分将完全相同——而不是像以前一样JDK把JRE包含在内。具体的结构如下:

  * bin: 由这个映像所链接的所有模块（还记得模块化的JDK代码吗，JEP 201）所定义的命令行launcher

  * conf: 包含了.properties，.policy和其他将会由开发者，部署者或者用户修改的配置参数

  * lib: 运行时所需要的动态链接库。除了少量的供外界使用的文件，其他文件将被视为是私有的（更改不会被通知）

  * legal: license和版权信息，按照模块组织

  * 完整的JDK还有demo，man，include等目录，但是samples没了（JEP 298，_这也要搞个JEP出来……_）

  * endorsed-standards override机制被移除！将会由可升级模块(upgradeable modules)来替代。

  * 拓展(extension)机制被移除。但是拓展类加载器被保留了，不过改名叫平台类加载器(platform class loader)

  * **重磅: rt.jar和tools.jar被移除了！**原来的被包含在这两个里面的类被移到lib里。同时这带来了一些问题：

    * 我们都知道原来`ClassLoader::getSystemResource`原来返回的是像这样的URI`jar:file:/usr/local/jdk8/jre/lib/rt.jar!/java/lang/Class.class`，然后你需要用`getContent`来读取这个jar里的资源。而现在由于引入了模块化，现在返回的是以jrt为scheme的URL，举个栗子:

      `ClassLoader.getSystemResource("java/lang/Class.class")`

      返回:

      `java.net.URL: jrt:/java.base/java/lang/Class.class`

    * 和上一条原因一样，原来的依赖于URL的`java.security.CodeSource`和安全策略文件，比如`file:${java.home}/lib/ext/sunec.jar`当然也不再合法了。

    * IDE和其他要直接打开rt.jar等来枚举类和资源文件的开发工具，现在当然也用不了啦

  * 用来解决上面一条的问题的，新的URI scheme，jrt，格式是`jrt:/[$MODULE[/$PATH]]`：

    * `jrt:/`表示所有包含在当前运行时映像中的类和资源文件
    * `jrt:/$MODULE`表示所有包含在这个模块中的类和资源文件
    * `jrt:/$MODULE/$PATH`表示某个特定的类或资源文件

    ​

    * `ClassLoader::getSystemResource`返回jrt的URL，如上面的例子所示

    * `java.security.CodeSource` API当然也一样啦

    * 对jrt scheme的URL提供了NIO FileSystem provider来实现枚举的目的。示例：

      ```java
      FileSystem fs = FileSystems.getFileSystem(URI.create("jrt:/"));
      byte[] jlo = Files.readAllBytes(fs.getPath("modules", "java.base", "java/lang/Object.class"));
      ```

      在这个文件系统中，顶级的modules目录中每个模块有一个目录，顶级的packages目录中每个包有一个子目录，这个子目录中包含了一个符号链接，指向定义了这个包的模块在modules下对应的子目录。

      另外，对于要在JDK 8上运行但是目标是支持JDK 9开发的工具，在lib目录下放了个在JDK 8下使用的jrt-fs.jar。_真贴心啊_

  * 当然了，构建系统也变化了。值得一提的是我们没放过这个机会，终于把`images/j2sdk-image`和`images/j2re-image`目录改名叫`images/jdk`和`images/jre`了。_感觉这背后一把辛酸泪_。

  * 标准上的一点微小的变化。有些需要在lib目录里查找配置文件的标准规格声明被删去了，因为这些文件现在放到conf目录了嘛。这项工作在JDK 8中由JEP 162已经完成了一部分了，去除了仅属于Java SE的一些类库，而现在一些SE和EE共有的也被完成了调整，包括

    `javax.xml.stream.XMLInputFactory`

    `javax.xml.ws.spi.Provider`

    `javax.xml.soap.MessageFactory`

* _这大概将是不兼容性的最大来源，也就是迁移至JDK 9的最大阻力了。但是这本身是件好事，映像结构变得更加清晰明了，资源的访问方式也会更优雅一些_

未完待续，看心情更