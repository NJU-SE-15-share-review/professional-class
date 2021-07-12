package HttpServer;

import HttpServer.persistentUtil.DefaultObjectAction;
import HttpServer.persistentUtil.ObjectAction;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ConcurrentHashMap;

import static Util.ColorUtil.*;

/**
 * @description: 长连接测试请求处理
 * @author: GZK
 * @date: 2021/6/27 10:16
 * @Modifiers: YDJSIR
 */
public class PersistentRequestHandler extends Thread{
    private int port;
    private boolean running=true;
    private long receiveTimeDelay = 8000; // 连接断开时间
    private ConcurrentHashMap<Class, ObjectAction> actionMapping = new ConcurrentHashMap<Class,ObjectAction>();
    private Thread connWatchDog;

    public PersistentRequestHandler(int port) {
        this.port = port;
    }

    /**
     * 进程启动
     */
    public void start(){
        System.out.println(ANSI_RED +"---->>>> Persistent Connection Keep Alive<<<<----"+ ANSI_RESET);
        connWatchDog = new ConnWatchDog();
        connWatchDog.start();
    }

        public static void main(String[] args) {
        int port = 8081;
        PersistentRequestHandler server = new PersistentRequestHandler(port);
        server.start();
    }

    /**
     * 持续监听端口，并处理客户端发来的连接维持包
     */
    class ConnWatchDog extends Thread {
        @Override
        public void start(){
            try {
                ServerSocket ss = new ServerSocket(port,5);
                printRed("WatchDog ON");
                while(running){
                    Socket s = ss.accept();
                    new SocketAction(s).start();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }

    /**
     * 具体处理客户端发来的连接维持包
     */
    class SocketAction extends Thread{
        Socket s;
        boolean run=true;
        int timeWarnAdvance = 3000;
        boolean hasWarned = false;
        long lastReceiveTime = System.currentTimeMillis();
        public SocketAction(Socket s) {
            this.s = s;
        }
        @Override
        public void start() {
            while(running && run) {
                if (System.currentTimeMillis() - lastReceiveTime > receiveTimeDelay - timeWarnAdvance) {
                    if (System.currentTimeMillis() - lastReceiveTime > receiveTimeDelay) {
                        overThis(); // 调用超时处理方法
                    }
                    else if (!hasWarned) {
                        printRed("没有收到维持包，\t3\t秒内连接即将关闭");
                        hasWarned = true;
                    }
                }
                else {
                    try {
                        InputStream in = s.getInputStream();
                        if (in.available() > 0) {
                            ObjectInputStream ois = new ObjectInputStream(in);
                            Object obj = ois.readObject();
                            lastReceiveTime = System.currentTimeMillis();
                            printGreen("\n接收来自 " +  s.getRemoteSocketAddress() + " " + obj);
                            ObjectAction oa = actionMapping.get(obj.getClass());
                            oa = oa == null ? new DefaultObjectAction() : oa;
                            Object out = oa.doAction(obj, PersistentRequestHandler.this);
                            if (out != null) {
                                ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());
                                oos.writeObject(out);
                                oos.flush();
                            }
                        } else {
                            Thread.sleep(10); // 读不到输入流就睡一会儿
                        }
                    } catch (Exception e) {
                        overThis();
                    }
                }
            }
        }

        /**
         * 超过等待时间后，服务端关闭连接
         */
        private void overThis() {
            if(run)run=false;
            if(s!=null){
                try {
                    s.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if(s != null)
                printRed("\n关闭与"+s.getRemoteSocketAddress() + "的连接");
                printRed("==========================================");
        }
    }
}
