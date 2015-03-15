# fastest_ubuntu_mirror
Find the fastest Ubuntu mirror out of the ones in http://mirrors.ubuntu.com/mirrors.txt

```bash
pip install -r requirements.txt 
python fastest_mirror.py
```

```bash
1/67 0:00:00.320435 http://mirror.pnl.gov/ubuntu/
2/67 0:00:00.202138 http://mirror.math.ucdavis.edu/ubuntu/
...
66/67 0:00:00.255311 http://mirrors.arpnetworks.com/Ubuntu/
67/67 0:00:00.284102 http://archive.ubuntu.com/ubuntu/
-------------------------------------------------------------------------------
TOP 3
92206 http://ftp.usf.edu/pub/ubuntu/
104478 http://repo.atlantic.net/ubuntu/
123291 http://mirrors.advancedhosters.com/ubuntu/
-------------------------------------------------------------------------------
http://ftp.usf.edu/pub/ubuntu/
```
