#!/usr/bin/python

# uh, yeah, a json pretty print/colorizer. json
# and pygments do all the work, this just stitches
# both together

import sys
import json
import fileinput
# http://pygments.org/  for color
import pygments
import pygments.formatters
import pygments.lexers
import pygments.styles

def main():
    json_buf = ""
    for line in fileinput.input():
        json_buf += line

    json_string = json.dumps(json.loads(json_buf), indent=4, sort_keys=True)

    lexer = pygments.lexers.get_lexer_by_name('json')
    style = pygments.styles.get_style_by_name('monokai')
    formatter = pygments.formatters.get_formatter_by_name('terminal256', style=style)

    color_json_string = pygments.highlight(json_string, lexer, formatter)
    print color_json_string

if __name__ == "__main__":
    main()
