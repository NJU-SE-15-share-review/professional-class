package HttpServer;

import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import static Util.ColorUtil.*;

/**
 * @Description: 服务端主进程
 * @Author:YDJSIR
 * @Date:2021-06-21 22:20
 * @Modifiers: YDJSIR
 */
public class Server extends Thread{
    private static boolean RUNNING = true;

    public Server(String hostname, int PORT){
    }
    /**
     * 服务器启动进程
     * @param hostname 服务器绑定的IP/域名
     * @param PORT  服务器监听的端口号
     * @throws Exception 各类异常
     */
    protected void run(String hostname, int PORT) throws Exception {
        ServerSocket server = new ServerSocket();
        server.bind(new InetSocketAddress(hostname, PORT));
        printRed("====>>>>server started<<<<====\n");

        while (RUNNING){
            try {
                Socket socket = server.accept();
                InetSocketAddress address = (InetSocketAddress) socket.getRemoteSocketAddress();
                printBlue("---->>>> request received <<<<----");
                System.out.println(address.getHostName());
                RequestHandler handler = new RequestHandler(socket);
                handler.start();
            }
            catch (Exception e){
                e.printStackTrace();
            }
        }
    }


}
