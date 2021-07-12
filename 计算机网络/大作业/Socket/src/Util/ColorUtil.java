package Util;

/**
 * @Author:YDJSIR
 * @Date:2021-06-23 15:20
 * @Description: 控制台按颜色输出
 * @Modifiers: YDJSIR
 */
public class ColorUtil {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_BLACK = "\u001B[30m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_PURPLE = "\u001B[35m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_WHITE = "\u001B[37m";

    /**
     * 输出特定参数
     * @param message 消息
     */
    public static void printBlue(String message) {
        System.out.println(ANSI_BLUE + message + ANSI_RESET);
    }

    /**
     * 输出特定类型内容，如HTTP响应头
     * @param message 消息
     */
    public static void printYellow(String message) {
        System.out.println(ANSI_YELLOW + message + ANSI_RESET);
    }

    /**
     * 输出特定步骤相关消息
     * @param message 消息
     */
    public static void printGreen(String message) {
        System.out.println(ANSI_GREEN + message + ANSI_RESET);
    }

    /**
     * 未用
     * @param message 消息
     */
    public static void printPurple(String message) {
        System.out.println(ANSI_PURPLE + message + ANSI_RESET);
    }

    /**
     * 输出错误消息
     * @param message 消息
     */
    public static void printRed(String message) {
        System.out.println(ANSI_RED + message + ANSI_RESET);
    }

    /**
     * 输出交互相关消息
     * @param message 消息
     */
    public static void printCyan(String message) {
        System.out.println(ANSI_CYAN + message + ANSI_RESET);
    }
}
