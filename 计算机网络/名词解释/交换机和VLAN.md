Symmetric Switching: 对称交换。交换机上所有端口带宽一样

Asymmetric Switching: 非对称交换。不同端口带宽不同

Store-and-Forward: 储存转发式交换。交换机收到帧后，先校验CRC再转发

Cut-through: 直通式交换。不校验就转发

​	Fast forward Switching: 快速转发交换。只查看目的MAC地址后就转发。

​	Fragment Free: 免碎片。转发前查看帧前64字节以减少线路上噪声造成的错误。

L2 Switching: Layer 2 Switching，二层交换

L3 Switching: Layer 3 Switching，三层交换

L4 Switching: Layer 4 Switching，四层交换

Multilayer Switching: 多层交换

STP: Spanning-Tree Protocol，生成树协议。具体内容自行查看讲义，太多了

BID: Bridge ID，桥接器ID。8字节，由优先级和交换机的MAC地址组成，用于选举根桥接器、根端口等

PID: Port ID，端口ID。2字节，由优先级和端口号组成，用于选举根端口和指派端口等。

BPDU: Bridge Protocol Data Unit，桥接数据单元。用于在STP中传递拓扑信息、选举等。

VLAN: Virtual LAN，虚拟局域网。用于划分逻辑子网。工作在第二层和第三层。**可以分割广播域**。

backbone: 主干。用于VLAN间的通信。

Frame Filtering: 帧过滤。阻止不符合条件的帧。

Frame Tagging: 帧标记。在每个要被在主干线路上转发的帧的头部加上一个独特的标签，用来标识它来自哪一个VLAN。离开主干线路时被去除。

ISL: Inter-Switch Link，交换机间链路。思科的专利，再封装一遍帧，加上VLAN的信息。

Static VLAN: 静态VLAN。直接指派端口所属的VLAN。

Dynamic VLAN: 动态VLAN。当有新的节点插入端口时，交换机查表来动态配置这个端口所属的VLAN

Port-Centric VLAN: 以端口为中心的VLAN。同一VLAN下的所有节点接入到同一个路由器接口上，或者反过来说，接入同一个路由器端口的节点被划分到同一个VLAN下。

Access Link: 接入链路。其上只有一个VLAN的链路。这个VLAN被称为这个链路对应的端口的本地VLAN。

Trunk Link: Trunk链路(就这么叫吧，硬要叫的话是 主干链路)。其上有多个VLAN的链路。用于连接交换机与交换机或路由器。(总之其实就是一根线上多个VLAN的帧在跑，所以这些帧得打上标签标识它来自于哪一个VLAN，不然就搞混了。到达对面的交换机之后再根据标签把这些帧转发到对应的VLAN里面去。Trunk链路最大的好处只是省端口和方便配置，以牺牲一点性能为代价。)

Trunk链路也可以有本地VLAN，即在trunk链路因为一些原因失败的时候使用的VLAN。

CDP: Cisco Discovery Protocol，思科设备发现协议

VTP: VLAN Trunking Protocol，VLAN中继协议

Routing Between VLANs: VLAN间路由