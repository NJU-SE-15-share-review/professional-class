package Util;

import java.util.HashMap;

/**
 * @description: 响应代码与对应相应类型
 * @author: YuDongjun
 * @email: ydjsirhere@gmail.com
 * @date: 2021/6/24 17:27
 */
public class StatusCodeAndPhrase {
    public static HashMap<Integer, String> codeList = new HashMap<Integer, String>();
    private static StatusCodeAndPhrase statusCodeAndPhrase = null;

    private StatusCodeAndPhrase(){
        // 视频部分
        codeList.put(200, "OK");
        codeList.put(301, "Moved Permanently");
        codeList.put(302, "Found");
        codeList.put(404, "Not Found");
        codeList.put(405, "Method Not Allowed");
        codeList.put(500, "Internal Server Error");
    }

    public static StatusCodeAndPhrase getStatusCodeList(){
        if(StatusCodeAndPhrase.statusCodeAndPhrase == null){
            StatusCodeAndPhrase.statusCodeAndPhrase = new StatusCodeAndPhrase();
        }
        return StatusCodeAndPhrase.statusCodeAndPhrase;
    }

    public String getPhrase(int status){
        return codeList.getOrDefault(status, "UNKNOWN OPERATION");
    }
}
