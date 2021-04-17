#from tkinter import Tk, ttk
import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import time

g_width=1000
g_height=1000

rec_side = 2  #四角の辺の大きさ 2より大きい値
bd_width = 1000 #フレームの横幅
bd_height = 1000#フレームの縦幅
clr = "black"#1から始まる螺旋の色
back_clr = "black"
prime_cnt = 700

Pnumcolor = "white"
Unumcolor = "black"

wait_time = 0.001
prime = [2]
prm_cnt = 1
prm_lp = 0
#Funcname:prime_func() Function Description
#Arg1:　素数か判定する数　これまで出現してきた素数で割って余りが出ないかチェック
#Arg2:　これまでに発見された素数の数
#Arg3:　素数のリスト　関数外から参照可能
#Return: 素数判定FLAG
def prime_func(num ):
    global prime
    global prm_lp
    cnt = 0
    ret = "FALSE"
    #num = num + 1

    for j in range(0,prm_lp):
        # rem = num % prm[j]
        rem = num % prime[j]

        if rem == 0:
            cnt = 1#FALSE
            break

    if cnt == 0:
            prm_lp += 1
            prime.append(num)
            ret = "TRUE"#TRUE

    # print(str(num)+":"+ret+":"+str(prime))
    return ret

#Function Description:螺旋状に四角を並べるプログラム
#Arg1:
#Arg2:螺旋描画開始位置　X
#Arg3:螺旋描画開始位置　Y
#Arg4:四角の一辺の大きさ
#Arg5:四角の色
#Return:　なし
# def DrawRecLine(dc,x,y,rec_side,clr):
def DrawRec1Line(root,x,y,rec_side):
    root.canvas.create_rectangle(x, y, x+rec_side, y+rec_side, fill = Pnumcolor)#普通の数の色の設定

def DrawRecLine(root,x,y,rec_side):
    xside = rec_side
    yside = rec_side
    num = 2
    # dc.SetBrush(wx.Brush(clr))
    lp_cnt = 0
    E_OK = "TRUE"

    # dc.DrawRectangle(x, y, rec_side, rec_side)
    clr=Unumcolor
    root.canvas.create_rectangle(x, y, rec_side, rec_side, fill = clr)#普通の数の色の設定
    for i in range(0,prime_cnt):
        #side_cnt=0
        for j in range(0,lp_cnt):
            num = num + 1
            ret = prime_func(
                num#素畔か判定する数
                # prm_cnt,#素数の発生した数
                # prime#素数のリスト
                )
            x = x + xside * pow(-1,lp_cnt)

            # dc.SetBrush(wx.Brush(Unumcolor))#普通の数の色の設定
            # clr=Unumcolor
            if E_OK == ret:#素数発見
                # dc.SetBrush(wx.Brush(Pnumcolor))
                # dc.DrawRectangle(x, y, rec_side, rec_side)
                clr = Pnumcolor
                root.canvas.create_rectangle(x, y, x+rec_side, y+rec_side, fill = clr)#塗りつぶし
            #print("%d,%d,%d,%d,ret=%s"%(num,x,y,k,ret))
                root.update()

        for k in range(0,lp_cnt):
            num = num + 1
            ret = prime_func(
                num#
                # prm_cnt,#
                # prime#
                )
            #if side_cnt == 1:
            y = y + yside * pow(-1,lp_cnt)
            # dc.SetBrush(wx.Brush(Unumcolor))#普通の数の色の設定
            # clr=Unumcolor
            if E_OK == ret:#素数発見
                # dc.SetBrush(wx.Brush(Pnumcolor))
                # dc.DrawRectangle(x, y, rec_side, rec_side)
                clr = Pnumcolor
                root.canvas.create_rectangle(x, y, x+rec_side, y+rec_side, fill = clr)#塗りつぶし
                root.update()

        #if j == lp_cnt -1:
        lp_cnt = lp_cnt + 1
        #print("lp_cnt=%d"%i)
    #dc.SetBrush(wx.Brush(P2color))
    #dc.DrawRectangle(bd_width/2 - rec_side, bd_height/2, rec_side, rec_side)
    d = len(prime)
    # print("last_num = %d, num of prime = %d,%d"%(num,d,prime[d-1]))
    # print(prime)



root = tkinter.Tk()
# root.geometry("1920x760") #Windowのサイズ設定
root.geometry( str(g_width) + "x" + str(g_height)) #Windowのサイズ設定

root.title("Let's Use a Canvvas") #タイトル作成
# app = MyApp1(master=root)
root.canvas = tkinter.Canvas(root, bg="black", width=g_width, height=g_height)
root.canvas.place(x=0, y=0)
root.canvas.pack()




# time.sleep(wait_time)
# root.update()
# root.canvas.create_rectangle(10, 20, 100, 50, fill = 'red')#塗りつぶし
# time.sleep(wait_time)
# root.update()
# root.canvas.create_polygon(250, 10, 220, 100, 150, 100,fill="green")
# time.sleep(wait_time)
# root.update()
# root.canvas.create_line(10, 200, 150, 150, fill='red')
# time.sleep(wait_time)
# root.update()
# root.canvas.create_oval(100, 100, 150, 150, fill='blue')
# time.sleep(wait_time)
# root.update()

# DrawRec1Line(root,g_width/2,g_height/2,rec_side)
DrawRecLine(root,g_width/2,g_height/2,rec_side)
root.canvas.postscript(file="hogehoge.ps", colormode='color')
root.mainloop()