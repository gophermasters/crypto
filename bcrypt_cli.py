#!/usr/bin/env python3
#
# Reads a password from stdin and hashes it with bcrypt
#

import argparse
import sys
import bcrypt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--salt-rounds', '-r', help="Salt rounds", type=int, required=False, default=10)
    args = parser.parse_args()

    rounds = args.salt_rounds

    cleartext = sys.stdin.readline().strip()
    if len(cleartext) == 0:
        print("ERROR: cleartext is empty.")
        sys.exit(1)

    ciphertext = bcrypt.hashpw(cleartext.encode("utf-8"), bcrypt.gensalt(rounds=rounds)).decode("ascii")
    print(ciphertext)

if __name__ == '__main__':
    main()