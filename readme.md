# 人妻约会指南

## 下载电子书

[点击这里下载最新版电子书](releases/人妻约会指南v1.5.pdf)
(最新版本：2025年11月11日 第一版v1.5)

## 版权、翻译和二创

### 版权

作者李新野自愿通过CC0协议（Creative Common Zero）放弃所有版权。此放弃版权的行为不可撤销。本文（包括模版之外的LaTeX源代码）在美国、中国和全球所有国家均永久属于公有领域。

### 维护

本repo由李新野维护，其他人如果需要提交修改建议，可以新建issue或者提交pull request。如果你对本版本不满意，可以随时fork本repo建立你自己的版本。

### 翻译

本repo仅维护简体中文原版，希望大家能够帮忙把本文翻译为其他语言。现在AI翻译的水平非常高（，毕竟现在的大语言模型一开始就是为了解决翻译问题）。所以即使大家外语水平普通，也可以在AI的帮助下翻译。

翻译的时候可以直接fork本repo源代码。如果想要把你的翻译版本放到作者个人博客，可以电邮作者: sinyaleesf@gmail.com

作者提供的繁体版本（不再维护）：[https://sinyalee.com/blog/?p=1072](https://sinyalee.com/blog/?p=1072)

### 二创

书中所有故事，都可以随意改编二创。言情小说、galgame、电影、电视剧，体裁不限。

### 盈利

所有翻译、二创作者都拥有衍生作品的版权。可以使用衍生作品盈利。

## 如果你想要自己编译

### 环境设置

本文使用xelatex。需要的包在[package.tex](package.tex)。

本人是先安装TeX Live获取全套LaTeX支持。再安装CTeX套装获取中文支持。再安装ccicons包获取CC0的标志。这个标志不是必要的，可以直接删除。

### 编译命令
要编译本书，请在根目录执行以下命令（注意要执行两次）：
```
xelatex -shell-escape book.tex
xelatex -shell-escape book.tex
```

最终生成文件是根目录的[book.pdf](book.pdf)

如果你不熟悉命令行，可以直接将项目上传至Overleaf，然后将编译器更换成XeLaTeX即可编译。

### 模版

本文使用中山大学博士生Nelson Cheung的LaTeX中文书籍模版。编译本书时可以参考该模版的说明。该模版的GitHub地址：[https://github.com/Nelson-Cheung/latex-book-template](https://github.com/Nelson-Cheung/latex-book-template)
