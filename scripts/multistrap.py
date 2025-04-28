# scripts/multistrap.py
print("Hello from Multistrap!")
import argparse
import os

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("-fasta", required=True, help="输入 FASTA 文件路径")
    parser.add_argument("-output", required=True, help="输出目录路径")
    args = parser.parse_args()

    # 创建输出目录（如果不存在）
    os.makedirs(args.output, exist_ok=True)

    # 写入日志文件
    log_path = os.path.join(args.output, "multistrap.log")
    with open(log_path, "w") as f:
        f.write("Multistrap 运行成功！\n")
        f.write(f"输入的 FASTA 文件：{args.fasta}\n")
    
    print(f"日志文件已生成：{log_path}")

if __name__ == "__main__":
    main()
