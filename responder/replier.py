import os.path
from abc import ABC, abstractmethod

from text_utils.text_filter import *
from .Chatgpt_Replier import investigator, newbies, bargainer, impatient

from secret import MAIL_ARCHIVE_DIR

text_filters = [
    RemoveSymbolLineTextFilter(),
    RemoveInfoLineTextFilter(),
    RemoveSensitiveInfoTextFilter(),
    RemoveSpecialPunctuationTextFilter(),
    RemoveStrangeWord(),
    MultiSymbolIntegrationTextFilter(),
]


class Replier(ABC):
    name = "AbstractReplier"

    @abstractmethod
    def _gen_text(self, prompt) -> str:
        print(f"Generating reply using {self.name}")
        return prompt

    def get_reply(self, content):
        for text_filter in text_filters:
            content = text_filter.filter(content)

        res = self._gen_text(content)

        if "[bait_end]" in res:
            res = res.split("[bait_end]", 1)[0]

        m = re.match(r"^.*[.?!]", res, re.DOTALL)
        if m:
            res = m.group(0)

        return res

    def get_reply_by_his(self, addr):
        with open(os.path.join(MAIL_ARCHIVE_DIR, addr + ".his"), "r", encoding="utf8") as f:
            content = f.read()
        return self.get_reply(content + "\n[bait_start]\n")


class ChatReplier1(Replier):
    name = "Investigator"

    def _gen_text(self, prompt) -> str:
        print(f"Generating reply using {self.name}")
        res = investigator(prompt)
        return res + "[bait_end]"


class ChatReplier2(Replier):
    name = "Newbies"

    def _gen_text(self, prompt) -> str:
        print(f"Generating reply using {self.name}")
        res = newbies(prompt)
        return res + "[bait_end]"


class ChatReplier3(Replier):
    name = "Bargainer"

    def _gen_text(self, prompt) -> str:
        print(f"Generating reply using {self.name}")
        res = bargainer(prompt)
        return res + "[bait_end]"


class ChatReplier4(Replier):
    name = "ImpatientConsumer"

    def _gen_text(self, prompt) -> str:
        print(f"Generating reply using {self.name}")
        res = impatient(prompt)
        return res + "[bait_end]"