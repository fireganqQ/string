#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/-3.0.en.html.

print("StringSession oluşturucu")

print("t ==> Telethon (docs.telethon.dev)")

  # (c) https://t.me/TelethonChat/37677
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Lütfen API ID Girin: "))
API_HASH = input("Lütfen API HASH Girin: ")
with TelegramClient(
    StringSession(),
    APP_ID,
    API_HASH
) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ Bu StringSession, https://fireganqstring.fireganqq.repl.run/ kullanılarak oluşturuldu! ")
    print("StringSession Telegram Kaydedilmiş Mesajlar Bölümünüze Gönderildi")
