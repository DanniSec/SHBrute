# SHBrute - Simple Http *form* Bruteforcer
Didn't want to use hydra so I made this little tool.
Using mechanize, argparse and rich (flashy colours WOOW)

Feel free to modify and redistribute this code.

## Basic usage
```
python SHBrute.py -t http://some.web.com/login -U users.txt  -P passwords.txt -f 0 -F Unauthorized -w 0 -uf username -pf password -v 
```
-t = target url to the form \
-U / -u = username wordlist or -u for single username \
-P / -p = password wordlist or -p for single password \
-f = if there is more then one form on site (0-n) \
-F = failed login response \
-w = time to wait after every attempt \
-v = verbose (shows failed tries) \
-uf = name of input box for username \
-pf = name of input box for password \


## Installation


Clone SHBrute
```
git clone https://github.com/SoudruhDanny/SHBrute
```
Install requirements
```
pip install -r requirements.txt
```
Finally run SHBrute
```
python SHBrute -h
```
```
usage: SHBrute.py [-h] [-t url] [-u name] [-U wordlist] [-p password] [-P wordlist] [-uf str] [-pf str] [-f num] [-w seconds] [-F str] [-v]

SHBrute - Simple Http *Form* Bruteforcer

options:
    -h, --help            show this help message and exit
    -t url, --target url  Whole url to the HTTP login form ex.
    "http://web.com/login"
    -u name, --user name  single username (For wordlist use -U)
    -U wordlist, --users wordlist
    wordlist option for username
    -p password, --password password
    single password (For wordlist use -P
    -P wordlist, --passwords wordlist
    wordlist option for password
    -uf str               login form name
    -pf str               password form name
    -f num, --form num    http form number (if there are multiple forms)
    -w seconds, --wait seconds
    wait time between requests
    -F str, --fail str    response with failed login
    -v, --verbose         verbose mode
```

<a href='https://ko-fi.com/DanniSec' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />
