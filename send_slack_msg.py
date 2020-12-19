#!/usr/bin/env python3

import argparse
import slacker
import sys

from slacker import Slacker

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('token', help='Slack bot token')
    parser.add_argument('channel', help='channel to send message')
    parser.add_argument('message', help='message to send')

    args = parser.parse_args()

    s = slacker.Slacker(args.token)
    s.chat.post_message(channel=args.channel, text=args.message)

if __name__ == '__main__':
    main()
