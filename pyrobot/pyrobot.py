#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from pyrogram import Client
from pyrogram import __version__
from pyrogram.api.all import layer

from pyrobot import (
    APP_ID = 1364592
    API_HASH = "bacb68050efb668d82dd9d1039759f49"
    HU_STRING_SESSION = "AgBjW8wN8FXkDCTt9HbrVsa2PaL8G4u1Fknd5Mpnb5y_g7vsPW3VmGrT40C6dDI76hrdjest0-FxjIrb23WSIGWps9WBIGi5K0mIrGzaRLFK3vKX-xOSEmvMXyhzgGexVyNs5gA3WPg8WpgU26c-qMS7H78MRtJsgdxs4sk85bQ9Dh4JqCmz9fdSN0QB70qrkyzJDAhk--GA7kRcFNcWzS16INy1MX_BIx2DonQH6-yMoYjnAg2VTiGY4S2sxRw13M3PL9QpnRknlnafGi86uzsetoDz-DUuid2ZIOXxzOct0PXN4Ur-aW6hZXxoDxYLWO-f-wNLFlRA7yXAEydQAnGHPscDggA"
#APP_ID,
#API_HASH,
#HU_STRING_SESSION,
    LOGGER,
    # OWNER_ID,
    # SUDO_USERS,
    TG_COMPANION_BOT,
    TMP_DOWNLOAD_DIRECTORY
)


class PyroBot(Client):

    def __init__(self):
        name = self.__class__.__name__.lower()

        if HU_STRING_SESSION is None:
            super().__init__(
                name,
                plugins=dict(root=f"{name}/plugins"),
                workdir=TMP_DOWNLOAD_DIRECTORY,
                api_id=APP_ID,
                api_hash=API_HASH,
                bot_token=TG_COMPANION_BOT
            )
        else:
            super().__init__(
                name,
                plugins=dict(root=f"{name}/plugins"),
                workdir=TMP_DOWNLOAD_DIRECTORY,
                api_id=APP_ID,
                api_hash=API_HASH,
            )


    async def start(self):
        await super().start()

        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        LOGGER.info(
            f"PyroGramBot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{usr_bot_me.username}. "
            "Hi."
        )


    async def stop(self, *args):
        await super().stop()
        print("PyroGramBot stopped. Bye.")
