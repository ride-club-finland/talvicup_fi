# talvicup_fi: ohje agenteille

E-pyöräilyn Suomen Cup – TalviCupin laskeutumissivu osoitteessa `talvicup.fi`. Staattinen sivu GitHub Pagesissa.
Tämä repo sisältää vain sivun.

## Tiedostot

| Polku | Mitä |
|---|---|
| `docs/index.html` | Koko sivu. Pages julkaisee vain `docs/`-kansion. |
| `docs/assets/` | Kuvat ja fontit (Saira Condensed, SIL OFL) |
| `docs/CNAME` | Pagesin oma domain |
| `tyokalut/tee_kuvat.py` | Renderöi kuvat (ja fontit `fontit`-argumentilla) Mediatehtaan TalviCup-kirjastosta: `uv run --project rcf_mediatehdas python talvicup_fi/tyokalut/tee_kuvat.py` juuresta |

## Säännöt

1. **Repo muuttuu julkiseksi, kun sivu julkaistaan.** Tänne ei tule henkilötietoja, salaisuuksia eikä sisäisiä päätöksiä,
   myöskään commit-viesteihin.
2. **Kisalinkit vain julkistuspäivänä ja vain tänne.** Linkit sisältävät salaisen osan ja jäävät repon historiaan.
   `index.html` merkitsee paikat kommenteilla `LINKKI 1`–`LINKKI 6`.
3. **Vain vahvistetut faktat.** Pisteet ja palkinnot lisätään, kun järjestäjä on vahvistanut ne (`PISTEET`-kommentti).
4. **Ei ulkoisia latauksia, lomakkeita, evästeitä eikä analytiikkaa.** Fontit ovat omalla palvelimella.
5. **Logot vain luvalla.**
6. **Ei ajajien nimiä tai lukuja ilman ylläpidon päätöstä.**

## Julkistuspäivän lista

1. Poista `noindex`-rivi tiedostosta `docs/index.html`.
2. Korvaa `LINKKI`-kohdat kisalinkeillä.
3. Täytä `PISTEET`- ja `KYSYMYKSET`-kohdat.

## Testit

Ei koodia eikä testejä. Tarkista sivu selaimessa työpöytä- ja puhelinleveydellä.
