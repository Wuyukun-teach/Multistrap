# scripts/multistrap.py
print("Hello from Multistrap!")
import argparse
import os

def main():
    try:
        # 调试：标记开始执行
        print("[DEBUG] 主函数开始执行")

        # 解析命令行参数
        parser = argparse.ArgumentParser()
        parser.add_argument("-fasta", required=True, help="输入 FASTA 文件路径")
        parser.add_argument("-output", required=True, help="输出目录路径")
        args = parser.parse_args()
        print(f"[DEBUG] 解析参数完成 | FASTA路径: {args.fasta}, 输出目录: {args.output}")

        # 创建输出目录
        os.makedirs(args.output, exist_ok=True)
        print(f"[DEBUG] 目录已创建 | 路径是否存在: {os.path.exists(args.output)}")

        # 写入日志文件
        log_path = os.path.join(args.output, "multistrap.log")
        print(f"[DEBUG] 日志文件路径: {log_path}")

        with open(log_path, "w") as f:
            f.write("Multistrap 运行成功！\n")
            f.write(f"输入的 FASTA 文件：{args.fasta}\n")
        print("[DEBUG] 日志文件已写入")

        # 最终输出
        print(f"日志文件已生成：{log_path}")

    except Exception as e:
        print(f"[ERROR] 发生异常: {e}")
        # 可选：打印详细错误堆栈
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()      
