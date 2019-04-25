from nonebot import on_command, CommandSession
@on_command("help", only_to_me = False)
async def help(session: CommandSession):
    readme = await get_readme()
    await session.send(readme, ensure_private = True)

async def get_readme():
    res = '''这里是由望村小居士(TPIOS)编写的QQ-Bot，
    你可以亲切地叫我居娘
    这是现在版本所能提供的命令：
    .jrrp: 获得今天的人品值，每个人一天的人品值一定是固定的
    .ra[空格][某事件][概率值]: 对某一事件进行玄学概率分析，从而得到结果，目前已经支持概率值之前有数字，概率值应不大于100，每个人在一天的不同时间测试相同的东西，概率也可能是不同的
    .help: 现在，在群里使用这个命令，本Bot会私发给请求该命令的用户，QQ-Bot的说明
    本居娘还搭载了图灵机器人功能，私聊居娘获得惊喜哦~
    --------
    接下来居娘还会更新的内容：
    1. FGOwiki API连接
    2. 着手准备.dnd功能的设计'''
    return res