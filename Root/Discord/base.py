import discord


class BotFace:
    def __init__(self):
        self.client = discord.Client()
        self.client.event(self.on_ready)
        self.client.event(self.on_message)
        self.token_file = open("./secrets/token.sec")
        self.token = self.token_file.read()
        self.token_file.close()

        self.main_loop()

    def get_client_link(self):
        return self.client

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$set_whiteboard'):
            target_channel = message.channel
            print(target_channel.guild)
            print(target_channel.name)
            print(target_channel.id)
            print(target_channel.category_id)

        if message.content.startswith('$get_history_test'):
            messages = await message.channel.history(limit=123).flatten()
            for entry in messages:
                print(entry.content)

    def main_loop(self):
        try:
            self.client.loop.run_until_complete(self.client.start(self.token))
        except (KeyboardInterrupt, SystemExit):
            self.client.loop.run_until_complete(self.client.logout())
        finally:
            self.client.loop.close()


if __name__ == "__main__":
    Illbien = BotFace()

