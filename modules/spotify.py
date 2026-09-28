import aiohttp
import os
import re
from PyroUbot import *

__MODULE__ = "sᴘᴏᴛɪғʏ"
__HELP__ = """
<blockquote><b>Bantuan Spotify</b>

Perintah:
<code>{0}spotify</code> judul lagu
→ Download lagu dari Spotify</blockquote>
"""

def clean_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "", text)

@PY.UBOT("spotify")
@PY.TOP_CMD
async def spotify_handler(client, message):
    text = message.text.split(None, 1)
    if len(text) < 2:
        return await message.reply(
            "<blockquote><b>📖 Cara pakai:</b>\n"
            "<code>spotify judul lagu</code></blockquote>"
        )

    query = text[1]
    msg = await message.reply("<blockquote><b>🔍 Mencari lagu...</b></blockquote>")

    try:
        async with aiohttp.ClientSession() as session:

            # SEARCH
            search_url = (
                "https://api.botcahx.eu.org/api/search/spotify"
                f"?query={query}&apikey=_@moire_mor"
            )
            async with session.get(search_url, timeout=20) as r:
                data = await r.json()

            if not data.get("status"):
                return await msg.edit("<blockquote><b>❌ Lagu tidak ditemukan</b></blockquote>")

            result = data["result"]["data"][0]
            track_url = result["url"]

            await msg.edit("<blockquote><b>📥 Mengunduh audio...</b></blockquote>")

            # DOWNLOAD INFO
            dl_url = (
                "https://api.botcahx.eu.org/api/download/spotify"
                f"?url={track_url}&apikey=_@moire_mor"
            )
            async with session.get(dl_url, timeout=20) as r:
                dl = await r.json()

            if not dl.get("status"):
                return await msg.edit("<blockquote><b>❌ Gagal download</b></blockquote>")

            res = dl["result"]["data"]
            title = clean_filename(res["title"])
            filename = f"{title}.mp3"

            # STREAM DOWNLOAD (anti lag)
            async with session.get(res["url"]) as audio:
                with open(filename, "wb") as f:
                    async for chunk in audio.content.iter_chunked(1024):
                        f.write(chunk)

        await client.send_audio(
            message.chat.id,
            audio=filename,
            caption=(
                "<blockquote><b>🎵 SPOTIFY DOWNLOADER</b>\n\n"
                f"<b>Judul:</b> <code>{res['title']}</code>\n"
                f"<b>Artis:</b> <code>{res['artist']['name']}</code>\n"
                f"<b>Durasi:</b> <code>{res['duration']}</code></blockquote>"
            ),
        )

        await msg.delete()
        os.remove(filename)

    except Exception as e:
        await msg.edit(
            "<blockquote><b>⚠️ Error:</b>\n"
            f"<code>{e}</code></blockquote>"
        )
            