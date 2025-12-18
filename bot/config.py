from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = config("DEV", default=7465574522, cast=int)
    OWNER = config("OWNER", default="7465574522")

    FFMPEG = config(
        "FFMPEG",
        default="""
ffmpeg -i "{}" -vf "drawtext=text='For More Animes In Low MB, Check Out @Animes_Guy in Telegram':x='if(gte(t,240),w-(t-240)*60,NAN)':y=10:fontsize=24:fontcolor=white:enable='gte(t,240)':box=0" \
-c:v libx265 -map 0 -crf 29 -s 1920x1080 -c:a libopus -b:a 32k -preset superfast \
-x265-params pools=2:frame-threads=1:wpp=1:pmode=0:pme=0:no-sao=1:aq-mode=1:aq-strength=0.8:psy-rd=1.0:ref=3:bframes=4:keyint=240:min-keyint=24:rc-lookahead=10 \
-tune animation -pix_fmt yuv420p -c:s copy "{}"
        """.strip()
    )

    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config("THUMBNAIL", default="https://files.catbox.moe/6ntaju.png")

except Exception as e:
    print("Environment vars Missing or Invalid")
    print("Something went wrong:", str(e))
    exit(1)
