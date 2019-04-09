def getUsername(data):
    '''
    data should be session.ctx
    '''
    if 'group_id' in data:
        if 'card' in data['sender'] and data['sender']['card'] != '':
            nickname = data['sender']['card']
        else:
            nickname = data['sender']['nickname']
    else:
        nickname = data['sender']['nickname']
    return nickname