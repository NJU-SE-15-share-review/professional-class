# 软件工程与计算Ⅰ-JAVABasics

> 本部分对应于PPT： JAVA系列



## 常用的结构

### Map

```Java
public static void main(String[] Args){
    HashMap<Integer, Integer> YDJMap = new HashMap<Integer, Integer>();
    YDJMap.put(3,4);
    System.out.println(YDJMap);
    YDJMap.put(3,6);
    System.out.println(YDJMap);
    YDJMap.put(3, YDJMap.get(3)+1);
    System.out.println(YDJMap);
    YDJMap.remove(3);
    System.out.println(YDJMap);
}
```

### StringBuilder(看他提示)

`append` ，`toString` ，`reverse` ，极大地节省空间。

### Set



### ArrayList

用Stream转换！

```java
int [] arr1 = Arrays.stream(data).mapToInt(num -> (Integer) num).toArray();//List<Integer>转为int[]
int [] arr1 = Arrays.stream(data.toArray()).mapToInt(num -> (Integer) num).toArray();//ArrayList<Integer>转为int[]
int [] arr1 = Arrays.stream(data).mapToInt(num -> (Integer) num).toArray();//Integer[]转为int[]
Integer[] integers1 = Arrays.stream(data).boxed().toArray(Integer[]::new);//int[]转为Integer[]
List<Integer> list1 = Arrays.stream(data).boxed().collect(Collectors.toList());//int[]转为List<Integer>
Integer[] integers1 = Arrays.stream(data).boxed().toArray(Integer[]::new);//int[]转为ArrayList<Integer>
```

### 文件IO

```java
try { f = new FileInputStream(fileName);
} catch (FileNotFoundException e) { e.printStackTrace();}
```

### 万能的正则

```java
String patternArchive = "^(\\w+\\/?)+(\\.)+((ZIP)|(zip)|(JAR)|(jar))$";
Pattern.matches(patternDir, item);
```



## 常用的算法

### 斐波拉契传统艺能

```java
n3 = n1+n2; n1 = n2; n2 = n3;
```

### 二分法不能忘

```java
while(data[mid] != target){
			if(start < end) {
				if (target > data[mid]) {
					start = mid + 1;
					mid = (start + end) / 2;
				} else if (data[mid] > target) {
					end = mid - 1;
					mid = (start + end) / 2;
				}
			}
			else {return -1;}
}
```

又不是叫你写，直接调用个包不就好了嘛……`binarySearch(intNum, key);`

### 冒泡的魔改

```java
for(int i=1;i<=k;i++){//不完整的冒泡，找第k大的元素
	for(int j=n-1;j>=i;j--){
		if(nums[j]>nums[j-1]){
			int temp=nums[j-1];
			nums[j-1]=nums[j];
			nums[j]=temp;}
		}
	}
```

![image-20200822232059471](%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%A1%E7%AE%97%E2%85%A0-JAVABasics.assets/image-20200822232059471.png)

```java
public static int[] threeSum(int[] nums, int target) {//双指针法解决三数和问题
       int n = nums.length;
       Map<Integer, Integer> m1 = new HashMap<Integer, Integer>();//记录下标
       for (int i = 0; i < n; i++) {m1.put(nums[i], i);}
       sort(nums);
       int []triplet = new int [3];
       for (int m = 0; m < n; m++) {
           int j = m + 1;
           int i = n - 1;
           while (j < i) {
               int sum= nums[m] + nums[j]+ nums[i];
               if (sum < target) {
                   j++;
               } else if (sum> target) {
                   i--;
               } else {
                   triplet[0] = m1.get(nums[m]) ;
                   triplet[1] = m1.get(nums[j]);
                   triplet[2] = m1.get(nums[i]);
                   System.out.println("Success");
                   Arrays.sort(triplet);
                   return triplet;
               }
           }
       }
       System.out.println("Error");
       return triplet;
   }
```

### 迭代的教训

算sin和cos。要转化为连乘而不是上下算完分开算！



### 位运算之歌

```java
public static int hammingDistance(int x, int y){
   int result = 0;
   for(int i = 0; i<32; i++){
      int digit = 1 << i;
      if(((x ^ y) & digit)!=0){result++;};
   }
   return result;
}
```

### TicTacToe & MyMatrix & GoodMap

```java
// 在场不要犯傻，算法逻辑也就那样，需要多态就考虑下接口/抽象类/父类
```