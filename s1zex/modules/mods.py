#
# 🔒 The MIT License (MIT)
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#
# ---------------------------------------------------------------------------------
#     ▀▄   ▄▀   👾 Module for s1zex User Bot (based on s1zex 6.0.0)
#    ▄█▀███▀█▄  🔒 The MIT License (MIT)
#   █▀███████▀█ ⚠️ Owner @s1zex
#   █ █▀▀▀▀▀█ █
#      ▀▀ ▀▀
# ---------------------------------------------------------------------------------
# meta developer: @s1zex

from .. import loader, utils
import logging


logger = logging.getLogger(__name__)


@loader.tds
class ModsMod(loader.Module):
    """List of all of the modules currently installed"""

    strings = {
        "name": "Mods",
        "amount": "<emoji document_id=5265204505565210841>👇</emoji> Right now there is <b>{}</b> modules loaded:\n",
        "partial_load": (
            "\n<emoji document_id=5393097151192509026>💬</emoji> <b>it's not all modules"
            " s1zex is loading</b>"
        ),
        "cmd": "<emoji document_id=5255880393558599480>😳</emoji><emoji document_id=5256142901959729905>😙</emoji><emoji document_id=5256150684440470680>🥹</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5255921814223201321>😉</emoji>  <emoji document_id=5406876368350751327>〰️</emoji>  <emoji document_id=5258306268396790997>😇</emoji><emoji document_id=5258372097360535274>🙃</emoji><emoji document_id=5255704549007566838>😆</emoji><emoji document_id=5258228271790694261>😘</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5256012833170139346>🤣</emoji><emoji document_id=5255880393558599480>😳</emoji> <i><b> <code>{}help</code></i></b>\n",
        "module": "<emoji document_id=5377762498743116673>🤍</emoji>",
        "core_module": "<emoji document_id=5379650961503428163>❤️</emoji>",
    }

    strings_ru = {
        "amount": "<emoji document_id=5265204505565210841>👇</emoji> Сейчас загружено <b>{}</b> модулей:",
        "partial_load": (
            "\n<emoji document_id=5393097151192509026>💬</emoji> <b>Это не все модули,"
            " s1zex загружается</b>"
        ),
        "cmd": "<emoji document_id=5255880393558599480>😳</emoji><emoji document_id=5256142901959729905>😙</emoji><emoji document_id=5256150684440470680>🥹</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5255921814223201321>😉</emoji>  <emoji document_id=5406876368350751327>〰️</emoji>  <emoji document_id=5258306268396790997>😇</emoji><emoji document_id=5258372097360535274>🙃</emoji><emoji document_id=5255704549007566838>😆</emoji><emoji document_id=5258228271790694261>😘</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5256012833170139346>🤣</emoji><emoji document_id=5255880393558599480>😳</emoji> <i><b> <code>{}help</code></i></b>\n",
        "module": "<emoji document_id=5377762498743116673>🤍</emoji>",
        "core_module": "<emoji document_id=5379650961503428163>❤️</emoji>", 
    }

    @loader.command(
        ru_doc="Показать все установленные модули"
    )
    async def modscmd(self, message):
        """- List of all of the modules currently installed"""

        prefix = f"{self.strings('cmd').format(str(self.get_prefix()))}\n"
        result = f"{self.strings('amount').format(str(len(self.allmodules.modules)))}\n"

        for mod in self.allmodules.modules:
            try:
                name = mod.strings["name"]
            except KeyError:
                name = mod.__clas__.__name__
            emoji = (
                self.strings("core_module")
                if mod.__origin__.startswith("<core")
                else self.strings("module")
            )
            result += f"\n {emoji} <code>{name}</code>"

        result += (
            ""
            if self.lookup("Loader").fully_loaded
            else f"\n\n{self.strings('partial_load')}"
        )
        result += f"\n\n {prefix}"

        await utils.answer(message, result)
