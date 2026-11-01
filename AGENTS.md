# talvicup_fi: ohje agenteille

E-pyöräilyn Suomen Cup – TalviCupin laskeutumissivu osoitteessa `talvicup.fi`. Staattinen sivu GitHub Pagesissa.
Tämä repo sisältää vain sivun.

## Tiedostot

| Polku | Mitä |
|---|---|
| `docs/index.html` | Pääsivu. Pages julkaisee vain `docs/`-kansion. |
| `docs/tulokset/index.html` | Sarjatilanne ja tiimitaulu. Generoidaan datamoottorin komennolla `talvicup.py sivu --kohde <talvicup_fi>/docs`, älä muokkaa käsin. |
| `docs/assets/` | Kuvat ja fontit (Saira Condensed, SIL OFL) |
| `docs/talvicup2027.ics` | Kisat kalenteritiedostona. Generoidaan: `py tyokalut/tee_kalenteri.py` (lukee `../rcf_talvicup/sarja/2027.json`), älä muokkaa käsin. |
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

Tässä järjestyksessä: sivu ei saa näkyä hakukoneille ennen kuin osoite ja kisalinkit toimivat.

1. Tarkista, että info@talvicup.fi:n sähköpostiohjaus toimii (testiviesti). Sivu ohjaa kysymykset, korjauspyynnöt ja luvat sinne.
2. Täytä LAHTORYHMAT, kun järjestäjä on vahvistanut kartan (kommentit `LAHTORYHMAT` tiedostossa `docs/index.html`, kaksi kohtaa).
   Lisää samat kirjaimet usein kysyttyjen kohtaan "Mikä lähtö on minun?".
3. Jos järjestäjä on vahvistanut pisteasteikon, poista sen esitysmerkintä.
4. Korvaa `LINKKI 1`–`LINKKI 6` kisalinkeillä ja poista teksti "Kisalinkki tulee tähän".
5. Poista `noindex`-rivi ja sen kommentti tiedostosta `docs/index.html`. Tulossivun `noindex` tulee generaattorista, eikä sitä muuteta käsin.
6. Jos kisapäivät tai reitit ovat muuttuneet, aja `py tyokalut/tee_kalenteri.py` ja commitoi `docs/talvicup2027.ics`.

## Testit

Ei koodia eikä testejä. Tarkista sivu selaimessa työpöytä- ja puhelinleveydellä.
