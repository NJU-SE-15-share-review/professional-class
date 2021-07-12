<div class="cover" style="page-break-after:always;font-family:方正公文仿宋;width:100%;height:100%;border:none;margin: 0 auto;text-align:center;">
    <div style="width:60%;margin: 0 auto;height:0;padding-bottom:10%;">
        </br>
        <img src="https://oss.ydjsir.com.cn/NJU-Black.png" alt="校名" style="width:86%;"/>
    </div>
    </br></br></br></br></br>
    <div style="width:60%;margin: 0 auto;height:0;padding-bottom:40%;">
        <img src="https://oss.ydjsir.com.cn/NJU-LOGO-Black.png" alt="校徽" style="width:45%;"/>
	</div>
    </br></br></br>
<span style="font-family:华文黑体Bold;text-align:center;font-size:24pt;margin: 10pt auto;line-height:30pt;">基于Java Socket API搭建简单的<br>HTTP客户端和服务器端程序</span>
    </br>
	</br>
    <table style="border:none;text-align:center;width:90%;font-family:仿宋;font-size:14px; margin: 0 auto;line-height:1.5">
    <tbody style="font-family:方正公文仿宋;font-size:16pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">指导教师</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 刘峰 </td>     </tr>
        <tr style="font-weight:normal;"> 
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">日　　期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">2021年6月27日</td>     </tr>
    </tbody>              
    </table>
</div>

<!-- 注释语句：导出PDF时会在这里分页 -->

<table  style="border:none;text-align:center;width:100%;font-family:华为细黑;font-size:12px; margin: 0 auto;line-height:1.5">
	<tr style="font-weight:normal;font-size:22px"> 
    	<td style="width:20%;text-align:left; ">组员信息</td>
	</tr>
</table>
<table style="text-align:center;width:100%;font-family:楷体;font-size:14px; margin: 0 auto;line-height:1.5">
    <tbody style="font-family:仿宋;font-size:14pt;">
    	<tr style="font-weight:normal;font-family:黑体"> 
            <td style="width:30%;text-align:center;">姓名</td>
            <td style="width:30%;text-align:center;">院系</td>
            <td style="width:30%;text-align:center;">学号</td>
         </tr>
    	<tr style="font-weight:normal;font-size:12pt;"> 
            <td style="width:30%;text-align:center;"></td>
            <td style="width:30%;text-align:center;"></td>
            <td style="width:30%;text-align:center;">191250</td>
        </tr>







<table  style="border:none;text-align:center;width:100%;font-family:华为细黑;font-size:22px; margin: 0 auto;line-height:1.5">
	<tr style="font-weight:normal;font-size:22px"> 
    	<td style="width:20%;text-align:left;">组员分工</td>
	</tr>
</table>
<table  style="border:none;text-align:center;width:100%;font-family:华文细黑;font-size:16px; margin: 0 auto;line-height:1.5">
	<tr style="font-weight:normal;"> 
    	<td style="width:100%;text-align:left;"></td>
	</tr>
</table>

选题与团队管理；

所有与`GET`方法相关部分；

`TUI`交互设计；

代码合并；

<table  style="border:none;text-align:center;width:100%;font-family:华文细黑;font-size:16px; margin: 0 auto;line-height:1.5">
	<tr style="font-weight:normal;"> 
    	<td style="width:100%;text-align:left;"></td>
	</tr>
</table>


参考资料搜集；

所有与`POST`方法相关部分；

登录接口实现；

<table  style="border:none;text-align:center;width:100%;font-family:华文细黑;font-size:16px; margin: 0 auto;line-height:1.5">
	<tr style="font-weight:normal;"> 
    	<td style="width:100%;text-align:left;"></td>
	</tr>
</table>

`HTTP` 长连接实现；

<table  style="border:none;text-align:center;width:100%;font-family:华文细黑;font-size:16px; margin: 0 auto;line-height:1.5">    <tr style="font-weight:normal;">         <td style="width:100%;text-align:left;"></td>    </tr></table>

