from nonebot import on_notice, NoticeSession
@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send("欢迎进群，请自习阅读群公告", at_sender = True)