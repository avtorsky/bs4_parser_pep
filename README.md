# Парсер документации Python

[Описание](#описание) /
[История изменений](#история-изменений) /
[Развернуть локально](#развернуть-локально) /
[Документация](#документация)


## Описание

Парсер [bs4_parser_pep](https://github.com/avtorsky/bs4_parser_pep) собирает данные с ресурсов [https://docs.python.org/3/](https://docs.python.org/3/), [https://peps.python.org/](https://peps.python.org/) и работает в четырёх режимах:

* whats-new - получить список изменений Python
* latest-versions - получить список версий Python и ссылки на документацию
* download - скачать архив с документацией в папку ./downloads
* pep - получить список статусов документов PEP и количество документов каждого статуса

## История изменений

Release 20230115:
* feat(./src/main.py): подготовлен режим парсинга статусов документов PEP и количества документов каждого статуса

## Развернуть локально

Склонировать проект, создать виртуальное окружение и проинициализировать зависимости:

```bash
git clone https://github.com/avtorsky/bs4_parser_pep.git
cd bs4_parser_pep
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Документация

Парсер запускается из директории ./src/

```bash
usage: main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
