import dotenv
from dotenv import load_dotenv

load_dotenv()
conf = dotenv.dotenv_values()

api_id = conf.get('tg_api_id')
api_hash = conf.get('tg_api_hash')

if api_id is None or api_hash is None:
    api_id = int(input('Введіть ваш api_id: '))
    api_hash = input('Введіть ваш api_hash: ')
    with open('.env', 'w') as env:
        env.write('tg_api_id=' + str(api_id) + '\n')
        env.write('tg_api_hash=' + api_hash)


print('Все добре! Зараз можна запускати warlord.py')
print('python3 warlord.py &')