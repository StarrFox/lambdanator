import pathlib

from discord.ext import commands
from loguru import logger


class Lambdanator(commands.Bot):
    def __init__(self, command_prefix, **options):
        options["help_command"] = commands.MinimalHelpCommand()
        options["owner_ids"] = [140516693242937345, 285148358815776768]
        super().__init__(command_prefix, **options)
        self.success_emojis = {
            True: "\N{WHITE HEAVY CHECK MARK}",
            False: "\N{CROSS MARK}",
        }

        self.ready_once = False

    async def on_ready(self):
        # on_ready is ran on websocket reconnects also
        if self.ready_once:
            return

        self.ready_once = True

        await self.load_extension("jishaku")

        root = pathlib.Path(__file__).parent
        extensions_path = root / "extensions"
        await self.load_extensions_from_dir(extensions_path)

        logger.info(f"Logged in as {self.user}.")
        logger.info(f"Bot ready with {len(self.extensions.keys())} extensions.")

    async def load_extensions_from_dir(self, path: str | pathlib.Path) -> int:
        """
        Loads any python files in a directory and it's children
        as extensions
        :param path: Path to directory to load
        :return: Number of extensions loaded
        """
        if not isinstance(path, pathlib.Path):
            path = pathlib.Path(path)

        if not path.is_dir():
            return 0

        before = len(self.extensions.keys())

        extension_names = []

        current_working_directory = pathlib.Path(os.getcwd())

        for subpath in path.glob("**/[!_]*.py"):  # Ignore if starts with _
            subpath = subpath.relative_to(current_working_directory)

            parts = subpath.with_suffix("").parts
            if parts[0] == ".":
                parts = parts[1:]

            extension_names.append(".".join(parts))

        for ext in extension_names:
            try:
                await self.load_extension(ext)
            except (commands.errors.ExtensionError, commands.errors.ExtensionFailed):
                logger.exception("Failed loading " + ext)

        return len(self.extensions.keys()) - before
