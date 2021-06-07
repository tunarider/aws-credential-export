#!/usr/bin/env python3
import os
import configparser
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=str, default="default")
    parser.add_argument("--config", type=str, default="~/.aws")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(os.path.expanduser(os.path.join(args.config, "credentials")))

    for key in config[args.profile]:
        print("export {}={}".format(key.upper(), config[args.profile][key]))
