from pyrogram import Client, filters
from utils import is_check_admin
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command('manage') & filters.group)
async def gestion_membres(client, message):
    if not await is_check_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("Vous n'êtes pas admin dans ce groupe.")
    btn = [[
        InlineKeyboardButton('Démuter tout le monde', callback_data='unmute_all_members'),
        InlineKeyboardButton('Débannir tout le monde', callback_data='unban_all_members')
    ], [
        InlineKeyboardButton('Expulser les utilisateurs muets', callback_data='kick_muted_members'),
        InlineKeyboardButton('Expulser les comptes supprimés', callback_data='kick_deleted_accounts_members')
    ]]
    await message.reply_text("Sélectionnez une fonction pour gérer les membres.", reply_markup=InlineKeyboardMarkup(btn))


@Client.on_message(filters.command('ban') & filters.group)
async def bannir_utilisateur_chat(client, message):
    if not await is_check_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("Vous n'êtes pas admin dans ce groupe.")
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.username or message.reply_to_message.from_user.id
    else:
        try:
            user_id = message.text.split(" ", 1)[1]
        except IndexError:
            return await message.reply_text("Répondez à un message utilisateur ou fournissez un ID utilisateur ou un nom d'utilisateur.")
    try:
        user_id = int(user_id)
    except ValueError:
        pass
    try:
        user = (await client.get_chat_member(message.chat.id, user_id)).user
    except:
        return await message.reply_text("Impossible de trouver l'utilisateur spécifié dans ce groupe.")
    try:
        await client.ban_chat_member(message.chat.id, user_id)
    except:
        return await message.reply_text("Je n'ai pas les permissions pour bannir cet utilisateur.")
    await message.reply_text(f"{user.mention} a été banni avec succès du groupe {message.chat.title}.")


@Client.on_message(filters.command('mute') & filters.group)
async def muter_utilisateur_chat(client, message):
    if not await is_check_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("Vous n'êtes pas admin dans ce groupe.")
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.username or message.reply_to_message.from_user.id
    else:
        try:
            user_id = message.text.split(" ", 1)[1]
        except IndexError:
            return await message.reply_text("Répondez à un message utilisateur ou fournissez un ID utilisateur ou un nom d'utilisateur.")
    try:
        user_id = int(user_id)
    except ValueError:
        pass
    try:
        user = (await client.get_chat_member(message.chat.id, user_id)).user
    except:
        return await message.reply_text("Impossible de trouver l'utilisateur spécifié dans ce groupe.")
    try:
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
    except:
        return await message.reply_text("Je n'ai pas les permissions pour muter cet utilisateur.")
    await message.reply_text(f"{user.mention} a été muté avec succès dans le groupe {message.chat.title}.")


@Client.on_message(filters.command(["unban", "unmute"]) & filters.group)
async def debannir_ou_demuter_utilisateur_chat(client, message):
    if not await is_check_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("Vous n'êtes pas admin dans ce groupe.")
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.username or message.reply_to_message.from_user.id
    else:
        try:
            user_id = message.text.split(" ", 1)[1]
        except IndexError:
            return await message.reply_text("Répondez à un message utilisateur ou fournissez un ID utilisateur ou un nom d'utilisateur.")
    try:
        user_id = int(user_id)
    except ValueError:
        pass
    try:
        user = (await client.get_chat_member(message.chat.id, user_id)).user
    except:
        return await message.reply_text("Impossible de trouver l'utilisateur spécifié dans ce groupe.")
    try:
        await client.unban_chat_member(message.chat.id, user_id)
    except:
        return await message.reply_text(f"Je n'ai pas les permissions pour {message.command[0]} cet utilisateur.")
    await message.reply_text(f"{user.mention} a été {message.command[0]} avec succès dans le groupe {message.chat.title}.")
