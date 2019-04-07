from nonebot import on_command, CommandSession
import datetime
@on_command("ra", only_to_me = False)
async def ra(session: CommandSession):
    ra_report = await calculate(session.ctx, session.current_arg)
    await session.send(ra_report)

async def calculate(data, dataString):
    if 'group_id' in data:
        if 'card' in data['sender'] and data['sender']['card'] != '':
            nickname = data['sender']['card']
        else:
            nickname = data['sender']['nickname']
    else:
        nickname = data['sender']['nickname']


    event = ""
    ch_flag = False
    prop = ""
    for ch in dataString:
        if "0" <= ch <= "9":
            ch_flag = True
            prop += ch
        else:
            if ch_flag: break
            event += ch
    prop = eval(prop)
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    minute = date.minute
    hour = date.hour
    second = date.second
    
    res = (((len(event) * second // month + second) * year // hour) % 99) + 1

    chineseRes = " "

    if res < prop*0.25:
        chineseRes += "极大成功"
    elif prop*0.25 <= res < prop*0.5:
        chineseRes += "大成功"
    elif prop*0.5 <= res < prop:
        chineseRes += "成功"
    elif prop == res:
        chineseRes += "一定成功"
    elif res > prop:
        chineseRes += "失败"
    
    return nickname + "进行" + event + "检定：D100=" + str(res) + "/" + str(prop) + chineseRes