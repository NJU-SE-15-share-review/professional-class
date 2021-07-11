package HttpClient;

import HttpClient.persistentUtil.DefaultObjectAction;
import HttpClient.persistentUtil.KeepAlive;
import HttpClient.persistentUtil.ObjectAction;
import java.io.*;
import java.net.Socket;
import java.util.concurrent.ConcurrentHashMap;
import static Util.ColorUtil.*;

/**
 * @description: 长连接专用客户端实现
 * @author: gzk
 * @date: 2021/6/27 9:53
 * @Modifiers: YDJSIR
 */
public class PersistentClient {
    private String HOSTNAME;
    private int maxTrial = 10;
    private int port;
    private Socket socket;
    private boolean running = false; // 连接状态
    private long lastSendTime; //   最后一次发送数据的时间
    private ConcurrentHashMap<Class, ObjectAction> actionMapping = new ConcurrentHashMap<Class, ObjectAction>();  //用于保存接收消息对象类型及该类型消息处理的对象

    /**
     * 构造方法
     * @param HOSTNAME 服务端地址
     * @param port 端口
     */
    public PersistentClient(String HOSTNAME, int port, int times) {
        this.HOSTNAME = HOSTNAME;
        this.port = port;
        this.maxTrial = times;
    }

    /**
     * 长连接客户端进程启动
     */
    public void start() {
        try {
            if (running) return;
            socket = new Socket(HOSTNAME, port);
            printPurple("本地端口：" + socket.getLocalPort());
            printBlue("---->>>> Persistent Connection Build Successfully! <<<<----");

            lastSendTime = System.currentTimeMillis();
            running = true;
            new Thread(new KeepAliveWatchDog()).start();  //保持长连接的线程，每隔2秒项服务器发一个一个保持连接的心跳消息
            new Thread(new ReceiveWatchDog()).start();    //接受消息的线程，处理消息
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }

    /**
     * 停止服务
     */
    public void stop() {
        printRed("\n本地" + socket.getLocalPort() + "端口上的连接维持包发送停止\n");
        if (running) running = false;
        System.out.print("Client to " + HOSTNAME + ':' + (port - 1) + ": ");
    }

    /**
     * 添加接收对象的处理对象。
     * @param cls    待处理的对象，其所属的类。
     * @param action 处理过程对象。
     */
    public void addActionMap(Class<Object> cls, ObjectAction action) {
        actionMapping.put(cls, action);
    }

    /**
     * 发送对象
     * @param obj 发送对象
     * @throws IOException IO异常
     */
    public void sendObject(Object obj) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
        oos.writeObject(obj);
        printGreen("发送：\t" + obj);
        oos.flush();
    }

    /**
     * 不断发送连接维持包维持与服务器的长连接
     */
    class KeepAliveWatchDog implements Runnable {
        long checkDelay = 10;   // 每10ms检查一次输入流情况
        long keepAliveDelay = 2000;  // 每隔2秒项服务器发一个一个保持连接的心跳消息

        int cnt = 1;

        public void run() {
            System.out.println();
            while (running) {
                if (System.currentTimeMillis() - lastSendTime > keepAliveDelay) {  //当线程距上次超过2s就发送信息
                    try {
                        if(cnt > maxTrial){
                            PersistentClient.this.stop();
                        }
                        else {
                            printRed("\n发送第" + cnt + "个连接维持包");
                            PersistentClient.this.sendObject(new KeepAlive());
                            cnt++;
                            lastSendTime = System.currentTimeMillis();
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                        PersistentClient.this.stop();
                    }
                } else {
                    try {
                        Thread.sleep(checkDelay);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                        PersistentClient.this.stop();
                    }
                }
            }
        }
    }

    /**
     * 不断接收连接维持包维持与服务器长连接
     */
    class ReceiveWatchDog implements Runnable {
        public void run() {
            while (running) {
                try {
                    InputStream in = socket.getInputStream();
                    if (in.available() > 0) {
                        ObjectInputStream ois = new ObjectInputStream(in);
                        Object obj = ois.readObject();
                        printBlue("接收：\t" + obj);
                        ObjectAction oa = actionMapping.get(obj.getClass());
                        oa = oa == null ? new DefaultObjectAction() : oa;
                        oa.doAction(obj, PersistentClient.this);
                    } else {
                        Thread.sleep(10);
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                    PersistentClient.this.stop();
                }
            }
        }
    }
}
