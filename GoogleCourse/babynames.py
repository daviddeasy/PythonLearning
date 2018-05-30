#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

REGEX_YEAR          = r'Popularity in (\d\d\d\d)'
REGEX_RANKED_NAMES  = r'<td>(\d+)<\/td><td>([A-z\-]+)<\/td><td>([A-z\-]+)<\/td>'


"""Baby Names exercise

Define the extract_names() function below and change main() to call it.

For writing regex, it's nice to include a copy of the target text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def main():

    filenames, summary_file_mode, summary_mode = parse_args()

    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    if summary_file_mode:
        print 'Generating a summary file (XXX.summary) for each input file'

    for filename in filenames:
        infos = extract_names(filename)
        if summary_file_mode:
            write_summary_file(filename, infos)
        elif summary_mode:
            print_summary(infos)
        else:
            print_details(infos)


def parse_args():
    # This command-line parsing code is provided.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    # Notice the summary flag and remove it from args if it is present.
    summary_flag = False
    summary_file_flag = False
    if args:
        if args[0] == '--summary':
            summary_flag = True
            del args[0]
        elif args[0] == '--summaryfile':
            summary_file_flag = True
            del args[0]

    check_args(args)

    return args, summary_file_flag, summary_flag


def check_args(args):
    if not args:
        print 'usage: [--summaryfile | --summary] file [file ...]'
        sys.exit(1)


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'rU') as f:
        text = f.read()

    result = [extract_year(text)]

    ranks_and_names = extract_ranked_names(text)
    ranked_names = rank_names(ranks_and_names)

    for name in sorted(ranked_names):
        result.append('%s %s' % (name, ranked_names[name]))

    return result


def extract_year(text):
    """ Extract the year """
    match = re.search(REGEX_YEAR, text)
    if not match:
        print 'Year not found'
        exit(2)
    return match.group(1)


def extract_ranked_names(text):
    """ Extract a list of tuples (rank, boyname, girlname)"""

    matches = re.findall(REGEX_RANKED_NAMES, text)
    # print matches

    # ranked_names = []
    # for match in matches:
    #     ranked_names.append((match[0], match[1], match[2]))
    ranked_names = [(match[0], match[1], match[2]) for match in matches]

    # print ranked_names
    return ranked_names


def rank_names(ranks_and_names):
    ranked_names = {}
    for (rank, boy_name, girl_name) in ranks_and_names:
        add_rank_and_name(boy_name, rank, ranked_names)
        add_rank_and_name(girl_name, rank, ranked_names)
    return ranked_names


def add_rank_and_name(name, rank, ranked_names):
    # Could just use the first rank for each name since we know this will be called in order of increasing rank.
    # But comparing the new rank vs. stored rank keeps this method more general / less brittle.
    if name in ranked_names:
        # print 'name: ', name, 'old rank: ', ranked_names[name], 'new rank:', rank, \
        #     '->', min(name, ranked_names[name])
        ranked_names[name] = min(rank, ranked_names[name])
    else:
        ranked_names[name] = rank


def write_summary_file(filename, infos):
    with open(filename + '.summary', 'w') as f:
        f.write('\n'.join(infos))


def print_details(infos):
    for item in infos:
        print item


def print_summary(infos):
    for item in infos[0:11]:
        print item
    print '...'
    for item in infos[-10:]:
        print item


if __name__ == '__main__':
    main()
