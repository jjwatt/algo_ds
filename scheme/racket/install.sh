#!/bin/sh
set -e
wget https://mirror.racket-lang.org/installers/7.4/racket-7.4-x86_64-linux.sh
chmod +x racket-7.4-x86_64-linux.sh
./racket-7.4-x86_64-linux.sh
rm ./racket-7.4-x86_64-linux.sh
export PATH=$HOME/racket/bin:$PATH
# raco pkg install minikanren
# raco pkg install pie
# raco pkg install dracula
raco pkg install --auto beautiful-racket

