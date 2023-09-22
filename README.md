
学习强国 基于uiautomator2实现的学习助手 免root 适配安卓 自动化脚本
适配V2.49.0 看文章& #10004 看视频& #10004 本地学习(北京)&#10004 每日答题& #10004 双人赛/四人赛& #10004 挑战答题& #10008
## 安装
1) 安装uiautomator2
``` pythn
pip install --pre uiautomator2 
```

2) 设备安装atx-agent

`首先设备连接到PC，并能够adb devices发现该设备。`
`执行下面的命令会自动安装本库所需要的设备端程序：uiautomator-server，atx-agent，openstf / minicap，openstf / minitouch`
```
# init就是所有USB连接电脑的手机上都安装uiautomator2
python -m uiautomator2 init
  
# 指定手机安装uiautomator2， 用 --mirror
python -m uiautomator2 init --mirror --serial $SERIAL
 
# 嫌弃慢的话，可以用国内的镜像
python -m uiautomator2 init --mir
```
## 连接
设备连接方法，有两种：

python-uiautomator2连接手机的方式有两种，一种是通过WIFI，另外一种是通过USB。两种方法各有优缺点。
WIFI最便利的地方要数可以不用连接数据线，USB则可以用在PC和手机网络不在一个网段用不了的情况。

1) 通过WiFi，假设设备IP 192.168.0.107和您的PC在同一网络中

```python
import uiautomator2 as u2
d = u2.connect('192.168.0.107')
```
2) 通过USB， 假设设备序列是123456789F

```python
import uiautomator2 as u2
d = u2.connect('123456789F') # USB链接设备。或者u2.connect_usb('123456f')
#d = u2.connect_usb() 或者 d = u2.connect() ，当前只有一个设备时可以用这个
```
