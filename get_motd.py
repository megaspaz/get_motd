#!/usr/bin/env python
#
# Copyright 2006 megaspaz
# All Rights Reserved.
#
# Date: January 19, 2006
# Script Name: get_motd.py

"""Gets a message from /etc/motd_list and sets /etc/motd with this message.

Gets a list from /etc/motd_list and randomly chooses a message. /etc/motd is
overwritten with a new /etc/motd containing the randomly chosen message.

"""

__author__ = "megaspaz <megaspaz2k7<at>gmail.com>"

import random
import socket
import sys

# Constants:
_MOTD_LIST = '/etc/motd_list'
_MOTD_FILE = '/etc/motd'
_LINE_DELIMITER = '\n\n'


def main():
  file_list = ''
  try:
    # Get the list from /etc/motd_list.
    fd = open(_MOTD_LIST, 'r')
    file_list = fd.read().strip()
    fd.close()

    # We've got the file's contents. Split this by the delimiter.
    msg_list = file_list.split(_LINE_DELIMITER)
    # Get the hostname.
    this_host = socket.gethostname().strip()
    # Set the message. Get a random message from the message list.
    motd_greet = "Welcome To %s!" % this_host.upper()
    motd = "\n%s%s%s%s" % (motd_greet, _LINE_DELIMITER,
      msg_list[random.randrange(0, len(msg_list))].strip(),_LINE_DELIMITER)

    # Write this to file.
    fd = open(_MOTD_FILE, 'w')
    fd.write(motd)
    fd.close()

    return 0

  except(IOError, OSError, MemoryError), err:
    sys.stderr.write("%s\n" % err)
    return err.errno

if '__main__' == __name__:
  sys.exit(main())
