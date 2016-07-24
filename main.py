# -*- coding: utf-8 -*-

import eyed3
import sys
import os
from os.path import dirname

log_file = ''
non_mp3 = 0
non_tag = 0
low_kbps = 0


def find_music(path):
    global non_mp3
    for root, dirs, files in os.walk(path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.mp3':
                yield os.path.join(root, filename)
            else:
                log_file.write('Non-MP3\t' + filename + '\n')
                non_mp3 += 1


def rename(mp3_path, mp3_eyed):
    new_name = dirname(mp3_path) + '/{0} - {1}.mp3'.format("%02d" % (mp3_eyed.tag.track_num[0],), mp3_eyed.tag.title)
    os.rename(mp3_path, new_name)


def analyze(mp3_path):
    global log_file, low_kbps, non_tag
    mp3_eyed = eyed3.load(mp3_path)
    if mp3_eyed.tag.title == '':
        log_file.write('Non-TAG\t' + mp3_path + '\n')
        non_tag += 1
    rename(mp3_path, mp3_eyed)
    if mp3_eyed.info.bit_rate[1] < 320:
        log_file.write(str(mp3_eyed.info.bit_rate[1]) + 'Kbps\t' + mp3_path + '\n')
        low_kbps += 1


def main():
    if len(sys.argv) != 2:
        print 'Usage: python main.py musicPath'
        exit(1);
    folder = sys.argv[1]
    global log_file
    count = 0
    log_file = open(folder + '/log.txt', 'w')
    print 'Directory:', folder
    for mp3_path in find_music(folder):
        analyze(mp3_path)
        count += 1
    print count, 'processed files'
    print non_tag, 'no metada'
    print non_mp3, 'no mp3'
    print low_kbps, 'low quality'
    print 'See', log_file.name

main()
