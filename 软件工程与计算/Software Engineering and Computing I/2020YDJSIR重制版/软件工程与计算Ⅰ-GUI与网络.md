# 软件工程与计算Ⅰ-GUI，网络与线程

> 本部分对应于PPT 19-20

我想，就这一部分而言，最好的例子莫过于HFJ上面的“程序料理”这个例子了。因而我将以注释的方式展开这一部分，其他部分单独补充。

注意到这里传输的是String这一整个对象，因而用的是`ObjectInputStream`和`ObjectOutputStream`因而没有采用PrintWriter。

> 以下代码均来自https://github.com/bethrobson/Head-First-Java ，但是注释显然是YDJSIR写的。



## 代码示例

### 两个按钮

```java
//重点：内部类与事件触发
public class TwoButtons  {

    JFrame frame;
    JLabel label;

    public static void main (String[] args) {
       TwoButtons gui = new TwoButtons();
       gui.go();
    }

    public void go() {
       frame = new JFrame();
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

       JButton labelButton = new JButton("Change Label");
       labelButton.addActionListener(new LabelButtonListener());
//		这里要先new一个对象，不然的话它会显示在静态内容中调用非静态方法的错误!
//		事实上，
       JButton colorButton = new JButton("Change Circle");
       colorButton.addActionListener(new ColorButtonListener());

       label = new JLabel("I'm a label");       
       MyDrawPanel drawPanel = new MyDrawPanel();
       
       frame.getContentPane().add(BorderLayout.SOUTH, colorButton);
       frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
       frame.getContentPane().add(BorderLayout.EAST, labelButton);
       frame.getContentPane().add(BorderLayout.WEST, label);
//		 实际上这样写也是可以的（YDJSIR实测）
//        this.frame.getContentPane().add("South", colorButton);
//        this.frame.getContentPane().add("Center", drawPanel);
//        this.frame.getContentPane().add("East", labelButton);
//        this.frame.getContentPane().add("West", this.label);
//	     你甚至还可以这样写（类+方法名，不过你会绕不开没有先new一个对象导致的静态内容中调用非静态方法的错误!
//        labelButton.addActionListener(this::actionPerformedLabel1);
//        colorButton.addActionListener(this::actionPerformedLabel2);
       frame.setSize(420,300);
       frame.setVisible(true);//千万别忘了
    }
    
    //注意到非静态的内部类中不能有静态方法，但是你可以拥有一个静态内部类
     class LabelButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            label.setText("Ouch!");
        }
     } // close inner class

     class ColorButtonListener implements ActionListener {//
     }  // close inner class
   
}
```

### GUI中的动画

温馨提示：一定要记得把原来的图案擦掉！以及，每次绘图的时候必须Sleep一下，否则可能出现奇奇怪怪的错误！

```java
public class Animate {
    int x = 1;
    int y = 1;

    public static void main (String[] args) {//}

	/**
     * 将一个模块运行的主调用方法写到一个名为go的方法里面是惯例
     */
    public void go() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyDrawP drawP = new MyDrawP();
        frame.getContentPane().add(drawP);
        frame.setSize(500,270);
        frame.setVisible(true);
        for (int i = 0; i < 124; i++,x++,y++ ) {
            x++;
            drawP.repaint();//你可以调用方法让系统来帮你重新绘制，这一过程是异步的
            try {
                Thread.sleep(50);//防止速度过快直接一步到位了或者发生奇怪的错误
            } catch(Exception ex) { 
                ex.printStackTrace();//必须有try和catch！防御性编程。但是catch后你可以什么都不做
            }
        }
    }

    //内部类
    class MyDrawP extends JPanel {
        public void paintComponent(Graphics g  ) {
            g.setColor(Color.white);
            g.fillRect(0,0,500,250);
            g.setColor(Color.blue);
            g.fillRect(x,y,500-x*2,250-y*2);
        }
    }
}
```

### 聊天客户端

