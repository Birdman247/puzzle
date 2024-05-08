This is a crossword puzzle to go with my crossword solver program CrosswordHelper on python!
My crossword helper wound up not working to help with crosswords I found onine, but it did still support hosting a local website 
which could be useful for other applications. 

For a brief run through:

Cells are generated to create a 24x24 grid divided by column and row. Twelve words from my word list are chosen and the letters are each bound to a grid. 
The unbound cells change to black and don't allow input. CSS is used to format the grid and cells.
The horizontalWords array stores horizontal words and veritcalWords stores the vertical ones.
Each cell containing the start of a word displays a number corresponding to the word's position in either the horizontal or vertical list of words.
The descriptions of the horizontal and vertical words are displayed in a list: "descriptionList"
Each description is accompanied by a number to identify the word.
When a cell in the grid is clicked, the handleCellClick function is invoked.
If the clicked cell is not a black cell, a prompt allows the user to input a letter.
If the input letter is correct for the word associated with the cell, it is displayed in green.
If the input letter is incorrect, it is displayed in red.
If a word is completed (all its letters are correctly input, it is marked as completed.
The code for randmozing the cells which words were bound to is done by chatGPT. I could not get them to input without overlapping and creating partial words.

The python code is in a text file named crosswordhelper.py. 

It utilizes Flask and BeautifulSoup
Flask is a micro web framework for Python used for building web applications.
BeautifulSoup is a Python library for pulling data out of HTML and XML files.
My Github "temnplate" provides the interface and responses

Link to the repository for my Interface template: https://github.com/Birdman247/templates

My name is Zander Bird
You can email me at alexanderbird@lewisu.edu or at zanderbird1@gmail.com
I reserve all rights to the code and it is all original to me. I grant permission to anyone to use this code in their own way.
