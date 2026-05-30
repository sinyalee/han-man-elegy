#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compile.py —— 用 latexmk 把《人妻约会指南》编译成 PDF（跨平台：macOS / Linux / Windows 通用）

默认是“自包含”编译：清理 → 编译 → 再清理，最终目录里只多出一个 book.pdf。
真正干活的是 latexmk：它会自动决定 xelatex 需要跑几次（通常 2~3 次），无需手动重复。

用法（在项目根目录）：
    python compile.py           自包含编译
    python compile.py --keep     保留中间文件并增量编译（调试/反复改稿时更快）
Windows 上若 `python` 不可用，可试 `py compile.py`。
"""
import argparse
import glob
import os
import platform
import shutil
import subprocess
import sys

MAIN = "text/book.tex"
JOB = "book"

# ---- 颜色：仅在交互式终端启用；Windows 上尝试打开 ANSI 支持，失败则退回纯文本 ----
_color = sys.stdout.isatty()
if _color and platform.system() == "Windows":
    try:
        import ctypes
        h = ctypes.windll.kernel32.GetStdHandle(-11)          # STD_OUTPUT_HANDLE
        ctypes.windll.kernel32.SetConsoleMode(h, 7)           # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    except Exception:
        _color = False


def _c(code):
    return code if _color else ""


GRN, RED, RST = _c("\033[32m"), _c("\033[31m"), _c("\033[0m")


def info(msg):
    print(f"{GRN}==>{RST} {msg}")


def err(msg):
    print(f"{RED}错误:{RST} {msg}", file=sys.stderr)


def tex_install_help():
    name = platform.system()
    if name == "Darwin":
        print("  macOS：安装 MacTeX（完整版，自带 latexmk 和全部宏包）：")
        print("      brew install --cask mactex      # 或从 https://www.tug.org/mactex/ 下载")
        print("    精简版 BasicTeX：brew install --cask basictex")
        print("      （之后：sudo tlmgr install latexmk ctex ccicons algorithm2e diagbox titlesec）")
    elif name == "Linux":
        print("  Linux：")
        print("    · Debian/Ubuntu:  sudo apt-get install texlive-full latexmk")
        print("    · Fedora:         sudo dnf install texlive-scheme-full")
    elif name == "Windows":
        print("  Windows：推荐安装 MiKTeX（缺宏包时会自动安装）：https://miktex.org/download")
        print("    或安装 TeX Live：https://www.tug.org/texlive/（两者都自带 latexmk）")
    else:
        print("  请从 https://www.tug.org/texlive/ 安装 TeX Live（含 latexmk）。")


def have(tool):
    return shutil.which(tool) is not None


def clean():
    """latexmk -c 清根目录中间文件，再手动清 text/ 里 \\include 产生的 .aux。"""
    subprocess.run(["latexmk", "-c", MAIN],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for f in glob.glob("text/*.aux"):
        try:
            os.remove(f)
        except OSError:
            pass


def main():
    parser = argparse.ArgumentParser(
        description="用 latexmk + xelatex 编译《人妻约会指南》为 PDF。")
    parser.add_argument("--keep", action="store_true",
                        help="保留中间文件并增量编译（更快，便于调试）")
    args = parser.parse_args()

    # 切到脚本所在目录（项目根目录），因此可在任何位置运行
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.isfile(MAIN):
        err(f"在当前目录找不到 {MAIN}，请把 compile.py 放在项目根目录运行。")
        sys.exit(1)

    # 硬性依赖：latexmk + xelatex
    missing = [t for t in ("latexmk", "xelatex") if not have(t)]
    if missing:
        err("找不到：" + "、".join(missing))
        tex_install_help()
        sys.exit(1)

    if not args.keep:
        info("清理旧的中间文件……")
        clean()

    info("用 latexmk 编译（自动运行 xelatex 多次）……")
    rc = subprocess.run(
        ["latexmk", "-xelatex", "-interaction=nonstopmode", MAIN]).returncode

    if rc == 0:
        if not args.keep:
            info("清理中间文件……")
            clean()
        info(f"编译完成！生成文件：{os.path.join(os.getcwd(), JOB + '.pdf')}")
    else:
        err(f"编译失败，已保留 {JOB}.log 供排查。若提示缺少宏包：")
        print("  · TeX Live / MacTeX:  sudo tlmgr install <宏包名>")
        print("  · MiKTeX (Windows):   通常会自动安装，或用 MiKTeX Console 安装")
        sys.exit(1)


if __name__ == "__main__":
    main()
