#!/usr/bin/python3
from wxpy import *
from tkinter import *

def closeWindow():
    root.destroy()

bot=Bot(login_callback=None)
groups = bot.groups()
root = Tk()
root.geometry('600x600+500+300')
root.title('微信客服机器人')
root.iconbitmap('favicon.ico')
v = []
choice = []
choice2 = ""
lf = LabelFrame(text='请选择你需要管理的群：')
lf.pack(fill='both', expand='yes')
for strGroup in groups:
    v.append(IntVar())
    b = Checkbutton(lf, text=strGroup.name, variable=v[-1])
    b.pack(anchor=W)

lf2 = LabelFrame(text='请选择你发送给好友要加的群：')
lf2.pack(fill='both',expand='yes')
v2=IntVar()
v2.set(1)
for strGroup in groups:
    Radiobutton(lf2, text=strGroup.name, variable=v2,value=groups.index(strGroup)+1).pack(anchor=W)
Button(root,text = '下一步',command=closeWindow).pack(side=RIGHT)
mainloop()
count = 0
for i in v:
    if i.get()==1:
        choice.append(groups[count])
    count += 1
# choice = groups[shuzi-1]  #这个群也是自动加好友后，自动拉好友进入的群。
choice2 = groups[v2.get()-1]
print(choice)
print(choice2)
root2 = Tk()
root2.geometry('600x600+500+300')
root2.title('微信客服机器人')
root2.iconbitmap('favicon.ico')
label = Label(root2,text = '请输入你的主题和目录：').grid()
# text1 = input('请输入第一条信息。')
# text2 = input('请输入第二条信息。')
# text3 = input('请输入第三条信息。')
root2.mainloop()

@bot.register(choice,'Text')
def print_messages(msg):
    print(msg.text)
    if msg.is_at:
        if '1' in msg.text:
            msg.reply(text1)
        elif '2' in msg.text:
            msg.reply(text2)
        elif '3' in msg.text:
            msg.reply(text3)

@bot.register(choice,'Note')
def welcome(msg):
    print(msg.text)
    if "邀请" in msg.text:
        name = msg.text.split('"')[3]
        welcome_you = "欢迎" + name + "加入我们的大家庭。"
        msg.reply(welcome_you)



@bot.register(msg_types=FRIENDS)                 # 自动添加好友请求类消息并且发送入群邀请
def auto_accept_friends(msg):
    new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
    choice2.add_members(new_friend, use_invitation=True)

# 堵塞线程，并进入 Python 命令行
embed()