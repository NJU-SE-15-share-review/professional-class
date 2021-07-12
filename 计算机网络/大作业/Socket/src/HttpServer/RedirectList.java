package HttpServer;

import java.io.*;
import java.util.HashMap;
import static Util.ColorUtil.*;

/**
 * @description: 重定向列表类
 * @author: YDJSIR
 * @date: 2021/6/24 19:51
 * @Modifiers: YDJSIR
 */
public class RedirectList {
    private static RedirectList redirectList = null;
    private boolean isDebug = true;
    public static HashMap<String, String> redirectLists = new HashMap<>();
    public static HashMap<String, Integer> redirectTypes = new HashMap<>();

    /**
     * 私有构造方法并进行重定向列表初始化
     */
    private RedirectList(){
        if(isDebug) {
            redirectLists.put("/301origin.html", "/301dest.html");
            redirectTypes.put("/301origin.html", 301);
            redirectLists.put("/302origin.html", "/302dest.html");
            redirectTypes.put("/302origin.html", 302);
        }
        else{
            String path = "";
            printBlue("请输入重定向列表文件路径");
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            try {
                path = bf.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            paraseConfig(path);
        }
    }

    /**
     * 获得单例定向
     * @return 单例对象
     */
    public static RedirectList getRedirectList(){
        if(RedirectList.redirectList == null){
            RedirectList.redirectList = new RedirectList();
        }
        return RedirectList.redirectList;
    }

    /**
     * 在重定向列表中查询URI
     * @param originURI 源URI
     * @return 不在则返回空字符串，在则返回字符串：状态码+目的URI
     */
    public String query(String originURI){
        if(!redirectLists.containsKey(originURI)){
            return "";
        }
        else{
            return redirectTypes.get(originURI) + redirectLists.get(originURI) ;
        }
    }

    /**
     * 从配置文件中读取重定向列表
     * @param path 配置文件路径
     */
    public static void paraseConfig(String path){
        String []line;
        File file = new File(path);
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String tempString;
            while ((tempString = reader.readLine()) != null) {
                line = tempString.split("\\s+");
                redirectLists.put(line[0], line[1]);
                redirectTypes.put(line[0], Integer.parseInt(line[2]));
            }
        } catch (IOException e) {
            printRed("配置文件读取失败");
        }
    }

}
