package HttpClient;

import java.awt.*;
import java.io.*;
import java.net.Socket;
import java.util.*;
import Util.MIMETypes;
import Util.MessageHeader;
import static Util.ColorUtil.*;

/**
 * @Description: 客户端请求方法合集
 * @Author: sugarXu
 * @Date: 2021-06-21 22:20
 * @Modifiers: YDJSIR
 */
public class NormalClient {
    private static final int MAX_TRIAL = 3;
    private static MIMETypes mimeTypes = MIMETypes.getMIMELists();
    private static HashMap<String, String> storageRedirect = new HashMap<>();
    private static Random random = new Random(191250); // 用来生成哈希后的本地缓存资源的名字

    /**
     * 实现get方式访问http server
     * @param host 访问主机名
     * @param port 访问主机端口
     * @param uri 访问URI
     */
    public void doGet(String host, int port, String uri) {
        Socket socket = null;
        try {
            // 创建连接
            int cnt = 0;
            while (socket == null) {
                try {
                    socket = new Socket(host, port);
                    printPurple("本地端口" + socket.getLocalPort());
                } catch (Exception e) {
                    return;
                }
            }

            // 创建http请求
            // 构建请求头
            MessageHeader curMessageHeader;
            if(storageRedirect.containsKey(host + ":" + port + uri)) {
                String trueURI = storageRedirect.get(host + ":" + port + uri);
                curMessageHeader = new MessageHeader("GET", trueURI); // 301重定向的本地存储
                printGreen("根据缓存，你将被重定向至" + trueURI);
            }
            else{
                curMessageHeader = new MessageHeader("GET", uri);
            }
            curMessageHeader.writeItem("Accept", "*/*");
            curMessageHeader.writeItem("Accept-Language", "zh-cn");
            curMessageHeader.writeItem("User-Agent", "WeDoRay-HTTPClient");
            if(port != 80 && port != 443) {
                curMessageHeader.writeItem("Host", host + ':' + port);
            }
            else{
                curMessageHeader.writeItem("Host", host); // 抓包发现访问默认端口的时候是不需要端口号的
            }
            curMessageHeader.writeItem("Connection", "Keep-Alive");

            //发送http请求
            OutputStream socketOut = socket.getOutputStream();
            socketOut.write(curMessageHeader.toBytesFromClient());

            /*
             * 此处已经不需要等待，但是结合POST地处理还没有做
             */

            //处理返回请求
            InputStream inputStream = socket.getInputStream();
            MessageHeader receiveMessageHeader = new MessageHeader(inputStream);

            printGreen("====>>>> RECEIVING MESSAGE <<<<===");
            printGreen("---->>>> header <<<<----");
            printYellow(new String(receiveMessageHeader.toBytesFromServer()));
            String receiveMIMEType = receiveMessageHeader.headerFields.get("Content-Type");


            String trueURI;
            switch (receiveMessageHeader.statusCode) { // 200状态码，展示内容，顺利结束
                case 404: // 404照样显示内容
                case 200: // 200正常访问
                    printGreen("---->>>> data <<<<----");
                    if(receiveMIMEType.substring(0, 4).equals("text")) {
                        CharArrayWriter charArray = new CharArrayWriter();
                        char[] buffer = new char[2048];
                        int totalLen = 0, lenc;
                        while ((lenc = receiveMessageHeader.reader.read(buffer)) > 0) {
                            charArray.write(buffer, 0, lenc);
                            totalLen += lenc;
                            if (totalLen == receiveMessageHeader.contentLength) break;
                        }
                        String response = new String(charArray.toCharArray());
                        System.out.println(response);
                    }
                    else{
                        int lena = receiveMessageHeader.allInBytes.length;
                        byte[] bytes = Arrays.copyOfRange(receiveMessageHeader.allInBytes,
                                (int) (lena - receiveMessageHeader.contentLength), lena);
                        String postfix = mimeTypes.getReverseMIMEType(receiveMIMEType);
                        File storeFile = new File(Objects.requireNonNull(this.getClass().getResource("")).getPath()
                                 +  "/tmp/" + random.nextLong() +
                                Math.abs(String.valueOf(System.currentTimeMillis()).hashCode()) + postfix);
                        if (!storeFile.exists()) {	//文件不存在则创建文件，先创建目录
                            File dir = new File(storeFile.getParent());
                            dir.mkdirs();
                            storeFile.createNewFile();
                        }
                        System.out.println("Store Files path: "+storeFile.toString());

                        BufferedOutputStream bos = null;
                        try{
                            bos = new BufferedOutputStream(new FileOutputStream(storeFile));
                            bos.write(bytes);
                            bos.flush();
                        }catch(Exception exception){
                            exception.printStackTrace();
                        }finally{
                            assert bos != null;
                            bos.close();
                        }
                        Desktop.getDesktop().open(storeFile);
                    }
                    break;
                case 301: // 301永久重定向
                    trueURI = receiveMessageHeader.headerFields.get("Location");
                    storageRedirect.put(host+':'+port+uri, trueURI);
                    printGreen("你将被301重定向至" + trueURI);
                    doGet(host, port, trueURI); // 跳转
                    break;
                case 302: // 302临时重定向
                    trueURI = receiveMessageHeader.headerFields.get("Location");
                    printGreen("你将被302重定向至" + trueURI);
                    doGet(host, port, trueURI); // 跳转
                    break;
//                case 304: // TODO 与PUT请求相关
//                    break;
                default:
                    printRed("UNKNOWN STATUS CODE!");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if(socket != null) {
                    socket.close();
                }
                printBlue("GET请求处理完毕");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

