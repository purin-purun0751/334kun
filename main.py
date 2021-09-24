import os
import discord
from discord.ext import tasks
from datetime import datetime , timedelta, timezone
from time import sleep
import numpy as np
from numpy import random

TOKEN = os.environ['ここは各々'] #トークン
CHANNEL_ID =  796357249743585290#チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

jst = timezone(timedelta(hours=9), name='JAPAN')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="色んなものが埋まってます|#help "))

#ここ ↓ は、特定のメッセージに対して反応をする系統

@client.event
async def on_message(message):
# メッセージの送り主がユーザーであるなら、動作を送ります。
    if message.author == client.user:
        return
    #elif message.author.bot:
    #    return

    # ずるいぞって誰かが言ったら　〇
    if message.content.startswith('ずるいぞ！') or message.content.endswith('ずるいぞ！'):
    # 藍染がずるいぞって言います
    #    await message.channel.send('https://pbs.twimg.com/media/DkZfWzGU0AAtVQt.jpg')
    # 藍染だけじゃなくて、与謝野晶子初め、魑魅魍魎がずるいぞって言いに来るようにしました
    # zuruizo_list 現在8つ    
        ZURUIZO_LIST = ['https://pbs.twimg.com/media/DkZfWzGU0AAtVQt.jpg',
                        'https://pbs.twimg.com/media/DJLmJjJVAAElBjF.jpg',
                        'https://cdn.discordapp.com/attachments/796357249743585290/888739926433222656/dc3b39f19e94c37d.jpg',
                        'https://cdn.discordapp.com/attachments/796357249743585290/888745753185501195/zuruu.jpg',
                        'https://cdn.discordapp.com/attachments/796357249743585290/888748787412135946/sm_3088_036.jpg',
                        'https://cdn.discordapp.com/attachments/796357249743585290/888743847646076928/image0.png',
                        'https://cdn.discordapp.com/attachments/796357249743585290/889538702655762542/image1.png',
                        'https://cdn.discordapp.com/attachments/796357249743585290/889538702336991264/image0.png']
        p = np.array([38,10,10,10,10,10,10,2])
        p = p / sum(p)
        await message.channel.send(np.random.choice((ZURUIZO_LIST),p=p))
    
    
    # ねないこって誰かが言ったら  〇
    if message.content.startswith('ねないこ'):
    # ねないこだれだ　が出てきます        
        await message.channel.send('https://images-na.ssl-images-amazon.com/images/I/81Yp7djAE+L.jpg')

       # ライナーに助けを求めたら　〇
    if message.content.startswith('ライナアアア') or message.content.endswith('アアアアアア'):
    # ライナーが複数パターンに分かれて答えてくれます    
        REINER_LIST = ['https://pbs.twimg.com/media/DqzBEMbU8AAzjbR.jpg',
                       'https://cdn.discordapp.com/attachments/796357249743585290/888675473293455450/ozaki.jpg']
        p = np.array([85,15])
        p = p / sum(p)
        await message.channel.send(np.random.choice((REINER_LIST),p=p))
    
    # いーじゃんって言ったら
    if message.content.startswith('いーじゃん') or message.content.startswith('イージャン'):
    # ラージャンがイージャンって言ってくれます
        await message.channel.send('https://pbs.twimg.com/media/EKljb9QWsAEePP2.jpg')
    elif message.content.endswith('いーじゃん') or  message.content.endswith('イージャン'):
        await message.channel.send('https://pbs.twimg.com/media/EKljb9QWsAEePP2.jpg')

    # すげーじゃんって言ったら
    if message.content.startswith('すげーじゃん') or message.content.startswith('スゲージャン'):
    # ラージャンがスゲージャンって言ってくれます
        await message.channel.send('https://pbs.twimg.com/media/Eo-I_NdVQAE6ZMR.jpg')
    elif message.content.endswith('すげーじゃん') or message.content.endswith('スゲージャン'):
        await message.channel.send('https://pbs.twimg.com/media/Eo-I_NdVQAE6ZMR.jpg')

    # 誰かがあげません！って言ったら　〇
    if message.content.startswith('あげません！') or message.content.endswith('あげません！'):
    # スぺちゃんがあげません！って言ってくれます
        await message.channel.send('https://img.cdn.nimg.jp/s/nicovideo/thumbnails/38460226/38460226.3466182.original/r1280x720l?key=17bf7d9be542944a7bf81eb51f7a5cd5225b4e4c78ed1de3efee305a3ff57f04')

    # くれよって言っても 〇
    if message.content.startswith('くれよ') or message.content.endswith('くれよ'):
    # スぺちゃんはくれません
        await message.channel.send('https://img.cdn.nimg.jp/s/nicovideo/thumbnails/38460226/38460226.3466182.original/r1280x720l?key=17bf7d9be542944a7bf81eb51f7a5cd5225b4e4c78ed1de3efee305a3ff57f04')

    # ハルトオオオオオオオオオオオオオ　〇
    if 'ハルトオオオ' in message.content:
    # ハルトオオオオオオオオオオオオオ
        HARUTO_LIST = ['https://cdn.discordapp.com/attachments/796357249743585290/841019229548707840/R6ac126fab28a92ff5b4ab89942728b15_1.png',
                       'https://cdn.discordapp.com/attachments/796357249743585290/888757735838064670/1.jpg']
        p = np.array([85,15])
        p = p / sum(p)
        await message.channel.send(np.random.choice((HARUTO_LIST),p=p))
        
        
    # 兄さんは嫌いだって言っちゃうと 〇
    if '兄さんは嫌いだ' in message.content:
    # ハルトも便乗してきます
        await message.channel.send('https://cdn.discordapp.com/attachments/796357249743585290/841052385731936276/afbf996c5911d45b.png')

    # いいぞ。って言うと　〇
    if message.content.startswith('いいぞ。') or message.content.endswith('いいぞ。'):
    # ジャンボ尾崎のワンポイントアドバイスが出ます
        await message.channel.send('http://nicovideo.cdn.nimg.jp/thumbnails/30324655/30324655.L')

    # よよよって言うと 〇
    if message.content.startswith('よよよ') or message.content.endswith('よよよ'):
    # マックイーンも落ち込みます
        await message.channel.send('https://cdn.discordapp.com/attachments/796782540895682603/844895684636442674/WS000200.JPG')
    
    # 勝ちですわって言っちゃうと　〇
    if '勝ちですわ' in message.content or '勝ちですわ！' in message.content:
    # マックイーンも勝利しちゃいます
        await message.channel.send('https://livedoor.blogimg.jp/risufx-q61dxwp6/imgs/f/9/f9c4c21a.png')
    
    elif 'チョコが一番ですわ' in message.content or 'チョコが一番ですわ！' in message.content:
        await message.channel.send('https://livedoor.blogimg.jp/risufx-q61dxwp6/imgs/f/9/f9c4c21a.png')
    
    elif 'チョコですわ' in message.content or 'チョコですわ！' in message.content:
        await message.channel.send('https://livedoor.blogimg.jp/risufx-q61dxwp6/imgs/f/9/f9c4c21a.png')
    

    # パクパクですわって言っちゃうと 〇
    if 'パクパクですわ' in message.content or 'パクパクですわ！' in message.content:
    # マックイーンもパクパクします
        await message.channel.send('https://imgur.com/B1qQVAJ')
   
    

    # 毎夜コレですわって言っちゃうと
    if '毎夜コレですわ！' in message.content or '毎夜これですわ！' in message.content:
    # マックイーンも便乗してきます
        await message.channel.send('https://imgur.com/9b7h58h')

    # 人に対して殺意を向けると 〇
    if 'お前を殺す' in message.content or 'お前を頃す' in message.content:
    # ヒイロ・ユイがやってきます
        await message.channel.send('https://img.gifmagazine.net/gifmagazine/images/4404342/original.gif')

