import srt, datetime

file1 = "chs.srt"
file2 = "eng.srt"

srt1 = []
srt2 = []


def assTime(x):
    ms = x.microseconds // 10000
    h = x.seconds // 3600
    m = x.seconds // 60
    s = x.seconds % 60
    return "%d:%02d:%02d.%02d" % (h, m, s, ms)


with open(file1, encoding='UTF-8-sig') as f:
    x = srt.parse(''.join(f.readlines()))
    for i in x:
        text = i.content.replace('\n-', '  -').replace('\n\n', '').replace('\n', '')
        srt1.append([i.start, i.end, text])

with open(file2, encoding='UTF-8-sig') as f:
    x = srt.parse(''.join(f.readlines()))
    for i in x:
        text = i.content.replace('\n-', ' -').replace('\n\n', '').replace('\n', '')
        srt2.append([i.start, i.end, text])

i = 0
out = []

while i < len(srt1):
    line2 = []
    for j in range(len(srt2)):
        if abs(srt2[j][0] - srt1[i][0]).total_seconds() < 0.5 or abs(srt2[j][1] - srt1[i][1]).total_seconds() < 0.5:
            line2.append(srt2[j][2])
    out.append([srt1[i], line2])
    i += 1

f = open('out.ass', 'w', encoding='UTF-8-sig')
f.write("""[Script Info]
ScriptType: v4.00+
ScaledBorderAndShadow: no
YCbCr Matrix: TV.601

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CN,方正黑体_GBK,22,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134
Style: CN2,方正黑体_GBK,20,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134
Style: EN,微软雅黑,14,&H00FFFFFF,&HF0000000,&H00000000,&H32000000,0,0,0,0,100,100,0,0,1,2,1,2,5,5,2,134

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")

for t in out:
    f.write("Dialogue: 0,%s,%s,CN,,0,0,0,,%s\\N{\\rEN}%s\n" % (
        assTime(t[0][0]), assTime(t[0][1]), t[0][2], ' '.join(t[1])))
f.close()
