package HttpServer.persistentUtil;

import HttpServer.PersistentRequestHandler;
import static Util.ColorUtil.*;

/**
 * @description: 服务端ObjectAction默认实现
 * @author: GZK
 * @date: 2021/6/27 10:30
 * @Modifiers: YDJSIR
 */
public final class DefaultObjectAction implements ObjectAction {
    @Override
    public Object doAction(Object rev, PersistentRequestHandler server) {
        printYellow("处理并返回："+rev);
        return rev;
    }
}
