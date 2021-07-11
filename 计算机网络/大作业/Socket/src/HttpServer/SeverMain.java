package HttpServer;

import Util.StatusCodeAndPhrase;

import static Util.ColorUtil.*;
import java.io.*;
import java.util.HashMap;
import java.util.Objects;

/**
 * @Description: 服务端进程主入口
 * @Author:sugarXu
 * @Date:2021-06-21 22:20
 * @Modifiers: YDJSIR
 */
public class SeverMain {
    public static  int DEFAULT_PORT = 8080;
    public static  String HOSTNAME = "127.0.0.1";
    public static  String NOT_FOUND_RES = "/404.html"; // 自定义404页面
    public static  String SERVER_ERROR_RES = "/500.html"; // 凡是服务器错误都返回这个页面
    public static  String BIND_DIR = "/Resources";
    public static  String[] DEFAULT_INDEX = {"index.html", "index.htm"}; // 默认主页
    public static boolean isDebug = true;
    public static HashMap<String,String> config = null;
    public static StatusCodeAndPhrase statusCodeList = StatusCodeAndPhrase.getStatusCodeList();
    public static RedirectList redirectList = RedirectList.getRedirectList();

    /**
     * 服务端进程主入口
     * @param args 程序启动参数
     */
    public static void main(String[] args) {

        Server httpServer;
        int port = DEFAULT_PORT;
        String hostname = HOSTNAME;
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        printCyan("__          __  _____        _____             \n" +
                " \\ \\        / / |  __ \\      |  __ \\            \n" +
                "  \\ \\  /\\  / /__| |  | | ___ | |__) |__ _ _   _ \n" +
                "   \\ \\/  \\/ / _ \\ |  | |/ _ \\|  _  // _` | | | |\n" +
                "    \\  /\\  /  __/ |__| | (_) | | \\ \\ (_| | |_| |\n" +
                "     \\/  \\/ \\___|_____/ \\___/|_|  \\_\\__,_|\\__, |\n" +
                "                                           __/ |\n" +
                "                                          |___/ ");
        printCyan("欢迎使用WeDoRay小组HTTP服务端！\n");
        if(!isDebug){
            printBlue("请输入配置文件位置，不需要则直接跳过");
            try {
                String path = bf.readLine();
                phraseConfig(path);
                if(config != null){
                    DEFAULT_PORT = Integer.parseInt(config.get("DEFAULT_PORT"));
                    HOSTNAME = config.get("HOSTNAME");
                    NOT_FOUND_RES = '/' + config.get("NOT_FOUND_RES");
                    SERVER_ERROR_RES = '/' + config.get("NOT_FOUND_RES");
                    BIND_DIR = '/' + config.get("BIND_DIR");
                    DEFAULT_INDEX = config.get("DEFAULT_INDEX").split(",");
                }
            } catch (IOException e) {
                printRed("配置文件加载失败");
            } catch(Exception e){
                printBlue("配置文件已加载");
            }
            printPurple("服务器监听" + port);
        }
        try {
            printBlue("输入PERSISTENT进入长连接服务器模式，否则进入普通服务器模式");
            String op = bf.readLine().toUpperCase();
            if(!op.equals("PERSISTENT")) {
                httpServer = new Server(hostname, port);
                printPurple(Objects.requireNonNull(httpServer.getClass().getClassLoader().getResource("")).getPath());
                httpServer.run(hostname, port);
            }
            else {
                PersistentRequestHandler persistentServer = new PersistentRequestHandler(port + 1);
                persistentServer.start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.exit(0);
    }

    // 读取配置文件
    public static void phraseConfig(String path) {
        String[] line;
        BufferedReader reader = null;
        File file = new File(path);
        try {
            System.out.println("读取配置文件开始");
            try {
                reader = new BufferedReader(new FileReader(file));
            }
            catch (Exception e){
                printRed("找不到路径对应配置文件，加载默认设置");
                return;
            }
            String tempString;
            while ((tempString = reader.readLine()) != null) {
                line = tempString.split("\\s+");
                config.put(line[0], line[1]);

            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                    printRed("读取IO异常");
                }
            }
        }
    }
}

