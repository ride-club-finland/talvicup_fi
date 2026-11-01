# talvicup_fi: ohje agenteille

E-pyöräilyn Suomen Cup – TalviCupin laskeutumissivu osoitteessa `talvicup.fi`. Staattinen sivu GitHub Pagesissa.
Tämä repo sisältää vain sivun.

## Tiedostot

| Polku | Mitä |
|---|---|
| `docs/index.html` | Pääsivu. Pages julkaisee vain `docs/`-kansion. |
| `docs/tulokset/index.html` | Sarjatilanne ja tiimitaulu. Generoidaan datamoottorin komennolla `talvicup.py sivu --kohde <talvicup_fi>/docs`, älä muokkaa käsin. |
| `docs/assets/` | Kuvat ja fontit (Saira Condensed, SIL OFL) |
| `docs/CNAME` | Pagesin oma domain |
| `tyokalut/tee_kuvat.py` | Renderöi kuvat (ja fontit `fontit`-argumentilla) Mediatehtaan TalviCup-kirjastosta: `uv run --project rcf_mediatehdas python talvicup_fi/tyokalut/tee_kuvat.py` juuresta |

## Säännöt

1. **Repo muuttuu julkiseksi, kun sivu julkaistaan.** Tänne ei tule henkilötietoja, salaisuuksia eikä sisäisiä päätöksiä,
   myöskään commit-viesteihin.
2. **Kisalinkit vain julkistuspäivänä ja vain tänne.** Linkit sisältävät salaisen osan ja jäävät repon historiaan.
   `index.html` merkitsee paikat kommenteilla `LINKKI 1`–`LINKKI 6`.
3. **Vain vahvistetut faktat, tai selvästi merkitty esitys.** Pisteasteikko saa näkyä ennen järjestäjän vahvistusta, kun sivu sanoo sen olevan esitys. Palkinnot vasta vahvistettuina.
4. **Ei ulkoisia latauksia, lomakkeita, evästeitä eikä analytiikkaa.** Fontit ovat omalla palvelimella.
5. **Logot vain luvalla.**
6. **Ajajien nimet ja luvut vain tulossivulle ja vain generaattorin kautta.** Generaattori hoitaa nimimuodon, kieltolistan ja alaikäisten suojan.

## Julkistuspäivän lista

1. Poista `noindex`-rivi tiedostosta `docs/index.html`.
2. Korvaa `LINKKI`-kohdat kisalinkeillä.
3. Tarkista, että info@talvicup.fi:n sähköpostiohjaus toimii (testiviesti).
4. Jos järjestäjä on vahvistanut pisteasteikon, poista sen esitysmerkintä.

## Testit

Ei koodia eikä testejä. Tarkista sivu selaimessa työpöytä- ja puhelinleveydellä.
