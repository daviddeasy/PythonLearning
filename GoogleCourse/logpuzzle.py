#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urlparse
# from copyspecial import maybe_create_dir
import copyspecial

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filepath):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    filename = os.path.basename(filepath)
    match_hostname = re.search(r'_(.+)$', filename)
    hostname = ''
    if match_hostname:
        hostname = match_hostname.group(1)
        # print 'hostname=' + str(hostname)
    else:
        print 'Error: not a valid log file name: ', filepath
        exit(1)

    with open(filepath, 'rU') as f:
        text = f.read()

    puzzle_file_matches = re.findall(r'GET\s+(\S*puzzle\S*)\s', text)
    # print puzzle_file_matches
    # print 'len(puzzle_file_matches)=' + str(len(puzzle_file_matches))

    puzzle_files = {}
    for puzzle_file in puzzle_file_matches:
        puzzle_files[puzzle_file] = True

    # print 'sorted(puzzle_files)=' + str(sorted(puzzle_files))
    # print 'len(puzzle_files)=' + str(len(puzzle_files))

    # ranked_names = []
    # for match_hostname in puzzle_file_matches:
    #     ranked_names.append((match_hostname[0], match_hostname[1], match_hostname[2]))
    # ranked_names = [(match_hostname[0], match_hostname[1], match_hostname[2]) for match_hostname in puzzle_file_matches]

    urls = ['http://%s:%s' % (hostname, f) for f in sorted(puzzle_files)]

    return urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """

    html_file_start = \
        '<!DOCTYPE html>\n' \
        '<html>\n' \
        '<body>\n'

    print 'html_file_start=' + str(html_file_start)

    html_file_end = \
        '</body>\n' \
        '</html>\n'

    i = 0
    filenames = []
    for url in img_urls:
        filename = 'img%.3d' % i
        filenames.append(filename)
        i += 1

        filepath = os.path.join(dest_dir, filename)
        # print 'SKIPPING URL DOWNLOADS'
        urllib.urlretrieve(url, filepath)
        print 'filepath=' + str(filepath)
        print 'url=' + str(url)

    # <img src="file.jpg">

    index_file = os.path.join(dest_dir, 'index.html')
    print 'index_file=' + str(index_file)
    f = open(index_file, 'w')
    f.write(html_file_start)
    for filename in filenames:
        f.write('<img src="%s">\n' % filename)
    f.write(html_file_end)


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        copyspecial.maybe_create_dir(todir)
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
