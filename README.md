# Discarium website

Strona produktu, nowości, pomoc, formaty, polityka prywatności i źródła aplikacji **Discarium: Lossless Player**. Statyczny HTML/CSS, mały skrypt galerii, bez frameworka, usług analitycznych, cookies i zewnętrznych fontów. Publiczny kontakt: **discarium@pisz.to**.

Aktualizacja treści: **8 października 2026**. Wersja **1.0 (24)** jest dostępna w App Store; **1.1 (28)** czeka na App Review. Strona ma zweryfikowany odnośnik do sklepu i historię zmian w `updates.html`. Zmiany tego commita wymagają pusha oraz ręcznego deploymentu przez właściciela.

## Uruchom lokalnie

Wymagany Python 3.10 lub nowszy. Brak pakietów do instalowania.

```sh
python3 scripts/build.py
python3 scripts/verify.py
python3 -m http.server 8875 --directory site
```

Otwórz http://localhost:8875. Gotowe pliki HTML są również zapisane w `site/`, więc samo wyświetlenie strony nie wymaga generatora. `node --check site/assets/site.js` opcjonalnie sprawdza składnię galerii.

## Push i deployment — wykonuje właściciel

Repozytorium: https://github.com/PawelFaron/DiscariumWebPage

1. W tym repo wykonaj `git push -u origin main`.
2. GitHub → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. GitHub → **Actions → Deploy GitHub Pages → Run workflow → main**.
4. Poczekaj na zielony wynik i otwórz adres z kroku `Deploy`. Sprawdź stronę w prywatnym oknie, bez logowania do GitHuba.
5. W Pages sprawdź **Enforce HTTPS**, jeśli GitHub pokazuje tę opcję. Dla adresu `github.io` HTTPS jest zapewniane przez GitHub.

Deployment jest **ręczny**. Push uruchamia wyłącznie sprawdzenie plików. Witryna została opublikowana i sprawdzona 6 października 2026: https://pawelfaron.github.io/DiscariumWebPage/.

**Jeśli zamiast strony pojawia się ten README:** Pages publikuje główny katalog gałęzi. Ustaw Source na **GitHub Actions** i uruchom workflow **Deploy GitHub Pages** — publikuje on gotową witrynę z `site/`. Nie wybieraj `Deploy from a branch → main → / (root)`. Ta konfiguracja została już poprawiona w repozytorium.

Docelowe adresy po poprawnym wdrożeniu:

| App Store Connect | Adres |
|---|---|
| Marketing URL | https://pawelfaron.github.io/DiscariumWebPage/ |
| Support URL | https://pawelfaron.github.io/DiscariumWebPage/support.html |
| Privacy Policy URL | https://pawelfaron.github.io/DiscariumWebPage/privacy.html |
| User Privacy Choices URL (opcjonalne) | https://pawelfaron.github.io/DiscariumWebPage/privacy.html#choices |

**Nie wklejaj adresów do zgłoszenia Apple przed sprawdzeniem, że rzeczywiście działają.** Dla tvOS Apple wymaga również tekstu w polu **Apple TV Privacy Policy**. Wersja do wklejenia: [`docs/apple-tv-privacy.txt`](docs/apple-tv-privacy.txt). Całe wymagania i źródła Apple: [`docs/APPLE-REQUIREMENTS.md`](docs/APPLE-REQUIREMENTS.md).

## Edycja

- Treść podstron: `src/pages/*.html`.
- Wspólny nagłówek, metadane i stopka: `src/template.html`.
- Adres strony, odnośnik App Store, publiczny e-mail i data polityki: `src/config.json`.
- Styl i galeria: `site/assets/site.css`, `site/assets/site.js`.
- Logo, zrzuty i obraz podglądu linku: `site/assets/`; pochodzenie w [`docs/ASSETS.md`](docs/ASSETS.md).
- Zawsze po edycji treści uruchom `python3 scripts/build.py`, a następnie `python3 scripts/verify.py`. Commituj również wygenerowane strony w `site/`.
- Gdy zmieniasz domenę lub nazwę repo, zmień `base_url` i przebuduj strony. Zwykłe odnośniki są względne; canonical, Open Graph, sitemap i strona 404 korzystają z `base_url`.

Teksty są po angielsku, zgodnie z głównym językiem sklepu. Informacja o sześciu językach dotyczy interfejsu aplikacji. Strona prezentuje obsługiwane funkcje, zrzuty aplikacji i instrukcję konfiguracji kolekcji. Link `https://apps.apple.com/app/id6819356965` został sprawdzony po publikacji 1.0. Nowości 1.1 są oznaczone jako oczekujące na zatwierdzenie.

Po publikacji 1.1 zaktualizuj status w `src/pages/updates.html`, zapowiedź na stronie głównej oraz wersję w `source.html`. W `support.html` i `compatibility.html` usuń oznaczenia „Coming in”, zachowując wskazówki dla użytkowników starszej wersji. Nie zmieniaj daty polityki prywatności przy aktualizacji samych informacji o wydaniu.

## Prywatność i źródła

Polityka rozróżnia dane lokalne aplikacji, żądania do serwerów użytkownika, TestFlight, zgłoszenia przez e-mail i logi hostingu GitHub Pages. Deklaruje przechowywanie korespondencji wsparcia do 12 miesięcy od ostatniej wymiany, z wyjątkami dla aktywnego sporu lub obowiązku prawnego. Właściciel musi stosować tę zasadę albo dostosować politykę przed publikacją. Dane recenzenta Apple i prywatne hasła nie są publikowane.

Strona `source.html` zawiera publiczny kontakt w sprawie odpowiadających źródeł konkretnego buildu. W repo aplikacji znajduje się aktualny pakiet `build/testflight/Discarium-1.1-28-CorrespondingSource.tar.gz` (SHA-256 `4b305618375b11dee81a0e3df29ef06421e2272852bc606ac4255be577d91bff`). Zachowaj też pakiety wcześniejszych wydań dla ich odbiorców. Pakiet można udostępnić jako Release asset w **repo aplikacji** i dodać sprawdzony publiczny URL do `src/pages/source.html`. Dużych archiwów nie dodawaj do zwykłego commita Git.

Strona zawiera działający link App Store. Linki do archiwów źródeł można dodać po ich publikacji; obecnie odbiorcy kontaktują się w tej sprawie przez publiczny e-mail.
