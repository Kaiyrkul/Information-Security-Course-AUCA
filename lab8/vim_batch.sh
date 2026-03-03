#!/bin/bash
# Скрипт для автоматической нумерации строк в file.txt через Vim
vim -es +"set number" +"wq" file.txt
echo "Done! Line numbers added to file.txt without opening the editor."
