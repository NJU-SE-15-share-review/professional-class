# 2021春《互联网计算》期末上机实验报告

## 小组信息

### 组长信息

| 项目 | 内容 |
| :--: | :--: |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |

### 组员信息

| 序号 | 成员姓名 | 学号 | 所在院系 | 专业 | 手机号码 |
| :--: | :------: | :--: | :------: | :--: | :------: |
|      |          |      |          |      |          |
|      |          |      |          |      |          |
|      |          |      |          |      |          |
|      |          |      |          |      |          |

## 实验信息

### 实验要求

1. 扑需使用动态路由协议。  
2. 拓扑中需包含`VLAN`及`trunk`技术。  
3. 拓扑至少需包含设备：2台交换机、4台路由器、4台PC。 
4. 每组时间为60分钟。  
5. 上机报告需包含拓扑说明、相关路由表信息、连通性说明。提交时现场助教或老师将在现场确认。  
6. 每组结束后需要清除设备配置保证设备正常交由助教确认后方可离开。
7. 提前较多时间(30分钟)完成考试、拓扑中设计较为复杂的网络技术（如`ACL`，`NAT`等）等将有加分。  

### 使用技术

- `RIP` 路由信息协议（动态路由协议）；
- `VLAN` 间路由与 `trunk` 技术；
- `NAT` 网络地址转换（复杂网络技术）；
- `ACL` 访问控制列表（复杂网络技术）；

### 实验目标

> 下面各项均以思科企业级路由器和交换机为平台。

- 进行IPv4静态组网；
- 进行不同 `VLAN` 之间路由的配置和 `trunk `的配置；
- 在路由器上启动 `RIP` 路由进程并查看和调试 `RIP` 路由协议相关信息；
- 配置静态 `NAT` 并进行基本调试；
- 掌握 `ACL` 的配置；

## 实验内容

- 静态组网；
- 配置`VLAN`和`trunk`；
- 配置`RIP`协议进行动态组网；
- 配置`静态NAT`；
- 配置`ACL`禁用特定链路上的特定`ICMP`协议；

## 实验拓扑

> 下面的图的内容都对应于现实中设备具体的摆放位置

![image-20210609180306779](计网实验报告初稿.assets/image-20210609180306779.png)

![image-20210609180211993](计网实验报告初稿.assets/image-20210609180211993.png)



## 实验步骤

### 进行物理上的连接操作

接线，给电脑桌子上放标签，把所有的设备命名为上图的名字

### 配置`VLAN`和`trunk`

#### 配置

##### Switch1 PC3 许礼孟

```python
Switch1(config)#int g1/0/24
# 实际操作不需要 Switch1(config-if)#switchport trunk encapsulation dot1q
Switch1(config-if)#switchport mode trunk
Switch1(config-if)#exit
Switch1(config)#vlan 10
Switch1(config-vlan)#exit
Switch1(config)#int g1/0/1
Switch1(config-if)#switchport access vlan 10
Switch1(config-if)#exit
Switch1(config)#vlan 20
Switch1(config-vlan)#exit
Switch1(config)#int g1/0/2
Switch1(config-if)#switchport access vlan 20
Switch1(config-if)#exit
Switch1(config)#int g1/0/23
# 实际操作不需要 Switch1(config-if)#switchport trunk encapsulation dot1q
Switch1(config-if)#switchport mode trunk
Switch1(config-if)#exit
```

##### Switch2 PC4 张蔚然

```python
Switch2(config)#int g1/0/24
# 实际操作不需要 Switch2(config-if)#switchport trunk encapsulation dot1q
Switch2(config-if)#switchport mode trunk
Switch2(config-if)#exit
Switch2(config)#int g1/0/1
Switch2(config-if)#switchport access vlan 10
% Access VLAN does not exist. Creating vlan 10
Switch2(config-if)#exit
Switch2(config)#int g1/0/2
Switch2(config-if)#switchport access vlan 20
% Access VLAN does not exist. Creating vlan 20
Switch2(config-if)#exit
```

##### Router2 PC5 许礼孟

```python
Router2(config)#int g0/0/0
Router2(config-if)#no ip address
Router2(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
    
Router2(config-if)# exit
Router2(config)#int g0/0/0.10

%LINK-5-CHANGED: Interface GigabitEthernet0/0/0.10, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0.10, changed state to up
    
Router2(config-subif)#encapsulation dot1q 10
Router2(config-subif)#ip address 192.168.10.1 255.255.255.0
Router2(config-subif)#exit
Router2(config)#int g0/0/0.20

%LINK-5-CHANGED: Interface GigabitEthernet0/0/0.20, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0.20, changed state to up
    
Router2(config-subif)#encapsulation dot1q 20
Router2(config-subif)#ip address 192.168.20.1 255.255.255.0
Router2(config-subif)#exit
```


