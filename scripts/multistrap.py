# scripts/multistrap.py
print("Hello from Multistrap!")
import argparse
import os

def main():
    try:
        
        print("[DEBUG] 主函数开始执行")    

        
        parser = argparse.ArgumentParser()    
        parser.add_argument("-fasta", required=True, help="输入 FASTA 文件路径")    
        parser.add_argument("-output", required=True, help="输出目录路径")    
        args = parser.parse_args()    
        print(f"[DEBUG] 解析参数完成 | FASTA路径: {args.fasta}, 输出目录: {args.output}")    

        
        os.makedirs(args.output, exist_ok=True)    
        print(f"[DEBUG] 目录已创建 | 路径是否存在: {os.path.exists(args.output)}")    

        
        log_path = os.path.join(args.output, "multistrap.log")    
        print(f"[DEBUG] 日志文件路径: {log_path}")    

        with open(log_path, "w") as f:    
            f.write("Multistrap 运行成功！\n")    
            f.write(f"输入的 FASTA 文件：{args.fasta}\n")    
        print("[DEBUG] 日志文件已写入")    

        
        print(f"日志文件已生成：{log_path}")    

    except Exception as e:    
        print(f"[ERROR] 发生异常: {e}")    
        
        import traceback    
        traceback.print_exc()    

if __name__ == "__main__":
    main()      
