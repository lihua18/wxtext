from tkinter import *
from wxpy import *
from PIL import Image,ImageTk


root = Tk()
root.geometry('500x300+500+200')
root.title('微信客服机器人')
root.iconbitmap('favicon.ico')
bot = Bot(qr_path='qrcode.jpg',qr_callback='status',console_qr=2)
img = Image.open('qrcode.jpg')
out = img.resize((300,300),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(out)
Label(root, text='扫码登录',image=photo,width=300,height=300).pack()
root.mainloop()

