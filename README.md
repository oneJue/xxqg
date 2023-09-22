
学习强国 基于uiautomator2实现的学习助手 免root 适配安卓 自动化脚本
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
