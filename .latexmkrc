# latexmk 配置（被所有 compile 脚本以及手动 `latexmk` 共用）
#
# 有了这个文件，在项目根目录直接运行：
#     latexmk        # 编译（自动决定 xelatex 跑几次）
#     latexmk -c     # 清理中间文件（保留 book.pdf）
# 即可，无需记任何参数。

$pdf_mode = 5;                                       # 5 = 用 xelatex 引擎
@default_files = ('text/book.tex');                  # 主文件在 text/ 子目录
$xelatex = 'xelatex -interaction=nonstopmode %O %S'; # 出错不卡住、继续到底
