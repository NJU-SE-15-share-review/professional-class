# 软件工程与计算Ⅰ-PythonBasics

> 本部分对应于PPT Python系列

## 常用API

### `System.in` 的读入

```python
n, m = [int(x) for x in input().split()] # 用元组对应过去
nums = [int(x) for x in input().split()] # 直接去读列表
intNum = (int(input())) # 一行单个
```

### 文件IO



### 方法的分配

```python
cmd_handler = {'-a': add_task, '-d': del_task, '-c': cop_task, '-f': fnd_task, '-all': all_task, '-quit': quit_todo} # 注意到这句话可以在方法外面
cmd_handler[input_cmd[1]](input_cmd) # 调用时再施展魔法
```



map是神器

list有妙用