客户端`MIME`解析；

登陆数据持久化；

协助报告撰写；

<table  style="border:none;text-align:center;width:100%;font-family:华文细黑;font-size:16px; margin: 0 auto;line-height:1.5">    <tr style="font-weight:normal;">         <td style="width:100%;text-align:left;"></td>    </tr></table>

`TUI`界面与交互优化；

视频录制与报告撰写；

<!-- 注释语句：导出PDF时会在<div STYLE="page-break-after: always;"></div>这里分页 -->

<div STYLE="page-break-after: always;">


# 基于Java Socket API搭建简单的<br>HTTP客户端和服务器端程序

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;"></div></center>

<center><span style="font-family:华文楷体;font-size:9pt;line-height:9mm">南京大学软件学院</span>
</center>
<div>
<div style="width:52px;float:left; font-family:方正公文黑体;">摘　要：</div> 
<div style="overflow:hidden; font-family:华文楷体;">本项目对应的HTTP客户端和服务端通信原型程序基于NIO模型实现了简单的HTTP请求与响应功能，能独立支持长连接，并在此基础上实现了注册与登录功能。本项目的客户端可以接收部分多媒体资源并调用系统相关程序处理。本项目的服务端能作为静态网页的服务端供正常浏览器访问。本项目完成了对应作业主题内所有要求的功能点，且有相当好的可视化效果。</div>
</div>
<div>
<div style="width:52px;float:left; font-family:方正公文黑体;">关键词：</div> 
<div style="overflow:hidden; font-family:华文楷体;">Socket；HTTP；Java；</div>
</div>





## 开发环境

| 项目     |      | 内容                |
| -------- | ---- | ------------------- |
| 操作系统 |      | Windows10 64位      |
| 开发语言 |      | Java                |
| 语言环境 |      | Oracle JDK 1.8 64位 |

## 程序运行详解

### IO模型

本项目的客户端采用了`BIO`，即同步阻塞的通信模式。客户端一请求一应答，客户端在等待服务器端响应的期间不会处理其他任务。而本项目的服务端采用了`NIO`，即同步非阻塞的模型，针对特定请求新建一个`RequestHandler`来进行处理，具有一定的并发性能。

### HTTP客户端基础请求

#### 客户端与服务器端连接

客户端命令行界面提示输入服务端的地址与端口号。

<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E8%BF%9E%E6%8E%A5c1.png" style="zoom: 67%;" />

<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E8%BF%9E%E6%8E%A5s1.png" style="zoom:67%;" />

#### 发起`GET`请求

HTTP客户端可以通过命令行发送请求报文、呈现响应报文，如在客户端命令行键入`GET /index.html`

![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/GET%20indexc1.png)

#### 对301、302、304的状态码处理

##### 301

​	在客户端命令行键入`GET /301origin.html`

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/301%201%20c1.png" style="zoom:67%;" />

在前面的`301重定向成功`的情况下，若再次在客户端命令行键入`GET /301origin.html`，系统会显示根据缓存被重定向到第一次服务地返回的地址。

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/301%202%20c.png" style="zoom: 80%;" />

##### 302

在客户端命令行键入`GET /302origin.html`

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/302%201%20c.png" style="zoom:67%;" />

在2前面已经有的`302重定向成功`经历情况下，再次在客户端命令行键入`GET /302origin.html`，和前一次操作得到的响应没有区别，因为302请求的地址不会被缓存。

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/302%202%20c.png" style="zoom: 67%;" />

301是永久性转移，会移除旧地址的资源，客户端抓取新内容的同时将旧地址转换为重定向到的新地址，即新地址可缓存；而302是暂时性转移，不会移除旧地址的资源，客户端抓取新内容保存旧地址，不会缓存新地址。

##### 304

对304响应码的处理，304指`没有改动`，虽然归为重定向一类，但与重定向没有太大的关系。

![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E7%99%BB%E5%BD%95s.png)

### HTTP服务端基础响应

#### 响应GET请求

