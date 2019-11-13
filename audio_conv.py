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

wej = input("Podaj format wejsciowy:> ")
wyj = input("Podaj format wyjsciowy:> ")

# wej = 'flac'
# wyj = 'mp3'

wej = wej.split(',')
print(wej)


def get_metadata(audio_files):
    metadata = []
    for file in audio_files:
        try:
            info = mediainfo(file).get('TAG', None)
            info = {k.upper(): v for k, v in info.items()}
        except Exception:

            decyzja = input(
                f"Czy artysta dla \"{file}\" to \"{metadata[-1]['ARTIST']}\" a album to \"{metadata[-1]['ALBUM']}\" (y/n):> ").upper()

            if decyzja == "Y" or decyzja == "" or decyzja == "T":
                info = {'ARTIST': metadata[-1]['ARTIST'], 'ALBUM': metadata[-1]['ALBUM']}
                if "DISC" in metadata[-1].keys():
                    decyzja2 = input(f"Czy dysk to {metadata[-1]['DISC']}:> ").upper()
                    if decyzja2 == "Y" or decyzja2 == "" or decyzja2 == "T":
                        info["DISC"] = metadata[-1]['DISC']
                    else:
                        info["DISC"] = input("Podaj numer dysku:> ")
                else:
                    pass
            else:
                artist = input("Podaj artyste:> ")
                album = input("Podaj album:> ")
                disc = input("Podaj numer dysku:> ")
                info = {"ARTIST": artist, "ALBUM": album, "DISC": disc}

        info['FILE'] = file
        print(info)
        metadata.append(info)
    print(f"Ilosc utworów: {len(metadata)}")
    return metadata


def make_dir(data):
    for meta in data:
        try:
            if "DISC" in meta.keys():
                export_dir_album = f"{export_dir}/{meta['ARTIST']}/{meta['ALBUM']}/disc{meta['DISC']}"
            else:
                export_dir_album = f"{export_dir}/{meta['ARTIST']}/{meta['ALBUM']}"
            os.makedirs(export_dir_album)
        except Exception:
            pass


def make_audio_files(meta):
    # for file in audio_files:
    filename = os.path.splitext(os.path.basename(meta['FILE']))[0]
    if "DISC" in meta.keys():
        export_dir_album = f"{export_dir}/{meta['ARTIST']}/{meta['ALBUM']}/disc{meta['DISC']}"
    else:
        export_dir_album = f"{export_dir}/{meta['ARTIST']}/{meta['ALBUM']}"
    mp3_filename = filename + f'.{wyj}'
    print(f'Start: {mp3_filename}')
    AudioSegment.from_file(meta['FILE']).export(export_dir_album + '/' + mp3_filename,
                                                format=wyj,
                                                tags={'artist': meta['ARTIST'], 'album': meta['ALBUM'],
                                                      'title': filename})
    return mp3_filename


for dirpath, dirnames, filenames in os.walk(os.getcwd() + '/Source'):
    os.chdir(dirpath)
    audio_files = []
    for w in wej:
        audio_files.extend(glob.glob(f'*.{w}'))
    if len(audio_files) > 0:
        print(audio_files)
        meta = get_metadata(audio_files)
        make_dir(meta)
        print(meta)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(make_audio_files, meta)
        for result in results:
            try:
                print(f'Koniec: {result}')
            except Exception as e:
                print(e)
