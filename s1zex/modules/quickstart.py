# ©️ Dan Gazizullin, 2021-2023
# This file is a part of s1zex Userbot
# 🌐 https://github.com/s1zexxx/userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# s1zex Team modifided s1zex files for s1zex
# 🌐 https://github.com/s1zexxx/userbot

import logging
import os
from random import choice

from .. import loader, translations, utils
from ..inline.types import BotInlineCall

logger = logging.getLogger(__name__)

imgs = [
    "https://i.gifer.com/Erie.gif",
    "https://i.gifer.com/QD5k.gif",
    "https://i.gifer.com/ZAAd.gif",
    "https://i.gifer.com/KmhC.gif",
]


@loader.tds
class QuickstartMod(loader.Module):
    """Notifies user about userbot installation"""

    strings = {
        "name": "Quickstart",
        "base": """👋🏻 <b>Hi!</b> I am a <B> inline-bot s1zex</B>, then let's go through a little training and configure s1zex for your needs

🤙🏻 <b>We advise you to join </b><a href="https://t.me/s1zexzxc "><b>our chat!</b></a><b> There you can find help if you don't understand something or if there are problems

</b> ⚡️ <b>You can search for interesting modules using </b>@s1zex_bot<b>, use it as a built-in installation on the required module.
</b> 💥 <i>You can find channels of confirmed developers can be found </i><a href="https://t.me/s1zexbee "><I> am here

</i></a> 🎯 <b>A brief guide</b>:

<i> 🔸 In order to find out the modules installed on you, use .mods
🔹 To install the module from the file, use </i> <code>.lm</code><i> (</i><code>.loadmod</code><i>) and to delete </i>.unloadmod
<i> 🔺 More usage guides can be found in the chat </i><a href="https://t.me/s1zexbee ">s1zex

</a><i> 🤝 <b>s1zex</b> is based on <b>s1zex</b>, therefore supports modules from <b>s1zex</b>, <b>FTG</b>, <b>DragonUB</b>, <b>GeekTG</b> and their own.</i>""",
        "railway": (
            "🚂 <b>Your userbot is installed on Railway</b>. This platform has only"
            " <b>500 free hours per month</b>. Once this limit is reached, your"
            " <b>s1zex will be frozen</b>. Next month <b>you will need to go to"
            " https://railway.app and restart it</b>."
        ),
        "language_saved": "🇬🇧 Language saved!",
        "language": "🇬🇧 English",
        "btn_support": "🥀 s1zex Chat",
    }

    strings_ru = {
        "base": """👋🏻 <b>Привет!</b> Я являюсь<b> Inline-ботом s1zex</b>, давай пройдем небольшое обучение и настроим s1zex под твои нужды 

🤙🏻 <b>Советуем вступить в </b><a href="https://t.me/s1zexzxc"><b>наш чат!</b></a><b> Там вы сможете найти помощь если чего то не поймете или если будут проблемы

</b>⚡️ <b>Искать интересные модули можно с помощью </b>@hikkamods_bot<b>, используйте его как Inline или как обычного бота и для установки нажмите ⛩ Install на требуемом модуле. 
</b>💥 <i>Вы можете найти каналы подтверждённых разработчиков можно найти </i><a href="https://t.me/s1zexbee "><i>тут

</i></a>🎯 <b>Краткий гайд</b>:

<i>🔸 Для того чтобы узнать модули установленные у вас используй .mods
🔹 Для установки модуля с файла используй</i> <code>.lm</code><i> (</i><code>.loadmod</code><i>) а для удаления </i>.unloadmod
<i>🔺 Больше гайдов по использованию можете найти в чате </i><a href="https://t.me/s1zexzxc">s1zex

</a><i>🤝 <b>s1zex</b> основан на <b>s1zex</b>, поэтому поддерживает модули <b>s1zex</b>, <b>FTG</b>, <b>DragonUB</b> и <b>GeekTG</b> и свои собственные.</i>
""",
        "railway": (
            "🚂 <b>Твой юзербот установлен на Railway</b>. На этой платформе ты"
            " получаешь только <b>500 бесплатных часов в месяц</b>. Когда лимит будет"
            " достигнет, твой <b>юзербот будет заморожен</b>. В следующем месяце <b>ты"
            " должен будешь перейти на https://railway.app и перезапустить его</b>."
        ),
        "language_saved": "🇷🇺 Язык сохранен!",
        "language": "🇷🇺 Русский",
        "btn_support": "🥀 Чат s1zex",
    }

    async def client_ready(self):
        if self.get("disable_quickstart"):
            raise loader.SelfUnload

        self.mark = (
            lambda: [
                [
                    {
                        "text": self.strings("btn_support"),
                        "url": "https://t.me/s1zexzxc",
                    }
                ],
            ]
            + [
                [
                    {
                        "text": "я",
                        "url": "https://t.me/s1zex",
                    },
                    {
                        "text": "канал",
                        "url": "https://t.me/s1zexbee",
                    },
                ]
            ]
            + utils.chunks(
                [
                    {
                        "text": (
                            getattr(self, f"strings_{lang}")
                            if lang != "en"
                            else self.strings._base_strings
                        )["language"],
                        "callback": self._change_lang,
                        "args": (lang,),
                    }
                    for lang in [
                        "en",
                        "ru",
                    ]
                ],
                2,
            )
        )

        self.text = lambda: self.strings("base") + (
            self.strings("railway") if "RAILWAY" in os.environ else ""
        )

        await self.inline.bot.send_animation(self._client.tg_id, animation=choice(imgs))
        await self.inline.bot.send_message(
            self._client.tg_id,
            self.text(),
            reply_markup=self.inline.generate_markup(self.mark()),
            disable_web_page_preview=True,
        )

        self.set("disable_quickstart", True)

    async def _change_lang(self, call: BotInlineCall, lang: str):
        self._db.set(translations.__name__, "lang", lang)
        await self.allmodules.reload_translations()

        await call.answer(self.strings("language_saved"))
        await call.edit(text=self.text(), reply_markup=self.mark())
