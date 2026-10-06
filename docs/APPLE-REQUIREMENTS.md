# Apple: wymagania dla strony Discarium

Sprawdzono **6 października 2026** w oficjalnej dokumentacji Apple i GitHub. Dotyczy przygotowania wersji tvOS 1.0. Działająca strona nie zastępuje pozostałej oceny App Review.

## Co jest wymagane

| Element | Wymaganie Apple | Przygotowane miejsce |
|---|---|---|
| Support URL | Wymagane pole wersji. Działająca strona z rzeczywistym kontaktem, umożliwiającym uzyskanie pomocy, przekazanie uwag i propozycji. Apple wymienia adres prawny, e-mail lub telefon, zależnie od lokalnego prawa. | `support.html`, publiczny e-mail `discarium@pisz.to`, autor Pawel Faron, instrukcje i FAQ. |
| Privacy Policy | Dostępna polityka prywatności w metadanych sklepu i wewnątrz aplikacji. Ma jasno opisywać zbierane dane, sposoby/cele ich użycia, udostępnianie, retencję, usuwanie i wybory użytkownika. | `privacy.html`; aplikacja ma już lokalny ekran prywatności. Przy kolejnym wydaniu zsynchronizuj politykę w aplikacji z wersją publiczną. |
| Apple TV Privacy Policy | Dokumentacja dla tvOS wskazuje **tekst** polityki w osobnym polu, nie tylko link do witryny. Ogólna tabela wymienia URL jako wymagany dla wszystkich aplikacji; najlepiej uzupełnić URL oraz pole tekstowe tvOS dostępne w App Store Connect. | `docs/apple-tv-privacy.txt` do wklejenia; URL `privacy.html`. |
| Działające linki | App Review wymaga działających odnośników do pomocy i polityki, z aktualnym kontaktem. Brak treści zastępczych. | Weryfikator lokalnych linków; po wdrożeniu właściciel sprawdza publiczne HTTPS. |
| Rzetelny opis | Możliwości aplikacji muszą odpowiadać opisowi. | Rozdzielone bezstratne audio, brak dodatkowego kodowania wideo i faktyczny sygnał HDMI. Menu HDMV/DVD opisane osobno od nieobecnego BD-J. |

## Co jest opcjonalne

- **Marketing URL**: strona produktu; przygotowana strona główna.
- **User Privacy Choices URL**: opcjonalny adres opisujący zarządzanie prywatnością, np. `privacy.html#choices`.
- Własna domena: cytowane wymagania Apple jej nie narzucają. Publiczna strona GitHub Pages z HTTPS spełnia wymaganie adresu strony, o ile jej treść i kontakt są poprawne.
- Polityka nie jest tym samym co ankieta **App Privacy**. Deklaracje zbierania danych w App Store Connect trzeba uzupełnić zgodnie z zachowaniem końcowego buildu.

## Ważne dla tej aplikacji

- E-mail/telefon dla recenzenta w App Review Information nie zastępują **publicznego** kontaktu pomocy. Publiczny e-mail właściciel podał osobno.
- Logo i zrzuty należą do projektu. Obrazy przedstawiają autorskie demo, nie komercyjne okładki ani prywatną bibliotekę.
- Nie używamy odznaki „Download on the App Store” ani fikcyjnego przycisku instalacji przed wydaniem.
- „Native disc playback” opisujemy jako bezpośrednie odtwarzanie kopii na Apple TV, bez wcześniejszej konwersji na serwerze. To nie deklaracja obsługi każdej płyty ani usuwania szyfrowania.
- „Lossless audio” nie oznacza gwarancji bit-perfect HDMI lub odtwarzania obiektów TrueHD Atmos/DTS:X. Wideo z płyt jest zwykle już stratnie skompresowane; prawidłowa deklaracja to brak **dodatkowego** stratnego kodowania przez aplikację.
- Strona zawiera informację o logach GitHub Pages: brak analityki w naszym kodzie nie oznacza, że hosting nie zapisuje adresów IP.
- Pełne warunki dystrybucji aplikacji GPL/LGPL pozostają osobną sprawą. Witryna zapewnia informację o źródłach; właściciel musi faktycznie dostarczać odpowiadający kod odbiorcom.
- Dostępność wersji językowej nie zmienia regionów dystrybucji. Wcześniejsze wyłączenie Francji pozostaje decyzją aplikacji, nie ustawieniem witryny.

## Źródła

1. [Apple — Platform version information: Support URL / Marketing URL](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/). „This property is required and can be localized” przy Support URL; kontakt rzeczywisty, pełny URL z protokołem.
2. [Apple — App privacy](https://developer.apple.com/help/app-store-connect/reference/app-information/app-privacy/). Privacy Policy URL wymagany; User Privacy Choices URL opcjonalny.
3. [Apple — Manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/). „If your app includes a tvOS platform, enter the text of your privacy policy in the Apple TV Privacy Policy field.”
4. [Apple — App Review: broken links / privacy policy issues](https://developer.apple.com/app-store/review/). Wymaga wsparcia z aktualnym kontaktem, polityki oraz opisu retencji/usuwania.
5. [Apple — Review Guidelines 1.5 Developer Information](https://developer.apple.com/app-store/review/guidelines/#developer-information), [2.3 Accurate Metadata](https://developer.apple.com/app-store/review/guidelines/#accurate-metadata), [5.1.1 Data Collection and Storage](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage).
6. [GitHub — What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages): strony projektu oraz zapis adresów IP dla bezpieczeństwa.
7. [GitHub — Securing your GitHub Pages site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https): obsługa HTTPS i jego wymuszenie.
