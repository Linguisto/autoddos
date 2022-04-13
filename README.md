## Ukrainian IT Army DDoS Machine 🇺🇦

___

### ПІДГОТОВКА

1. Переконатися, що ви підписані на канал [IT Army of Ukraine](https://t.me/itarmyofukraine2022)
2. Також переконатися, що у вас є сервер, на якому ви будете запускати скрипт
3. Якщо такого немає, можна завести собі інстанс на AWS, [детальна інструкція тут](https://ain.ua/2022/03/02/yak-nalashtuvaty-ddos-rosijskyh-sajtiv-na-aws/)
4. Зайти на [https://my.telegram.org]()
5. Після авторизації зайти на API Development Tools і заповнини форму
6. Отримати `api_id` та `api_hash`

### ІНСТАЛЯЦІЯ

1. Скачати цей репозиторій
```commandline
git clone https://github.com/Linguisto/autoddos.git
```
2. Зайти в папку `autoddos`
```commandline
cd autoddos
```
3. Інсталювати залежності

```commandline
pip install -r requirements.txt
```

3. Інсталювати залежності у папці `mhddos_proxy`

```commandline
pip install -r ./mhddos_proxy/requirements.txt
```

4. Запустити `warlord.py`

```commandline
python3 warlord.py &
```

5. Слідкувати инструкціям

### Слава Україні!