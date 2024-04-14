import discord
import random 

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

def catrandomfunction():
    #cats dictionary with image links
    catdictionary = {'gatinho1':'https://www.petz.com.br/blog/wp-content/uploads/2020/04/meu-primeiro-gato.jpg', 'gatinho2':'https://i0.statig.com.br/bancodeimagens/2n/y9/zl/2ny9zlk3myviabfr6wd6k8ccz.jpg', 'gatinho3': 'https://img.freepik.com/fotos-premium/gatinho-fofo-rindo-pequeno-gato-domestico-bocejando-ou-sorrindo-ia-generativa_116953-2823.jpg', 'gatinho4':'https://s2.glbimg.com/kmbgBzKPL0URISIQenPiAKo4ORI=/e.glbimg.com/og/ed/f/original/2017/08/23/5c147f01-dff6-4952-98a0-9394c88361c2.jpg', 'gatinho5': 'https://catland.org.br/wp-content/uploads/2023/04/foto-1.png', 'gatinho6': 'https://static6.depositphotos.com/1004769/598/i/450/depositphotos_5981131-stock-photo-small-kittens-in-straw-basket.jpg', 'gatinho7':'https://1.bp.blogspot.com/-Wq2lcq9_a4I/Tc2lLWOkNVI/AAAAAAAABVM/Wao0rm-vWe4/s1600/gatinho-5755.jpg', 'gatinho8': 'https://blog.ferplast.com/wp-content/uploads/2020/09/gattino-biberon-come-dare-latte-1024x683.jpg'}

    namecat, imagecat = random.choice(list(catdictionary.items()))

    catrandom = random.choice(list(catdictionary.values()))

    return catrandom

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        conteudo = message.content
        l_conteudo = conteudo.lower()

        print('Message from {0.author}: {0.content}'.format(message))
        if l_conteudo.startswith('miau'):
            await message.channel.send(catrandomfunction())

client = MyClient(intents=intents)

client.run('''TOKEN''')