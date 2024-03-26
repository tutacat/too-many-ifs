#Python generator
import subprocess;

filename = b'iseven_o.py'

subprocess.run(b"touch",filename);

with open(filename,'wb') as file:
    maxi = 2**16
    out = b"import sys.argv\n"
    out += b"m="+hex(maxi).encode()+b"\n"
    out += b"sys.argv+=(0,)\n"
    out += b"x=int(float(sys.argv[1]))\n"
    out += b"if x<0 or x>=m:raise ValueError('Your ints are too powerful ('+str(m-1)+')!')\n"
    i=0;
    for i in range(0,maxi,2):
        out += b"if x==" + hex(i).encode() + b":print(0)\n";
        if(len(output)>=0x1000): # 4KB
            file.write(output[:0x1000])
            output = output[0x1000:]

    out += (b"exit(1)\n")
    file.write(output)

os.chmod(filename,os.stat(filename).st_mode|0o1)
