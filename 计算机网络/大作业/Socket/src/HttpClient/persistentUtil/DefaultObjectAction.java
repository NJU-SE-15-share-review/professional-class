package HttpClient.persistentUtil;

import HttpClient.PersistentClient;

import static Util.ColorUtil.printYellow;

/**
 * @description: 客户端ObejectAction的默认实现
 * @author: GZK
 * @date: 2021/6/27 12:27
 * @Modifiers: YDJSIR
 */
public final class DefaultObjectAction implements ObjectAction {
    public void doAction(Object obj, PersistentClient LongClient) {
        printYellow("处理：\t" + obj.toString());
    }
}

