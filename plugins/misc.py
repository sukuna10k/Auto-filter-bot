from info import ADMINS
from speedtest import Speedtest, ConfigRetrievalError
from pyrogram import Client, filters, enums
from utils import get_size
from datetime import datetime


@Client.on_message(filters.command('id'))
async def afficher_id(client, message):
    type_chat = message.chat.type
    message_repondu = bool(message.reply_to_message)
    if message_repondu:
        return await message.reply_text(f"""L'ID du message transféré provenant de {message_repondu.chat.title} est : <code>{message_repondu.chat.id}</code>.""")
    if type_chat == enums.ChatType.PRIVATE:
        await message.reply_text(f'★ ID Utilisateur : <code>{message.from_user.id}</code>')

    elif type_chat in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await message.reply_text(f'★ ID Groupe : <code>{message.chat.id}</code>')

    elif type_chat == enums.ChatType.CHANNEL:
        await message.reply_text(f'★ ID Canal : <code>{message.chat.id}</code>')


@Client.on_message(filters.command('speedtest') & filters.user(ADMINS))
async def test_de_vitesse(client, message):
    # Source : https://github.com/weebzone/WZML-X/blob/master/bot/modules/speedtest.py
    msg = await message.reply_text("Lancement du Speedtest...")
    try:
        speed = Speedtest()
    except ConfigRetrievalError:
        await msg.edit("Impossible de se connecter au serveur pour le moment, réessayez plus tard !")
        return
    speed.get_best_server()
    speed.download()
    speed.upload()
    speed.results.share()
    result = speed.results.dict()
    photo = result['share']
    texte = f'''
➲ <b>INFORMATIONS SUR LE SPEEDTEST</b>
┠ <b>Téléchargement :</b> <code>{get_size(result['upload'])}/s</code>
┠ <b>Débit :</b>  <code>{get_size(result['download'])}/s</code>
┠ <b>Ping :</b> <code>{result['ping']} ms</code>
┠ <b>Heure :</b> <code>{datetime.strptime(result['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")}</code>
┠ <b>Données envoyées :</b> <code>{get_size(int(result['bytes_sent']))}</code>
┖ <b>Données reçues :</b> <code>{get_size(int(result['bytes_received']))}</code>

➲ <b>SERVEUR DE SPEEDTEST</b>
┠ <b>Nom :</b> <code>{result['server']['name']}</code>
┠ <b>Pays :</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
┠ <b>Sponsor :</b> <code>{result['server']['sponsor']}</code>
┠ <b>Latence :</b> <code>{result['server']['latency']}</code>
┠ <b>Latitude :</b> <code>{result['server']['lat']}</code>
┖ <b>Longitude :</b> <code>{result['server']['lon']}</code>

➲ <b>DÉTAILS DU CLIENT</b>
┠ <b>Adresse IP :</b> <code>{result['client']['ip']}</code>
┠ <b>Latitude :</b> <code>{result['client']['lat']}</code>
┠ <b>Longitude :</b> <code>{result['client']['lon']}</code>
┠ <b>Pays :</b> <code>{result['client']['country']}</code>
┠ <b>Fournisseur d'accès :</b> <code>{result['client']['isp']}</code>
┖ <b>Évaluation du fournisseur :</b> <code>{result['client']['isprating']}</code>
'''
    await message.reply_photo(photo=photo, caption=texte)
    await msg.delete()
