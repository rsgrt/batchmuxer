
import os
import json
import lang_list

cd = os.getcwd()
file = open('config.json')
config = json.loads(file.read())
mkvmerge = config['mkv']
ext = config['extension']
audio_lang = config['audio_language']
prefix = config['prefix']
suffix = config['suffix']

print(" \n"
      "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n"
      "     rsg batch-muxer via mkvmerge   \n"
      "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

input_file = input('\nfile name of video w/o extension: ')
ep_start = input("episode number start: ")
ep_end = input("episode number end:  ")
ep_temp = int(ep_end) + 1

def mux(e):
    mux_prep = []
    sub_count = []
    sub_ext_list = ['ass', 'srt', 'vtt', 'ssa']

    for lang in lang_list.mkvtoolnix_languages:
        if audio_lang in lang.lower().split('|')[1:]:
            mux_prep.insert(0, f'''--language 1:{audio_lang} --track-name 0:{lang.split('|')[0]} ( {cd}\\{input_file}{e}{ext} ) ''')
        
        for sub in os.listdir(cd):
            single_ep = f"{input_file.split('.')[0]}{e}"
            if sub.split('.')[-1].lower() in sub_ext_list and single_ep in sub.lower().strip().split('.') and sub.lower().split('.')[-2] in lang.lower().split('|')[1:]:
                sub_count.append(sub)
                mux_prep.append(f'''--language 0:{sub.split('.')[-2]} --track-name 0:{lang.split('|')[0]} ( {cd}\{sub} ) ''')

    track_order = [f'{item}:0,' for item in range(0, len(sub_count)+1)]

    if e <= 9:
        os.system(f'''{mkvmerge} --ui-language en --output {cd}\\{prefix}0{e}.{suffix}.mkv --language 0:und {"".join(mux_prep)} --track-order {"".join(track_order).rstrip(',')}''')
    elif e >= 100:
        os.system(f'''{mkvmerge} --ui-language en --output {cd}\\{prefix}00{e}.{suffix}.mkv --language 0:und {"".join(mux_prep)} --track-order {"".join(track_order).rstrip(',')}''')
    elif e >= 10:
        os.system(f'''{mkvmerge} --ui-language en --output {cd}\\{prefix}{e}.{suffix}.mkv --language 0:und {"".join(mux_prep)} --track-order {"".join(track_order).rstrip(',')}''') 


filelist = []

for path, subdirs, files in os.walk(cd):
    print("Scanning and listing files..")
    for filename in files:
        filelist.append(filename)

for e in range(int(ep_start), ep_temp):
    mux(e)