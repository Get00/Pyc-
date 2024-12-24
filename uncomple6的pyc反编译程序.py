# -*-coding:utf-8 -*-
import sys
import os
from uncompyle6 import main as uncompyle_main

def print_help():
    help_text = """
用法: python uncompyle6.py [选项] 文件...

选项:
  -h, --help            显示此帮助信息并退出
  -o DIR, --output-dir=DIR
                        指定输出目录，默认为与输入文件相同的目录
"""
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print("缺少参数，请使用 -h 查看帮助信息")
        return

    output_dir = None
    files_to_decompile = []

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ['-h', '--help']:
            print_help()
            return
        elif arg in ['-o', '--output-dir']:
            if i + 1 >= len(sys.argv):
                print("错误: 缺少输出目录参数")
                return
            output_dir = sys.argv[i + 1]
            i += 1
        else:
            files_to_decompile.append(arg)
        i += 1

    if not files_to_decompile:
        print("没有指定要反编译的文件，请使用 -h 查看帮助信息")
        return

    for file_path in files_to_decompile:
        if not os.path.isfile(file_path):
            print(f"错误: 文件 {file_path} 不存在")
            continue

        base_name = os.path.basename(file_path)
        name_without_ext = os.path.splitext(base_name)[0]

        if output_dir is None:
            output_dir = os.path.dirname(file_path)

        output_file_path = os.path.join(output_dir, f"{name_without_ext}.py")

        try:
            with open(output_file_path, 'w') as out_file:
                uncompyle_main.decompile_file(file_path, out_file)
            print(f"成功反编译 {file_path} 到 {output_file_path}")
        except Exception as e:
            print(f"反编译 {file_path} 时出错: {e}")

if __name__ == "__main__":
    main()



