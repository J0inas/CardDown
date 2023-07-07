import markdown
from learningcards import *
from tags import tags_html
from file_loader import is_valid_cardfile
from cardparser import simple_parser


def mdToHtml(card_file: str, html_output: str):
    """
    converts the given md_file to a simple new html_file with the given output name
    - card_file is the filename of Markdown-File with cards
    - html_output is the filename of the HTML page that will be generated

    returns: file with html name
    """
    # load the md file
    md_str = is_valid_cardfile(card_file)
    # parse the md text into the cards
    md_cards = simple_parser.get_cards_from_file(md_str)
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
    img_content = replace_tag(
        content,
        tags_md["obsidian_img_begin"],
        tags_md["obsidian_img_end"],
        tags_md["img_begin"],
        tags_md["img_end"],
    )
    
    replaced_content = replace_tag (
        img_content,
        tags_md["link_file_begin"],
        tags_md["link_file_end"],
        tags_md["font_color_begin"],
        tags_md["font_color_end"],
    )
    
    latex_content = replace_tag(
        replaced_content,
        tags_md["latex_in_md_begin"],
        tags_md["latex_in_md_end"],
        tags_md["latex_anki_begin"],
        tags_md["latex_anki_end"],
    )
    
    html_content = markdown.markdown(latex_content)
    
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
    # -1 if tag not found
    find = string.find(md_tag_begin)
    i = 1
    while find != -1:
        if i % 2 == 0:
            string = string[:find] + tag_replacement_end + string[find + len(md_tag_end):]
            print(string)
            find = string.find(md_tag_begin)
            i = 1
        else:
            string = string[:find] + tag_replacement_begin + string[find + len(md_tag_end):]
            print (string)
            i += 1
            find = string.find(md_tag_end)
       
    return string

"""
replace_tag - Test
---

"""
test_string = "Das ist ein [[Test]] für [[Latex]]: WTF passiert hier $frac12$ nennt man auch Einhalb. $\pi$ ist kleiner als drei Äpfel!"
# test_string = "Das ist ein [[Test]] für [[Latex]]"
test_tag = replace_tag(
    test_string,
    tags_md["latex_in_md_begin"],
    tags_md["latex_in_md_end"],
    tags_md["latex_anki_begin"],
    tags_md["latex_anki_end"],
    )

replaced_content = replace_tag (
        test_tag,
        tags_md["link_file_begin"],
        tags_md["link_file_end"],
        tags_md["font_color_begin"],
        tags_md["font_color_end"],
    )

print (replaced_content)