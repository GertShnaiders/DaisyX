from DaisyX.pyroplugs.inlinehelper import app
from DaisyX.pyroplugs.errors import capture_err
from DaisyX.pyroplugs.fetch import fetch
from pyrogram import filters
import time


__mod_name__ = "WebSS"
__help__ = "/webss | .webss [URL] - Take A Screenshot Of A Webpage"


@app.on_message(filters.command("webss"))
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
