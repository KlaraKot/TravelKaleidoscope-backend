#create virtual environement <br />
`pip install virtualenv` <br />
`mkvirtualenv tk` <br />

#activate your virtual environment<br />
`workon tk` <br />

#install requirements<br />
`pip install -r requirements.txt` <br />

#for add new requirements<br />
`pip freeze > requirements` <br />

#create constraints <br />
`python manage.py install_labels` <br />

#run api server <br />
`python manage.py runserver` <br />

#open Django shell <br />
`python manage.py shell` <br />

<br />
<br />


# Kalejdoskop Podróży
Nasza aplikacja pozwala na wyszukiwanie najodpowiedniejszego miejsca do odwiedzenia, bazując na informacji podanej przez użytkownika, a także na doświadczeniach innych osób zarejestrowanych w systemie.

## Z perspektywy użytkownika
Aby skorzystać z aplikacji należy założyć konto oraz wypełnić krótką ankietę. Po zarejestrowaniu użytkownik otryzma listę najlepiej ocenianych miejsc na platformie. Może również oceniać miejsca klikając na liczbę gwiazdek (skala 1-5).


## Ankieta

Aplikacja wymaga założenia konta i wypełnienia krótkiej ankiety pozwalającej na określenie preferencji. Pytania zawarte w ankiecie to:
1. Ulubione miejsce?
2. Odwiedzone miejsca?
3. Preferowana pogoda?
4. Czy miejce ma być przystosowane do kwaterowania zwierząt?
5. Czy miejsce ma posiadać udogodnienia dla osoby niepełnosprawnej?


## Opinie
Każde miejsce odwiedzone przez użytkownika może zostać ocenione w skali 1 - 5 gwiazdek. Pozwoli nam to na lepsze dopasowywanie miejsc w przyszłości. 


## Kwestie techniczne
Backend aplikacji zostanie zaprogramowany w Pythonie, oraz przy użyciu Django REST framework, natomiast do wykonania frontendu wykorzystany zostanie typeScript oraz React. Systemem zarządzającym bazą danych jest MongoDB.

Poniżej diagram klas aplikacji:

![enter image description here](https://media.discordapp.net/attachments/893836286035640333/903968201937915966/unknown.png?width=1060&height=489)

OpenAPI:

https://app.swaggerhub.com/apis/KLARAKOT_1/Travel-Kaleidoscope/1.0.0#/


