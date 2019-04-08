from nonebot import on_command, CommandSession
@on_command("fa", only_to_me = True)
async def fa(session: CommandSession):
    await session.send("fa" + session.current_arg)