import srt, os, datetime


def assTime(x):
    ms = x.microseconds // 10000
    h = x.seconds // 3600
    m = x.seconds // 60
    s = x.seconds % 60
    return "%d:%02d:%02d.%02d" % (h, m, s, ms)


# ■■■此处需要手动输入■■■
episodes = 9
input = "./"
output = "Mythic.Quest.Ravens.Banquet.S01E%02d.1080p.WEB.H264-AMCON.ass"
cnFlag = '_chi'
enFlag = '_eng'

files = os.listdir(input)

for episode in range(episodes):

    file1 = ""
    file2 = ""

    for file in files:
        if file.find(cnFlag) > 0 and file.find('E%02d.' % (episode + 1)) > 0:
            file1 = file
            break
    for file in files:
        if file.find(enFlag) > 0 and file.find('E%02d.' % (episode + 1)) > 0:
            file2 = file
            break
    print("第%d集 %s %s" % (episode + 1, file1, file2))

    srt1 = []
    srt2 = []

    with open(input + file1, encoding='UTF-8-sig') as f:
        x = srt.parse(''.join(f.readlines()))
        for i in x:
            text = i.content.replace('\n-', '  -').replace('\n\n', '').replace('\n', '')
            srt1.append([i.start, i.end, text])

    with open(input + file2, encoding='UTF-8-sig') as f:
        x = srt.parse(''.join(f.readlines()))
        for i in x:
            text = i.content.replace('\n-', ' -').replace('\n\n', '').replace('\n', '')
            srt2.append([i.start, i.end, text])

    f = open(output % (episode + 1), 'w', encoding='UTF-8-sig')
    f.write("""[Script Info]
    ScriptType: v4.00+
    ScaledBorderAndShadow: no
    YCbCr Matrix: TV.601
    
    [V4+ Styles]
    Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
    Style: CN,方正黑体_GBK,20,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134
    Style: CN2,方正黑体_GBK,20,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134
    Style: EN,微软雅黑,12,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134
    
    [Events]
    Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
    """)

    c1 = 0
    c2 = 0
    while c1 < len(srt1):
        if c2 < len(srt2) and (srt1[c1][0] == srt2[c2][0] or srt1[c1][1] == srt2[c2][1]):
            f.write("Dialogue: 0,%s,%s,CN,,0,0,0,,%s\\N{\\rEN}%s\n" % (
                assTime(srt1[c1][0]), assTime(srt1[c1][1]), srt1[c1][2], srt2[c2][2]))
            c1 += 1
            c2 += 1
        elif c2 >= len(srt2) or srt1[c1][0] < srt2[c2][0]:
            f.write("Dialogue: 0,%s,%s,CN2,,0,0,0,,%s\n" % (assTime(srt1[c1][0]), assTime(srt1[c1][1]), srt1[c1][2]))
            print("注释字幕", assTime(srt1[c1][0]), assTime(srt1[c1][1]), srt1[c1][2])
            c1 += 1
        elif srt1[c1][0] > srt2[c2][0]:
            print("放弃英文字幕", assTime(srt2[c2][0]), assTime(srt2[c2][1]), srt2[c2][2])
            c2 += 1
        else:
            print("WTF")
    f.close()

    maxl = 30
    max1 = 0
    for i in range(len(srt1)):
        if len(srt1[i][2]) > maxl:
            maxl = len(srt1[i][2])
            max1 = i
    if max1>0:
        print("建议检查 该行中文字幕字数", maxl, (assTime(srt1[max1][0]), assTime(srt1[max1][1]), srt1[max1][2]))
    maxl = 90
    max1 = 0
    for i in range(len(srt2)):
        if len(srt2[i][2]) > maxl:
            maxl = len(srt2[i][2])
            max1 = i
    if max1 > 0:
        print("建议检查 该行英文字符数", maxl, (assTime(srt2[max1][0]), assTime(srt2[max1][1]), srt2[max1][2]))
