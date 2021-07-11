package Util;

import java.util.HashMap;

/**
 * @description: MIME类型映射表
 * @author: YDJSIR
 * @date: 2021/6/24 16:25
 * @Modifiers: fanny-zhang
 */
public class MIMETypes {
    public static HashMap<String, String> MIMEList = new HashMap<>();
    public static HashMap<String, String> reverseMIMEList = new HashMap<>();
    public static MIMETypes mimeTypes = null;

    private MIMETypes(){
        // 视频部分
        MIMEList.put(".avi", "video/x-msvideo");
        MIMEList.put(".mp4", "video/mp4");
        MIMEList.put(".mpeg", "video/mpeg");
        MIMEList.put(".ogv", "video/ogg");
        MIMEList.put(".ts", "video/mp2t");
        MIMEList.put(".webm", "video/webm");
        MIMEList.put(".3gp", "video/3gpp");
        MIMEList.put(".3g2", "video/3gpp2");
        // 图片部分
        MIMEList.put(".png", "image/png");
        MIMEList.put(".jpg", "image/jpeg");
        MIMEList.put(".jpeg", "image/jpeg");
        MIMEList.put(".gif", "image/gif");
        MIMEList.put(".svg", "image/svg+xml");
        MIMEList.put(".tif", "image/tiff");
        MIMEList.put(".tiff", "image/tiff");
        MIMEList.put(".webp", "image/webp");
        MIMEList.put(".ico", "image/vnd.microsoft.icon");
        MIMEList.put(".bmp", "image/bmp");
        // 文本部分
//        MIMEList.put(".xml", "text/xml");
        MIMEList.put(".htm", "text/html");
        MIMEList.put(".html", "text/html");
        MIMEList.put(".css", "text/css");
        MIMEList.put(".csv", "text/csv");
        MIMEList.put(".ics", "text/calendar");
        MIMEList.put(".js", "text/javascript");
        MIMEList.put(".mjs", "text/javascript");
        MIMEList.put(".txt", "text/plain; charset=utf-8");
        // 字体部分
        MIMEList.put(".otf", "font/otf");
        MIMEList.put(".ttf", "font/ttf");
        MIMEList.put(".woff", "font/woff");
        MIMEList.put(".woff2", "font/woff2");
        // 音频部分
        MIMEList.put(".mp3", "audio/mpeg");
        MIMEList.put(".wav", "audio/wav");
        MIMEList.put(".aac", "audio/aac");
        MIMEList.put(".oga", "audio/ogg");
        MIMEList.put(".mid", "audio/midi");
        MIMEList.put(".midi", "audio/x-midi");
        MIMEList.put(".opus", "audio/opus");
        MIMEList.put(".weba", "audio/webm");
        // 默认
        MIMEList.put(".bin", "application/octet-stream");
        MIMEList.put(".abw", "application/x-abiword");
        MIMEList.put(".arc", "application/x-freearc");
        MIMEList.put(".azw", "application/vnd.amazon.ebook");
        MIMEList.put(".bz", "application/x-bzip");
        MIMEList.put(".bz2", "application/x-bzip2");
        MIMEList.put(".cda", "application/x-cdf");
        MIMEList.put(".csh", "application/x-csh");
        MIMEList.put(".doc", "application/msword");
        MIMEList.put(".docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
        MIMEList.put(".eot", "application/vnd.ms-fontobject");
        MIMEList.put(".epub", "application/epub+zip");
        MIMEList.put(".gz", "application/gzip");
        MIMEList.put(".jar", "application/java-archive");
        MIMEList.put(".json", "application/json");
        MIMEList.put(".jsonld", "application/ld+json");
        MIMEList.put(".mpkg", "application/vnd.apple.installer+xml");
        MIMEList.put(".odp", "application/vnd.oasis.opendocument.presentation");
        MIMEList.put(".ods", "application/vnd.oasis.opendocument.spreadsheet");
        MIMEList.put(".odt", "application/vnd.oasis.opendocument.text");
        MIMEList.put(".ogx", "application/ogg");
        MIMEList.put(".pdf", "application/pdf");
        MIMEList.put(".php", "application/x-httpd-php");
        MIMEList.put(".ppt", "application/vnd.ms-powerpoint");
        MIMEList.put(".pptx", "application/vnd.openxmlformats-officedocument.presentationml.presentation");
        MIMEList.put(".rar", "application/vnd.rar");
        MIMEList.put(".rtf", "application/rtf");
        MIMEList.put(".sh", "application/x-sh");
        MIMEList.put(".swf", "application/x-shockwave-flash");
        MIMEList.put(".tar", "application/x-tar");
        MIMEList.put(".vsd", "application/vnd.visio");
        MIMEList.put(".xhtml", "application/xhtml+xml");
        MIMEList.put(".xls", "application/vnd.ms-excel");
        MIMEList.put(".xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
        MIMEList.put(".xml", "application/xml");
        MIMEList.put(".xul", "application/vnd.mozilla.xul+xml");
        MIMEList.put(".zip", "application/zip");
        MIMEList.put(".7z", "application/x-7z-compressed");
        for (String val:MIMEList.keySet()
             ) {
            reverseMIMEList.put(MIMEList.get(val), val); // 直接反向操作
        }
    }

    public static MIMETypes getMIMELists(){
        if(MIMETypes.mimeTypes == null){
            MIMETypes.mimeTypes = new MIMETypes();
        }
        return MIMETypes.mimeTypes;
    }

    /**
     * 根据传入URI返回对应的MIME类型，找不到默认按照 application/octet-stream 处理
     * @param oUri 传入的URI
     * @return MIME类型字符串
     */
    public String getMIMEType(String oUri){
        int locPoint = oUri.lastIndexOf(".");
        if(locPoint == -1){
            return MIMEList.get(".bin");
        }
        String end = oUri.substring(locPoint);
        return MIMEList.getOrDefault(end, "application/octet-stream"); // 默认按照bin处理
    }

    public String getReverseMIMEType(String MIME){
        return reverseMIMEList.getOrDefault(MIME, ".bin");
    }
}