​	服务器端对客户端的GET请求予以响应，服务器的表现如下。

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/get%20index%20s1.png" style="zoom: 80%;" />

#### 响应POST请求

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/post%20server.png" style="zoom: 50%;" />

#### 对200、301、302、304、404、405、500状态码的处理

##### 200	

服务器端返回`200`以及对应资源，已在前面的例子`GET index.html`可以说明。

##### 301

服务器端返回`301`以及对应资源。

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/301%201%20s1.png)

##### 302

服务器端返回`302`以及对应资源。

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/302%202%20s.png)

##### 304

服务器端返回`304`。![](report (1).assets/登录s.png)

##### 404

如在客户端键入一个对不存在资源的请求，则服务端返回`404`状态码和设置好的`404`页面。

![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/404%20c1.png)

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/404%20S.png)

##### 405

​	如客户端未被授权，返回`405` 方法不被允许。![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/s%20405.png)

##### 500

此处用一个全局的布尔状态值模拟此种情况。

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/500%20c.png" style="zoom:80%;" />

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/500%20s.png)

### 长连接支持

<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E9%95%BF%E8%BF%9E%E6%8E%A5c1.png" style="zoom:80%;" />

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E9%95%BF%E8%BF%9E%E6%8E%A5s1.png)

​	![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E9%95%BF%E8%BF%9E%E6%8E%A5c2.png)

### MIME支持

我们支持多种类型的MIME，包含图片等非文本类型，可以将图片通过弹窗展示

#### 文本类

之前的例子已可说明。下以`text/javascript`为例。

​	<img src="https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/js%20c.png" style="zoom:80%;" />

#### 图片类

客户端请求`GET \images\1.jpg`，受到相应后将文件存到本地并用系统默认图片查看器打开。

![](https://se-hw.oss-cn-shanghai.aliyuncs.com/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A/%E8%AE%A1%E7%BD%91%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%88%AA%E5%9B%BE/%E5%9B%BE%E7%89%87%E6%98%BE%E7%A4%BAc.jpg)

### 注册，登录功能的实现

- 更多内容请参考操作的录制视频

## 关键代码解析

 1. 服务器端实现重定向构造了一个`class RedirectList`类，这个类构造了表示重定向列表的旧地址以及相应新地址的哈希表，和表示重定向类型的表。该类通过从配置文件中获取重定向的列表，从而处理服务端发来的对重定向文件的请求。

	```java
        public static HashMap<String, String> redirectLists = new HashMap<>();
        public static HashMap<String, Integer> redirectTypes = new HashMap<>();
    ```

 2. 服务端的`class PersistentRequestHandler`是实现长连接的关键类。
 3. 服务端对客户端请求的处理、响应被封装在`class RequestHandler`中，并由`class Server`创建此类的对象，并调用该类的开始处理的方法，Server类是服务端的主进程，而SeverMain类承担着提供服务器主进程入口的职责。
 4. 客户端由两个主要的模块，一个是对客户端主进程的实现，一个是独立于HTTP进程的客户端向服务端发送维持连接包的实现，并且要不断地接收服务器发来的维持连接包。
 5. 与服务端类似，ClientMain是客户端主进程的入口，而Client类封装了客户端的主进程。

 - 更多请参考代码注释。

## 总结

本小组基于Java Socket API实现了基本的HTTP请求和响应功能以及用户的注册和登录的功能。

由于客户端与服务端的通信模型是BIO，程序在功能完整的情况下，也存在着效率偏低的问题。

## 致谢

感谢小组成员的付出！感谢刘峰老师的指导！

## 参考资料

1. https://docs.oracle.com/javase/tutorial/networking/sockets/index.html
2. http://www.runoob.com/java/java-networking.html
3. https://tools.ietf.org/html/rfc2616
4. https://github.com/Jekton/libhttp
5. https://github.com/germania/httpclient
6. https://github.com/TooTallNate/Java-WebSocket
7. https://juejin.cn/post/6844903630047281159