```java
package chap15;
import java.io.*;
import java.net.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class SimpleChatClient
{
    JTextArea incoming;
    JTextField outgoing;
    BufferedReader reader;
    PrintWriter writer;
    Socket sock;
    
    public void go() {
        JFrame frame = new JFrame("Ludicrously Simple Chat Client");
        JPanel mainPanel = new JPanel();
        incoming = new JTextArea(15, 50);
        incoming.setLineWrap(true);
        incoming.setWrapStyleWord(true);
        incoming.setEditable(false);
        JScrollPane qScroller = new JScrollPane(incoming);
        qScroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        qScroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        outgoing = new JTextField(20);
        JButton sendButton = new JButton("Send");
        sendButton.addActionListener(new SendButtonListener());
        mainPanel.add(qScroller);
        mainPanel.add(outgoing);
        mainPanel.add(sendButton);
        frame.getContentPane().add(BorderLayout.CENTER, mainPanel);
        setUpNetworking();
        Thread readerThread = new Thread(new IncomingReader());
        readerThread.start();
        frame.setSize(650, 500);//窗口大小
        frame.setVisible(true);
        
    }
    
    private void setUpNetworking() {
        try {
            sock = new Socket("127.0.0.1", 5000);
            InputStreamReader streamReader = new InputStreamReader(sock.getInputStream());
            reader = new BufferedReader(streamReader);
            writer = new PrintWriter(sock.getOutputStream());
            System.out.println("networking established");}
        catch(IOException ex)
        {ex.printStackTrace();}}
    
    //特别注意其中从文本框获取内容并发送的过程！
    public class SendButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent ev) {
            try {
                writer.println(outgoing.getText());
                writer.flush();
                
            }
            catch (Exception ex) {
                ex.printStackTrace();
            }
            outgoing.setText("");
            outgoing.requestFocus();
        }
    }
    
    public static void main(String[] args) {
        new SimpleChatClient().go();
    }
    
    class IncomingReader implements Runnable {
        public void run() {
            String message;
            try {
                while ((message = reader.readLine()) != null) {
                    System.out.println("client read " + message);
                    incoming.append(message + "\n");
                }
            } catch (IOException ex)
            {
                ex.printStackTrace();
            }
        }
    }
}


```

### BeatBox服务端

```JAVA
/**
 * 这实际上是一个聊天服务器
 */
public class BeatBoxServer
{
    ArrayList clientOutputStreams;

    public static void main(String[] args) {
        new BeatBoxServer().go();
    }

    //内部类！客户端请求处理者（暴力翻译）
    public class ClientHandler implements Runnable {
        ObjectInputStream in;
        Socket sock;

        public ClientHandler(Socket clientSOcket) {
            try {
                sock = clientSOcket;
                in = new ObjectInputStream(sock.getInputStream());
            } catch (Exception ex) {ex.printStackTrace(); }
        }

        public void run() {
            Object o1;
            Object o2;
            try {
                while ((o1 = in.readObject()) != null) {
                    o2 = in.readObject();
                    System.out.println("read two objects");
                    tellEveryone(o1, o2);
                }
            } catch (Exception ex) { ex.printStackTrace(); }
        }
    }//End of ClientHandler



    public void go() {
        clientOutputStreams = new ArrayList();//初始化
        try {
            //服务多个用户的能力有所增强，毕竟他一旦获取到一个请求他就开一个新的线程让新线程完成进一步的处理了
            ServerSocket serverSock = new ServerSocket(4242);
            while(true) {
                Socket clientSocket = serverSock.accept();
                ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
                clientOutputStreams.add(out);

                Thread t = new Thread(new ClientHandler(clientSocket));
                t.start();
                System.out.println("got a connection");
            }
        } catch (Exception ex) { ex.printStackTrace(); }
    }
    
    public void tellEveryone(Object one, Object two) {
        Iterator it = clientOutputStreams.iterator();
        while (it.hasNext()) {
            try {
                ObjectOutputStream out = (ObjectOutputStream) it.next();
                out.writeObject(one);
                out.writeObject(two);
            } catch (Exception ex) { ex.printStackTrace(); }
        }
    }
}//End of BeatBoxServer
```

### DailyAdvice

```java
/**
* 流式的优势在这里体现的很明显。不难发现，下面的操作极为类似于从System.in读取内容的过程和从文件中读取的内容，在提高运行效率的同时，
* 也的确让编码更为简易。
*/
public class DailyAdviceClient
{
    public void go() {
        try {
            Socket s = new Socket("127.0.0.1", 4242);
            InputStreamReader streamReader = new InputStreamReader(s.getInputStream()); 
            BufferedReader reader = new BufferedReader(streamReader);
            String advice = reader.readLine();
            System.out.println("Today you should: " + advice);
            reader.close();
        }
        catch (IOException ex)
        {ex.printStackTrace();}
    }
    
    public static void main(String[] args){//
    }
}

```

