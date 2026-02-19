# Audio Converter

## Opis

Audio Converter to prosty program napisany w Pythonie, który pozwala na konwersję plików audio między różnymi formatami. Program automatycznie organizuje pliki w strukturze katalogów na podstawie metadanych (artysta, album, dysk) i zapisuje je w folderze `Export`. Wykorzystuje bibliotekę `pydub` do przetwarzania dźwięku oraz wielowątkowość dla szybszej konwersji.

### Główne funkcje:
- Konwersja plików audio (np. MP3, WAV, FLAC itp.).
- Pobieranie metadanych z tagów audio (artysta, album, tytuł).
- Interaktywne wprowadzanie metadanych, jeśli nie są dostępne.
- Organizacja plików w hierarchii katalogów: `Artysta/Album/discX/`.
- Równoległa konwersja z użyciem maksymalnie 8 procesów.
- Obsługa rekursywna dla podfolderów w katalogu `Source`.

## Wymagania

- Python 3.6 lub nowszy
- Biblioteka `pydub` (do instalacji: `pip install pydub`)
- `ffmpeg` lub `avconv` (wymagane przez pydub do obsługi audio; zainstaluj systemowo)

## Instalacja

1. Sklonuj lub pobierz repozytorium.
2. Zainstaluj zależności:
   ```
   pip install pydub
   ```
3. Upewnij się, że `ffmpeg` jest zainstalowany w systemie (np. poprzez Chocolatey na Windowsie: `choco install ffmpeg`).

## Użycie

1. Umieść pliki audio do konwersji w folderze `Source` (program utworzy go automatycznie, jeśli nie istnieje).
2. Uruchom program:
   ```
   python audio_conv.py
   ```
3. Program przeskanuje wszystkie podfoldery w `Source`, pobierze metadane i skonwertuje pliki.
4. Wyniki będą dostępne w folderze `Export`.

### Konfiguracja formatów
Domyślnie program konwertuje z MP3 na MP3. Aby zmienić formaty:
- Edytuj zmienne `wej` i `wyj` w kodzie (np. `wej = 'wav'`, `wyj = 'mp3'`).
- Możesz również odkomentować linie z `input()` dla interaktywnego wprowadzania formatów.

### Przykład
Załóżmy, że masz pliki MP3 w `Source/Artysta1/Album1/`:
- Program pobierze metadane.
- Jeśli metadane są niedostępne, zapyta o artystę, album itp.
- Skonwertuje pliki i zapisze w `Export/Artysta1/Album1/`.

## Struktura projektu
```
MyAudioConverter/
├── audio_conv.py    # Główny plik programu
├── README.md        # Ten plik
├── Source/          # Folder na pliki wejściowe (utworzony automatycznie)
└── Export/          # Folder na pliki wyjściowe (utworzony automatycznie)
```

## Uwagi
- Program działa rekursywnie na wszystkich podfolderach w `Source`.
- Jeśli metadane nie są dostępne, program pyta użytkownika o dane (nie jest w pełni automatyczny).
- Dla dużych kolekcji audio, konwersja może zająć czas, ale wielowątkowość przyspiesza proces.
- Upewnij się, że pliki audio nie są uszkodzone, aby uniknąć błędów.

## Licencja
Ten projekt jest dostępny na licencji MIT. Możesz go używać, modyfikować i dystrybuować zgodnie z warunkami licencji.

## Autor
[Twoje imię lub pseudonim] - Jeśli chcesz dodać kontakt lub więcej informacji.

Jeśli masz pytania lub problemy, sprawdź logi w konsoli lub zgłoś issue.