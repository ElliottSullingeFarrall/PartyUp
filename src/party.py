from discord import (
    ButtonStyle, Colour, Embed, Interaction, Role, TextChannel, User,
)
from discord.ext import tasks
from discord.ui import Button, View, button


class Party:
    def __init__(self, channel: TextChannel, creator: User, role: Role, size: int):
        self.creator = creator
        self.channel = channel
        self.category = channel.category

        self.role = role
        self.size = size

        self.players = {creator}

        self.updater.start()

    def __del__(self) -> None:
        self.updater.cancel()
        del self

    @property
    def is_empty(self) -> bool:
        return len(self.players) == 0

    @property
    def is_full(self) -> bool:
        return len(self.players) == self.size

    def add(self, player: User) -> None:
        if not self.is_full:
            self.players.add(player)

    def remove(self, player: User) -> None:
        if player in self.players:
            self.players.remove(player)

    @tasks.loop(minutes=5)
    async def updater(self) -> None:
        if hasattr(self, "message"):
            await self.message.delete()

        if self.is_empty:
            self.__del__()
        elif not self.is_full:
            self.message = await self.channel.send(
                embed=self.msg_embed, view=self.msg_view
            )

    @property
    def msg_embed(self) -> Embed:
        return PartyMsg(self)

    @property
    def msg_view(self) -> View:
        return PartyBtn(self)


class PartyMsg(Embed):
    def __init__(self, party: Party) -> None:
        super().__init__(title=f"Party for {party.role.name}", colour=Colour.blurple())
        self.party = party

        self.add_field(name="Role", value=party.role.mention)
        self.add_field(name="Size", value=f"{len(party.players)}/{party.size}")
        self.add_field(
            name="Players",
            value="\n".join(player.mention for player in party.players),
            inline=False,
        )


class PartyBtn(View):
    def __init__(self, party: Party) -> None:
        super().__init__()
        self.party = party

    @button(label="Join", style=ButtonStyle.green)
    async def join_button(self, button: Button, interaction: Interaction) -> None:
        if interaction.user not in self.party.players:
            self.party.add(interaction.user)
            await interaction.response.edit_message(
                content=f"{interaction.user.mention} joined the party!",
                embed=self.party.msg_embed,
                view=self.party.msg_view,
            )
        else:
            await interaction.response.edit_message(
                content=f"{interaction.user.mention} is already in the party!",
                embed=self.party.msg_embed,
                view=self.party.msg_view,
            )

    @button(label="Leave", style=ButtonStyle.red)
    async def leave_button(self, button: Button, interaction: Interaction) -> None:
        if interaction.user in self.party.players:
            self.party.remove(interaction.user)
            await interaction.response.edit_message(
                content=f"{interaction.user.mention} left the party!",
                embed=self.party.msg_embed,
                view=self.party.msg_view,
            )
        else:
            await interaction.response.edit_message(
                content=f"{interaction.user.mention} is not in the party!",
                embed=self.party.msg_embed,
                view=self.party.msg_view,
            )
