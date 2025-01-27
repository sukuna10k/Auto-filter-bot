import random
import os
import sys
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from info import ADMINS, LOG_CHANNEL, PICS, SUPPORT_LINK, UPDATES_LINK
from database.users_chats_db import db
from utils import temp, get_settings
from Script import script


@Client.on_chat_member_updated(filters.group)
async def bienvenue(bot, message):
    if message.new_chat_member and not message.old_chat_member:
        if message.new_chat_member.user.id == temp.ME:
            buttons = [[
                InlineKeyboardButton('Mise à jour', url=UPDATES_LINK),
                InlineKeyboardButton('Support', url=SUPPORT_LINK)
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            user = message.from_user.mention if message.from_user else "Cher utilisateur"
            await bot.send_photo(chat_id=message.chat.id, photo=random.choice(PICS), caption=f"👋 Bonjour {user},\n\nMerci de m'avoir ajouté au groupe <b>'{message.chat.title}'</b>. N'oubliez pas de me donner les droits d'admin. Si vous avez des questions, contactez le groupe de support. 😘</b>", reply_markup=reply_markup)
            if not await db.get_chat(message.chat.id):
                total = await bot.get_chat_members_count(message.chat.id)
                username = f'@{message.chat.username}' if message.chat.username else 'Privé'
                await bot.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(message.chat.title, message.chat.id, username, total))       
                await db.add_chat(message.chat.id, message.chat.title)
            return
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            WELCOME = settings['welcome_text']
            welcome_msg = WELCOME.format(
                mention=message.new_chat_member.user.mention,
                title=message.chat.title
            )
            await bot.send_message(chat_id=message.chat.id, text=welcome_msg)


@Client.on_message(filters.command('restart') & filters.user(ADMINS))
async def redemarrer_bot(bot, message):
    msg = await message.reply("Redémarrage en cours...")
    with open('restart.txt', 'w+') as file:
        file.write(f"{msg.chat.id}\n{msg.id}")
    os.execl(sys.executable, sys.executable, "bot.py")


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def quitter_un_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Fournissez-moi un ID de chat')
    r = message.text.split(None)
    if len(r) > 2:
        raison = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        raison = "Aucune raison fournie."
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Groupe de support', url=SUPPORT_LINK)
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text=f"Bonjour,\nMon propriétaire m'a demandé de quitter ce groupe, donc je pars. Si vous souhaitez me réinviter, contactez mon groupe de support ou mon propriétaire : **@kingcey** .\nRaison : <code>{raison}</code>",
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
        await message.reply(f"<b>✅ Le bot a quitté ce groupe avec succès - `{chat}`</b>")
    except Exception as e:
        await message.reply(f'Erreur - {e}')


@Client.on_message(filters.command('ban_grp') & filters.user(ADMINS))
async def desactiver_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Fournissez-moi un ID de chat')
    r = message.text.split(None)
    if len(r) > 2:
        raison = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        raison = "Aucune raison fournie."
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Fournissez-moi un ID de chat valide')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat introuvable dans la base de données")
    if cha_t['is_disabled']:
        return await message.reply(f"Ce chat est déjà désactivé.\nRaison : <code>{cha_t['reason']}</code>")
    await db.disable_chat(int(chat_), raison)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Chat désactivé avec succès')
    try:
        buttons = [[
            InlineKeyboardButton('Groupe de support', url=SUPPORT_LINK)
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f"Bonjour,\nMon propriétaire m'a demandé de quitter ce groupe, donc je pars. Si vous souhaitez me réinviter, contactez mon groupe de support.\nRaison : <code>{raison}</code>",
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Erreur - {e}")


@Client.on_message(filters.command('unban_grp') & filters.user(ADMINS))
async def re_activer_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Fournissez-moi un ID de chat')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Fournissez-moi un ID de chat valide')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat introuvable dans la base de données")
    if not sts.get('is_disabled'):
        return await message.reply('Ce chat n\'est pas désactivé.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat réactivé avec succès")


@Client.on_message(filters.command('invite_link') & filters.user(ADMINS))
async def generer_lien_invitation(bot, message):
    if len(message.command) == 1:
        return await message.reply('Fournissez-moi un ID de chat')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Fournissez-moi un ID de chat valide')
    try:
        link = await bot.create_chat_invite_link(chat)
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    await message.reply(f'Voici votre lien d\'invitation : {link.invite_link}')


@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def lister_utilisateurs(bot, message):
    raju = await message.reply('Récupération de la liste des utilisateurs')
    users = await db.get_all_users()
    out = "Utilisateurs enregistrés dans la base de données :\n\n"
    async for user in users:
        out += f"**Nom :** {user['name']}\n**ID :** `{user['id']}`"
        if user['ban_status']['is_banned']:
            out += ' (Utilisateur banni)'
        if user['verify_status']['is_verified']:
            out += ' (Utilisateur vérifié)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="Liste des utilisateurs")
        await raju.delete()
        os.remove('users.txt')


@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def lister_chats(bot, message):
    raju = await message.reply('Récupération de la liste des chats')
    chats = await db.get_all_chats()
    out = "Chats enregistrés dans la base de données :\n\n"
    async for chat in chats:
        out += f"**Titre :** {chat['title']}\n**ID :** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += ' (Chat désactivé)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="Liste des chats")
        await raju.delete()
        os.remove('chats.txt')
