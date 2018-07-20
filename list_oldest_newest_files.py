# Script will locates the files and subdirectories inside the give directory,
# Sorts them, get the latest and older along side
# Lists all files including the path.
# Run the script by calling python {filename.py} -path {Directory path}
import os
import argparse

# Path of the directory to search must be passed as an Argument


def get_parser():
    from argparse import ArgumentParser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-path',
        '--path',
        required=True,
        help="Path of the directory that needs to be scanned for files"
    )
    return parser


# This method will scan the give directory and gets the path and name of file and skips the symbolic links

def scan_the_directory():
    args = get_parser().parse_args()
    for path, subdirs, files in os.walk(args.path, followlinks=False):
        # Skipping symbolic links in side subfolders
        if (os.path.islink(os.path.join(path))) == True:
            pass
        else:
            # Get the list of subdirectories inside the directory
            subdirectory = (os.path.join(path))
            print("\nSubdirectory:%s " % subdirectory)
            # Change directory to subdirectory
            os.chdir(subdirectory)
            # Sorts the files inside the directory
            files = sorted(os.listdir(os.getcwd()), key=os.path.getctime)

            # Checking if the sub folder is empty
            if len(files) == 0:
                print("No files inside the directory")
            else:
                oldest = files[0]
                newest = files[-1]
                # Condition where only onefile or same files create at same time
                if oldest == newest:
                    print("Only one file available : %s " %
                          os.path.join(path, oldest))
                # Else it prints the oldest and newest files inside the directory based on time created
                else:
                    print("Oldest file : %s " %
                          os.path.join(path, oldest), "\nNewest file : %s " % os.path.join(path, newest))
                    all_files_list = []
                    # Creating a list scan through all files inside the subdirectory
                    for filename in files:
                        all_files = os.path.join(path, filename)
                        all_files_list.append(all_files)
                    print("All files : %s" % '\n'.join(all_files_list))


if __name__ == '__main__':
    scan_the_directory()
