from nonebot import on_command, CommandSession
import datetime
from awesome.plugins.utils import getUsername, get_stroke
rp_dict = dict()

@on_command('jrrp', only_to_me = False)
async def jrrp(session: CommandSession):
    rp_report = await get_today_rp(session.ctx)
    await session.send(rp_report)

async def get_today_rp(data):
    nickname = getUsername(data)
    strokes = get_stroke(nickname)
    date = datetime.datetime.now()
    year, month, day = date.year, date.month, date.day
    today = str(year) + '-' + str(month) + '-' + str(day)
    qqid = str(data["sender"]["user_id"])
    id_cnt = 0
    for c in qqid: id_cnt += int(c)

    if today in rp_dict:
        if qqid not in rp_dict[today]:
            rp_dict[today][qqid] = ((strokes+id_cnt)*year*month // day % 99) + 1
    else:
        rp_dict[today] = dict()
        rp_dict[today][qqid] = ((strokes+id_cnt)*year*month // day % 99) + 1

    rp = rp_dict[today][qqid]
    res = nickname + "今天的人品是：" + str(rp)
    return res