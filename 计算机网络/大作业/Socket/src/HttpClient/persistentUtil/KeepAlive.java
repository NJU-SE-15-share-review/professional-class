package HttpClient.persistentUtil;

import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @description: 维持连接包
 * @author: GZK
 * @date: 2021/6/27 10:44
 * @Modifiers: YDJSIR
 */
public class KeepAlive implements Serializable {
    @Override
    public String toString() {
        return new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date())+"\t维持连接包";
    }
}
