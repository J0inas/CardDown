start_tag = "<!---->"

# dict of tags for the md syntax of the cards
tags_md = {
    "card_begin": "# ",
    "card_section": "## ",
    "seperator": "---",
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
    "obsidian_img_begin": "![[",
    "obsidian_img_end": "]]",
    "img_begin": '![](<',
    "img_end": '>)',
    "link_file_begin": "[[",
    "link_file_end": "]]",
    "font_color_begin": "<font color = #FF8C00>",
    "font_color_end": "</font>",
    "latex_in_md_begin" : "$",
    "latex_in_md_end" : "$",
    "latex_anki_begin" :" <anki-mathjax>",
    "latex_block" : "$$",
    "l_block_begin" : ' <anki-mathjax block="true">',
    "latex_anki_end" : "</anki-mathjax> ",
    "code_block_md" : "```",
    "code_html_begin" : " <pre> <code>",
    "code_html_end" : "</code> </pre> "
}

# controls the file traversal
card_control = {"simple": False, "question": False, "back": False}

# html syntax that will replace md
tags_html = {
    "strike_begin": "<del>",
    "strike_end": "</del>",
}
