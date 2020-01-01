from nonebot import on_command, CommandSession
@on_command("search", only_to_me = False)
async def search(session: CommandSession):
    searchRes = await get_res(session.ctx, session.current_arg)
    await session.send(searchRes, ensure_private = True)

async def get_res(data, datastring):
    print(datastring)
    if datastring == "":
        res = "请输入搜索的从者名"
    else:
        res = "fgo.wiki/w/"+datastring
    return res