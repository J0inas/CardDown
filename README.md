# CardDown
 A tool to create Anki-LearningCards from Markdown-Files.
 Provide a single file or path into the program and get a stack of Anki-Cards in return!
 Very useful if you want to get some flashcards out of your [Obsidian](https://obsidian.md/) notes or other note taking apps based on markdown.

## Installation

## Usage
### Simple Parser
At some point in your file there needs to be a `<!---->` for the program to recognize it as a flashcard and a chosen tag e.g. `#test` that determines the belonging stack of the flashcards.
We recommend to write it at the very beginning or very end.
Then just write your normal notes.
Everything in the heading `# ` or `## ` will be your question.
The following content is your answer, meaning the backside of the card.
(you can change these up to preference in the `tags.py` file.)

### Block Parser

## Development

 ### What is the current status?
The most needed requirements are done or at least close to finish.
That encludes full support for Obsidian-syntax elements.

 ### What is the next goal?
Test the product, look for bugs and ultimately make slight improvements.
Adding a GUI for quicker usage and broader appeal.
Updating Read-Me with images.

 ### What is the motivation behind this project?
 We are computer science students who want to use this tool to create flashcards in anki through our notes from Obsidian and other Markdown-Editors without the extra effort of typing out every flashcard. 
 Instead we wrote a programm that create the flashcards for us from our notes.
