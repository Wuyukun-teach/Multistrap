# scripts/multistrap.py
print("Hello from Multistrap!")
import argparse
import os
import csv
from Bio import SeqIO

def process_fasta(fasta_path):
    """处理FASTA文件并返回统计信息"""
    total_sequences = 0
    total_bases = 0
    try:        
        for record in SeqIO.parse(fasta_path, "fasta"):        
            total_sequences += 1        
            total_bases += len(record.seq)        
        return total_sequences, total_bases
    except Exception as e:
        raise RuntimeError(f"FASTA文件处理失败: {str(e)}")

def main():
    try:    
        parser = argparse.ArgumentParser(description="FASTA文件分析工具")    
        parser.add_argument("-fasta", required=True, help="输入FASTA文件路径")    
        parser.add_argument("-output", required=True, help="输出目录路径")    
        args = parser.parse_args()    

        os.makedirs(args.output, exist_ok=True)    
        print(f"[状态] 输出目录已创建: {args.output}")    

        print(f"[状态] 正在分析FASTA文件: {args.fasta}")    
        total_seqs, total_bases = process_fasta(args.fasta)    
        
        log_path = os.path.join(args.output, "multistrap.log")    
        with open(log_path, "w") as f:        
            f.write("Multistrap 运行成功！\n")        
            f.write(f"输入文件: {args.fasta}\n")        
            f.write(f"总序列数: {total_seqs}\n")        
            f.write(f"总碱基数: {total_bases}\n")        
        print(f"[状态] 日志文件已生成: {log_path}")    

        report_path = os.path.join(args.output, "report.csv")    
        with open(report_path, "w") as csvfile:    
                    
            writer = csv.writer(csvfile)        
            writer.writerow(["统计项", "数值"])        
            writer.writerow(["总序列数", total_seqs])        
            writer.writerow(["总碱基数", total_bases])        
        print(f"[状态] CSV报告已生成: {report_path}")    

        print("\n===== 分析结果 =====")    
        print(f"总序列数: {total_seqs}")    
        print(f"总碱基数: {total_bases}")    

    except FileNotFoundError as e:    
        print(f"[错误] 文件不存在: {str(e)}")    
    except RuntimeError as e:    
        print(f"[错误] {str(e)}")    
    except Exception as e:    
        print(f"[错误] 未知错误: {str(e)}")    
        import traceback    
        traceback.print_exc()    


if __name__ == "__main__":
    main()    
