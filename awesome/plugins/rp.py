from nonebot import on_command, CommandSession
import time, datetime
import random
from awesome.plugins.utils import getUsername, getProbability
rp_dict = dict()

@on_command('jrrp', only_to_me = False)
async def jrrp(session: CommandSession):
    rp_report = await get_today_rp(session.ctx)
    await session.send(rp_report)

async def get_today_rp(data):
    nickname = getUsername(data)
    date = datetime.datetime.now()
    year, month, day = date.year, date.month, date.day
    today = str(year) + '-' + str(month) + '-' + str(day)
    userid = str(data["sender"]["user_id"])
    if today in rp_dict:
        if userid not in rp_dict[today]:
            rp_dict[today][userid] = getProbability(userid, nickname, random.randint(1, 100))
    else:
        random.seed(time.time())
        rp_dict[today] = dict()
        rp_dict[today][userid] = getProbability(userid, nickname, random.randint(1, 100))

    rp = rp_dict[today][userid]
    res = nickname + "今天的人品是：" + str(rp)
    return res