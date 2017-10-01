#hat's new in Java 9

Java 9疯狂跳票之后终于在2017.9.24出了，因为引入了源于Jigsaw的模块化系统，这个版本可谓是一次伤筋动骨的调整。不过除了模块化还有哪些改变呢？不妨一起来看一看

源网页在<http://openjdk.java.net/projects/jdk9/>。按JEP的顺序简单提炼了下每一条中的信息，附带一点个人观点。

####JEP 102: 进程API升级

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

* 锵锵，总所周知的模块化，这个JEP是针对模块化JDK的，关于模块化的内容在多个JEP中，请往下看


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

* 把JDK代码模块化，便于编译
* _没我们啥事儿_

#### JEP 211: 去除了import带来的的deprecation警告

* 如题，就是你import一个@Deprecated的类或者静态方法的时候不会警告了（就是只import但是没用的话，用了还是要警告的）
* _反正本来就没什么用_

#### JEP 212: 解决Lint和Doclint警告

* 把JDK代码里原来有的警告给解决了
* _原来大佬们也不看warning的_

#### JEP 213: Project Coin的改进

* Project Coin就是JDK 7的那一系列改进的统称，这个JEP是对这些改进的进一步优化
* `@SafeVarargs`允许用在私有实例方法上了
* 允许在`try-with-resource`的初始化部分是用effectivly-final的变量了，意思就是不在需要直接在try(...)里面直接new出来Closeable，可以拿个effectively-final的变量放进去了（这个提案在Project Coin提出时已经来不及加进标准里了，所以现在才加（所以为什么不在Java 8加呢，非要等同一个JEP的其他部分全部完成才行吗））
* 可以把可表示的匿名类放在<>里面了。我一时想不到可表示的匿名类是什么样的，等我想到了更一下这边……
* 下划线不再是合法的变量名了！
* 私有非abstract接口方法！让你不用把一堆代码全都塞到default方法里。最直接的，实现模板模式可以直接用一个接口完成了


未完待续，看心情更
