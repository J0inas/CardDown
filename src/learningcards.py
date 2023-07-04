from file_loader import start_tag
from tags import tags_md, card_control


class LearningCard:
    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        return "=== ===\n" + str(self.front) + "----\n" + str(self.back)

    def set_front_content():
        pass

    def set_back_content():
        pass

    def get_front_content(self):
        return self.front

    def get_back_content(self):
        return self.back

    def get_content(self):
        return self.front + "\n" + self.back

    def is_valid(self):
        return self.front is not None and self.back is not None

    def print_to_console(cardlist):
        for x in range(len(cardlist)):
            print(cardlist[x].get_content() + "\n")


class SimpleCard(LearningCard):
    def __init__(self):
        super().__init__()
        self.front = None
        self.back = None

    def set_front_content(self, line):
        self.front = line

    def set_back_content(self, line):
        if self.back is None:
            self.back = line
        # lines get concatenated
        else:
            self.back += "\n" + line


class QuestionCard(SimpleCard):
    def __init__(self):
        super().__init__()
        self.front = None
        self.back = None

    def set_front_content(self, line):
        # line without front-tag
        self.front = line[0: (-len((tags_md.get("front"))))]