##### PC1~PC4 郭子坤、许礼孟、孟剑卫、张蔚然

###### 1、关掉所有PC上的Windows7自带防火墙

![image-20210609174433854](计网实验报告初稿.assets/image-20210609174433854.png)

###### 2、配置IP地址

| PC   | IP地址       | 子网掩码      | 默认网关     |
| ---- | ------------ | ------------- | ------------ |
| PC1  | 192.168.10.2 | 255.255.255.0 | 192.168.10.1 |
| PC2  | 192.168.10.3 | 255.255.255.0 | 192.168.10.1 |
| PC3  | 192.168.20.2 | 255.255.255.0 | 192.168.20.1 |
| PC4  | 192.168.20.3 | 255.255.255.0 | 192.168.20.1 |

所有网络连接均设置为“家庭网络”。

#### 验证

##### PC4 `ping` 检验 张蔚然

`ping`两个网关地址和同网段不同交换机下设备/不同网段不同交换机下设备/不同网段同交换机下设备，结果是均可行。

```powershell
C:\>ping 192.168.20.1
Pinging 192.168.20.1 with 32 bytes of data:

...

Ping statistics for 192.168.20.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
    
C:\>ping 192.168.10.1

Pinging 192.168.10.1 with 32 bytes of data:

...

Ping statistics for 192.168.10.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>ping 192.168.20.3

Pinging 192.168.20.3 with 32 bytes of data:

...

Ping statistics for 192.168.20.3:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>ping 192.168.10.3

Pinging 192.168.10.3 with 32 bytes of data:

...

Ping statistics for 192.168.10.3:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
    
C:\>ping 192.168.10.2

Pinging 192.168.10.2 ith 32 bytes of data:

...

Ping statistics for 192.168.10.2
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
    
```

### 路由静态组网

#### 配置

##### Router2 PC5 许礼孟

```python
Router2(config)#int s0/1/1
Router2(config-if)#ip address 202.202.202.1 255.255.255.0
Router2(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/1, changed state to down
    
Router2(config-if)#int s0/1/0
Router2(config-if)#ip address 203.203.203.1 255.255.255.0
Router2(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/0, changed state to down
    
Router2(config-if)#exit
```

##### Router4 PC6 张蔚然

```python
Router4(config)#int s0/1/1
Router4(config-if)#ip address 202.202.202.2 255.255.255.0
Router4(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial0/1/1, changed state to up
    
Router4(config-if)#exit
```

##### Router1 PC1 郭子坤

```python
Router1(config)#int s0/1/0
Router1(config-if)#ip address 203.203.203.2 255.255.255.0
Router1(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial0/1/0, changed state to up
    
Router1(config-if)#exit
Router1(config)#int s0/1/1
Router1(config-if)#ip address 204.204.204.1 255.255.255.0
Router1(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/1, changed state to down
    
Router1(config-if)#exit
```

##### Router3 PC2 孟剑卫

```python
Router3(config)#int s0/1/1
Router3(config-if)#ip address 204.204.204.2 255.255.255.0
Router3(config-if)#no shutdown

%LINK-5-CHANGED: Interface Serial0/1/1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial0/1/1, changed state to up

Router3(config-if)#exit
```

### 3、配置`RIP`协议进行动态组网

#### 配置

##### Router4 PC6 张蔚然

```python
Router4(config)#router rip
Router4(config-router)#network 202.202.202.0
Router4(config-router)#exit
```

##### Router2 PC5 许礼孟

```python
Router2(config)#router rip
Router2(config-router)#network 202.202.202.0
Router2(config-router)#network 203.203.203.0
Router2(config-router)#exit
```

##### Router1 PC1 郭子坤

```python
Router1(config)#router rip
Router1(config-router)#network 204.204.204.0
Router1(config-router)#network 203.203.203.0
Router1(config-router)#exit
```

##### Router3 PC2 孟剑卫

```python
Router3(config)#router rip
Router3(config-router)#network 204.204.204.0
Router3(config-router)#exit
```

#### 验证

##### Router2 路由表 PC5 许礼孟

```python
Router2#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C       192.168.10.0/24 is directly connected, GigabitEthernet0/0/0.10
L       192.168.10.1/32 is directly connected, GigabitEthernet0/0/0.10
     192.168.20.0/24 is variably subnetted, 2 subnets, 2 masks
C       192.168.20.0/24 is directly connected, GigabitEthernet0/0/0.20
L       192.168.20.1/32 is directly connected, GigabitEthernet0/0/0.20
     202.202.202.0/24 is variably subnetted, 2 subnets, 2 masks
C       202.202.202.0/24 is directly connected, Serial0/1/1
L       202.202.202.1/32 is directly connected, Serial0/1/1
     203.203.203.0/24 is variably subnetted, 2 subnets, 2 masks
C       203.203.203.0/24 is directly connected, Serial0/1/0
L       203.203.203.1/32 is directly connected, Serial0/1/0
R    204.204.204.0/24 [120/1] via 203.203.203.2, 00:00:17, Serial0/1/0
```

