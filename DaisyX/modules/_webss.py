from DaisyX.pyroplugs.inlinehelper import app, app2
from DaisyX.pyroplugs.errors import capture_err
from DaisyX.pyroplugs.fetch import fetch
from Python_ARQ import ARQ
from pyrogram import filters
import time

SUDOERS = OWNER_ID
ARQ_API = "http://35.240.133.234:8000"
arq = ARQ(ARQ_API)



__MODULE__ = "WebSS"
__HELP__ = "/webss | .webss [URL] - Take A Screenshot Of A Webpage"


@app.on_message(filters.command("webss") & filters.user(SUDOERS))
@app2.on_message(filters.command("webss", prefixes=["."]) & filters.user(SUDOERS))
@capture_err
async def take_ss(_, message):
    if len(message.command) != 2:
        await message.reply_text("Give A Url To Fetch Screenshot.")
        return
    url = message.text.split(None, 1)[1]
    start_time = time.time()
    m = await message.reply_text("**Taking Screenshot**")
    screenshot = await fetch(f"https://patheticprogrammers.cf/ss?site={url}")
    await m.edit("**Uploading**")
    end_time = time.time()
    await app.send_photo(
            message.chat.id,
            photo=screenshot['url'],
            caption=(f"{url}\n__Took {round(end_time - start_time)} Seconds.__")
            )
    await m.delete()
