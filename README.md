# Commenting on Telegram
This program can make the first comment in Telegram channels.

## install required libraries

First, install the required Python libraries.

```
pip3 install -U pyrogram tgcrypto
```

## Creating your Telegram Application to get api_hash & and api_id

After installing the library, use this [**address**](https://my.telegram.org/auth/) to set up api_hash and api_id in the program.
After logging in to the site, you should put the api_id and api_hash in **lines 6 and 7** of the program file.
[**for more help**](https://core.telegram.org/api/obtaining_api_id) .

## Find channel IDs

We use [**this robot**](https://t.me/chatIDrobot) to find the IDs of the channels to which we intend to send the first comment. 
Just forward a message from the target channel to the bot to find the channel ID. Copy the ID and paste it in **line 21**. 

## 

Now just run the file and always be the first comment. enjoy:) <3