### DailyAdviceServer

```java
//注意：这个服务端一次显然只能为一个客户提供服务！
public class DailyAdviceServer
{
    String[] adviceList = {"Take smaller bites", "Go for the tight jeans. No they do NOT make you look fat",
        "One word: inappropriate", "Just for today, be honest.  Tell your boss what you *really* think", 
        "You might want to rethink that haircut"};
        
    public void go() {
        try {
            ServerSocket serverSock = new ServerSocket(4242);
            while (true)//持续运行
            {
                Socket sock = serverSock.accept();//一获取到客户端的请求，立刻建立连接并向客户端推送内容
                PrintWriter writer = new PrintWriter(sock.getOutputStream());
                String advice = getAdvice();
                writer.println(advice);
                writer.close();
                System.out.println(advice);
            }
        } catch (IOException ex)
        {
            ex.printStackTrace();
        }
    }
    
    private String getAdvice() {//}
    
    public static void main(String[] args){//}

}
```

## 补遗拾阙

### 线程锁，原子化（Synchronized方法关键字与默认的asynchronized情形）

多线程并发情况下，进程执行的先后顺序是不确定的（与具体的平台相关）

典型例子：取钱问题（夫妇一起取钱，都是先检验余额后取钱，但是多线程一起执行时，看余额与取钱总可能有时间差导致最终余额为负数）

解决方案：将取钱（检验余额与划拨这一步骤整合到一个带有Synchronized关键词的方法中，并只允许夫妇两人调用该方法。

### 线程的生命周期

一旦线程的`run()`方法完成之后，该线程就不再能重新启动。此时的Thread即使仍然在堆中，也已经失去了可执行性。

- 

  ### 三大布局管理器

| BorderLayout                                             | FlowLayout         | BoxLayout                                         |
| -------------------------------------------------------- | ------------------ | ------------------------------------------------- |
| 东南西北中，东西宽度优先，南北高度优先，中间的就挑剩下的 | 从上至下，从左至右 | 从上到下，也可以从左到右，也可以手动插入换行/换列 |

### GUI中的补充细节（HFJ第412页）

- 布局管理器会控制嵌套在其他组件中组件的大小和位置；

- 当某个组件添加到背景组件上面时，被加入的组件是由背景组件的布局管理器管理的；

- 布局管理器在做决定之前会询问组建的理想大小，并根据策略来决定选择采用哪些数据（但是你自己setSize得到的尺寸只能是向系统提供一个建议，并不能起决定性作用）；

- `pack()`方法会使窗口的大小符合内含组件的大小；

- 框架（JFrame）默认使用BoxLayout布局，然而面板默认使用FlowLayout布局；

- 框架上面不能直接加组件，框架的布局管理器可以自己换掉，也可以在关闭布局管理器之后直接定位；`然而在YDJSIR的JDK8里面，事实上真的可以这么做！`

- 给panel来add一个scroller就可以让他成为可以滚动的面板；

### GUI常见对象一览

GUI反正可以一层层反复套娃，进而得到繁复的结果。

| 名称               | 描述                       | 备注                                                         |
| ------------------ | -------------------------- | ------------------------------------------------------------ |
| JFrame - 框架      | 可以用来放JPanel           | 可以指定布局，默认是BoxLayout                                |
| JPanel - 面板      | 用来放具体的组件           | 可以指定布局，默认是FlowLayout                               |
| JButton - 普通按钮 | 一按下就触发事件并自动复位 |                                                              |
| JTextField         | 单行文本                   |                                                              |
| JTextArea          | 多行文本                   |                                                              |
| JList              | 列表                       |                                                              |
| JCheckBox          | 复选框                     | 用`isSelected`来判断是否被勾选，用`setSelected`来手动更改状态 |
| 还有？             |                            |                                                              |

### GUI绘图一览

可以类比LOGO里面那种编程画图的方式。

牢牢把握`setColor`和`fill<某种图形>`（Rect，Oval之类的）就好。注意到这里的setColor是改变笔触的颜色！

如有需要再继续补充。