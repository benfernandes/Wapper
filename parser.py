import re
from datetime import datetime
from typing import List

import attr


@attr.s
class Message:
    date_time: datetime = attr.ib()
    sender: str = attr.ib()
    media_url: str = attr.ib()  # TODO - Change to Path
    media_type: str = attr.ib()  # TODO - Change to FileType
    _parts: List[str] = attr.ib(default=[])

    def add_part(self, part: str) -> None:
        self._parts.append(part)


@attr.s
class Chat:
    title: str = attr.ib()
    _messages: List[Message] = attr.ib(default=[])

    def add_message(self, message: Message) -> None:
        self._messages.append(message)


class Parser:
    def parse(self, rows: List[str]) -> Chat:
        chat = Chat(title='Test')

        for row in rows:
            try:  # Check if line starts with datetime
                pattern = "\[(\d{2})\/(\d{2})\/(\d{4}), (\d{2}):(\d{2}):(\d{2})\] (.*): (.*)"
                r = re.split(pattern, row)
                r = list(filter(None, r))

                for i in range(6):
                    r[i] = int(r[i])

                date_time = datetime(r[2], r[1], r[0], r[3], r[4], r[5])
                sender = r[6]
                text = r[7]

                message = Message(
                    date_time=date_time,
                    sender=sender,
                    media_url='',
                    media_type=''
                )

                message.add_part(text)

                chat.add_message(message)
            except Exception as err:
                raise (err)

        return chat
