from tags import tags_md, card_control
from learningcards import SimpleCard, QuestionCard


def get_cards_from_file(file_name: str, start_tag="") -> list:
    """
    Parser for the simple Markdown-Heading Card Syntax
    returns: List of different LearningCards
    """
    learningcard_list = []
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found, try again.")
        return []

    # traversing through file, line by line
    for line in file:

      # empty line skipped
        if line == "":
            continue
        if line == start_tag:

            continue

        if tags_md["seperator"] in line:
            card_control["simple"] = False

        # start tag of the card
        if line.startswith(tags_md["card_begin"]) or line.startswith(tags_md["card_section"]):

            card_control["simple"] = False

            # new questioncard
            # checking last letters for the given question_card-tag

            if line.rstrip().endswith(tags_md["question_card"]):
                # for card content
                card_control["question"] = True
                new_questioncard = QuestionCard()
                learningcard_list.append(new_questioncard)

            # content of questioncard
            if card_control["question"] is True:
                # if section-tag is detected
                if line.startswith(tags_md["card_section"]):
                    card_control["back"] = False

                    # if front-tag detected
                    if line.rstrip().endswith(tags_md["front"]):
                        # function slices the string so that the front tag is removed
                        learningcard_list[-1].set_front_content(
                            line
                        )

                    # back
                    elif line.rstrip().endswith(tags_md["back"]):

                        card_control["back"] = True

            # new simplecard
            else:
                # for card content
                card_control["simple"] = True
                card_control["question"] = False
                new_simplecard = SimpleCard()
                new_simplecard.set_front_content(line)
                learningcard_list.append(new_simplecard)

        elif card_control["back"] or card_control["simple"]:
            learningcard_list[-1].set_back_content(line)

        else:
            continue

    file.close()
    return learningcard_list
