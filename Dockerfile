FROM python:3.9.7

WORKDIR /dockerHangman
COPY /hangman.py /dockerHangman/

CMD ["python", "hangman.py"]