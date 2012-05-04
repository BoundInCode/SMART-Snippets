import os
import fnmatch
import sublime

snippet_triggers = []
snip_files = {}

def init_snipfiles():
    pkg = sublime.packages_path()+'/SMART_Snippets/'
    for root, dirnames, filenames in os.walk(pkg):
        for filename in fnmatch.filter(filenames, '*.smart_snippet'):
            fn = os.path.join(root, filename)
            is_regex = 'n'  # n is no
            f = open(fn, 'r')
            for line in f:
                if line.startswith('###regex:'):
                    param, regex = line.split(":", 1)
                    if 'yes' in regex: 
                        is_regex = 'y'  # y is yes
                elif line.startswith('###trigger:'):
                    param, trig = line.split(":",1)
                    trigger = is_regex + trig.strip()
                    snippet_triggers.append(trigger)
                    snip_files[trigger] = fn
                    break
            f.close()