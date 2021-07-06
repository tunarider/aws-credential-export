#!/usr/bin/env python3

import os
import configparser
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=str, default="default")
    parser.add_argument("--config", type=str, default="~/.aws")
    args = parser.parse_args()

    credentials = configparser.ConfigParser()
    credentials.read(os.path.expanduser(os.path.join(args.config, "credentials")))
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(os.path.join(args.config, "config")))

    for key in credentials[args.profile]:
        print("export {}={}".format(key.upper(), credentials[args.profile][key]))
    for key in config["profile {}".format(args.profile)]:
        print("export AWS_DEFAULT_{}={}".format(key.upper(), config["profile {}".format(args.profile)][key]))
