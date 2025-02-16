class script(object):

    START_TXT = """<b>Salut {}, <i>{}</i>
    
Je suis un puissant bot de filtrage automatique avec un raccourcisseur de liens. 
Vous pouvez l'utiliser comme filtre automatique avec un raccourcisseur de liens
C'est simple à utiliser : je suis uniquement là pour te fournir des films, des séries, des Animes, Miraculous et tout autres.\n\nPar @AntiFlix_A... ♻️</b>"""

    MY_ABOUT_TXT = """★ Serveur : <a href=https://www.heroku.com>Heroku</a>
★ Base de données : <a href=https://www.mongodb.com>MongoDB</a>
★ Langage : <a href=https://www.python.org>Python</a>
★ Librairie : <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """★ Nom : 🇰ιηg¢єу
★ Nom d’utilisateur : @Kingcey
★ Pour tout problème contacter mes administrateurs
★ Ville : Lomé 🇹🇬"""

    STATUS_TXT = """🗂 Total de fichiers : <code>{}</code>
👤 Total d'utilisateurs : <code>{}</code>
👥 Total de groupes : <code>{}</code>
🤑 Utilisateurs premium : <code>{}</code>
✨ Espace utilisé : <code>{}</code>
🗳 Espace libre : <code>{}</code>
🚀 Temps de fonctionnement du bot : <code>{}</code>"""

    NEW_GROUP_TXT = """#NouveauGroupe
Titre - {}
ID - <code>{}</code>
Nom d’utilisateur - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NouvelUtilisateur
★ Nom : {}
★ ID : <code>{}</code>"""

    NOT_FILE_TXT = """👋 Bonjour {},

Je ne trouve pas <b>{}</b> dans ma base de données ! 🥲

👉 Faites une recherche Google et vérifiez votre orthographe.
👉 Veuillez lire les instructions pour obtenir de meilleurs résultats.
👉 Ou le contenu n'est pas encore publié."""
    
    EARN_TXT = """<b>Comment gagner avec ce bot

➥ Vous pouvez gagner de l'argent en utilisant ce bot.

» Étape 1 : Ajoutez ce bot dans votre groupe avec des permissions d'admin.

» Étape 2 : Créez un compte sur <a href=https://telegram.me/how_to_download_channel/14>mdisklink.link</a> 
[Vous pouvez aussi utiliser d'autres sites de raccourcisseurs].

» Étape 3 : Cliquez sur le bouton ci-dessous pour savoir comment connecter votre raccourcisseur à ce bot.

➥ Ce bot est gratuit pour tous, vous pouvez l'utiliser dans vos groupes sans frais.</b>"""

    HOW_TXT = """<b>Comment connecter votre propre raccourcisseur ‼️

➥ Si vous souhaitez connecter votre propre raccourcisseur, envoyez les détails dans ce format correct dans votre groupe.

➥ Format ↓↓↓

<code>/set_shortlink site_raccourcisseur api_raccourcisseur</code>

➥ Exemple ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ Si vous voulez vérifier quel raccourcisseur est connecté à votre groupe, envoyez cette commande dans le groupe : /get_shortlink

📝 Note : Vous ne devez pas être admin anonyme dans le groupe. Envoyez la commande sans être admin anonyme.</b>"""

    IMDB_TEMPLATE = """✅ Trouvé : <code>{query}</code>

🏷 Titre : <a href={url}>{title}</a>
🎭 Genres : {genres}
📆 Année : <a href={url}/releaseinfo>{year}</a>
🌟 Note : <a href={url}/ratings>{rating} / 10</a>
☀️ Langues : {languages}
📀 Durée : {runtime} minutes

🗣 Demandé par : {message.from_user.mention}
©️ Propulsé par : <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 Veuillez cliquer sur le bouton "Fermer" si vous avez vu le film 🚫"""

    WELCOME_TEXT = """👋 Bonjour {mention}, Bienvenue dans le groupe {title} ! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Essayez chaque commande sans argument pour voir plus de détails 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Voici les commandes admin du bot 👇

/index_channels - pour vérifier le nombre d'ID de chaînes indexées
/stats - pour obtenir l'état du bot
/delete - pour supprimer des fichiers via une requête
/delete_all - pour supprimer tous les fichiers indexés
/broadcast - pour envoyer un message à tous les utilisateurs du bot
/grp_broadcast - pour envoyer un message à tous les groupes
/pin_broadcast - pour envoyer un message épinglé à tous les utilisateurs
/pin_grp_broadcast - pour envoyer un message épinglé à tous les groupes
/restart - pour redémarrer le bot
/leave - pour retirer le bot d'un groupe particulier
/unban_grp - pour activer un groupe
/ban_grp - pour désactiver un groupe
/ban_user - pour bannir des utilisateurs du bot
/unban_user - pour débannir des utilisateurs
/users - pour obtenir les détails de tous les utilisateurs
/chats - pour obtenir la liste des groupes
/invite_link - pour générer un lien d'invitation
/set_pm_search - pour activer ou désactiver la recherche privée
/index - pour indexer les chaînes accessibles au bot</b>"""
    
    USER_COMMAND_TXT = """<b>Voici les commandes utilisateur du bot 👇

/start - pour vérifier si le bot est actif
/settings - pour modifier les paramètres du groupe
/set_template - pour définir un modèle IMDB personnalisé
/set_caption - pour définir une légende personnalisée pour les fichiers
/set_shortlink - les admins du groupe peuvent définir un raccourcisseur personnalisé
/get_custom_settings - pour obtenir les détails des paramètres du groupe
/set_welcome - pour définir un message d'accueil personnalisé pour les nouveaux membres du groupe
/set_tutorial - pour définir un lien de tutoriel dans les résultats
/id - pour vérifier l'ID du groupe ou de la chaîne
/set_fsub - pour définir les chaînes de forçage d'abonnement
/remove_fsub - pour supprimer toutes les chaînes de forçage d'abonnement</b>"""
    
    SOURCE_TXT = """<b>Code source du bot -

- Ce bot est un projet open source.

- Source - <a href=https://t.me/bot_kingdox>ici</a>

vous pouvez également acheté ce bot 

- Développeur - @Kingcey"""

    PREMIUM_PLAN_TEXT = """<b><i><u>- Plans disponibles - </u>

- 700F - 1 semaine
- 1500F - 1 mois
- 2500F - 3 mois
- 4000F - 6 mois
Les Prix sont en Franc CFA

<u>🎁 Avantages premium 🎁</u>

○ Pas besoin de vérification
○ Pas besoin d'ouvrir de lien
○ Fichiers directs   
○ Expérience sans publicité 
○ Lien de téléchargement à haute vitesse                           
○ Films et séries illimités                                                                         
○ Support complet de l'admin                              
○ Les demandes seront traitées en 1h si disponibles   

✨ UPI ID - <code>{}</code>

Cliquez pour vérifier votre plan actif : /myplan

💢 Vous devez envoyer une capture d'écran après paiement

‼️ Après avoir envoyé une capture d'écran, veuillez nous donner un peu de temps pour vous ajouter à la liste premium</i></b>"""
