分數=[32,43,56,74,19,89,64]
分數.append(100)
分數[0]=60
del 分數[2]
print(len(分數))
print(分數)
print(sum(分數)/len(分數))
分數.reverse()
print("反轉順序：", 分數)
分數.sort()
print("升序排序：", 分數)

分數.reverse()
print("反轉順序：", 分數)

分數.sort(reverse=True)
print("降序排序：", 分數)

商品={
    '品名':'珍奶',
    '價格':65,
    '冰塊':'少冰'
}
print(商品.items())
a=商品['價格']
商品['價格']=a+5
print(商品.items())

A = {'蘋果', '香蕉', '葡萄'}
B = {'香蕉', '橘子', '鳳梨'}
print(A & B)
print(A|B)
print(A - B)
print(B-A)

客人A = {'珍珠', '椰果', '愛玉'}
客人B = {'椰果', '布丁', '芋圓'}
print(客人A&客人B)
print(客人A|客人B)
print(客人A-客人B)
print(客人B-客人A)
x=(客人A-客人B)
s=(客人B-客人A)
print(x|s)

資料 = ('小綠', 25, True)
print(資料[0])
print(資料[1])
def 姓名():
    return (資料[0])

def 年齡():
    return (資料[1])

print(年齡())
print(姓名())


for h in range(5):
    print("第", h + 1, "次 Hello")

#菜單
菜單={'紅茶','綠茶','奶茶','冬瓜茶','烏龍茶',}
加料選項={'珍珠','椰果','布丁','多多'}
x=[]#x為訂單項目(所有
d=0#d是總金額
#點物

while True:
    print('請問要喝什麼我們有',菜單,'每杯35元')
    q=input('請輸入您想喝的飲料，如不需要請按0')#q是所點的飲料
    a=[]#a是加料暫存
    e=0#e是單一金額
    if q != '0' and q not in 菜單:
        print('沒有賣')

    if q in 菜單:
        e+=35
        while True:
            print('請問要加點什麼嗎?我們有',加料選項,'每樣加5元')
            z=input('請輸入您想加的配料如不需要請按0')#z是所點的加料選項
            if z=='0':
                g=input('請輸入杯數')#g是杯數(單一)
                j=float(g)#j杯數(轉
                e*=j
                d+=e
                s={
                    '飲料':q,
                    '配料':a,
                    '價格':e,
                    '杯數':g
                }#s為單筆訂單
                x.append(s)
                print('目前訂單',x)
                break
            if z in 加料選項:
                a.append(z)
                print('目前加的料',a)
                e+=5
            else:
                print('沒有這個料喔！')
            
        n=input('是否還要點餐，是(1)否(0)')
        if n=='0':
            break
    if q=='0' :
        break
o=input('======請輸入備註======')
print('感謝您的購買')
print('======訂單項目======')
for i ,s in enumerate(x,1):
    print(f"第{i}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯")
print('======備註======')
print(o)
print('總金額為',d,'元')






#GPT修改版(下)
# 菜單
菜單 = {'紅茶', '綠茶', '奶茶', '冬瓜茶', '烏龍茶'}
加料選項 = {'珍珠', '椰果', '布丁', '多多'}
訂單清單 = []  # 所有訂單
總金額 = 0

# 點餐流程
while True:
    print('請問要喝什麼？我們有：', 菜單, '每杯35元')
    飲料 = input('請輸入想喝的飲料（不想點請按0）：')
    單杯金額 = 0
    加料清單 = []

    if 飲料 == '0':
        break
    elif 飲料 not in 菜單:
        print('不好意思，我們沒有這個飲料')
        continue
    else:
        單杯金額 += 35

        # 加料流程
        加料輸入 = input('請輸入加料（可多種，用空格分開，不加請輸入0）：')
        if 加料輸入 != '0':
            加料們 = 加料輸入.split()
            for 料 in 加料們:
                if 料 in 加料選項:
                    加料清單.append(料)
                    單杯金額 += 5
                else:
                    print(f'我們沒有這個加料：{料}')

        杯數 = input('請輸入杯數：')
        try:
            杯數 = int(杯數)
        except:
            print('杯數請輸入數字！')
            continue

        小計 = 單杯金額 * 杯數
        總金額 += 小計

        單筆訂單 = {
            '飲料': 飲料,
            '配料': 加料清單,
            '價格': 小計,
            '杯數': 杯數
        }
        訂單清單.append(單筆訂單)
        print('目前訂單：', 訂單清單)

        繼續 = input('是否還要點餐？是(1) / 否(0)：')
        if 繼續 == '0':
            break

# 備註
備註 = input('====== 請輸入備註（可空白）======\n')

