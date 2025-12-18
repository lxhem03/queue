#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = "23340285"
    API_HASH = "ab18f905cb5f4a75d41bb48d20acfa50"
    BOT_TOKEN = "7567477886:AAH_uOFdmt77spRT7S93oelmJgLnUKScEYs"
    DEV = 7465574522
    OWNER = "7465574522"
    FFMPEG = """
    ffmpeg -i "{}" -vf "drawtext=text='For More Animes In Low MB, Check Out @Animes_Guy in Telegram':x='if(gte(t,240),w-(t-240)*60,NAN)':y=10:fontsize=24:fontcolor=white:enable='gte(t,240)':box=0" -c:v libx265 -crf 29 -s 1920x1080 -c:a libopus -b:a 32k -preset superfast -x265-params pools=2:frame-threads=1:wpp=1:pmode=0:pme=0:no-sao=1:aq-mode=1:aq-strength=0.8:psy-rd=1.0:ref=3:bframes=4:keyint=240:min-keyint=24:rc-lookahead=10 -tune animation -pix_fmt yuv420p -map 0 -c:s copy "{}"
    """
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://files.catbox.moe/6ntaju.png"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
