# Persona1-text-tools Documentation

| Language                            | Link                                     |
| ----------------------------------- | ---------------------------------------- |
| English                             | [Documentation](#english)                |
| Русский                             | [Документация](#Русский)                 |
| 日本語                               | [ドキュメンテーション](#日本語)           |
| Русский дореформенный               | [Документація](#)             |
| Esperanto                           | [Dokumentado](#Esperanto)                |
| Українська                          | [Документація](#Українська)               |
| Latine                              | [Documentatio](#Latine)                   |
| Русский стихотворный                | [Документация в стихах](#Русский стихотворный) |
| "Горе от кода"                      | ["Горе от кода"](#"Горе от кода")          |
|"Горе от кода" (в пересказе DeepSeek)|["Горе от кода"](#"Горе от Кода" (в пересказе DeppSeek))        |

---

## English

### Persona1-text-tools

**Persona1-text-tools** is a Python module for working with text strings and binary files in Persona 1. It provides tools for extracting, modifying, and reinserting text.

### Installation
```bash
pip install Persona1-text-tools
```

### Available Functions

#### Parsing Event Strings
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Extracts event strings and saves them as `output.json` and `output.txt`.

#### Injecting Event Strings
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Inserts modified JSON text back into the binary file.

#### Working with BIN Files
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Extracts binary files

to_bin("extracted_folder")  # Rebuilds a BIN file
```

#### Command-line Usage
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Русский

### Persona1-text-tools

**Persona1-text-tools** – это Python-модуль для работы с текстами и бинарными файлами Persona 1. Он позволяет извлекать, редактировать и вставлять строки.

### Установка
```bash
pip install Persona1-text-tools
```

### Доступные функции

#### Парсинг строк событий
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Извлекает строки событий и сохраняет их в `output.json` и `output.txt`.

#### Инъекция строк событий
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Вставляет строки из JSON обратно в бинарный файл.

#### Работа с BIN-файлами
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Извлекает бинарные файлы

to_bin("extracted_folder")  # Собирает BIN-файл обратно
```

#### Использование в командной строке
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## 日本語

### Persona1-text-tools

**Persona1-text-tools** は、Persona 1 のテキストデータおよびバイナリファイルを処理するための Python モジュールです。
テキストの抽出、編集、再挿入の機能を提供します。

### インストール
```bash
pip install Persona1-text-tools
```

### 利用可能な機能

#### イベントテキストの解析
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
バイナリファイルからイベントテキストを抽出し、`output.json` と `output.txt` に保存します。

#### イベントテキストの挿入
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
JSONファイルのテキストをバイナリファイルに挿入します。

#### BINファイルの処理
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # バイナリファイルを抽出

to_bin("extracted_folder")  # BINファイルを再構築
```

#### コマンドラインの使用方法
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Русский дореформенный

### Persona1-text-tools

**Persona1-text-tools** – сіе модуль для работы съ текстами и бінарными файлами изъ игры Persona 1. Онъ позволяетъ извлекать, редактироватьъ и вставлять строки.

### Установкѣ
```bash
pip install Persona1-text-tools
```

### Доступныя функции

#### Парсингъ строкъ событій
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Извлекаетъ строки событій и сохраняетъ ихъ въ `output.json` и `output.txt`.

#### Инъекція строкъ событій
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Вставляетъ строки изъ JSON обратно въ бінарный файлъ.

#### Работа съ BIN-файлами
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Извлекаетъ бінарные файлы

to_bin("extracted_folder")  # Собираетъ BIN-файлъ обратно
```

#### Употребленіе въ командной строкѣ
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Esperanto

### Persona1-text-tools

**Persona1-text-tools** estas Python-modulo por labori kun tekstaj ĉenoj kaj binaraj dosieroj en Persona 1. Ĝi disponigas ilojn por ekstrakti, modifi kaj reenmeti tekston.

### Instalado
```bash
pip install Persona1-text-tools
```

### Haveblaj Funkcioj

#### Analizado de Eventaj Ĉenoj
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Ekstraktas eventajn ĉenojn kaj konservas ilin kiel `output.json` kaj `output.txt`.

#### Enmeto de Eventaj Ĉenoj
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Enmetas modifitajn JSON-ĉenojn reen en la binaran dosieron.

#### Laborado kun BIN-dosieroj
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Ekstraktas binarajn dosierojn

to_bin("extracted_folder")  # Rekonstruas BIN-dosieron
```

#### Uzado en la Komandlinio
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Українська

### Persona1-text-tools

**Persona1-text-tools** — це Python-модуль для роботи з текстовими рядками та бінарними файлами в Persona 1. Він надає інструменти для витягування, редагування та повторного вставлення тексту.

### Встановлення
```bash
pip install Persona1-text-tools
```

### Доступні функції

#### Парсинг рядків подій
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Витягує рядки подій і зберігає їх у `output.json` та `output.txt`.

#### Вставка рядків подій
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Вставляє рядки з JSON назад у бінарний файл.

#### Робота з BIN-файлами
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Витягує бінарні файли

to_bin("extracted_folder")  # Збирає BIN-файл назад
```

#### Використання в командному рядку
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Latine

### Persona1-text-tools

**Persona1-text-tools** est Python modulo ad operandum cum textibus et fasciculis binariis in Persona 1. Praebet instrumenta ad extrahendum, mutandum et iterum insertandum textum.

### Instauratio
```bash
pip install Persona1-text-tools
```

### Functiones Disponibiles

#### Parsatio Eventuum
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Extrahit eventuum textus et eos servat ut `output.json` et `output.txt`.

#### Iniectio Eventuum
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Inserit textus mutatos ex JSON in fasciculum binarium.

#### Operatio cum BIN Fasciculis
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Extrahit fasciculos binarios

to_bin("extracted_folder")  # Redintegrat fasciculum BIN
```

#### Usus in Linea Comandorum
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

---

## Русский стихотворный

### Вступление

Внимание, о, читатель! Внимай! Слушай, как я тебе вещаю: Модуль есть, что текстами играет, Persona1-text-tools зовется. В Python'е он живет и процветает, С ним строки ты редактировать научишься. Скачай его, и путь откроется:

```bash
pip install Persona1-text-tools
```
Так начни же, не теряй ни дня!

### Доступные функции

#### Парсинг строк событий
Ты хочешь строки из игры извлечь? Смело к делу приступай, не робей! В Python'е код напишешь ты такой:
```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```
Вот и все! Строки в JSON и TXT Сохранятся, ждут тебя, как светлый путь. Не забудь про кодировку свою, Чтоб все было верно, как в мечтах твоих.

#### Инъекция строк событий
Теперь, когда ты строки извлек, В игру их вставить ты готов. С JSON'ом в руках, вперед иди:
```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```
Вот и все! Строки вернутся в файл, Игра твоя обновится, как мечта. Не забудь про кодировку свою, Чтоб все было верно, как в мечтах твоих.

#### Работа с BIN-файлами
```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Извлекает бинарные файлы

to_bin("extracted_folder")  # Собирает BIN-файл обратно
```
Вот и все! Файлы будут у тебя, Как хочешь, так и обрабатывай. Не забудь про кодировку свою, Чтоб все было верно, как в мечтах твоих.

#### Использование в командной строке
Ты любишь командную строку? С ней работать ты привык? Вот команды, что тебе помогут:
```
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```
Вот и все! Команды просты, С ними ты все сделаешь, как надо. Не забудь про кодировку свою, Чтоб все было верно, как в мечтах твоих.


---

## "Горе от Кода"

*(Сатирическая документация в стиле грибоедовской комедии)*

---

### ДЕЙСТВИЕ I. ПРОЛОГ МОДУЛЯ   
**Чацкий**, _вбегая с ноутбуком в руках, обращается к толпе разработчиков:_

> "О вы, чьи руки жаждут текстов власти,  
> Кто файлы бинарные рвётся покорить —  
> Услышьте глас прогресса и страсти!  
> Мой инструмент поможет вам творить.  

> **Persona1-text-tools** — вот имя дивной силы,  
> Что строки спрятанные извлечёт,  
> Как ключ, что отпирает мрачные могилы  
> Где текст под бинарным кодом стонет и живёт.  

> Установите смело, не робейте:  
> `pip install Persona1-text-tools` —  
> И Пайтон вам крылья даст скорее,  
> Чем Фамусову служба чины и престол!  

> Пусть завидует Скалозуб-стажёр,  
> Что в консоли команды, как шпаги, остры —  
> Мы кодом, как Чацкий, взорвём договор  
> Меж человеком и машиной хитросплетённой споры!"  

---

### ДЕЙСТВИЕ II. ПАРСИНГ СТРОК   
_Чацкий размахивает файлом gamefile.bin, обращаясь к Софье-IDE:_

> "Смотрите же! Сияет encoding.tbl,  
> Как древний свиток магов в час луны.  
> Командой `parse_event_strings` — без лишних слов —  
> Мы вырвем текст из бинарной тишины!  

> Извлечь строки? Легче, чем правду в салоне Фамусова:  
> output.txt и JSON — вот двойной улов.  
> Как Чацкий, что истину режет без покрова,  
> Мой код разорвёт оковы бинарных основ!  

> Пусть Репетиловы твердят: «Нельзя! Не смейте!» —  
> Мы смело файлы в тексты превратим.  
> И даже Молчалин, склонившись в тайной ревности,  
> Признает: парсинг здесь непобедим!"  

---

### ДЕЙСТВИЕ III. ИНЪЕКЦИЯ ПОЭЗИИ   
_Чацкий в ярости стучит по клавиатуре, сравнивая JSON с любовным письмом:_

> "О времена! О файлы! Где ж ваш стыд?  
> Чтоб строки в бинарник вернуть обратно —  
> `inject_event_strings` пусть будет вам щит,  
> Как Чацкий — защитник истины непонятой!  

> Возьмите output.json — святой грааль изменений,  
> encoding.tbl — компас в море кодов.  
> И пусть ваш бинарник, как бал у Хлестовой,  
> Заискрится текстами новых стихов!  

> Не страшны нам ошибки, как сплетни в салоне —  
> Мы в файл вольём и метафоры, и страсть.  
> Пусть шепчут: «Он сумасшедший!» — в тихом ужасе,  
> Но код наш будет вечно в репозитории красоваться!"  

---

### ДЕЙСТВИЕ IV. БИНАРНЫЕ МЕТАМОРФОЗЫ   
_Чацкий танцует с папкой extracted_folder, пародируя Фамусова:_

> "Разберите BIN-файл! Пусть каждый байт  
> Предстанет, как дворянин на балу —  
> Команда `from_bin` сорвёт с секретов флёр,  
> А `to_bin` соберёт их вновь к исходному числу!  

> Как Чацкий, что видит суть за мишурой чинов,  
> Мой код распотрошит game.BIN до нитки.  
> И даже Скалозуб-сисадмин, скрепя сердце,  
> Признает: бинарник наш — не крепостной уклад!"  

---

### ЭПИЛОГ. КОМАНДНАЯ СТРОКА КАК ПОЭМА   
_Чацкий уезжает, оставляя консоль открытой:_

> "Прощай, Москва кодировок пыльная!  
> parse-event-strings — мой последний монолог.  
> inject-event-strings — как выстрел в зал фамусовский,  
> bin-tool import/export — финальный эпилог.  

> Пусть Молчалины шепчут: «Не надо новшеств!»,  
> А Лиза-IDE тайком сохранит наш след.  
> Кто понял — в репозиторий звезду поставит,  
> Кто нет — пусть читает Грибоедова впредь!"  

---

**Примечание автора-переводчика**:  
> "Сей текст — не буквальный перевод, но дух документации,  
> Облечённый в ямб четырёхстопный, как в «Горе» грибоедовском.  
> Чтоб merge request ваш, как Чацкий, пробил сердце main-ветки,  
> А код ваш стал бессмертным, как классика в мире цифровом!" 




---


## "Горе от Кода" (в пересказе DeppSeek)

Вот перевод документации `Persona1-text-tools`, выполненный в стиле "Горя от ума", с использованием стихотворного слога и фраз из произведения Грибоедова.

### Persona1-text-tools – Модуль, в котором Python зарыт, как клад!

(_Явление 1. Гостиная в доме Фамусова. Чацкий входит._)

Ах! Этот Python! Что за дивная машина!
Для текста, для бинарных файлов – господин!
**Persona1-text-tools** – вот имя горделиво,
Что строки извлекает так игриво!

Редактировать, вставлять – всё может он, поверьте,
Как будто пишет заново бессмертье!
И если текст вам нужно изменить,
То этот модуль – дар, что не купить!

Как Чацкий я, стремлюсь к познаньям новым,
И этот модуль мне, как воздух, нужен словом!
Чтоб строки извлекать, как золото из руд,
И в файлы BIN вдохнуть вдруг новый труд!

О, век! О, нравы! Модули плодятся,
И каждый что-то новое творится.
Но этот – исключенье, без сомненья,
В нём вижу я прогресса откровенье!

Как Фамусов, твердят: "Ученье – свет!"
Но что есть свет, когда и пользы нет?
А здесь и польза, и красы не счесть,
И с этим модулем приятно жить и есть!

Я вижу, как София смотрит с укоризной,
Но мне важны лишь истины отчизны!
И если модуль этот – часть прогресса,
То буду я хвалить его без стресса!

Пускай Молчалин шепчет там украдкой,
Что лучше старый метод, чем накладка,
Но я скажу вам прямо, без затей,
Что этот модуль – лучше всех затей!

Как Скалозуб, он крепок и надёжен,
И в мире текста он совсем не гож?
Он словно генерал, что знает дело,
И строки правит так умело!

Ах, господа! Зачем нам эти споры?
Когда есть модуль, что решает горы!
Проблем с текстами, с файлами бинарными,
Он словно маг, с решениями дарными!

И я, как Чацкий, буду продвигать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этом модуле – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире текста будем словно я!
Свободны, смелы, полны вдохновенья,
И модулем творить свои творенья!

Как Лизанька, он лёгок и послушен,
И в сложных задачах совсем не скушен!
Он словно друг, что помогает в деле,
И строки правит в самом лучшем виде!

Ах, Фамусов, зачем ты так сердит?
Когда есть модуль, что нам всем годит!
Он словно зеркало, что отражает,
Всю суть бинарных файлов открывает!

И я, как Чацкий, буду настаивать,
Что этот модуль нужно развивать!
Ведь в нём потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И этот модуль – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире текста он совсем не тём!
Он словно гений, что творит чудесно,
И строки правит так прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть модуль, что решает споры!
Проблем с текстами, с файлами бинарными,
Он словно маг, с решениями дарными!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этом модуле – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире текста будем словно я!
Свободны, смелы, полны вдохновенья,
И модулем творить свои творенья!

### Установка

(_Явление 2. Фамусов и Чацкий._)

```bash
pip install Persona1-text-tools
```

Что нового покажет нам сей "pip"?
Установка проста, лишь в код взгляни ты!
Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но код – он лучше в раз!

Вот "pip install" – команда нехитрая,
Как Скалозуб, она всегда упёртая!
Установит модуль вам в момент,
И станет он помощник, аргумент!

Ах, этот "pip"! Как много в нём чудес,
Он словно маг, что к знаньям нас вознёс!
Установит всё быстро и легко,
И станет вам на сердце хорошо!

Как Молчалин, он тих и незаметен,
Но дело делает, хоть не приметен!
Установит модуль, без сомненья,
И станет вам доступно обученье!

Пусть София твердит, что это скучно,
Но я скажу вам прямо, без прискучки,
Что этот "pip" – помощник верный мой,
И с ним я буду, как герой!

Как Лизанька, он быстр и точен,
И в установке он совсем не мочен!
Он словно ветер, что летит вперёд,
И модуль нам в мгновенье принесёт!

Ах, Фамусов, зачем ты так ворчишь?
Когда есть "pip", что нам всем годишь!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

И я, как Чацкий, буду настаивать,
Что этот "pip" нужно прославлять!
Ведь в нём потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И этот "pip" – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И модуль ставит так прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть "pip", что решает споры!
Проблем с установкой, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этом "pip" – залог успеха,
И с ним установка – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И "pip"-ом творить свои творенья!

Что нового покажет нам сей "pip"?
Установка проста, лишь в код взгляни ты!
Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но код – он лучше в раз!

Вот "pip install" – команда нехитрая,
Как Скалозуб, она всегда упёртая!
Установит модуль вам в момент,
И станет он помощник, аргумент!

Ах, этот "pip"! Как много в нём чудес,
Он словно маг, что к знаньям нас вознёс!
Установит всё быстро и легко,
И станет вам на сердце хорошо!

Как Молчалин, он тих и незаметен,
Но дело делает, хоть не приметен!
Установит модуль, без сомненья,
И станет вам доступно обученье!

Пусть София твердит, что это скучно,
Но я скажу вам прямо, без прискучки,
Что этот "pip" – помощник верный мой,
И с ним я буду, как герой!

Как Лизанька, он быстр и точен,
И в установке он совсем не мочен!
Он словно ветер, что летит вперёд,
И модуль нам в мгновенье принесёт!

Ах, Фамусов, зачем ты так ворчишь?
Когда есть "pip", что нам всем годишь!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

И я, как Чацкий, буду настаивать,
Что этот "pip" нужно прославлять!
Ведь в нём потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И этот "pip" – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И модуль ставит так прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть "pip", что решает споры!
Проблем с установкой, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этом "pip" – залог успеха,
И с ним установка – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И "pip"-ом творить свои творенья!

### Доступные функции

(_Явление 3. Чацкий и Молчалин._)

#### Парсинг строк событий

(_Чацкий входит, оглядываясь._)

```python
from Persona1_text_tools import parse_event_strings
parse_event_strings("gamefile.bin", "encoding.tbl")
```

Ах! Парсинг строк событий – вот задача!
Как разобрать всё это, неудача?
Но модуль наш поможет, без сомненья,
И строки извлечёт он, без сомненья!

Как Молчалин, он тих и незаметен,
Но дело делает, хоть не приметен!
Извлечёт он строки из файла BIN,
И в JSON их сложит, как один!

"gamefile.bin" – вот имя файла,
Где строки спят, как будто в коконе, тайно!
"encoding.tbl" – таблица кодов,
Что даст нам ключ к разгадке переходов!

Как Скалозуб, он крепок и надёжен,
И в парсинге он вовсе не гож?
Он разберёт всё чётко и умело,
И строки выдаст нам он в дело!

Ах, София, что ты знаешь о парсинге?
Когда в нём столько тайн и разногласий!
Но модуль наш развеет все сомненья,
И даст нам ключ к разгадке разуменья!

Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но парсинг – лучше в раз!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

"output.json" – вот имя файла,
Куда все строки сложатся удало!
"output.txt" – в нём текст простой найдётся,
И каждый в нём легко прочтётся!

И я, как Чацкий, буду настаивать,
Что парсинг строк нужно прославлять!
Ведь в нём потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И парсинг строк – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И строки парсит так прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть парсинг, что решает споры!
Проблем с текстами, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этом парсинге – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И парсингом творить свои творенья!

#### Инъекция строк событий

(_Явление 4. Чацкий и София._)

```python
from Persona1_text_tools import inject_event_strings
inject_event_strings("gamefile.bin", "output.json", "encoding.tbl")
```

Ах! Инъекция строк – что за задача!
Как строки в файл вставить, удача?
Но модуль наш поможет, без сомненья,
И строки вставит он, без сомненья!

Как София, она смотрит свысока,
Но инъекция – наука нелегка!
Вставит строки в файл BIN обратно,
И станет он как новый, аккуратно!

"gamefile.bin" – вот имя файла,
Куда все строки вернуться удало!
"output.json" – в нём строки все хранятся,
И в файл BIN они все возвращаются!

Как Скалозуб, он крепок и надёжен,
И в инъекции он вовсе не гож?
Он вставит всё чётко и умело,
И строки выдаст нам он в дело!

Ах, София, что ты знаешь об инъекции?
Когда в ней столько тайн и комплектации!
Но модуль наш развеет все сомненья,
И даст нам ключ к разгадке разуменья!

Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но инъекция – лучше в раз!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

"encoding.tbl" – таблица кодов,
Что даст нам ключ к разгадке переходов!
И строки все на место встанут,
И файл BIN как новый станет!

И я, как Чацкий, буду настаивать,
Что инъекцию строк нужно прославлять!
Ведь в ней потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И инъекция строк – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И строки вставит так прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть инъекция, что решает споры!
Проблем с текстами, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь в этой инъекции – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И инъекцией творить свои творенья!

#### Работа с BIN-файлами

(_Явление 5. Чацкий и Фамусов._)

```python
from Persona1_text_tools import from_bin, to_bin
from_bin("game.BIN")  # Извлекает бинарные файлы

to_bin("extracted_folder")  # Собирает BIN-файл обратно
```

Ох, BIN-файлы, что за диво!
Как извлечь их, чтоб не сгореть ретиво?
Но модуль наш поможет, без сомненья,
И BIN-файлы разложит, без сомненья!

Как Фамусов, он строго смотрит,
Но BIN-файлы модуль наш не портит!
Извлечёт он файлы из BIN-архива,
И сложит их по папкам учтиво!

"game.BIN" – вот имя файла,
Где файлы спят, как будто в коконе тайно!
"from_bin" – команда, что извлечёт,
И в папку их отдельную сложит в счёт!

Как Скалозуб, он крепок и надёжен,
И с BIN-файлами он вовсе не гож?
Он разберёт всё чётко и умело,
И файлы выдаст нам он в дело!

Ах, София, что ты знаешь о BIN-файлах?
Когда в них столько тайн и лабиринтов тайных!
Но модуль наш развеет все сомненья,
И даст нам ключ к разгадке разуменья!

Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но BIN-файлы – лучше в раз!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

"extracted_folder" – вот имя папки,
Куда все файлы сложатся в охапке!
"to_bin" – команда, что соберёт,
И в BIN-файл их снова унесёт!

И я, как Чацкий, буду настаивать,
Что с BIN-файлами нужно прославлять!
Ведь в них потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И с BIN-файлами – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И BIN-файлы разложит прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть BIN-файлы, что решают споры!
Проблем с извлечением, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь с BIN-файлами – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И с BIN-файлами творить свои творенья!

#### Использование в командной строке

(_Явление 6. Чацкий и все._)

```bash
parse-event-strings gamefile.bin encoding.tbl
inject-event-strings gamefile.bin output.json encoding.tbl
bin-tool import extracted_folder
bin-tool export game.BIN
```

Ах! Командная строка – что за картина!
Как строки запустить, чтоб не застила?
Но модуль наш поможет, без сомненья,
И команды выполнит он, без сомненья!

Как все глядят с удивленьем на меня,
Но командная строка – вот где броня!
Запустит парсинг, инъекцию и BIN-tool,
И всё исполнит он, как верный слуга, cool!

"parse-event-strings" – команда первая,
Что строки извлечёт, как будто дева!
"gamefile.bin" – файл, где строки спят,
"encoding.tbl" – ключ, что даст им взгляд!

Как Скалозуб, он крепок и надёжен,
И в командной строке он вовсе не гож?
Он выполнит всё чётко и умело,
И результат покажет нам он в дело!

Ах, София, что ты знаешь о командах?
Когда в них столько тайн и улик на планах!
Но модуль наш развеет все сомненья,
И даст нам ключ к разгадке разуменья!

Как Фамусов, скажу я вам сейчас:
"Ученье – свет", но команды – лучше в раз!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

"inject-event-strings" – команда номер два,
Что строки вставит в файл, как трава!
"output.json" – файл, где строки ждут,
"encoding.tbl" – ключ, что путь им тут!

"bin-tool import" – команда третья,
Что файлы в BIN соберёт, как дети!
"extracted_folder" – папка, где файлы спят,
И в BIN-файл они все полетят!

"bin-tool export" – команда номер четыре,
Что файлы из BIN извлечёт в мире!
"game.BIN" – файл, где файлы хранятся,
И в папку их отдельную они все возвратятся!

И я, как Чацкий, буду настаивать,
Что командную строку нужно прославлять!
Ведь в ней потенциал огромный скрыт,
И с ним наш мир бинарный будет слит!

Пусть старый мир твердит: "Зачем нам это?"
Но новое всегда найдёт ответы!
И командная строка – словно луч надежды,
Что освещает тёмные невежды!

Как София, он прекрасен и умён,
И в мире кода он совсем не тём!
Он словно гений, что творит чудесно,
И команды выполнит прелестно!

Ах, господа! Зачем нам эти ссоры?
Когда есть команды, что решают споры!
Проблем с выполнением, нет больше их,
Он словно маг, что ставит в миг!

И я, как Чацкий, буду воспевать
Всё то, что может пользу людям дать!
Пусть старый мир твердит своё упрямо,
Но новое всегда пробьётся прямо!

Ведь с командной строкой – залог успеха,
И с ним работа – вовсе не помеха!
Он словно ключ, что двери открывает,
И мир бинарный нам он представляет!

Так будем же использовать его, друзья,
И в мире кода будем словно я!
Свободны, смелы, полны вдохновенья,
И командами творить свои творенья!
