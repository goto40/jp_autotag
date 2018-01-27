from __future__ import print_function
import eyed3

def show_info(files):
    for file in files:
        f = eyed3.load(file)
        print("{}:".format(file))
        for a in dir(f.tag):
            print(" - {}: {}".format(a,f.tag.__getattribute__(a)))
    for file in files:
        f = eyed3.load(file)
        print("> {}".format(f.tag.title))


def adjust_titles(files, format, do_it):
    for file in files:
        f = eyed3.load(file)
        tag=f.tag
        new_title = eval(format)
        print("> {} -> {}".format(f.tag.title,new_title))
        if do_it:
            tag.title = new_title
            tag.save()

def autotag():
    import argparse
    cmd = r'"{:02d}-{}".format(tag.track_num[0],tag.title)'
    parser = argparse.ArgumentParser(description='generate code for the custom idl model.')
    parser.add_argument('files', type=str, nargs='+')
    parser.add_argument('--show-info', dest='show_info', default=False,
                        action='store_true', help='just shows the tag info (no change)')
    parser.add_argument('--adjust-title-format', dest='adjust_title_format', default=cmd, type=str,
                        help='command to replace title, use tag object as source (see show_info). Example: {}'.format(cmd))
    parser.add_argument('-r','--replace-title', dest='replace_title', default=False,
                        action='store_true', help='replace name')

    args = parser.parse_args()
    files = model_file=args.files

    if args.show_info:
        show_info(files)
    else:
        adjust_titles(files, args.adjust_title_format, args.replace_title)

if __name__ == "__main__":
    autotag()
