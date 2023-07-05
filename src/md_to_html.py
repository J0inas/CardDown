import markdown
from learningcards import *
from tags import tags_html


def mdToHtml(card_file: str, html_output: str):
    """
    converts the given md_file to a simple new html_file with the given output name
    - card_file is the filename of Markdown-File with cards
    - html_output is the filename of the HTML page that will be generated

    returns: file with html name
    """
    # load the md file
    md_str = load_one_file(card_file)
    # parse the md text into the cards
    md_cards = parse_md_cards(md_str)
    # parse the md_cards to html-text
    html_cards = parse_html_cards(md_cards)
    # write the html_cards into a new file
    html_file = open(html_output, "w")
    html_file.write(html_cards)
    html_file.close()

    return html_file


def card_content_to_html(content: LearningCard) -> str:
    """
    Converts markdown content of a card to html.

    returns: html in String format
    """
    replaced_content_img = replace_tag(
        content,
        tags_md["obsidian_img_begin"],
        tags_md["obsidian_img_end"],
        tags_md["img_begin"],
        tags_md["img_end"],
    )
    
    replaced_content = replace_tag (
        replaced_content_img,
        tags_md["link_file_begin"],
        tags_md["link_file_end"],
        tags_md["font_color_begin"],
        tags_md["font_color_end"],
    )
    
    html_content = markdown.markdown(replaced_content)
    
    final_html = replace_tag(
        html_content,
        tags_md["strike"],
        tags_md["strike"],
        tags_html["strike_begin"],
        tags_html["strike_end"],
    )
    return final_html


def parse_html_cards(learningcards: list) -> str:
    """
    parses the learningcards from list into html-string
    """
    html = ""
    print(html)

    for card in learningcards:
        # getting content front list
        front = LearningCard.get_front_content(card)
        back = LearningCard.get_back_content(card)

        # the simple solution with a library i hold very dear to my heart
        #  converts the md-syntax from the cards to html
        html += markdown.markdown(front) + "\n"
        html += markdown.markdown(back) + "\n"

        # exception: strike-case
        html = replace_tag(
            html, tags_md["strike"], tags_md["strike"], tags_html["strike_begin"], tags_html["strike_end"]
        )

    return html


def replace_tag(
    string: str, md_tag_begin: str, md_tag_end: str, tag_replacement_begin: str, tag_replacement_end: str
) -> str:
    # prints -1 if tag not found
    find = string.find(md_tag_begin)
    i = 1
    while find != -1:
        replace_tag = tag_replacement_begin
        # begin or end tag?
        if i % 2 == 0:
            replace_tag = tag_replacement_end
            i = 0
        if find != -1:
            string = string[:find] + replace_tag + " " + string[find + len(md_tag_end) :]
            i += 1
            # breakpoint()
        find = string.find(md_tag_end)
    return string


# Testing
# MD-Parser
# cards_md = load_card_file("cards.md")
# learningcards = parse_md_cards(cards_md)
# parse_html_cards(learningcards)
# LearningCard.print_to_console(learningcards)
# HTML converter
# mdToHtml("test_card.md", "example.html")
