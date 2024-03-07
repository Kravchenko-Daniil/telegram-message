from telethon import TelegramClient, events, functions, types
import asyncio, random


api_id = 28018058
api_hash = 'c0740a79857a374d7830d10156298c1c'
app_hash = 'b18441a1ff607e10a989891a5462e627'
phone_number = '+1 581 257 3538'.strip().replace('+', '')
# phone_number = 'Mikayel99'


target_username = 'arsen_allpowerful'
message = 'Hello, this is a test message!'


async def send_message():
    async with TelegramClient(r'sessions//79959122099_telethon', api_id, api_hash) as client:
        user_id = await client(functions.contacts.ImportContactsRequest(
            contacts=[types.InputPhoneContact(
                client_id=random.randrange(-2 ** 63, 2 ** 63),
                phone=phone_number,
                first_name='some string here',
                last_name='some string here'
            )]
        ))

        user_id = str(user_id).split()[0].split('=')[-1].replace(',', '')
        user_id = int(user_id)
        user_id = phone_number

        await client.send_message(user_id, message)


async def main():
    await send_message()


asyncio.run(main())
