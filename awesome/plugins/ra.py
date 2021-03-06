from nonebot import on_command, CommandSession
import random
from awesome.plugins.utils import getUsername, getProbability

@on_command("ra", only_to_me = False)
async def ra(session: CommandSession):
    ra_report = await calculate(session.ctx, session.current_arg)
    await session.send(ra_report)

def eventprop(dataString):
    prop = ""
    event = ""
    for idx, ch in enumerate(list(dataString)[::-1]):
        if ch.isdigit():
            prop += ch
        else:
            event = dataString[:len(dataString)-idx]
            break
    return event, "".join(prop[::-1])

def checkavail(event, prop):
    if len(event) == 0: return True
    if len(prop) == 0 or prop == "0": return True
    if eval(prop) > 100: return True
    return False

def getRes(res, prop):
    if res < prop*0.25:
        return "极大成功"
    elif prop*0.25 <= res < prop*0.5:
        return "大成功"
    elif prop*0.5 <= res < prop:
        return "成功"
    elif prop == res:
        return "一定成功"
    elif res > prop:
        return "失败"

async def calculate(data, dataString):
    nickname = getUsername(data)
    userid = str(data["sender"]["user_id"])
    event, prop = eventprop(dataString)
    if checkavail(event, prop): return nickname + "指令输入错误，请检查"
    prop = eval(prop)
    res = getProbability(userid, nickname, random.randint(1, 100), event)
    chineseRes = " " + getRes(res, prop)
    return nickname + "进行" + event + "检定：D100=" + str(res) + "/" + str(prop) + chineseRes