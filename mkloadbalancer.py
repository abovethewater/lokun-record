# -*- coding: utf-8 -*-
import sys

usage = """Inserts a new server to the loadbalancer table
Uses the db specified in config.py. 

Usage:
    ./mkloadbalancer.py name ip

Example:
    $ python mkapikey.py vpn3.beta 1.2.3.4
    $
"""


def main():
        if len(sys.argv) =! 3:
                print usage()
                sys.exit(1)

        name = sys.argv[1]
	import model
        model.DB.get().lb_add(sys.argv[1], sys.argv[2])
	exit(0)


if __name__ == '__main__':
	main()