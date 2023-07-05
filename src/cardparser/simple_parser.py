from tags import tags_md, card_control
from file_loader import start_tag
from learningcards import SimpleCard, QuestionCard


def get_cards_from_file(filepath: str) -> list:
    """
    Parser for the simple Markdown-Heading Card Syntax
    returns: List of different LearningCards
    """
    learningcard_list = []

    file = open(filepath, "r")

    # traversing through file, line by line
    for line in file:
        # empty line skipped
        if line == "":
            continue

        if line == start_tag:
            continue

        if tags_md["seperator"] in line:
            card_control["simple"] = False
            card_control["question"] = False

        # start tag of the card
        if line.startswith(tags_md["card_begin"]) or line.startswith(tags_md["card_section"]):

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
                        learningcard_list[-1].set_front_content(
                            line
                        )

                    # back
                    elif line.endswith(tags_md["back"]):

                        card_control["back"] = True

        elif card_control["back"] or card_control["simple"]:
            learningcard_list[-1].set_back_content(line)

    file.close()
    return learningcard_list
