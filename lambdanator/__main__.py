import os.path

import toml

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

    bot = Lambdanator("lm/")

    bot.load_extension("lambdanator.extensions.emote_manager")

    bot.run(config["discord"]["token"])


if __name__ == "__main__":
    main()
