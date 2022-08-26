# batchmuxer
automate muxing of your video files

This script is for automating muxing of video and subtitle for series that you might want to upload. Script is interactive.

Requirements:

- Latest Python 3
- mkvmerge.exe

Usage:

Before running the script, edit the config.json file. It's pretty self-explanatory but here's the guide:
```
^ mkv is where you set the path for mkvmerge.exe - set it once and forget.
  make sure to put double-slash and that your mkvmerge.exe is in a directory with no space
^ extension is the file extension of the video. separate audio and video is not supported
^ audio_language is the 2 to 4 letter country code for the audio. multiple audio not supported
^ prefix is your release prefix. the format is SERIES.NAME.YEAR.SEASON.E - yes, you should put E on the last part
^ suffix is your release suffix. the format is RESOLUTION.SOURCE.AUDIO_CODEC.VIDEO_CODEC.GROUP_NAME
```
Prepare your video and subtitle files:
```
^ The format for video is VIDEOepisodenumber so sample is evil20 (meaning episode 20 of the series named evil)
^ The format for subtitle is VIDEOepisodenumber.subtitle_language_code.extension so sample is evil20.th.srt
  (meaning episode 20 of the series named evil. subtitle language is Thai and extension is srt)
```
For subtitle, only the following extensions are accepted: ass, ssa, vtt, srt

If you need to batch-rename your files to use for this script, good software to use is Bulk Rename Utility.


Run the script and provide the asked input from you. Feel free to modify based on your specific use case.

No support will be provided. Read how the script works, fork and improve.
