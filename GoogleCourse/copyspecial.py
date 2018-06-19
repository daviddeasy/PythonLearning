#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

REGEX_SPECIAL_FILES = r'__[A-z\d]+__'

"""Copy Special exercise
"""


def main():
    from_dirs, todir, tozip = parse_args()

    if todir:
        copy_special_files(from_dirs, todir)

    elif tozip:
        zip_special_files(from_dirs, tozip)

    else:
        print_special_files_in(from_dirs)


def parse_args():
    # Make a list of command line arguments, omitting the [0] element which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    tozip = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    elif args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
    if len(args) == 0:
        print 'ERROR: Must specify at least one directory to copy from'
        sys.exit(1)

    return args, todir, tozip


def copy_special_files(from_dirs, todir):
    maybe_create_dir(todir)
    special_paths = find_special_files_in(from_dirs)
    error_exit_if_dup_filename(special_paths)

    for file_path in special_paths:
        print 'Copying', file_path, 'to', todir
        shutil.copy(file_path, todir)


def zip_special_files(from_dirs, tozip):
    special_paths = find_special_files_in(from_dirs)
    error_exit_if_dup_filename(special_paths)

    zip_cmd = 'zip -j %s %s' % (tozip, (' '.join(special_paths)))
    # print 'ABOUT TO RUN:', zip_cmd
    (status, output) = commands.getstatusoutput(zip_cmd)
    if status:
        print output
        sys.exit(4)


def print_special_files_in(dirs):
    special_paths = find_special_files_in(dirs)
    error_exit_if_dup_filename(special_paths)

    for path in special_paths:
        print path


def error_exit_if_dup_filename(special_paths):
    dup = check_for_repeat_filename(special_paths)
    if dup:
        print 'ERROR: Special filenames are not unique.', dup
        sys.exit(3)


def check_for_repeat_filename(file_paths):
    """ Check that base filenames are unique.

    Return empty string if all unique, else a string describing the first clash.
    """
    dict_filenames = {}

    for path in file_paths:
        filename = os.path.basename(path)
        # print 'filename:', filename
        if filename in dict_filenames:
            return 'CLASH: %s AND: %s' % (dict_filenames[filename], path)
        else:
            dict_filenames[filename] = path
    return ''


def find_special_files_in(dirs):

    specials = []
    try:
        for directory in dirs:
            for filename in os.listdir(directory):
                if re.search(REGEX_SPECIAL_FILES, filename):
                    specials.append(os.path.join(directory, filename))

    except (IOError, OSError) as e:
        print 'Error ({0}): {1}'.format(e.errno, e.strerror)
        exit(2)

    except:
        print 'Error listing directories:', sys.exc_info()[0]
        raise

    return specials


def maybe_create_dir(directory):
    if not os.path.exists(directory):
        print "MAKING DIRECTORY: ", directory
        try:
            os.makedirs(directory)
        except OSError as e:
            print 'Error ({0}): {1}'.format(e.errno, e.strerror)
            sys.exit(4)


if __name__ == "__main__":
    main()
