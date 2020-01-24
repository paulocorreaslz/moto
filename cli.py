import argparse
import traceback
import sys
import os

import asyncio
import testrunner


def get_args():
    parser = argparse.ArgumentParser(
        description='Runs a checkup test based on your environment',
        prog='status_cli')

    parser.add_argument('--service-file', type=str, default='services.yml',
                        help='Which services file to use. Default: "services.yml"')
    parser.add_argument('--hosts-file', type=str, default='hosts.yml',
                        help='Which host file to use. Default: "hosts.yml"')

    args = parser.parse_args()

    return args


def main():
    loop = asyncio.get_event_loop()
    args = get_args()
    loop.run_until_complete(testrunner.run_all_tests(hosts_filepath=args.hosts_file,
                                                     services_filepath=args.service_file))


if __name__ == '__main__':
    main()
