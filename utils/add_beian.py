import os
import sys

def replace_copyright_line(filename, beian):
    """
    替换文件中以 'copyright: ' 开头的行（在原内容后追加新内容）
    """
    new_content = f' <br> <a target="_blank" href="https://beian.miit.gov.cn/">{beian}</a>'
    
    try:
        # 创建备份文件（原文件名.bak）
        backup = filename + '.bak'
        os.replace(filename, backup)
        print(f"已创建备份: {backup}")
        
        # 处理文件内容
        modified = False
        with open(backup, 'r') as fin, open(filename, 'w') as fout:
            for line in fin:
                # 匹配以copyright开头的行（不修改其他行）
                if line.startswith('copyright: '):
                    # 移除可能的换行符（\n或\r\n）
                    stripped_line = line.rstrip('\r\n')
                    fout.write(stripped_line + new_content + '\n')
                    modified = True
                    print("已修改匹配行")
                else:
                    fout.write(line)
        
        if not modified:
            print("警告: 未找到以 'copyright: ' 开头的行！")
            os.replace(backup, filename)  # 恢复原文件
            print("已恢复原文件")
        else:
            print(f"成功更新文件: {filename}")
            
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python replace_copyright.py <文件名> <备案信息>")
        sys.exit(1)
    
    replace_copyright_line(sys.argv[1], sys.argv[2])
