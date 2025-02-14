import pytchat,csv,sys

def get_comment(video_id):
    livechat=pytchat.create(video_id,topchat_only=True)
    time_f=True
    text=[]
    file_name=f"{video_id}_not4.csv"
    starttime=0
    difftime=-1
    count=0
    now=0

    print(f"{video_id} start")

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
            message=f"{count}  {time[0]}:{time[1]}:{time[2]}"
            sys.stdout.write("\033[2K\033[G%s"%message)
            sys.stdout.flush()
    
    print()
    print(f"{video_id} finish")
    
    with open(file_name,'w',newline='',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerows(text)

video_list=["YAt2rFMmK8M","MUgc5iYsOR8"]
for i in range(len(video_list)):
    print(f"task {i+1}/{len(video_list)}")
    get_comment(video_list[i])
print("all complete")