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

def getStroke(s):
    strokes_path = "strokes.txt"
    strokes = []
    file = open(strokes_path, "r")
    for line in file.readlines():
        strokes.append(int(line.strip()))
    
    total_strokes = 0
    for c in s:
        code = ord(c)
        if 13312 <= code <= 64045: 
            total_strokes += strokes[code-13312]
        elif 131072 <= code <= 194998:
            total_strokes += strokes[code-80338]
    
    return total_strokes

def getProbability(userid, username, rand, event = None):
    cnt = sum(map(int, list(userid)))
    if event == None:
        return (cnt*getStroke(username) + rand) % 99 + 1
    else:
        return (cnt*getStroke(event)*getStroke(username) + rand) % 99 + 1