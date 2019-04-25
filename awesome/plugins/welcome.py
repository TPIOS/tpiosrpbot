from nonebot import on_notice, NoticeSession
@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send("欢迎进群，请仔细阅读群公告哦~", at_sender = True)