# サボテンをサンドでサンドすると
    if 'サボテンをサンドでサンド' in message.content:
    # サボテンをサンドでサンドします
        await message.channel.send('https://cdn.discordapp.com/attachments/796357249743585290/865931723668455444/2021-07-17_21.20.34-removebg-preview.png')
    elif 'SSS' in message.content:
        await message.channel.send('https://cdn.discordapp.com/attachments/796357249743585290/865931723668455444/2021-07-17_21.20.34-removebg-preview.png')

    
    # もうめんどうみきれよう。って言うと
    if 'もうめんどうみきれよう。' in message.content or 'もうめんどうみきれよう' in message.content:
        # 尾崎も便乗してくれます　偶にカイトも言ってくれます
        MENDOU_LIST = ['https://cdn.discordapp.com/attachments/796945445380816906/867359623913013248/ozaki.jpg',
                       'https://cdn.discordapp.com/attachments/796357249743585290/888742212022714368/mikireyoooo.jpg']
        p = np.array([90,10])
        p = p / sum(p)
        await message.channel.send(np.random.choice((MENDOU_LIST),p=p))

    # 伝説って？
    if 'って？' in message.content:
        DENSETSU_LIST = ['https://cdn.discordapp.com/attachments/796357249743585290/890819533986746388/En_43HBVkAEQToc.jpg',
                         'https://cdn.discordapp.com/attachments/796782540895682603/890845463278911488/yosanoaakiko.jpg']
        # ああ！
        p = np.array([90,10])
        p = p / sum(p)
        await message.channel.send(np.random.choice((DENSETSU_LIST),p=p))


# 静かな時に叫ぶと爆発します　発見されたらちょっと弄る 踏まれました
    # if 'ああああああああああああああああああああ' in message.content:
        # await message.channel.send('https://i.pinimg.com/originals/80/ec/09/80ec096e76939aa048bfdc9f7ad73804.gif')

        
        
