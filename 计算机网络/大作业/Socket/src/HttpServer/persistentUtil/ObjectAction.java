package HttpServer.persistentUtil;

import HttpServer.PersistentRequestHandler;

/**
 * @description: 要处理客户端发来的对象，并返回一个对象，实现该接口。
 * @author: YuDongjun
 * @date: 2021/6/27 10:32
 * @Modifiers: GZK
 */
public interface ObjectAction{
    Object doAction(Object rev, PersistentRequestHandler server);
}
