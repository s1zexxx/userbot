#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2023
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# s1zex Team modifided s1zex files for s1zex
# 🌐 https://github.com/s1zexxx/userbot

from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils, version
from ..inline.types import InlineQuery

import psutil

@loader.tds
class s1zexInfoMod(loader.Module):
    """Show userbot info"""

    strings = {
        "name": "Info",
        "owner": "Owner",
        "version": "Version",
        "build": "Build",
        "prefix": "Prefix",
        "uptime": "Uptime",
        "branch": "Branch",
        "send_info": "Send userbot info",
        "description": "ℹ This will not compromise any sensitive info",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>😢</emoji> <b>You need to specify"
            " text to change info to</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>🎉</emoji> <b>Info changed"
            " successfully</b>"
        ),
        "_cfg_cst_msg": (
            "Custom message for info. May contain {me}, {version}, {prefix},"
            " {platform}, {upd}, {uptime}, {cpu_usage}, {ram_usage} keywords"
        ),
        "_cfg_cst_btn": "Custom button for info. Leave empty to remove button",
        "_cfg_banner": "URL to image banner",
        "desc": (
            "<emoji document_id=4929415445443773080>🚀</emoji>"
            " <b>s1zex</b>\n\nTelegram userbot with a lot of features, like inline"
            " galleries, forms, lists lists based on s1zex. Userbot - software,"
            " running on your Telegram account. If you write a command to any chat, it"
            " will get executed right there. Check out live examples at <a"
            ' href="https://github.com/s1zexxx/userbot">GitHub</a'
        ),
    }

    strings_ru = {
        "version": "Версия",
        "prefix": "Префикс",
        "uptime": "Аптайм",
        "send_info": "Отправить информацию о юзерботе",
        "description": "ℹ Это не раскроет никакой личной информации",
        "_ihandle_doc_info": "Отправить информацию о юзерботе",
        "_cfg_cst_msg": (
            "Кастомный текст сообщения в info. Может содержать ключевые слова {me},"
            " {version}, {prefix}, {platform}, {upd}, {uptime}, {cpu_usage},"
            " {ram_usage}"
        ),
        "_cfg_cst_btn": (
            "Кастомная кнопка в сообщении в info. Оставь пустым, чтобы убрать кнопку"
        ),
        "_cfg_banner": "Ссылка на баннер-картинку",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>😢</emoji> <b>Тебе нужно указать"
            " текст для кастомного инфо</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>🎉</emoji> <b>Текст инфо успешно"
            " изменен</b>"
        ),
        "desc": (
            "<emoji document_id=5062291541624619917>😀</emoji> <b>s1zex</b>"
            " Юзербот, основанный на s1zex с богатым функционалом."
            " Юзербот работает во всех чатах от имени твоего аккаунта. <b>Исходный код s1zex можешь всегда посмотреть на <a"
            ' href="https://github.com/s1zexxx/userbot">GitHub</a'
        ),
    }

    strings_uk = {
        "version": "Версія",
        "prefix": "Префікс",
        "uptime": "Аптайм",
        "send_info": "Надіслати інформацію про юзербот",
        "опис": " ℹ Це не розкриє жодної особистої інформації",
        "_ihandle_doc_info": "Надіслати інформацію про юзербот",
        "_cfg_cst_msg": (
            "Кастомний текст повідомлення в info. Може містити ключові слова {me},"
            " {version}, {prefix}, {platform}, {upd}, {uptime}, {cpu_usage},"
            " {ram_usage}"
        ),
        "_cfg_cst_btn": (
            "Кастомна кнопка в повідомленні в info. Залиш порожнім, щоб прибрати кнопку"
        ),
        "_cfg_banner": "посилання на банер-картинку",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698> 😢 </emoji> <b> вам потрібно вказати"
            "текст для кастомного Інфо</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>🎉</emoji> <b>Текст Інфо успішно"
            " змінено</b>"
        ),
        "desc": (
            "<emoji document_id=5062291541624619917>😀</emoji> <b>s1zex</b>"
            " Юзербот, заснований на s1zex з багатим функціоналом."
            " Юзер бот працює у всіх чатах від імені Твого аккаунта. <b>Вихідний код Netfol можеш завжди подивитися на <a"
            ' href="https://github.com/s1zexxx/userbot">GitHub</a'
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_message",
                doc=lambda: self.strings("_cfg_cst_msg"),
            ),
            loader.ConfigValue(
                "custom_button",
                None,
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Union(
                    loader.validators.Series(fixed_len=2),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "banner_url",
                "https://github.com/s1zexxx/userbot/assets/banner.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
        )

    async def client_ready(self):
        self._me = await self._client.get_me()
        if (
            self.config["banner_url"]
            == "https://github.com/s1zexxx/userbot/assets/banner.png"
        ):
            self.config[
                "banner_url"
            ] = "https://github.com/s1zexxx/userbot/assets/banner.png"

    def _render_info(self, inline: bool) -> str:
        me = '<b><a href="tg://user?id={}">{}</a></b>'.format(
            self._me.id,
            utils.escape_html(get_display_name(self._me)),
        )
        build = utils.get_commit_url()
        _version = f'<i>{version.branch} {".".join(list(map(str, list(version.netver))))} {version.netrev}</i>'
        prefix = f"«<code>{utils.escape_html(self.get_prefix())}</code>»"

        platfo = utils.get_named_platform()
        if "Termux" not in platfo:
            usage = f" ({psutil.cpu_percent()}% | {utils.get_ram_usage()} RAM)</b>"
        else:
            usage = "\n"

        platform = utils.get_named_platform()

        for emoji, icon in {
            "🍊": "<emoji document_id=5449599833973203438>🧡</emoji>",
            "🍇": "<emoji document_id=6334737201485579954>🍇</emoji>",
            "❓": "<emoji document_id=5866460679594053316>📱</emoji>",
            "🍁": "<emoji document_id=5866334008123591985>💻</emoji>",
            "🦾": "<emoji document_id=5386766919154016047>🦾</emoji>",
            "🚂": "<emoji document_id=5359595190807962128>🚂</emoji>",
            "🐳": "<emoji document_id=6334586503968065308>🐳</emoji>",
            "🕶": "<emoji document_id=5866460679594053316>📱</emoji>",
            "🐈‍⬛": "<emoji document_id=6334750507294262724>🐈‍⬛</emoji>",
            "👾": "<emoji document_id=5866169914603081371>🐧</emoji>",
            "🧩": "<emoji document_id=6334313137889609341>🧩</emoji>",
            "😎": "<emoji document_id=5364105417569868801>😎</emoji>",
        }.items():
            platform = platform.replace(emoji, icon)

        return (
            self.config["custom_message"].format(
                me=me,
                version=_version,
                build=build,
                prefix=prefix,
                platform=platform,
                uptime=utils.formatted_uptime(),
                cpu_usage=psutil.cpu_percent(),
                ram_usage=f"{utils.get_ram_usage()} MB",
                branch=version.branch,
            )
            if self.config["custom_message"]
            else (
                f"<b>{{}} for {me}</b>\n\n"
                f"<emoji document_id=6334456392228800167>🪢</emoji> <b>{self.strings('version')}:</b> {_version} {build}\n"
                f"<emoji document_id=6334701737940616970>💫</emoji> <b>{self.strings('prefix')}:</b> {prefix}\n"
                f"<emoji document_id=6334620339720423126>🕛</emoji> <b>{self.strings('uptime')}:</b>"
                f" {utils.formatted_uptime()}\n\n"
                f"<b>{platform}"
                f"{usage}"
            ).format(
                *map(
                    lambda x: utils.remove_html(x) if inline else x,
                    (
                        utils.get_platform_emoji()
                        if self._client.s1zex_me.premium and not inline
                        else "🥀 s1zex",
                    ),
                )
            )
        )

    def _get_mark(self):
        return (
            {
                "text": self.config["custom_button"][0],
                "url": self.config["custom_button"][1],
            }
            if self.config["custom_button"]
            else None
        )

    @loader.inline_handler(
        thumb_url="https://img.icons8.com/nolan/512/info-squared.png"
    )
    @loader.inline_everyone
    async def Info(self, _: InlineQuery) -> dict:
        """Send userbot info"""

        return {
            "title": self.strings("send_info"),
            "description": self.strings("description"),
            **(
                {"photo": self.config["banner_url"], "caption": self._render_info(True)}
                if self.config["banner_url"]
                else {"message": self._render_info(True)}
            ),
            "thumb": ("https://github.com/s1zexxx/userbot/assets/bot_pfp.png"),
            "reply_markup": self._get_mark(),
        }

    @loader.command(alias="инфо")
    async def info(self, message: Message):
        """Send userbot info"""

        if self.config["custom_button"]:
            await self.inline.form(
                message=message,
                text=self._render_info(True),
                reply_markup=[
                    {
                        "text": self.config["custom_button"][0],
                        "url": self.config["custom_button"][1],
                    }
                ],
                **(
                    {"photo": self.config["banner_url"]}
                    if self.config["banner_url"]
                    else {}
                ),
            )
        else:
            try:
                await self._client.send_file(
                    message.peer_id,
                    self.config["banner_url"],
                    reply_to=utils.get_topic(message),
                    caption=self._render_info(False),
                )
            except Exception:
                await utils.answer(message, self._render_info(False))
            else:
                if message.out:
                    await message.delete()

    @loader.command(
        ru_doc="Отправить информацию по типу 'Что такое s1zex?'",
    )
    async def whos1zex(self, message: Message):
        """Send info aka 'What is s1zex?'"""
        await utils.answer(message, self.strings("desc"))

    @loader.command(
        ru_doc="<текст> - Изменить текст в .info",
    )
    async def setinfo(self, message: Message):
        """<text> - Change text in .info"""
        args = utils.get_args_html(message)
        if not args:
            return await utils.answer(message, self.strings("setinfo_no_args"))
        self.config["custom_message"] = args
        await utils.answer(message, self.strings("setinfo_success"))