# 真面目な系統はここに入れる（技術的なテスト込み）    

    # 無期限招待URLの発効コマンド
    embed1 = discord.Embed(title="https://discord.gg/AbU5vwBsHG",description="無期限の招待URLです", color=0x24adff)
    embed1.set_author(name="多目的トイレ", url="https://discord.gg/AbU5vwBsHG", icon_url="https://cdn.discordapp.com/attachments/796425344278069328/798959598005780500/A5zT8yyCQAAzURO.jpg")
    if message.content == '#inv':
        # await message.channel.send('招待URLはこちらです。''\n''https://discord.gg/AbU5vwBsHG')
        await message.channel.send(embed=embed1)
    
    # Discordの標準チャットコマンド一覧を出すコマンド
    embed2 = discord.Embed(title="Discordチャットコマンド", color=0x24abff)
    embed2.add_field(name="太字", value='`** **で囲む`', inline=True)
    embed2.add_field(name="下線", value='`__ __で囲む`', inline=True)
    embed2.add_field(name="取り消し線", value='`~~ ~~で囲む`', inline=True)
    embed2.add_field(name="文字を隠す", value="`|| ||で囲む`", inline=True)
    embed2.add_field(name="なんか線を出す", value="`> を左側に置く`", inline=True)
    if message.content == '#tyc':
        await message.channel.send(embed=embed2)

    # botコマンドEmbed
    embed3 = discord.Embed(title="botコマンド一覧",description="It's 334のコマンド",color=0x12adff)
    embed3.add_field(name="#inv",value="`無期限招待URLを発行`",inline=True)
    embed3.add_field(name="#tyc",value="`ディスコのチャットコマンド一覧`",inline=True)
    embed3.add_field(name="#dice",value="`サイコロが振れます`",inline=True)
    embed3.add_field(name="#yt",value="`Youtube Togetherのコピペ用コマンドを出せます`",inline=True)

    if message.content == '#command':
        await message.channel.send(embed=embed3)
    elif message.content == '#help':
        await message.channel.send(embed=embed3)

    # logcを全消しするコマンド（管理者のみ）
    cleanmessage=('confirm clean up')
    warningmessge=('このコマンドを使う権利がありません')
    
    if message.content == '#logclean':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send(cleanmessage)
        else:
            await message.channel.send(warningmessge)

    # サイコロ振らせます        
    if '#dice' in message.content:
        if client.user != message.author:
            # 乱数を作成
            OCHINCHIN = ':regional_indicator_o: :regional_indicator_c: :regional_indicator_h: :regional_indicator_i: :regional_indicator_n: :regional_indicator_c: :regional_indicator_h: :regional_indicator_i: :regional_indicator_n:'
            CHINKO = ':regional_indicator_c: :regional_indicator_h: :regional_indicator_i: :regional_indicator_n: :regional_indicator_k: :regional_indicator_o:'
            UNCHI = ':regional_indicator_u: :regional_indicator_n: :regional_indicator_c: :regional_indicator_h: :regional_indicator_i:'
            UNKO = ':regional_indicator_u: :regional_indicator_n: :regional_indicator_k: :regional_indicator_o:'
            MANKO = ':regional_indicator_m: :regional_indicator_a: :regional_indicator_n: :regional_indicator_k: :regional_indicator_o:'
            OMANCO = ':regional_indicator_o: :regional_indicator_m: :regional_indicator_a: :regional_indicator_n: :regional_indicator_c: :regional_indicator_o:'
            OPPAI = ':regional_indicator_o: :regional_indicator_p: :regional_indicator_p: :regional_indicator_a: :regional_indicator_i: '
            # サイコロの面を指定
            dice_list = [':one:',':two:',':three:',':four:',':five:',':six:',OCHINCHIN,CHINKO,UNCHI,UNKO,MANKO,OMANCO,OPPAI]
            p = np.array([0.15,0.15,0.15,0.15,0.15,0.15,0.01,0.015,0.015,0.015,0.015,0.015,0.015])
            p = p / sum(p) # サイコロの確率の総和を1に近づける（はず）
            m = 'サイコロを振ります…'
            dice_roll = np.random.choice(dice_list,p=p) # サイコロを振ります
            await message.reply(m) # #dice コマンドの発信者に対して返信を行う
            sleep(1) # 1秒待たせる
            await message.reply(dice_roll) # #dice コマンドの発信者に対して、サイコロの結果を返信する
            
            
    #Youtube Togetherのコピペ用コマンド（多分使わね）
    embed4 = discord.Embed(title="yt! party 796979552093077534",description="Youtube Togetherのコピペ用コマンドです。\nコピペして使ってください。", color=0x24adff)
    if message.content == '#yt':
       await message.channel.send(embed=embed4)
            
# ここ ↓ は時間指定で送る系統

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now(jst).strftime('%H:%M')
    if now == '03:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('3時34分をお知らせします。')
    elif now == '15:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('午後3時34分をお知らせします。')
    
    # テスト運用（提案があったので）
    elif now == '19:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('**__現在テスト運用中__**\n19時19分をお知らせします。')
       
    elif now == '04:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://pbs.twimg.com/profile_images/1251531393324052480/wdvQIHtO_400x400.jpg')
    
    # ここもテスト運用中（提案）
    elif now == '08:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('**__現在テスト運用中__**\n8時10分をお知らせします。')

#ループ処理実行
loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
