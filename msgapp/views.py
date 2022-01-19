from django.shortcuts import render
from datetime import datetime

def msgproc(request):
    datalist = []   # 用于最终传给模板的表格数据列表

    # 若HTTP方法为POST，往文件中写入信息
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    
    # 若HTTP方法为GET，则按行累计读取10行，并将其写入到datalist列表中
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt =0
                for line in f:
                    linedata = line.split('--') # 把数据按“--”分割开
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, 'msgapp/MsgSingleWeb.html', {"data": datalist}) # 返回html模板和datalist

