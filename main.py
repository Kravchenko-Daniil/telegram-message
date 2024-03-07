import time, threading, json, random, asyncio
from telethon import TelegramClient
import pandas as pd


api_id = 28018058
api_hash = 'c0740a79857a374d7830d10156298c1c'
missed = []


async def sending(session, data):
    # print(session, data)
    async with TelegramClient(rf"{session}", api_id, api_hash) as client:

        count = 0
        count_time = 0
        for i in range(len(data)):
            if count_time == 30:
               time.sleep(60)

            # user_id = await client(functions.contacts.ImportContactsRequest(
            #     contacts=[types.InputPhoneContact(
            #         client_id=random.randrange(-2 ** 63, 2 ** 63),
            #         phone=data[i],
            #         first_name=str(data[i]),
            #         last_name=''
            #     )]
            # ))
            # user_id = str(user_id).split()[0].split('=')[-1].replace(',', '')
            # user_id = int(user_id)
            user_id = data[i]

            names = ['Vančo Lestat', 'Balduíno Yıldız', 'Laura Hubert']
            try:
                await client.send_message(user_id, f"Hi, my name is {random.choice(names)}")
                print(f"success {session} - {user_id}")
                count_time += 1
                count += 1
            except Exception as ex:
                with open('missed.txt', 'w') as file:

                    file.write(f"{user_id}\n")
                print(f'WRONG - {ex} - {session} - {user_id}')

            time.sleep(2)


def wrapper(session, data):
    asyncio.run(sending(session, data))


def accounts(sessions, targets):
    step = len(targets) // len(account_phones)
    start = 0
    end = step
    for i in range(len(sessions)):
        data = targets[start:end]
        start += step
        end += step
        session = sessions[i]

        threading.Thread(target=wrapper, args=(session, data,)).start()


def get_targets():
    df = pd.read_excel('targtes.xlsx', na_filter=False)
    df = list(df['Username'])

    for i in df:
        if i == '':
            df.remove(i)

    # df = df.reverse()
    return df


if __name__ == "__main__":
    file = json.load(open('accounts.json'))
    account_phones = []
    account_sessions = []
    for i in file:
        if i['status']:
            account_phones.append(i['id'])
            account_sessions.append(i['session'])

    targets = get_targets()
    print(targets)
    accounts(account_sessions, targets)
