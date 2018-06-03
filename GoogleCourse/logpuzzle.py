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
from copyspecial import maybe_create_dir

HTML_FILE_END = '</body>\n' \
                '</html>\n'

HTML_FILE_START = '<!DOCTYPE html>\n' \
                  '<html>\n' \
                  '<body>\n'

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" 
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(logfile):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    hostname = extract_hostname_from(logfile)
    if not hostname:
        print 'Error: not a valid log file name: ', logfile
        exit(1)

    puzzle_files = extract_image_filenames_from_log(logfile)
    urls = ['http://%s:%s' % (hostname, f) for f in sorted(puzzle_files, key=url_sort_key)]
    return urls


def extract_hostname_from(filepath):
    # Extract web hostname from log file name - it is the last part of the filename, after _
    filename = os.path.basename(filepath)
    match_hostname = re.search(r'_(.+)$', filename)
    hostname = ''
    if match_hostname:
        hostname = match_hostname.group(1)
    return hostname


def extract_image_filenames_from_log(logfile):
    with open(logfile, 'rU') as f:
        puzzle_file_matches = re.findall(r'GET\s+(\S*puzzle\S*)\s', f.read())
    puzzle_files = set(puzzle_file_matches)
    return puzzle_files


def url_sort_key(filename):
    """Sort by the last word in filename (YYY) if like -XXX-YYY.jpg, else sort by filename"""
    match = re.search(r'-\w+-(\w+).jpg', filename)
    if match:
        return match.group(1)
    else:
        return filename


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    filenames = generate_image_filenames(len(img_urls))
    download_images_urls(dest_dir, filenames, img_urls)
    generate_index_file(dest_dir, filenames)


def generate_image_filenames(num_urls):
    filenames = []
    for i in xrange(num_urls):
        filename = 'img%d' % i
        print "filename=" + filename
        filenames.append(filename)
    return filenames


def download_images_urls(dest_dir, filenames, img_urls):
    for i in xrange(len(img_urls)):
        filepath = os.path.join(dest_dir, filenames[i])
        print "filepath=" + filepath
        # print 'SKIPPING URL DOWNLOADS'
        urllib.urlretrieve(img_urls[i], filepath)


def generate_index_file(dest_dir, filenames):
    index_file = os.path.join(dest_dir, 'index.html')
    print 'index_file=' + str(index_file)
    f = open(index_file, 'w')
    f.write(HTML_FILE_START)
    for filename in filenames:
        f.write('<img src="%s">' % filename)
    f.write(HTML_FILE_END)


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
        maybe_create_dir(todir)
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
