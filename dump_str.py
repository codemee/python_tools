# dump_str.py
from ctypes import string_at
from binascii import hexlify
import sys

s = 'abc'
if len(sys.argv) > 1:
    s = sys.argv[1]       # 取得命令行指定的字串

b = hexlify(              # 以 16 進位表示
    string_at(            # 取得一段記憶體的內容
        id(s),            # s 在記憶體中的啟始位址
        sys.getsizeof(s)  # s 佔的記憶體大小
    ),
    ' '                   # 每個位元組之間的分隔字元
)

print(b)