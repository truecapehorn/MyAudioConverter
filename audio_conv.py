import os
import glob
from pydub import AudioSegment
from pydub.utils import mediainfo
import concurrent.futures

try:
    os.mkdir('Export')
    os.mkdir('Source')
except Exception:
    pass

export_dir = os.getcwd() + '/Export'

wej = input("Podaj format wejsciowy: ")
wyj = input("Podaj format wyjsciowy: ")

wej= wej.split(',')
print(wej)

def make_dir(audio_files):
    global export_dir_album, artist, album
    for file in audio_files:

        try:
            info = mediainfo(file).get('TAG', None)
            # print(info)
            if 'ARTIST' in info.keys():
                artist, album = info['ARTIST'], info['ALBUM']
            elif 'artist' in info.keys():
                artist, album = info['artist'], info['album']
            else:
                artist, album = "Brak", "Brak"
        except Exception:
            print(f'Folder: {os.getcwd()}; Plik: {file}')
            artist = input("Podaj artyste: ")
            album = input("Podaj album: ")
    try:
        export_dir_album = f'{export_dir}/{artist}/{album}'
        os.makedirs(export_dir_album)
    except Exception:
        pass
    print(export_dir_album)
    return export_dir_album, artist, album


def make_audio_files(file):
    # for file in audio_files:
    filename = os.path.splitext(os.path.basename(file))[0]
    mp3_filename = filename + f'.{wyj}'
    print(f'Start: {mp3_filename}')
    AudioSegment.from_file(file).export(export_dir_album + '/' + mp3_filename,
                                        format=wyj,
                                        tags={'artist': artist, 'album': album, 'title': filename})
    return mp3_filename


for dirpath, dirnames, filenames in os.walk(os.getcwd() + '/Source'):
    os.chdir(dirpath)
    for w in wej:
        audio_files = glob.glob(f'*.{w}')
        if len(audio_files) > 0:
            # print(audio_files)
            try:
                export_dir_album, artist, album = make_dir(audio_files)
            except Exception as e:
                print(f'Problem w {dirpath}')
                exit(1)

            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = executor.map(make_audio_files, audio_files)
            for result in results:
                print(f'Koniec: {result}')