##### Router1 路由表 PC1 郭子坤

```python
Router1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

R    202.202.202.0/24 [120/1] via 203.203.203.1, 00:00:21, Serial0/1/0
     203.203.203.0/24 is variably subnetted, 2 subnets, 2 masks
C       203.203.203.0/24 is directly connected, Serial0/1/0
L       203.203.203.2/32 is directly connected, Serial0/1/0
     204.204.204.0/24 is variably subnetted, 2 subnets, 2 masks
C       204.204.204.0/24 is directly connected, Serial0/1/1
L       204.204.204.1/32 is directly connected, Serial0/1/1
```

##### Router4 路由表 PC6 张蔚然

```python
Router4#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     202.202.202.0/24 is variably subnetted, 2 subnets, 2 masks
C       202.202.202.0/24 is directly connected, Serial0/1/1
L       202.202.202.2/32 is directly connected, Serial0/1/1
R    203.203.203.0/24 [120/1] via 202.202.202.1, 00:00:09, Serial0/1/1
R    204.204.204.0/24 [120/2] via 202.202.202.1, 00:00:09, Serial0/1/1
```

##### Router3 路由表 PC2 孟剑卫

```python
Router3#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

R    202.202.202.0/24 [120/2] via 204.204.204.1, 00:00:28, Serial0/1/1
R    203.203.203.0/24 [120/1] via 204.204.204.1, 00:00:28, Serial0/1/1
     204.204.204.0/24 is variably subnetted, 2 subnets, 2 masks
C       204.204.204.0/24 is directly connected, Serial0/1/1
L       204.204.204.2/32 is directly connected, Serial0/1/1
```

##### Router4 `ping`检测 PC6 张蔚然

```python
Router4>ping 204.204.204.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 204.204.204.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 20/35/46 ms
Router4#traceroute 204.204.204.2
Type escape sequence to abort.
Tracing the route to 204.204.204.2

  1   202.202.202.1   16 msec   12 msec   4 msec    
  2   203.203.203.2   12 msec   16 msec   12 msec   
  3   204.204.204.2   19 msec   26 msec   12 msec  
Router4>ping 192.168.10.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
```

注意到这里`ping` 192.168.10.2是通不了的，因为`Router2`在进行`RIP`广播时并没有将`192.168.10.0`这个网络加入。

### 4、配置`静态NAT`

#### 配置

##### Router2 PC5 许礼孟

```python
Router2(config)#ip nat inside source static 192.168.10.2 202.202.202.4
Router2(config)#int g0/0/0
Router2(config-if)#ip nat inside
Router2(config-if)#exit
Router2(config)#int s0/1/1
Router2(config-if)#ip nat outside
Router2(config-if)#exit
```

#### 验证 PC6 张蔚然

```python
Router4>ping 202.202.202.4

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 202.202.202.4, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 13/16/18 ms

Router4>ping 192.168.10.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
```

由此可见，此时`Router4`已经可以通过`202.202.202.4`与`PC1`进行通信，NAT已经生效。但是，`Router4`仍然无法通过`192.168.10.2`与`PC1`进行通信。`NAT`已经起到了隐藏内部IP地址的作用。

### 5、配置`ACL`禁用特定链路上的`ping`协议

#### 配置

##### Router2 PC5 许礼孟

```python
Router2(config)#access-list 100 deny icmp host 202.202.202.2 host 202.202.202.4
Router2(config)#access-list 100 permit icmp any any
Router2(config)#int s0/1/1
Router2(config-if)#ip access-group 100 in
```

#### 验证 PC6 张蔚然

```python
Router4>ping 202.202.202.4

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 202.202.202.4, timeout is 2 seconds:
UUUUU
Success rate is 0 percent (0/5)
Router4>ping 204.204.204.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 204.204.204.2, timeout is 2 seconds:
....!
Success rate is 20 percent (1/5), round-trip min/avg/max = 27/27/27 ms

Router4>ping 204.204.204.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 204.204.204.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 31/35/38 ms
```

## 实验总结

- 实现4个路由器之间的静态组网；

- 通过 RIP 进行联通部分网段；

- 192.168.10.0 网段和 192.168.20.0 网段通过 VLAN 和 Trunk技术相互通信；

- 192.168.10.2 通过 NAT 技术将局部地址映射到 202.202.202.4 与其他网段实现通信；

- 通过在 Router2设置 ACL，实现阻止 从204.204.204.2 到 204.204.204.4 的ICMP 报文，但不阻止其他经过对应端口的ICMP报文；