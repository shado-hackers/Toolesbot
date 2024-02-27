from geopy.geocoders import Nominatim
from pyrogram import Client, filters




async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await app.get_chat_member(chat.id, user)
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):

        ui = await app.resolve_peer(user)
        ps = (
            await app.get_chat_members(chat.chat_id, filter="administrators")
        )
        return isinstance(
            next((p for p in ps if p.user.id == ui.id), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    return None


GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@Client.on_message(filters.command("gps"))
async def _(client, message):
    if message.forward_from:
        return
    if message.chat.type == "group":
        if not (await is_register_admin(message.chat, message.from_user.id)):
            await message.reply(
                "You are not Admin. So, You can't use this."
            )
            return

    args = message.text.split()[1]

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await Client.send_location(
            message.chat.id,
            latitude,
            longitude,
            disable_notification=True,
        )
        await message.reply(
            "Open with: [Google Maps]({})".format(gm),
            disable_web_page_preview=True,
        )
    except Exception as e:
        print(e)
        await message.reply("I can't find that")

