from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_async, run_js

import asyncio

chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100

async def main():
    global chat_msgs

    put_markdown("Добро пожаловать в онлайн-чат")
    msg_box = output()
    put_scrolltable(msg_box, height = 100, keep_bottom = True)

    nickname = await input("Войти в чат", required=True, placeholder="Ваше имя", validate=lambda n: "Такой пользователь уже существует!" if n in online_users or n == "Круто!" else None)
    online_users.add(nickname)

    chat_msgs.append("Круто!", f"'{nickname}' присоединился к чату")
    msg_box.append(put_markdown(f"'{nickname}' присоединился к чату"))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input_group(" Новое сообщение", [
            input(placeholder="Текст сообщения", name="msg"),
            actions(name="cmd", buttos=["Отправить", {'label':"Выйти из чата", 'type':'cancel'}])
        ], validate = lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m["msg"] else None)

        if data is None