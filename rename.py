import os, re, sys

class Git(object):

    @staticmethod
    def rename(src, ds ):
        cmd = 'git mv {} {}'.format( src, dst )
        return cmd

class SVN(object):

    @staticmethod
    def rename(src, ds ):
        cmd = 'svn mv {} {}'.format( src, dst )
        return cmd

# Test commands
# python rename.py git D:\follow ^ch b
# python rename.py svn D:\follow ^ch b
# python rename.py git D:\follow change(\d+).txt item\1.txt
# 參數輸入
py_file, *argv = sys.argv
sub_version = argv[0] if len(argv) > 0 else input('請輸入版控類型:\n')
sub_version = SVN if sub_version.lower() == 'svn' else Git

base_file = argv[1] if len(argv) > 1 else input('請輸入檔案路徑:\n')
replacer = argv[2] if len(argv) > 2 else input('請輸入欲修改的檔名規則(正則):\n')
target = argv[3] if len(argv) > 3 else input('請輸入欲取代的字串):\n')

target_files = []
for file_name in os.listdir(base_file):
    match = re.search(replacer, file_name)
    if match is None:
        continue
        
    target_files.append(file_name)
    result = re.sub(replacer, target, file_name)
    print('{} -> {}'.format(file_name, result))
    
confirm = input('確認檔名修改結果[y/N]:\n')
if confirm == 'y':
    for file_name in target_files:
        src = os.path.join(base_file, file_name)
        new_file_name = re.sub(replacer, target, file_name)
        dst = os.path.join(base_file, new_file_name)
        
        cmd = sub_version.rename(src, dst)
        # print(cmd)
        os.system(cmd)

input('修改完成')
    