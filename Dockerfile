FROM python:3.9.7

WORKDIR /coolgame1
COPY /hangman.py /dockerHangman/

CMD ["python", "hangman.py"]
