package HttpClient;

import java.io.*;
import static Util.ColorUtil.*;

/**
 * @Description: 客户端交互主入口
 * @Author: YDJSIR
 * @Date: 2021-06-16 21:02
 * @Modifiers: YDJSIR
 */
public class ClientMain {
    public static boolean isDebug = false;
    public static NormalClient client = new NormalClient();
    private static boolean RUNNING = true;

    /**
     * 客户端主进程入口
     * @param args 程序启动参数
     */
    public static void main(String[] args){
        String hostname = "127.0.0.1";
        int portNo = 8080;
        boolean needHelp = false;
        printCyan("__          __  _____        _____             \n" +
                " \\ \\        / / |  __ \\      |  __ \\            \n" +
                "  \\ \\  /\\  / /__| |  | | ___ | |__) |__ _ _   _ \n" +
                "   \\ \\/  \\/ / _ \\ |  | |/ _ \\|  _  // _` | | | |\n" +
                "    \\  /\\  /  __/ |__| | (_) | | \\ \\ (_| | |_| |\n" +
                "     \\/  \\/ \\___|_____/ \\___/|_|  \\_\\__,_|\\__, |\n" +
                "                                           __/ |\n" +
                "                                          |___/ ");
        printCyan("欢迎使用WeDoRay小组HTTP客户端！\n" +
                "===============================\n" +
                " \n请初始化服务器地址与端口号");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        if(!isDebug){
            System.out.print(ANSI_BLUE + "请输入服务器的地址："  + ANSI_RESET);
            try {
                hostname = bf.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.print(ANSI_BLUE + "请输入服务器端口号：" + ANSI_RESET);
            try {
                portNo = Integer.parseInt(bf.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        System.out.println(ANSI_BLUE + "请开始操作，如需帮助，请输入 Help" + ANSI_RESET);
        while(RUNNING) {
            if(needHelp){
                showHelp();
            }
            else{
                System.out.print("Client to " + hostname + ':' + portNo + ": ");
            }
            String cmd = null;
            try {
                cmd = bf.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            if(cmd != null) {
                String[] ops = cmd.split("\\s+");
                String op = ops[0].toUpperCase();
                switch (op) {
                    case "HELP":
                        needHelp = true;
                        break;
                    case "POST": // 模拟POST请求 //TODO
                        break;
                    case "GET": // 模拟GET请求
                        printGreen(op + ' ' + ops[1]);
                        try {
                            client.doGet(hostname, portNo, ops[1]);
                        } catch (Exception e) {
                            printRed("连接失败，请检查网络或重试！");
                            e.printStackTrace();
                        }
                        break;
                    case "PERSISTENT":
//                        int maxTrialPersistentPacket = 10;
//                        printBlue("请输入长连接发送维持包的数量，默认每两秒发送一个");
                        try {
                            PersistentClient persistentClient = new PersistentClient(hostname, portNo + 1, Integer.parseInt(ops[1]));
                            persistentClient.start();
                        }catch (Exception ignored){
                            printRed("命令解析错误");
                        }
                        break;
                    case "EXIT":
                        return;
                    case "THANKS":
                        needHelp = false;
                        break;
                    default:
                        printRed("命令解析错误，请重新解析");
                        break;
                }
            }
        }
    }

    /**
     * 展示提示信息
     */
    public static void showHelp(){
        System.out.println(ANSI_BLUE + "GET命令格式：GET + URI （以空格分开）" + ANSI_RESET);
        System.out.println(ANSI_BLUE + "POST命令格式：POST + URI （以空格分开） + 内容" + ANSI_RESET);
        System.out.println(ANSI_BLUE + "长连接测试：Persistent + 维持包数量" + ANSI_RESET);
        System.out.println(ANSI_BLUE + "输入 Thanks 关闭命令提示" + ANSI_RESET);
        System.out.println(ANSI_BLUE + "输入 Help 打开命令提示" + ANSI_RESET);
        printBlue("请输入长连接发送维持包的数量，默认每两秒发送一个");
    }

}
