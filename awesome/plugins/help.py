from nonebot import on_command, CommandSession
@on_command("help", only_to_me = False)
async def help(session: CommandSession):
    readme = await get_readme()
    await session.send(readme)

async def get_readme():
    res = '''
    这里是由望村小居士(TPIOS)编写的QQ-Bot
    这是现在版本所能提供的命令：
    .jrrp : 获得今天的人品值
    .echo : 回声(复读)，返回自己的在.echo之后说的话 (仅限添加此Bot为好友才能使用)
    .ra[空格][某事件][概率值]: 对某一事件进行玄学概率分析，从而得到结果
    .help : 返回QQ-Bot的说明
    --------
    接下来本Bot还会更新的内容：
    1. FGOwiki API连接
    2. 更新.jrrp的一些设计
    '''
    return res