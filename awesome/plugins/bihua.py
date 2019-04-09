def get_stroke(s):
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