import argparse
from core.runner import run_modules

parser = argparse.ArgumentParser(description="WebHunter v1.4 - Bug Bounty Automation Tool")
parser.add_argument('--target', required=True, help='Target domain')
parser.add_argument('--modules', help='Modules to run (comma-separated)', default='full')
parser.add_argument('--profile', help='Recon profile: full, web3, passive, custom', default='full')

args = parser.parse_args()
run_modules(args.target, args.modules, args.profile)
