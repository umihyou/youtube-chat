import pytchat,csv,sys

def get_comment(video_id):
    livechat=pytchat.create(video_id,topchat_only=True)
    time_f=True
    text=[]
    file_name=f"testdata/ver5/{video_id}_not6.csv"
    starttime=0
    difftime=-1
    count=0
    now=0

    print(f"{video_id} start")
    sys.stdout.write("\033[2K\033[G%s"%"0 0:0:0 0")

    while livechat.is_alive():
        chatdata=livechat.get()
        for c in chatdata.items:
            if ':' in c.message or ',' in c.message or c.message=="" or c.type!="textMessage":
                continue
            elif c.elapsedTime[0]!='-':
                if time_f:
                    starttime=c.timestamp
                    time_f=False
                difftime=c.timestamp-starttime
            text.append([difftime,c.message])
        count+=1
        if count%10==0:
            now=difftime/1000
            time=[int(now//3600),int(now%3600)//60,int(now%60)]
            message=f"{count} {time[0]}:{time[1]}:{time[2]} {len(text)}"
            sys.stdout.write("\033[2K\033[G%s"%message)
            sys.stdout.flush()

    print()
    print(f"{video_id} finish")
    
    with open(file_name,'w',newline='',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerows(text)
        err_f=0
    if text==[]:
        print("チャットを取得できなかったため、空白のファイルを作成しました")
        err_f=1
    return err_f

video_list=["XCkfiyLskS8","FNwrKDTkWGI","fDtUy1PTor0"]
err_message=[]
for i in range(len(video_list)):
    print(f"task {i+1}/{len(video_list)}")
    err_f=get_comment(video_list[i])
    if err_f:
        err_message.append([i,video_list[i],err_f])
if err_message==[]:
    print("all complete")
else:
    print(f"{len(err_message)} error happened")
    for err in err_message:
        print(err)