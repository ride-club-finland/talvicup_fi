"""Write the season calendar docs/talvicup2027.ics from the series facts.

    py tyokalut/tee_kalenteri.py [polku/2027.json]

Default input is ../rcf_talvicup/sarja/2027.json (sibling repo). Output is RFC 5545: CRLF line endings,
UTF-8, lines folded at 75 octets. Only the talvicup.fi link goes in; the Zwift event links stay on the page.
DTSTAMP is the facts' check date, so re-running without changes gives an identical file.
"""
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_SRC = REPO.parent / "rcf_talvicup" / "sarja" / "2027.json"
OUT = REPO / "docs" / "talvicup2027.ics"
SITE = "https://talvicup.fi/"
DURATION = timedelta(hours=1, minutes=15)


def escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line: str) -> str:
    """Split a content line into chunks of at most 75 octets without breaking a UTF-8 character."""
    out, chunk, size, limit = [], "", 0, 75
    for ch in line:
        n = len(ch.encode("utf-8"))
        if size + n > limit:
            out.append(chunk)
            chunk, size, limit = " ", 1, 75
        chunk += ch
        size += n
    out.append(chunk)
    return "\r\n".join(out)


def km(value: float) -> str:
    return f"{value:.1f}".replace(".", ",")


def build(facts: dict) -> str:
    hh, mm = (int(x) for x in facts["alkaa_utc"].split(":"))
    stamp = date.fromisoformat(facts["tarkistettu"]).strftime("%Y%m%dT000000Z")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//talvicup.fi//TalviCup 2027//FI",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:TalviCup 2027",
        "X-WR-TIMEZONE:Europe/Helsinki",
    ]
    for race in facts["kisat"]:
        start = datetime.combine(date.fromisoformat(race["pvm"]), datetime.min.time()).replace(
            hour=hh, minute=mm, tzinfo=timezone.utc)
        end = start + DURATION
        laps = f" × {race['kierrokset']}" if race["kierrokset"] > 1 else ""
        summary = f"TalviCup 2027 · Kisa {race['n']}: {race['reitti']}{laps}"
        desc = (f"{race['muoto'].capitalize()} · {race['maailma']} · {km(race['km'])} km"
                f" · nousua noin {race['nousu_m_arvio']} m\n"
                f"Lähtö klo 18.30 Suomen aikaa. Valitse lähtö ikäkategoriasi mukaan.\n"
                f"Kisalinkki: {SITE}#kisat\n"
                f"Sarjatilanne: {SITE}tulokset/")
        lines += [
            "BEGIN:VEVENT",
            f"UID:talvicup2027-kisa{race['n']}@talvicup.fi",
            f"DTSTAMP:{stamp}",
            f"DTSTART:{start:%Y%m%dT%H%M%SZ}",
            f"DTEND:{end:%Y%m%dT%H%M%SZ}",
            f"SUMMARY:{escape(summary)}",
            f"DESCRIPTION:{escape(desc)}",
            "LOCATION:Zwift",
            f"URL:{SITE}#kisat",
            "STATUS:CONFIRMED",
            "TRANSP:OPAQUE",
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{escape(summary)} alkaa klo 18.30",
            "TRIGGER:-PT2H",
            "END:VALARM",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "".join(fold(line) + "\r\n" for line in lines)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    facts = json.loads(src.read_text(encoding="utf-8"))
    OUT.write_bytes(build(facts).encode("utf-8"))
    print(f"{OUT} ({len(facts['kisat'])} kisaa)")


if __name__ == "__main__":
    main()
