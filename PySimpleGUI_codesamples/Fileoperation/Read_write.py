from pathlib import Path
cd = Path.cwd()
filepath = cd/'read_write.txt'
contents = filepath.read_text(encoding='utf-8')
print(contents)
newfilepath = cd/'read_write2.txt'
newcontents = '新しい書き込み'
newfilepath.write_text(newcontents,encoding='utf-8')