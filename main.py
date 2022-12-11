import shutil
from tinytag import TinyTag  # https://pypi.org/project/tinytag/
import os
import glob
import sys

MIN_ALBUM_SONGS = 6
FILE_EXTENTION = ['mp3', 'flac']


class Album:

    def __init__(self) -> None:
        self.name: str = None
        self.songs: list[str] = []
        self.dir: str = None

    def __repr__(self) -> str:
        s = self.name + '\n'
        for song in self.songs:
            s += '\t' + song + '\n'
        return s

    # update dir to a valid directory name
    def get_dir_name(self) -> None:
        dir = self.name
        dir = dir.replace(':', '_')
        for c in '\\/*?"<>|':
            dir = dir.replace(c, '')
        dir = dir.strip()
        self.dir = dir


if __name__ == '__main__':
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    else:
        os.chdir(input('path of music directory: '))

    file_list: list[str] = []
    for ext in FILE_EXTENTION:
        file_list += glob.glob('*.' + ext)

    album_map: dict[str, Album] = {}

    # update map/dict
    for f in file_list:
        tag = TinyTag.get(f)
        name = tag.album

        if name in album_map:
            album_map[name].songs.append(f)
        else:
            album = Album()
            album.name = name
            album.songs.append(f)
            album.get_dir_name()
            album_map[name] = album

    # create directories and move files
    count_mv = 0
    count_mkdir = 0

    for name in album_map:
        album = album_map[name]
        print(album)
        if len(album.songs) < MIN_ALBUM_SONGS:
            continue

        # move songs to the same directory
        # if they have the same formatted album path
        if not os.path.exists(album.dir):
            os.mkdir(album.dir)
            count_mkdir += 1
        for f in album.songs:
            shutil.move(f, album.dir)
            count_mv += 1

    # summarize
    print('===== Summarize =====')
    print('Number of created directories: ', count_mkdir)
    print('Number of files moved: ', count_mv)
