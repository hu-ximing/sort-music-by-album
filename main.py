from tinytag import TinyTag
import os
import sys

MIN_ALBUM_FILES = 3
AUDIO_EXTENTIONS = ('mp3', 'flac')


# convert string to a valid directory name
def convert_to_valid_dirname(s: str):
    for c in ':\\/*?"<>|':
        s = s.replace(c, '_')
    return s.strip()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        music_dir = sys.argv[1]
    else:
        print('ERROR: Please specify the directory in the argument.')
        exit()

    album_files: dict[str, list[str]] = {}
    count_skip = 0
    count_mv = 0
    count_mkdir = 0

    # Iterate over the files in the directory
    for file in os.listdir(music_dir):
        if not file.endswith(AUDIO_EXTENTIONS):
            continue

        # Read the metadata from the file
        metadata = TinyTag.get(os.path.join(music_dir, file))

        # Get the album from metadata
        album = metadata.album

        # Keep track of which files are in each album
        if album not in album_files:
            album_files[album] = []
        album_files[album].append(file)

    for album, files in album_files.items():
        if len(files) < MIN_ALBUM_FILES:
            count_skip += len(files)
            continue

        # Create the directory for the album, if it doesn't already exist
        album_dir = os.path.join(music_dir, convert_to_valid_dirname(album))
        if not os.path.exists(album_dir):
            os.makedirs(album_dir)
            count_mkdir += 1

        # Move the file to the album directory
        for file in files:
            os.rename(os.path.join(music_dir, file),
                      os.path.join(album_dir, file))
            count_mv += 1

    # summarize
    print('===== summarize =====')
    print('skipped files:', count_skip)
    print('created directories:', count_mkdir)
    print('moved files:', count_mv)
