# Little python tools 

## dump_str.py

Show the string object memory view:

```bash
❯ python .\dump_str.py abc
b'02 00 00 00 00 00 00 00 40 61 b3 9e fc 7f 00 00 03 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff e4 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 61 62 63 00'
❯ python .\dump_str.py 測試
b'02 00 00 00 00 00 00 00 40 61 b3 9e fc 7f 00 00 02 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff a8 00 00 00 00 00 00 00 88 59 c5 62 4a 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 2c 6e 66 8a 00 00'
```

## print_output.py

Show program output in binary, big5 decoded text, and utf8 decoded text:

```bash
❯ python .\print_output.py python -c "print('hello')"
Prefered encoding:cp950
Program output 7 bytes:
68 65 6C 6C 6F 0D 0A
BIG5 output:hello

UTF-8 output:hello

❯ python .\print_output.py python -c "print('測試')"
Prefered encoding:cp950
Program output 6 bytes:
B4 FA B8 D5 0D 0A
BIG5 output:測試

UTF-8 output err:invalid start byte

❯ python .\print_output.py python -X utf8 -c "print('測試')"
Prefered encoding:cp950
Program output 8 bytes:
E6 B8 AC E8 A9 A6 0D 0A
BIG5 output:皜祈岫

UTF-8 output:測試
```