class Translation(object):

    ERROR = "<b>ERROR :</b> {}\n\nSent This Code To @DevsChats"

    START_TEXT = """**Hi {},**
I'm a **URL Uploader Bot!**
Just send me any Direct download link and I'll give you the file!

**/help for more details!**"""
.   ABOUT_TEXT = """**📰 About Me**

**Language:** Python 3
**Framework:** Pyrogram
**Channel:** @MyownBots
**Group:** @DevsChats
**Hosted On:** Heroku

Thanks For Using This Bot🤗"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Downloading Please Wait..."
    UPLOAD_START = "Uploading Please Wait..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using Me\n\n<b>Join : @MyOwnBots</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """<b>How to Use Me? Follow These steps!</b>

<b>Steps:</b>
<b>1.</b> Send url (example.domain/File.mp4 | New Filename.mp4).
<b>2.</b> Send Image As Custom Thumbnail (Optional).
<b>3.</b> Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @DevsChats"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    ERROR_YTDLP = "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."
