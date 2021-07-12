package HttpClient.persistentUtil;

import HttpClient.PersistentClient;

/**
 * @description: 处理服务端发回的对象，实现该接口。
 * @author: YuDongjun
 * @date: 2021/6/27 12:25
 * @Modifiers: YDJSIR
 */
public interface ObjectAction {
    void doAction(Object obj, PersistentClient LongClient);
}
