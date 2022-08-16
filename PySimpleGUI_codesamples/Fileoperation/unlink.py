from pathlib import Path
cd = Path.cwd()
newfilepath = cd/'read_write2.txt'
newfilepath.unlink()