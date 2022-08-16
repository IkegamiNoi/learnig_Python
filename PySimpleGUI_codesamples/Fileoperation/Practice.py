from pathlib import Path
cd = Path.cwd()
print(cd)
#filepath = cd/'Practice.py'
filepath = cd/'sample.txt'
print(filepath)
with filepath.open(encoding='utf-8') as f:
    print(f.read())
contents = '上書き保存'
with filepath.open(mode='w',encoding='utf-8') as f:
    f.write(contents)