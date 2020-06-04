# srt-2-bilingual-ass
combine 2 SRT files into a bilingual ASS (SubStation Alpha) subtitle file

# version 2.0 update notes
# 第二版更新

add main.py

使用```main.py```可以模糊匹配两个字幕文件

# 合并两种语言的SRT字幕为双语ASS字幕

## For English Users
You won't need subtitles to watch TV shows LOL.

## For Bilingual Users
### TL;DR 

Prepare 2 SRT files, edit some parameters in the py file, run the py file, done.

### Details

TODO If you want it, make an issue and I will update.

## Warning
The StartTime or Endtime of the same dialog in 2 srt files should be the same or this dialog in the second language will be ignored.

The algorithm is **simple** and **naive**

## 使用方法
准备2个SRT文件，修改py文件内的参数，运行py文件。

## 用到的库
```pip3 install srt```

## 前提条件 注意事项
两个SRT文件对应句子是相同的（至少开头或结尾时间轴完全相等），否则第二种语言（例如英文）的对应句子会被忽略

## 高级玩法
只有第一种语言没有第二种语言的句子使用的样式是```CN2```，一般为对时间地点画面中出现的英文的注释，便于制作特效字幕快速找到对应句子。

## 已测试
在Windows平台，对```神话任务：群鸦盛宴 Mythic Quest: Raven’s Banquet```字幕进行测试顺利输出双语字幕

## 输出字幕样式
采用人人影视的字幕样式（字体：方正黑体_GBK 和 微软雅黑），优化了双语样式控制方法

