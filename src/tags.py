start_tag = "<!---->"

# dict of tags for the md syntax of the cards
tags_md = {
    "card_begin": "# ",
    "card_section": "## ",
    "question_card": "{QUESTION}",
    "front": "{FRONT}",
    "back": "{BACK}",
    "bold": "**",
    "italic": "*",
    "strike": "~~",
    "heading1": "#",
    "heading2": "##",
    "heading3": "###",
    "heading4": "####",
    "heading5": "#####",
    "heading6": "######",
    "ulist1": "-",
    "ulist2": "+",
    "ulist3": "*",
    "code": "`",
}

# controls the file traversal
card_control = {"simple": False, "question": False, "back": False}

# html syntax that will replace md
tags_html = {"strike_begin": "<del>", "strike_end": "</del>"}
