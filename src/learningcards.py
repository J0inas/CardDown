from tags import tags_md, card_control
from file_loader import start_tag


def parse_md_cards(file_string: str) -> list:
    """
    returns: List of different LearningCards
    """
    learningcard_list = []

    # traversing through file, line by line
    for line in file_string.splitlines():
        # empty line skipped
        if line == "":
            continue

        if line == start_tag:
            continue

        # start tag of the card
        if line.startswith(tags_md["card_begin"]):

            card_control["simple"] = False
            card_control["question"] = False

            # new questioncard
            # checking last letters for the given question_card-tag

            if line.endswith(tags_md["question_card"]):
                # for card content
                card_control["question"] = True
                new_questioncard = QuestionCard()
                learningcard_list.append(new_questioncard)

            # new simplecard
            else:
                # for card content
                card_control["simple"] = True
                new_simplecard = SimpleCard()
                new_simplecard.set_front_content(line)
                learningcard_list.append(new_simplecard)

        elif line.startswith(tags_md["card_section"]):
            # content of questioncard
            if card_control["question"] is True:
                # if section-tag is detected
                if line.startswith(tags_md["card_section"]):
                    card_control["back"] = False

                    # if front-tag detected
                    if line.endswith(tags_md["front"]):
                        # function slices the string so that the front tag is removed
                        learningcard_list[len(learningcard_list) - 1].set_front_content(
                            line
                        )

                    # back
                    elif line.endswith(tags_md["back"]):

                        card_control["back"] = True

        elif card_control["back"] or card_control["simple"]:
            learningcard_list[len(learningcard_list) -
                              1].set_back_content(line)

    return learningcard_list


class LearningCard:
    def __init__(self):
        self.front = None
        self.back = None

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
