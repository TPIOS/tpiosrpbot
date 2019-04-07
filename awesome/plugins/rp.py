from nonebot import on_command, CommandSession
import datetime

@on_command('jrrp', only_to_me = False)
async def jrrp(session: CommandSession):
    print(session.ctx)
    rp_report = await get_today_rp(session)
    await session.send(rp_report)

async def get_today_rp(session: CommandSession):
    if 'group_id' in session.ctx:
        if 'card' in session.ctx['sender'] and session.ctx['sender']['card'] != '':
            res = session.ctx['sender']['card']+"今天的人品是"+str(getrp(session.ctx))
        else:
            res = session.ctx['sender']['nickname']+"今天的人品是"+str(getrp(session.ctx))
    else:
        res = session.ctx['sender']['nickname']+"今天的人品是"+str(getrp(session.ctx))
    
    return res

def getrp(data):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    male2bool = {'male': 0, 'female': 1}
    if data['sender']['sex'] in male2bool:
        res = ((data['sender']['user_id'] * year // month + day) % 99) + 1 + male2bool[data['sender']['sex']]
    else:
        res = ((data['sender']['user_id'] * year // month + day) % 99) + 1
    return res
    