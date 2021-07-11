package HttpServer;

import Util.MIMETypes;
import Util.MessageHeader;
import Util.StatusCodeAndPhrase;
import com.sun.net.httpserver.HttpServer;
import java.io.*;
import java.net.Socket;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

import static HttpServer.SeverMain.*;
import static Util.ColorUtil.*;

/**
 * @Description: 服务端请求处理进程
 * @Author: YDJSIR
 * @Date: 2021-06-21 22:20
 * @Modifiers: YDJSIR
 */
public class RequestHandler extends Thread {

    private static MIMETypes MIMEList = MIMETypes.getMIMELists();
    private static StatusCodeAndPhrase statusCodeList = StatusCodeAndPhrase.getStatusCodeList();
    private static RedirectList redirectList = RedirectList.getRedirectList();
    private Socket mSocket;
    private String Request;
    private String uri;
    private String trueURI;
    private boolean isDown = false; // 模拟服务器挂掉的情况
    private int statusCode;
    private long dataLen = 0;
    private String HTTPVersion = "HTTP/1.1";

    /**
     * 构造方法
     * @param mSocket 处理socket
     */
    public RequestHandler(Socket mSocket) {
        this.mSocket = mSocket;
    }

    /**
     * 进程开始
     */
    @Override
    public void start() {

        // 读取客户端请求
        printGreen("---->>>> read request <<<<----");
        try {
            readRequest(mSocket);
        } catch (IOException e) {
            printRed("Network is WRONG.");
        }

        // TODO 处理客户端请求（针对POST请求）

        // TODO 发送返回请求，目前只有GET
        String MIMEType;
        printGreen("---->>>>send response <<<<----");

        byte[] data;
        InputStream in = null;
        try {
            if (isDown) {
                statusCode = 500;
                data = getResAsStream(HttpServer.class.getResourceAsStream(BIND_DIR + SERVER_ERROR_RES));
                MIMEType = MIMEList.getMIMEType(BIND_DIR + SERVER_ERROR_RES);
            }
            else {
                String redirectQuery = redirectList.query(uri);
//                TODO 如何把请求优雅地传递给后方？
                if (!redirectQuery.equals("")) { // 有301/302跳转项目，则执行跳转
                    statusCode = Integer.parseInt(redirectQuery.substring(0, 3));
                    String Location = redirectQuery.substring(3);
                    trueURI = Location;
                    data = getResAsStream(HttpServer.class.getResourceAsStream(BIND_DIR + Location));
                    MIMEType = MIMEList.getMIMEType(BIND_DIR + Location);
                }
                else {
                    if(uri.lastIndexOf(".") > uri.lastIndexOf("/")) { // 这里已经假设都是访问目录情形了
                        in = HttpServer.class.getResourceAsStream(BIND_DIR + uri);
                    }
                    else{
                        String addedURI = uri.endsWith("/") ? BIND_DIR + uri : BIND_DIR + uri + '/';
                        for (String defaultIndex : DEFAULT_INDEX) {
                            printRed(addedURI);
                            in = HttpServer.class.getResourceAsStream(addedURI + defaultIndex);
                            if (in != null) {
                                printRed(addedURI + defaultIndex);
                                uri = addedURI + defaultIndex;
                                break;
                            }
                        }
                    }
                    if (in == null) { // 找不到资源，按照404处理
                        statusCode = 404;
                        data = getResAsStream(HttpServer.class.getResourceAsStream(BIND_DIR + NOT_FOUND_RES));
                        MIMEType = MIMEList.getMIMEType(BIND_DIR + NOT_FOUND_RES);
                    } else {
                        statusCode = 200;
                        data = getResAsStream(in);
                        MIMEType = MIMEList.getMIMEType(uri);
                    }
                }
            }
            sendResponse(mSocket, data, MIMEType);
        } catch (IOException e) {
            printRed("IO Exception in GETTING RESOURCES!");
        }
        try {
            mSocket.close();
        } catch (IOException e) {
            printRed("IO Exception in CLOSING SOCKET");
            e.printStackTrace();
        }
        printBlue("---->>>> response finished <<<<----\n\r");
    }

    /**
     * 从资源输入流构建返回byte数组
     * @param in 输入流
     * @return byte数组流
     */
    private byte[] getResAsStream(InputStream in){
        ByteArrayOutputStream os = new ByteArrayOutputStream();
        int len = 0; // 单次读取长度
        int totalLen = 0; // 所有内容长度
        byte[] bytes = new byte[2048];
        while(true)
        {
            try {
                if ((len = in.read(bytes)) == -1) break;
            } catch (IOException e) {
                e.printStackTrace();
            }
            totalLen += len;
            try {
                os.write(bytes);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        dataLen = totalLen;
        return os.toByteArray();
    }

    /**
     * 读取客户端发来的请求
     * @param socket 客户端对应socket
     * @throws IOException IO错误
     */
    private void readRequest(Socket socket) throws IOException {
        InputStream is = socket.getInputStream();
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        byte[] buffer = new byte[2048];
        int len;
        while ((len = is.read(buffer)) > 0) {
            bos.write(buffer, 0, len);
            if (len < 2048) break;
        }
        Request = new String(bos.toByteArray());
        String typeUriHttp = Request.split("\\s+")[0];
        uri = Request.split("\\s+")[1];
        printGreen(typeUriHttp + ' ' + uri + HTTPVersion);
        printYellow(Request);
    }

    /**
     * 发送200、404和500响应（有内容）
     * @param socket 对应socket
     * @param data  写入数据本体
     * @param Content_Type 内容MIME类型
     * @throws IOException IO错误
     */
    private void sendResponse(Socket socket, byte [] data,
                              String Content_Type) throws IOException {
        OutputStream os = socket.getOutputStream();

        // 发送响应头
        String phrase = statusCodeList.getPhrase(statusCode);
        MessageHeader sendMessageHeader = new MessageHeader(statusCode, phrase);
        PrintStream print = new PrintStream(os);
        sendMessageHeader.writeItem("Server", "WeDoRay-HttpServer");
        if(statusCode == 301 || statusCode == 302){
            sendMessageHeader.writeItem("Location", trueURI);
        }
        sendMessageHeader.writeItem("Content-Length", String.valueOf(dataLen));
        sendMessageHeader.writeItem("Content-Type", Content_Type);
        print.write(sendMessageHeader.toBytesFromServer());

        // 发送响应数据
        for(int i = 0; i < dataLen; i++){
            print.write(data[i]);
        }
        os.flush();
    }
}

