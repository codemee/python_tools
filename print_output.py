import sys
import subprocess
import locale

if len(sys.argv) < 2:
    print("Error: .py file needed.")
    sys.exit(1)

pycmd = sys.argv[1:]
print("Prefered encoding:{}".format(locale.getpreferredencoding()))
r = subprocess.run(pycmd, capture_output=True)
if r.returncode != 0:
    print("Error running {} with exit code {}.".format(
        pycmd,
        r.returncode
    ))
    sys.exit(1)

print("Program output {} bytes:".format(len(r.stdout)))
for b in r.stdout:
    print('{:02X} '.format(b), end='')
print('')
try:
    print('BIG5 output:{}'.format(r.stdout.decode('BIG5')))
except UnicodeDecodeError as e:
    print("BIG5 output err:{}".format(e.reason))
try:
    print('UTF-8 output:{}'.format(r.stdout.decode('UTF-8')))
except UnicodeDecodeError as e:
    print("UTF-8 output err:{}".format(e.reason))