# 顯示訂單
print('\n====== 感謝您的購買 ======')
print('====== 訂單明細 ======')
print(f'{"編號":<4} {"飲料":<6} {"加料項目":<20} {"杯數":<4} {"小計":<5}')
print('-' * 45)

for i, 訂單 in enumerate(訂單清單, 1):
    飲料 = 訂單['飲料']
    配料 = '、'.join(訂單['配料']) if 訂單['配料'] else '無'
    杯數 = 訂單['杯數']
    價格 = int(訂單['價格'])
    print(f'{i:<4} {飲料:<6} {配料:<20} {杯數:<4} ${價格:<5}')

print('====== 備註 ======')
print(備註 if 備註 else '（無）')
print('====== 總金額：', 總金額, '元 ======')






第一=input('第一筆')
第二=input('第二筆')

with open('C:/Users/user/Desktop/新增資料夾/drink_log.txt','w',encoding='utf-8') as f:
    f.write(第一+'\n')
    f.write(第二+'\n')

with open('C:/Users/user/Desktop/新增資料夾/drink_log.txt','r',encoding='utf-8') as f:
    內容=f.read()
    print(內容)



#菜單
菜單={'紅茶','綠茶','奶茶','冬瓜茶','烏龍茶',}
加料選項={'珍珠','椰果','布丁','多多'}
x=[]#x為訂單項目(所有
d=0#d是總金額
#點物

while True:
    print('請問要喝什麼我們有',菜單,'每杯35元')
    q=input('請輸入您想喝的飲料，如不需要請按0')#q是所點的飲料
    a=[]#a是加料暫存
    e=0#e是單一金額
    if q != '0' and q not in 菜單:
        print('沒有賣')

    if q in 菜單:
        e+=35
        while True:
            print('請問要加點什麼嗎?我們有',加料選項,'每樣加5元')
            z=input('請輸入您想加的配料如不需要請按0')#z是所點的加料選項
            if z=='0':
                g=input('請輸入杯數')#g是杯數(單一)
                j=float(g)#j杯數(轉
                e*=j
                d+=e
                s={
                    '飲料':q,
                    '配料':a,
                    '價格':e,
                    '杯數':g
                }#s為單筆訂單
                x.append(s)
                print('目前訂單',x)
                break
            if z in 加料選項:
                a.append(z)
                print('目前加的料',a)
                e+=5
            else:
                print('沒有這個料喔！')
            
        n=input('是否還要點餐，是(1)否(0)')
        if n=='0':
            break
    if q=='0' :
        break
o=input('======請輸入備註======')
print('感謝您的購買')
print('======訂單項目======')
for i ,s in enumerate(x,1):
    print(f"第{i}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯")
print('======備註======')
print(o)
print('總金額為',d,'元')


with open('C:/Users/user/Desktop/新增資料夾/drink_log.txt','w',encoding='utf-8')as w:
    for m,s in enumerate(x,1):
        w.write(f"第{m}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯\n")
    w.write('備註')
    w.write(o)
    w.write('\n總金額為')
    w.write(str(d))




    import csv

訂單紀錄 = [
    {'品項': '奶茶', '加料': '珍珠', '杯數': 2, '價格': 80},
    {'品項': '綠茶', '加料': '椰果,布丁', '杯數': 1, '價格': 75}
]

