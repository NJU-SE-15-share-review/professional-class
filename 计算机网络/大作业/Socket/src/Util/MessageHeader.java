package Util;

import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static Util.ColorUtil.*;

/**
 * Author:YDJSIR
 * Date:2021-06-23 15:20
 * Description: 消息头部类
 * Modifiers: YDJSIR
 */
public class MessageHeader {
    public String version = "HTTP/1.1";
    public String operation; // 客户端 GET 或者 PUT
    public String uri;
    public int statusCode = -1;
    public String phrase; // 服务端 状态代码后面的短语
    public HashMap<String, String> headerFields = new HashMap<>();
    public byte[] dataFields; // 报文数据段
    public long contentLength = 0;
    public BufferedReader reader;
    public byte[] allInBytes;

    /**
     *
     * @param op
     */
    public MessageHeader(String op){
        this.operation = op;
    }

    /**
     * 客户端构建给服务器的报文头
     * @param op 客户端请求方法
     * @param uri 请求URI
     */
    public MessageHeader(String op, String uri){
        this.operation = op;
        this.uri = uri;
    }

    /**
     * 服务端构建返回给客户端的报文头
     * @param statusCode 返回状态码
     * @param phrase 状态值
     */
    public MessageHeader(int statusCode, String phrase){
        this.statusCode = statusCode;
        this.phrase = phrase;
    }

    //

    /**
     * 客户端基于服务器给的输入流构建报文头
     * @param inputStream 服务端输入流
     */
    public MessageHeader(InputStream inputStream){
        try {
            ByteArrayOutputStream byteArrayOutputStreamOS = new ByteArrayOutputStream();
            byte[] bufferB = new byte[2048];
            int lenc;
            while ((lenc = inputStream.read(bufferB)) > 0) {
                byteArrayOutputStreamOS.write(bufferB, 0, lenc);
            }
            allInBytes = byteArrayOutputStreamOS.toByteArray();
            reader = new BufferedReader(new InputStreamReader(new ByteArrayInputStream(allInBytes)));
            //System.out.println("-->>>> response line <<<<--");
            String statusLine = reader.readLine();
            String[] elements = statusLine.split("\\s+");
            version = elements[0];
            statusCode = Integer.parseInt(elements[1]);
            int len =  elements.length;
            String[] phrases = Arrays.copyOfRange(elements, 2, len);
            phrase = String.join(" ", phrases);

            String header = reader.readLine();
            while (!"".equals(header)) {
                String[] array = header.split(":");
                String key = array[0].trim(); // 去掉头尾空白符
                String value = array[1].trim();
                headerFields.put(key, value);
                if (key.equalsIgnoreCase("Content-Length")) {
                    contentLength = Long.parseLong(value);
                }
                header = reader.readLine();
            }
        }
        catch (IOException e){
            printRed("IO ERROR in READING RESPONSE!");
        }
    }

    /**
     * 写入头部字段
     * @param key 头部字段名
     * @param value 值
     */
    public void writeItem(String key, String value){
        headerFields.put(key, value);
    }

    /**
     * 将客户端发送报文转换为 byte
     * @return 发送报文byte数组
     */
    public byte[] toBytesFromClient(){
        StringBuilder resStringBuilder = new StringBuilder();

        resStringBuilder.append(operation);
        resStringBuilder.append(' ');
        resStringBuilder.append(uri);
        resStringBuilder.append(' ');
        resStringBuilder.append(version);
        resStringBuilder.append("\r\n");
        for (String key: headerFields.keySet()
             ) {
            resStringBuilder.append(key);
            resStringBuilder.append(": ");
            resStringBuilder.append(headerFields.get(key));
            resStringBuilder.append("\r\n");
        }
        resStringBuilder.append("\r\n");
        return resStringBuilder.toString().getBytes();
    }

    /**
     * 将服务端返回给客户端的报文转换为 byte
     * @return 返回报文byte数组
     */
    public byte[] toBytesFromServer(){
        StringBuilder resStringBuilder = new StringBuilder();
        resStringBuilder.append(version);
        resStringBuilder.append(' ');
        resStringBuilder.append(statusCode);
        resStringBuilder.append(' ');
        resStringBuilder.append(phrase);
        resStringBuilder.append("\r\n");
        for (String key: headerFields.keySet()
        ) {
            resStringBuilder.append(key);
            resStringBuilder.append(": ");
            resStringBuilder.append(headerFields.get(key));
            resStringBuilder.append("\r\n");
        }
        resStringBuilder.append("\r\n");
        return resStringBuilder.toString().getBytes();
    }

    public String getResponseLineFromServer(){
        return version + ' ' + statusCode + ' ' + phrase;
    }

    public String getRequestLineForClient(){
        return operation + ' ' + uri + version;
    }
}
