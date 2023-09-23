
import time
import random
import uiautomator2 as u2
from operator import itemgetter
#
# 连接到设备
# d = u2.connect('192.168.3.5:5555')
d = u2.connect('NAB0220630013667')

#打印设备信息以确认连接成功
print(d.device_info)
# d.app_stop("cn.xuexi.android")
print("在ATX中启动UIAUTOMATOR")
time.sleep(10)
d.app_start("cn.xuexi.android")

###################################################################


#点击要闻
while True:
    element = d(text="要闻")
    if element.exists():
        element.click()
        break
print("--------------------------------------------------------")
print("开始阅读文章")

#看文章
j=0
for i in range(1,9):
    j=j+1
    element = d.xpath('//android.widget.ListView/android.widget.FrameLayout[{}]'.format(j))
    if element.exists:
        element.click()
        time.sleep(50 + random.random() * 5)
        if i == 8:
            print("--------------------------------------------------------")
            print("正在发表观点")
            print("--------------------------------------------------------")

            d(text="欢迎发表你的观点").click()
            time.sleep(1)
            d(text="好观点将会被优先展示").set_text("坚定信念，走强国之路")  # 输入新的文本
            time.sleep(1)
            d(text="发布").click()
            time.sleep(1)
            if d(text="访问异常").exists:
                time.sleep(30)
            d.xpath('//*[@resource-id="cn.xuexi.android:id/TOP_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()
            break
            # d.xpath('//*[@resource-id="cn.xuexi.android:id/BOTTOM_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()
        d.xpath('//*[@resource-id="cn.xuexi.android:id/TOP_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()

    else:
        d.swipe_ext("up")
        j = 2
        time.sleep(3)



###################################################################
#本地

print("--------------------------------------------------------")
print("本地学习中")


time.sleep(1)
d.xpath('//*[@resource-id="cn.xuexi.android:id/view_pager"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
time.sleep(1)
d(text="北京").click()
time.sleep(1)
d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
time.sleep(1)
d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[3]/android.widget.ImageView[1]').click()

###################################################################
print("--------------------------------------------------------")
print("看视频")

#点百灵
time.sleep(2)
d.xpath('//*[@resource-id="cn.xuexi.android:id/home_bottom_tab_button_ding"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
time.sleep(1)
d(text="竖").click()
time.sleep(1)
d.xpath('//android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
time.sleep(1)
for i in range(1,10):
    d.swipe_ext("up")
    time.sleep(40+random.random()*5)
d(resourceId="cn.xuexi.android:id/iv_back").click()

###################################################################
##答题





time.sleep(1)
d(resourceId="cn.xuexi.android:id/comm_head_xuexi_mine").click()
time.sleep(1)
d.click(0.502, 0.396)
time.sleep(1)
if d(text="").exists():
    d(text="").click()

#获取提示
def getanswer():
    d.swipe_ext("up")
    d(text="查看提示").click()
    time.sleep(1)
    answer = d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]').get_text()
    print("答案",answer)
    d(text="").click()
    return answer

#获取相似度
import difflib
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def daydati():
    time.sleep(1)
    d(text="每日答题").click()
    try:
        while "/5" in d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').get_text():
            time.sleep(1)
            answer = getanswer()
            if answer == "请观看视频":
                d(text="").click()
                time.sleep(1)
                d(text="").click()
                time.sleep(1)
                d(text="退出").click()
                daydati()
                break

            if d(text="单选题").exists() or d(text="多选题").exists():
                elements = d.xpath('//android.widget.ListView').all()
                xuanxiangs = []
                for son in elements:
                    gsons = son.elem.getchildren()
                    for gson in gsons :
                        ggsons = gson.getchildren()
                        for ggson in ggsons:
                            gggsons = ggson.getchildren()
                            xuanxiangs.append(gggsons[2].get("text"))
                            print(gggsons[2].get("text"))

                i=0
                for xuanxiang in xuanxiangs:
                    if "错误" in xuanxiang:
                        d(text="错误").click()
                        time.sleep(1)
                        if d(text="答案解析").exists():
                            d(text="").click()
                            time.sleep(1)
                            d(text="退出").click()
                            daydati()
                            break
                    elif xuanxiang in answer:
                        d(text=xuanxiang).click()
                        i=i+1
                        time.sleep(0.5)
                if i == 0:
                    sim=[]
                    for xuanxiang in xuanxiangs:
                        sim.append(string_similar(xuanxiang, answer))
                    max_index, max_number = max(enumerate(sim), key=itemgetter(1))
                    time.sleep(1)
                    d(text=xuanxiangs[max_index]).click()
                time.sleep(2)

                if d(text="确定").exists():
                    d(text="确定").click()
                time.sleep(1)
                if d(text="答案解析").exists():
                    time.sleep(1)
                    print("出现错误")
                    d(text="").click()
                    time.sleep(1)
                    d(text="退出").click()
                    daydati()
                    break

            elif d(text="填空题").exists():
                elements = d.xpath(

                    '//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]').all()
                for eles in elements:
                    sons = eles.elem.getchildren()
                    if answer.find(sons[0].get("text")[-5:]) != -1:
                        answer = answer[answer.find(sons[0].get("text")[-5:]) + 5:]
                    answer = answer[:answer.find(sons[2].get("text")[:5])]
                d.set_clipboard(answer)
                time.sleep(1)
                d.xpath(
                    '//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]').click()
                time.sleep(1)
                d(resourceId="com.huawei.ohos.inputmethod:id/clip_tv_content").click()
                time.sleep(1)
                if d(text="确定").exists():
                    d(text="确定").click()
                time.sleep(1)
                if d(text="答案解析").exists():
                    time.sleep(1)
                    print("出现错误")
                    d(text="").click()
                    time.sleep(1)
                    d(text="退出").click()
                    daydati()
                    break


    except:
        return

daydati()
time.sleep(1)
d(text="返回").click()


###################################################################
#双人赛


def twoxontest():
    d(text="").click()
    while True:
        try:
            if d(text="继续挑战").exists:
                break
            if d.xpath('//android.widget.ListView/android.view.View[1]').exists:
                d.xpath('//android.widget.ListView/android.view.View[{}]'.format(random.randint(1, 2))).click()
                time.sleep(random.random()/3)
        except:
            break
    time.sleep(1)
    d(text="").click()
    time.sleep(1)
    d(text="").click()
    time.sleep(1)
    d(text="退出").click()

###################################################################
#四人赛


def fourcontest():
    d(text="开始比赛").click()
    while True:
        try:
            if d(text="继续挑战").exists:
                break
            if d.xpath('//android.widget.ListView/android.view.View[1]').exists:
                d.xpath('//android.widget.ListView/android.view.View[{}]'.format(random.randint(1, 2))).click()
                time.sleep(random.random()/3)
        except:
            break
    time.sleep(1)
    d(text="").click()
    time.sleep(1)
    d(text="").click()
    time.sleep(1)
    d(text="").click()

###################################################################
#挑战答题


# def tzcontest():
#     while True:
#         try:
#             if d(text="再来一局").exists:
#                 break
#             elif d(text="立即复活").exists:
#                 d(text="立即复活").click()
#             elif d.xpath('//android.widget.ListView/android.view.View[1]').exists:
#                 d.xpath('//android.widget.ListView/android.view.View[{}]'.format(random.randint(1, 2))).click()
#                 time.sleep(random.random()/3)
#         except:
#             break
#     time.sleep(1)
#     d(text="").click()
#     time.sleep(1)
#     d(text="").click()
#     time.sleep(1)
#     d(text="").click()

###################################################################

time.sleep(1)
# for i in range(1,4):
#     d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[3]/android.view.View[8]/android.view.View[{}]'.format(i)).click()
#     time.sleep(1)
#     if d(text="").exists:
#         twoxontest()
#     elif d(text="开始比赛").exists:
#         fourcontest()
#     else:d(text="时事政治").click()
d.xpath(
    '//*[@resource-id="app"]/android.view.View[1]/android.view.View[3]/android.view.View[8]/android.view.View[1]').click()
time.sleep(1)
if d(text="").exists:
    twoxontest()
elif d(text="开始比赛").exists:
    fourcontest()
# else:
#     # d(text="时事政治").click()




###################################################################


###################################################################

time.sleep(1)
d.app_stop("cn.xuexi.android")

