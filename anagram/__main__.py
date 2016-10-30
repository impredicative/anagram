#!/usr/bin/env python3.5
"""Find anagrams."""

import argparse
import sys

PROGRAM = 'anagram'


class ArgumentParser(argparse.ArgumentParser):
    """Parse command-line arguments."""

    def __init__(self):
        """Initialize parser with arguments."""
        super().__init__(prog=PROGRAM, description=__doc__, add_help=False)
        self._add_arguments()

    def _add_arguments(self):
        """Add arguments to parser."""
        add_arg = self.add_argument_group('Arguments').add_argument
        add_arg('-h', '--help', action='help',
                help='Show this help message and exit')
        add_arg('--word', required=True,
                help='Word, e.g. "empires"')
        add_arg('--file', default='words.txt', type=argparse.FileType('r'),
                help='Words file (default: "%(default)s")')

    def parse_args(self, args=None, namespace=None):
        """Parse and validate args.

        In case of a validation error, print the error and exit.
        """
        namespace = super().parse_args()
        if len(namespace.word) == 0:
            self.error('Word must not be empty.')
        return namespace


class AnagramFinder:
    def __init__(self, file):
        pass

    def find(self, word):
        return []


def main():
    """Parse arguments and run program."""
    try:
        namespace = ArgumentParser().parse_args()
        for anagram in AnagramFinder(namespace.file).find(namespace.word):
            print(anagram)
    except (Exception,  # pylint: disable=broad-except
            KeyboardInterrupt) as exc:
        sys.exit(exc)

if __name__ == '__main__':
    main()
