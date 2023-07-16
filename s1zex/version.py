"""Represents current userbot version"""
# ©️ Dan Gazizullin, 2021-2023
# This file is a part of s1zex Userbot
# 🌐 https://github.com/s1zexxx/userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# s1zex Team modifided s1zex files for s1zex
# 🌐 https://github.com/s1zexxx/userbot

__version__ = (6, 0, 0)
netver = (0, 4, 3)
netrev = ""
import os
import git

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "stable"
