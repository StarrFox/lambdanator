from discord.ext import commands


class Lambdanator(commands.Bot):
    def __init__(self, command_prefix, **options):
        options["help_command"] = commands.MinimalHelpCommand()
        options["owner_ids"] = [140516693242937345, 285148358815776768]
        super().__init__(command_prefix, **options)
        self.success_emojis = {
            True: "\N{WHITE HEAVY CHECK MARK}",
            False: "\N{CROSS MARK}",
        }