with open('C:/Users/user/Desktop/新增資料夾/訂單紀錄.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['品項', '加料', '杯數', '價格'])
    writer.writeheader()
    writer.writerows(訂單紀錄)
with open('C:/Users/user/Desktop/新增資料夾/訂單紀錄.csv','r',encoding='utf-8-sig') as fr:
    reader=csv.DictReader(fr)
    for row in reader:
        print(row)
        
#菜單
菜單={'紅茶','綠茶','奶茶','冬瓜茶','烏龍茶',}
加料選項={'珍珠','椰果','布丁','多多'}
x=[]#x為訂單項目(所有
d=0#d是總金額
#點物

while True:
    print('請問要喝什麼我們有',菜單,'每杯35元')
    q=input('請輸入您想喝的飲料，如不需要請按0')#q是所點的飲料
    a=[]#a是加料暫存
    e=0#e是單一金額
    if q != '0' and q not in 菜單:
        print('沒有賣')

    if q in 菜單:
        e+=35
        while True:
            print('請問要加點什麼嗎?我們有',加料選項,'每樣加5元')
            z=input('請輸入您想加的配料如不需要請按0')#z是所點的加料選項
            if z=='0':
                g=input('請輸入杯數')#g是杯數(單一)
                j=float(g)#j杯數(轉
                e*=j
                d+=e
                s={
                    '飲料':q,
                    '配料':a,
                    '價格':e,
                    '杯數':g
                }#s為單筆訂單
                x.append(s)
                print('目前訂單',x)
                break
            if z in 加料選項:
                a.append(z)
                print('目前加的料',a)
                e+=5
            else:
                print('沒有這個料喔！')
            
        n=input('是否還要點餐，是(1)否(0)')
        if n=='0':
            break
    if q=='0' :
        break
o=input('======請輸入備註======')
print('感謝您的購買')
print('======訂單項目======')
for i ,s in enumerate(x,1):
    print(f"第{i}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯")
print('======備註======')
print(o)
print('總金額為',d,'元')
print(x)

import csv

with open('C:/Users/user/Desktop/新增資料夾/訂單紀錄.csv', 'w', newline='', encoding='utf-8-sig') as ef:
    writer = csv.DictWriter(ef,fieldnames=['飲料','配料','價格','杯數'])
    writer.writeheader()
    writer.writerows(x)
dx=0
with open('C:/Users/user/Desktop/新增資料夾/訂單紀錄.csv', 'r', newline='', encoding='utf-8-sig') as rf:
    rfe=csv.DictReader(rf)
    for ex in rfe:
        print(ex)
        print(ex['價格'])
        dxx=float(ex['價格'])
        dx+=dxx
        print('0',dx)

try:
    x = 1 / 1
except ZeroDivisionError:
    print("錯誤：除以 0 了！")
else:
    print("沒錯誤會執行這裡")
finally:
    print("不管有沒有錯，這裡都會執行")


try:
    print('11')
except ValueError:
    print('錯誤-類別:轉型錯誤')
except TypeError:
    print('錯誤-類別:類型錯誤')
except ZeroDivisionError:
    print('錯誤-類別:除以零')
except IndexError:
    print('錯誤-類別:索引超出範圍')
except KeyError:
    print('錯誤-類別:找不到鍵')
except FileNotFoundError:
    print('錯誤-類別:找不到檔案')
except PermissionError:
    print('錯誤-類別:沒有權限打開檔案')
except ImportError:
    print('錯誤-類別:模組載入失敗')
except AttributeError:
    print('錯誤-類別:沒有這個屬性或方法')
except NameError:
    print('錯誤-類別:使用位定義的變數')
except Exception as a:
    print('錯誤-類別:其他',a)




try:
    print('11')
    x=1
    x.不存在()
    亂碼
    import opcod
    z='zxz'
    open("xxx.txt")
    x=5+z
    c=1/0
except ValueError:
    print('錯誤-類別:轉型錯誤，例如 int("abc")')
except TypeError:
    print('錯誤-類別:類型錯誤，例如數字加字串：1 + "2"')
except ZeroDivisionError:
    print('錯誤-類別:除以零')
except IndexError:
    print('錯誤-類別:索引超出範圍')
except KeyError:
    print('錯誤-類別:找不到鍵')
except FileNotFoundError:
    print('錯誤-類別:找不到檔案')
except PermissionError:
    print('錯誤-類別:沒有權限打開檔案')
except ImportError:
    print('錯誤-類別:模組載入失敗')
except AttributeError:
    print('錯誤-類別:沒有這個屬性或方法')
except NameError:
    print('錯誤-類別:使用未定義的變數')
except Exception as a:
    print('錯誤-類別:其他',a)

import math

x = float(input("請輸入一個數字："))
print("平方根：", math.sqrt(x))
print("平方：", math.pow(x, 2))
print("捨去小數：", math.floor(x))
print("進位：", math.ceil(x))

    import math
    g=float(input('請輸入您的體重(公斤)'))
    cm=float(input('請輸入您的身高(公分)'))
    m=cm/100
    bmi=g/(math.pow(m,2))
    bmi*=100
   
    bmi=(math.floor(bmi))
    bmi/=100
    print('您的BMI約為',bmi)
    if bmi>24:
        print('您目前狀態:過重')
    elif bmi<18.5:
        print('您目前狀態:過輕')
    else:
        print('您目前狀態:適中')


    import random
    m=random.randint(1,99)
    a=0
    z=100
    k=0
    print(a)
    while True:
        print('猜數字',a,'到',z)
        x=input()
        q=int(x)
        k+=1
        if q==m:
            print('恭喜你答對了!!!')
            print('一共花了',k,'次')
            break
        elif q<m:
            a=q
        elif q>m:
            z=q


    import random
飲=['紅茶','奶茶','烏龍茶','冬瓜茶','綠茶']
o=random.choice(飲)
print(o)


import datetime
    nt=datetime.datetime.now()
    print('現在是',nt)
    nd=nt.date()
    print(nd)
    m=int(input('出生月'))
    d=int(input('出生日'))
    y=2025
    生日=datetime.datetime(y,m,d,0,0)
    差=生日-nt
    if 差.days==-1:
        print('生日快樂!!!')
    elif 差.days<-1:
        y+=1
        生日=datetime.datetime(y,m,d,0,0)
        差=生日-nt
        print('距離生日還有',差.days,'個完整天')
    elif 差.days>-1:
        print('距離生日還有',差.days,'個完整天')


import datetime
    nt=datetime.datetime.now()
    print(nt)
    ytw=int(nt.strftime('%Y'))
    ytw-=1911
    mtw=int(nt.strftime('%m'))
    dtw=int(nt.strftime('%d'))
    w=nt.strftime('%a')
    if w=='Sun':
        w='天'
    elif w=='Mon':
        w='一'
    elif w=='Tue':
        w='二'
    elif w=='Wed':
        w='三'
    elif w=='Thu':
        w='四'
    elif w=='Fri':
        w='五'
    elif w=='Sat':
        w='六'
    print('現在時間',ytw,'年',mtw,'月',dtw,'號','(星期',w,')')
    print(nt.strftime('%H點%M分%S秒'))

print('5')
    print(os.getcwd())
    print('2')
    os.chdir('C:/Users/user/Desktop')  # 換到桌面（Windows 範例）
    print('6')
    files = os.listdir('.')  # 列出目前資料夾
    print(files)
    os.mkdir('測試資料夾')
    os.makedirs('a/b/c/d',exist_ok=True)
    os.rmdir('測試資料夾')
    folder = '資料'
    filename = '訂單紀錄.csv'
    path = os.path.join(folder, filename)
    print(path)  # Windows: 資料\訂單紀錄.csv，mac/Linux: 資料/訂單紀錄.csv
    p = 'a'

    print(os.path.exists(p))     # 檢查存在
    print(os.path.isfile(p))     # 是檔案嗎？
    print(os.path.isdir(p))      # 是資料夾嗎？
    path = 'C:/Users/user/Desktop/訂單紀錄.csv'
    print(os.path.exists(path))
    print(os.path.basename(path))  # 訂單紀錄.csv
    print(os.path.dirname(path))   # C:/Users/user/Desktop
    root, ext = os.path.splitext(path)
    print(root)  # .../訂單紀錄
    print(ext)   # .csv


import os
    import time
    print(os.getcwd())
    os.chdir('C:/Users/user/Desktop/測試區')
    print(os.getcwd())
    os.makedirs('drinks_data',exist_ok=True)
    x=os.listdir('.')
    print(x)
    t=os.path.join('drinks_data','log.txt')
    with open(t,'w',encoding='utf-8') as f:
        f.write('Hello 小綠！這是測試檔案')
    os.chdir('C:/Users/user/Desktop/測試區/drinks_data')
    x=os.listdir('.')
    print(x)
    time.sleep(3)
    os.rename('log.txt','log_v2.txt')


import os,time,shutil
    print(os.getcwd())
    bata=os.path.join('C:/Users/user/Desktop/測試區','drinks_data')
    os.chdir(bata)
    print(os.getcwd())
    back=os.path.join('C:/Users/user/Desktop/測試區','drinks_backup')
    shutil.copytree(bata,back)
    os.chdir(back)
    print(os.getcwd())
    shutil.move('log_v2.txt','drink_log.txt')
    桌面=os.path.join('C:/Users/user/Desktop')
    os.chdir(桌面)
    shutil.move(back,桌面)
    time.sleep(5)
    backup=os.path.join(桌面,'drinks_backup')
    shutil.rmtree(backup)



import json
    訂單={
        '品名':"紅茶",
        '加料':['珍珠','多多'],
        '價格':40,
        '外帶':True
    }
    訂單j=json.dumps(訂單,ensure_ascii=False)
    print(訂單j)
    with open('my_order.json','w',encoding='utf-8') as f:
        json.dump(訂單j,f,ensure_ascii=False,indent=2)
    with open('my_order.json','r',encoding='utf-8')as f:
        讀取=json.load(f)
    print(讀取)



import os
    print(os.getcwd())
    os.chdir('C:/Users/user/Desktop/測試區')
    print(os.getcwd())
    測試區=os.path.join('C:/Users/user/Desktop/測試區')
    資料=os.path.join('C:/Users/user/Desktop/測試區/test.txt')
    print(os.path.exists(資料))

    if os.path.exists(資料)==False:
        with open(資料,'x',encoding='utf-8') as f:
            pass
    else:
        pass


    #菜單
    菜單={'紅茶','綠茶','奶茶','冬瓜茶','烏龍茶',}
    加料選項={'珍珠','椰果','布丁','多多'}
    x=[]#x為訂單項目(所有
    d=0#d是總金額
    #點物

    while True:
        print('請問要喝什麼我們有',菜單,'每杯35元')
        q=input('請輸入您想喝的飲料，如不需要請按0')#q是所點的飲料
        a=[]#a是加料暫存
        e=0#e是單一金額
        if q != '0' and q not in 菜單:
            print('沒有賣')

        if q in 菜單:
            e+=35
            while True:
                print('請問要加點什麼嗎?我們有',加料選項,'每樣加5元')
                z=input('請輸入您想加的配料如不需要請按0')#z是所點的加料選項
                if z=='0':
                    g=input('請輸入杯數')#g是杯數(單一)
                    j=float(g)#j杯數(轉
                    e*=j
                    d+=e
                    s={
                        '飲料':q,
                        '配料':a,
                        '價格':e,
                        '杯數':g
                    }#s為單筆訂單
                    x.append(s)
                    print('目前訂單',x)
                    break
                if z in 加料選項:
                    a.append(z)
                    print('目前加的料',a)
                    e+=5
                else:
                    print('沒有這個料喔！')

            n=input('是否還要點餐，是(1)否(0)')
            if n=='0':
                break
        if q=='0' :
            break
    o=input('======請輸入備註======')
    print('感謝您的購買')
    print('======訂單項目======')
    for i ,s in enumerate(x,1):
        print(f"第{i}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯")
    print('======備註======')
    print(o)
    print('總金額為',d,'元')

    with open(資料,'a',encoding='utf-8')as w:
        for m,s in enumerate(x,1):
            w.write(f"第{m}項:{s['飲料']}，加料項目:{s['配料']}---${s['價格']}，{s['杯數']}杯\n")
        w.write('備註')
        w.write(o)
        w.write('\n總金額為')
        w.write(str(d))
        w.write('\n\n')

import time
    print(time.time())
    time.sleep(1)
    now = time.localtime()
    print(time.strftime('%y,%m,%D,%h,%m,%S'))
    print(time.strftime("%Y-%m-%d %H:%M:%S", now))
    for t in range(10,0,-1):
        print(t)
        time.sleep(1)
    print('!!!')

import time
    Q=input('請輸入計時時間')
    t=int(Q)
    print(t)
    for i in range(t,0,-1):
        print('飲料還需等',i,'秒')
        time.sleep(1)
    print('完成了')

import re
    u='irejie,dsmier0912345678，jiegj(06)7264446，rgj+886965899965jf(2)gu0965488862'
    ph=r'\(\d{}\)'
    p=re.findall(ph,u)
    print(p)
    pass


import statistics
    資料=[]
    
    while True:
        a=input('請輸入(n為結束，d為刪除)')#a為輸入
        if a!='n'and a!='d':
            ab=int(a)
            資料.append(ab)
            print('資料:',資料)
        elif a=='d':
            b=input('請輸入想要刪除的資料')#b為刪除資料
            bb=int(b)
            資料.remove(bb)
            print('資料:',資料)
        elif a=='n':
            break
    
    平均=statistics.mean(資料)
    中位數=statistics.median(資料)
    眾數=statistics.mode(資料)
    print('平均=',平均)
    print('中位數=',中位數)
    print('眾數=',眾數)


#失敗區下
import csv,os
    print(os.getcwd())
    os.chdir('C:/Users/user/Desktop/測試區')
    print(os.getcwd())
    測試區=os.path.join('C:/Users/user/Desktop/測試區')
    資料=os.path.join('C:/Users/user/Desktop/測試區/訂單紀錄.csv')
    print(os.path.exists(資料))

    if os.path.exists(資料)==False:
        with open(資料,'x',encoding='utf-8') as f:
            pass
    else:
        pass







    # ====== 1. 點餐流程 ======
    菜單 = {"紅茶", "綠茶", "奶茶", "冬瓜茶", "烏龍茶"}
    加料選項 = {"珍珠", "椰果", "布丁", "多多"}

    訂單 = []   # 所有訂單
    總金額 = 0

    while True:
        print("請問要喝什麼？我們有", 菜單, "每杯35元")
        飲料 = input("請輸入您想喝的飲料，如不需要請按0：")

        if 飲料 == "0":
            break
        if 飲料 not in 菜單:
            print("不好意思，沒有賣這個飲料")
            continue

        # 基本價格
        單價 = 35
        配料 = []

        while True:
            print("請問要加什麼料？我們有", 加料選項, "每樣加5元")
            加料 = input("請輸入您想加的配料，如不需要請按0：")

            if 加料 == "0":
                break
            elif 加料 in 加料選項:
                配料.append(加料)
                單價 += 5
                print("目前加料：", 配料)
            else:
                print("沒有這個料喔！")

        杯數 = int(input("請輸入杯數："))
        總價 = 單價 * 杯數
        總金額 += 總價

        訂單.append({
            "飲料": 飲料,
            "配料": ";".join(配料),  # 多個配料用 ; 分隔
            "價格": 總價,
            "杯數": 杯數
        })

        n = input("是否還要點餐？是(1) 否(0)：")
        if n == "0":
            break

    # ====== 2. 寫入 CSV 檔案 ======
    with open(資料, "a", newline="", encoding="utf-8-sig") as f:
        欄位 = ["飲料", "配料", "價格", "杯數"]
        writer = csv.DictWriter(f, fieldnames=欄位)
        writer.writeheader()
        writer.writerows(訂單)

    print("✅ 訂單已存入 訂單紀錄.csv")

    # ====== 3. 再讀取 CSV 並計算總金額 ======
    新總金額 = 0
    with open(資料, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)  # 查看每一筆訂單
            新總金額 += int(row["價格"])

    print("📌 訂單總金額：", 新總金額, "元")
#失敗區上





import csv, os, datetime,time

    # 1. 產生檔名 (根據日期)
    今天 = datetime.date.today().strftime("%Y-%m-%d")
    檔案名稱 = f"訂單紀錄_{今天}.csv"
    資料夾 = "C:/Users/user/Desktop/測試區"
    資料 = os.path.join(資料夾,檔案名稱)

    # 2. 菜單
    菜單 = {"紅茶", "綠茶", "奶茶", "冬瓜茶", "烏龍茶"}
    加料選項 = {"珍珠", "椰果", "布丁", "多多"}

    訂單 = []
    總金額 = 0

    while True:
        print("請問要喝什麼？我們有", 菜單, "每杯35元")
        飲料 = input("請輸入您想喝的飲料，如不需要請按0：")

        if 飲料 == "0" or 飲料 == "查看":
            break
        if 飲料 not in 菜單:
            print("不好意思，沒有賣這個飲料")
            continue

        # 基本價格
        單價 = 35
        配料 = []

        while True:
            print("請問要加什麼料？我們有", 加料選項, "每樣加5元")
            加料 = input("請輸入您想加的配料，如不需要請按0：")

            if 加料 == "0":
                break
            elif 加料 in 加料選項:
                配料.append(加料)
                單價 += 5
                print("目前加料：", 配料)
            else:
                print("沒有這個料喔！")

        杯數 = int(input("請輸入杯數："))
        總價 = 單價 * 杯數
        總金額 += 總價
        now = time.localtime()
        訂單.append({
            "飲料": 飲料,
            "配料": ";".join(配料),
            "價格": 總價,
            "杯數": 杯數,
            "時間":time.strftime("%Y-%m-%d %H:%M:%S", now)
        })

        n = input("是否還要點餐？是(1) 否(0)：")
        if n == "0":
            break

    # 3. 檢查檔案是否存在 → 決定要不要寫表頭
    寫新檔 = not os.path.exists(資料) or os.path.getsize(資料) == 0

    with open(資料, "a", newline="", encoding="utf-8-sig") as f:
        欄位 = ["飲料", "配料", "價格", "杯數","時間"]
        writer = csv.DictWriter(f, fieldnames=欄位)
        if 寫新檔:
            writer.writeheader()
        writer.writerows(訂單)

    print("✅ 訂單已存入", 資料)
    print('本訂單種金額',總金額)

    # 4. 再讀取並計算總金額
    if 飲料=='查看':
        密=input('請輸入密碼:')
        if 密=='au4a83':
            新總金額 = 0
            with open(資料, "r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    新總金額 += int(row["價格"])

            print("本日訂單總金額：", 新總金額, "元")
        else:
            print('警告!!!')
            pass



import csv, os, datetime, time
    from collections import defaultdict
    import matplotlib.pyplot as plt  # 📌 用來畫圖
    
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']   # Windows 常用
    plt.rcParams['axes.unicode_minus'] = False

    # 1. 產生檔名 (根據日期)
    今天 = datetime.date.today().strftime("%Y-%m-%d")
    檔案名稱 = f"訂單紀錄_{今天}.csv"
    資料夾 = "C:/Users/user/Desktop/測試區"
    資料 = os.path.join(資料夾, 檔案名稱)

    # 2. 菜單
    菜單 = {"紅茶", "綠茶", "奶茶", "冬瓜茶", "烏龍茶"}
    加料選項 = {"珍珠", "椰果", "布丁", "多多"}

    訂單 = []
    總金額 = 0

    while True:
        print("請問要喝什麼？我們有", 菜單, "每杯35元")
        飲料 = input("請輸入您想喝的飲料，如不需要請按0，輸入「查看」查詢：")

        if 飲料 == "0":   # 結束點餐
            break
        if 飲料 == "查看":   # 查看模式
            密 = input("請輸入密碼:")
            if 密 == "au4a83":
                if os.path.exists(資料):
                    新總金額 = 0
                    統計 = defaultdict(lambda: {"杯數": 0, "金額": 0})

                    with open(資料, "r", encoding="utf-8-sig") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            新總金額 += int(row["價格"])
                            統計[row["飲料"]]["杯數"] += int(row["杯數"])
                            統計[row["飲料"]]["金額"] += int(row["價格"])

                    print("\n📌 本日訂單總金額：", 新總金額, "元")
                    print("📊 銷售統計：")
                    for 飲料名, 資料 in 統計.items():
                        print(f"  {飲料名}: {資料['杯數']} 杯，共 {資料['金額']} 元")

                    # === 📈 畫圖 ===
                    飲料名稱 = list(統計.keys())
                    杯數列表 = [統計[飲料]["杯數"] for 飲料 in 飲料名稱]

                    plt.bar(飲料名稱, 杯數列表, color="skyblue")
                    plt.xlabel("飲料")
                    plt.ylabel("銷售杯數")
                    plt.title(f"{今天} 飲料銷售統計")
                    plt.show()

                else:
                    print("⚠️ 今日尚無訂單")
            else:
                print("🚨 密碼錯誤!")
            continue

        if 飲料 not in 菜單:
            print("不好意思，沒有賣這個飲料")
            continue

        # 基本價格
        單價 = 35
        配料 = []

        while True:
            print("請問要加什麼料？我們有", 加料選項, "每樣加5元")
            加料 = input("請輸入您想加的配料，如不需要請按0：")

            if 加料 == "0":
                break
            elif 加料 in 加料選項:
                配料.append(加料)
                單價 += 5
                print("目前加料：", 配料)
            else:
                print("沒有這個料喔！")

        杯數 = int(input("請輸入杯數："))
        總價 = 單價 * 杯數
        總金額 += 總價
        now = time.localtime()
        訂單.append({
            "飲料": 飲料,
            "配料": ";".join(配料),
            "價格": 總價,
            "杯數": 杯數,
            "時間": time.strftime("%Y-%m-%d %H:%M:%S", now)
        })

        n = input("是否還要點餐？是(1) 否(0)：")
        if n == "0":
            break

    # 3. 檢查檔案是否存在 → 決定要不要寫表頭
    if 訂單:
        寫新檔 = not os.path.exists(資料) or os.path.getsize(資料) == 0
        with open(資料, "a", newline="", encoding="utf-8-sig") as f:
            欄位 = ["飲料", "配料", "價格", "杯數", "時間"]
            writer = csv.DictWriter(f, fieldnames=欄位)
            if 寫新檔:
                writer.writeheader()
            writer.writerows(訂單)

        print("✅ 訂單已存入", 資料)
        print("本訂單總金額", 總金額, "元")


import matplotlib.pyplot as plt

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']   # Windows 常用
    plt.rcParams['axes.unicode_minus'] = False  #中文
    # 範例數據
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]
    水果 = ["蘋果", "香蕉", "葡萄", "橘子", "芒果"]
    銷售量 = [40, 25, 20, 10, 5]
    資料 = [7, 8, 5, 6, 9, 10, 6, 7, 8, 6, 5, 7, 9]

    # 設定畫布大小
    plt.figure(figsize=(12, 8))

    # 1. 折線圖
    plt.subplot(2, 2, 1)  # 2x2 格子 → 第 1 張
    plt.plot(x, y, color="blue", marker="o", linestyle="--", label="數據A")
    plt.title("折線圖")
    plt.xlabel("X軸")
    plt.ylabel("Y軸")
    plt.legend()
    plt.grid(True)

    # 2. 長條圖
    plt.subplot(2, 2, 2)  # 第 2 張
    plt.bar(水果, 銷售量, color="orange")
    plt.title("長條圖 - 水果銷售量")
    plt.xlabel("水果種類")
    plt.ylabel("銷售量")

    # 3. 圓餅圖
    plt.subplot(2, 2, 3)  # 第 3 張
    plt.pie(銷售量, labels=水果, autopct="%1.1f%%", startangle=90, explode=[0.1, 0, 0, 0, 0])
    plt.title("圓餅圖 - 銷售比例")

    # 4. 直方圖
    plt.subplot(2, 2, 4)  # 第 4 張
    plt.hist(資料, bins=5, color="green", edgecolor="black")
    plt.title("直方圖 - 成績分布")
    plt.xlabel("分數區間")
    plt.ylabel("人數")

    # 顯示圖表
    plt.tight_layout()  # 自動調整間距
    plt.show()


import itertools,random

    # 飲料 & 加料選項
    飲料 = ["紅茶", "綠茶", "奶茶"]
    加料 = ["珍珠", "椰果", "布丁"]
    全=[]
    # 產生所有「一杯飲料 + 任意加料」的組合
    print("=== 所有飲料+加料組合 ===")
    for d in 飲料:
        # 加料可以 0 個 ~ 全部都加
        for r in range(len(加料) + 1):
            for toppings in itertools.combinations(加料, r):
                print(d, "+", toppings if toppings else "無加料")
                單一=d,toppings if toppings else "無加料"
                全.append(單一)
    
    
    print(random.choice(全))


import itertools, random

    # 飲料 & 加料選項
    飲料 = ["紅茶", "綠茶", "奶茶"]
    加料 = ["珍珠", "椰果", "布丁"]
    全 = []

    print("=== 所有飲料+加料組合 ===")
    for d in 飲料:
        for r in range(len(加料) + 1):
            for toppings in itertools.combinations(加料, r):
                組合 = (d, toppings if toppings else "無加料")
                全.append(組合)

                # 美化輸出
                if toppings:
                    print(f"{d} + {', '.join(toppings)}")
                else:
                    print(f"{d} + 無加料")

    # 隨機推薦一組
    隨機組合 = random.choice(全)
    飲 = 隨機組合[0]
    料 = 隨機組合[1]

    if isinstance(料, tuple):  # 有加料
        print("\n🎲 今天推薦:", 飲, "+", ", ".join(料))
    else:  # 無加料
        print("\n🎲 今天推薦:", 飲, "+ 無加料")

    import random
    from collections import Counter

    # 模擬菜單
    菜單 = ["紅茶", "綠茶", "奶茶", "烏龍茶", "冬瓜茶"]

    # 模擬 100 筆訂單
    訂單紀錄 = []
    for i in range(100):
        飲料 = random.choice(菜單)
        訂單紀錄.append(飲料)
        print(訂單紀錄)
    # 用 Counter 統計飲料出現次數
    統計 = Counter(訂單紀錄)

    print("=== 今日銷售統計 ===")
    for 飲料, 數量 in 統計.items():
        print(f"{飲料}: {數量} 杯")

    # 取出最受歡迎的飲料
    熱門 = 統計.most_common(1)[0]
    print("\n⭐ 最受歡迎的飲料是：", 熱門[0], "（賣出", 熱門[1], "杯）")

    # 顯示一筆隨機訂單
    隨機訂單 = random.choice(訂單紀錄)
    print("\n🎲 隨機挑選一筆訂單：", 隨機訂單)
    import csv, os
    from collections import namedtuple

    # 定義命名元組
    Drink = namedtuple('Drink', ['名稱', '加料', '杯數', '價格'])

    # 建立資料夾與檔案路徑
    資料夾 = 'C:/Users/user/Desktop/測試區'
    os.makedirs(資料夾, exist_ok=True)
    檔案 = os.path.join(資料夾, '命名元組訂單.csv')

    # 菜單與加料
    菜單 = {'紅茶': 35, '綠茶': 35, '奶茶': 40, '烏龍茶': 40}
    加料選項 = {'珍珠': 5, '椰果': 5, '布丁': 10}

    訂單 = []
    總金額 = 0

    while True:
        print("請問要喝什麼？我們有：", list(菜單.keys()))
        飲料 = input("輸入飲料名稱（或輸入 0 結束）：")

        if 飲料 == "0":
            break
        if 飲料 not in 菜單:
            print("沒有這個飲料喔～")
            continue

        # 加料部分
        加料列表 = []
        單價 = 菜單[飲料]

        while True:
            print("可加料項目：", list(加料選項.keys()))
            加料 = input("請輸入想加的料（或輸入 0 結束）：")
            if 加料 == "0":
                break
            if 加料 in 加料選項:
                加料列表.append(加料)
                單價 += 加料選項[加料]
            else:
                print("沒有這個料喔！")

        杯數 = int(input("請輸入杯數："))
        小計 = 單價 * 杯數
        總金額 += 小計

        # 建立命名元組
        item = Drink(名稱=飲料, 加料=";".join(加料列表) if 加料列表 else "無", 杯數=杯數, 價格=小計)
        訂單.append(item)

    # === 寫入 CSV ===
    寫新檔 = not os.path.exists(檔案) or os.path.getsize(檔案) == 0

    with open(檔案, "a", newline="", encoding="utf-8-sig") as f:
        欄位 = ['名稱', '加料', '杯數', '價格']
        writer = csv.DictWriter(f, fieldnames=欄位)
        if 寫新檔:
            writer.writeheader()
        for d in 訂單:
            writer.writerow(d._asdict())  # namedtuple 轉 dict 寫入

    print("✅ 訂單已寫入：", 檔案)
    print("💰 今日總金額：", 總金額, "元")

    # === 顯示 CSV 內容 ===
    print("\n====== 檔案內容 ======")
    with open(檔案, "r", encoding="utf-8-sig") as f:
        print(f.read())

        def 點餐(*a,**info):
        print('點了:',a)
        for key, value in info.items():
            print(f"{key}：{value}")



print((lambda 基本價, 加料數, 杯數: 基本價 + 加料數 * 5 * 杯數)(35, 2, 3))


