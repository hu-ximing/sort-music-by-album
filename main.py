from tinytag import TinyTag
import os
import sys

MIN_ALBUM_FILES = 3
AUDIO_EXTENTIONS = ('mp3', 'flac')


# convert string to a valid directory name
def convert_to_valid_dirname(s: str):
    for c in ':\\/*?"<>|':
        s = s.replace(c, '_')
    s.strip()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        music_dir = sys.argv[1]
    else:
        print('ERROR: Please specify the directory in the argument.')
        exit()

    album_files: dict[str, list[str]] = {}
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
            print('Skipping album "%s",' % album)
            print('because it has less than %d files. count = %d' %
                  (MIN_ALBUM_FILES, len(files)))
            print()
            continue

        # Create the directory for the album, if it doesn't already exist
        album_dir = os.path.join(music_dir, convert_to_valid_dirname(album))
        if not os.path.exists(album_dir):
            print('Creating directory: "%s"' % album_dir)
            os.makedirs(album_dir)
            count_mkdir += 1

        # Move the file to the album directory
        for file in files:
            print('Moving file "%s" to directory "%s"' % (file, album_dir))
            os.rename(os.path.join(music_dir, file),
                      os.path.join(album_dir, file))
            count_mv += 1

    # summarize
    print('===== Summarize =====')
    print('Number of created directories: %d' % count_mkdir)
    print('Number of files moved: %d' % count_mv)
