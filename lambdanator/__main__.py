import os.path

import toml
from discord import Intents

from lambdanator import Lambdanator


STATIC_CONFIG = """
[discord]
token = ""
""".strip("\n")


def make_config():
    with open("config.toml", "w+") as fp:
        fp.write(STATIC_CONFIG)


def main():
    if not os.path.exists("config.toml"):
        make_config()
        print("Config.toml not found; created.")
        exit()

    with open("config.toml") as fp:
        config = toml.load(fp)

    bot = Lambdanator("lm/", intents=Intents(members=True, guilds=True, messages=True, reactions=True))

    bot.load_extension("lambdanator.extensions.emote_manager.emote_manager")
    bot.load_extension("lambdanator.extensions.gamer_words.gamer_words")
    bot.load_extension("lambdanator.extensions.meta")
    bot.load_extension("jishaku")

    bot.run(config["discord"]["token"])


if __name__ == "__main__":
    main()
