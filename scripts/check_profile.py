"""Check this profile's inline Markdown/HTML links without extra dependencies."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = ("README.md", "REPOSITORY_GUIDE.md")
ONLINE_HOSTS = {"github.com", "raw.githubusercontent.com", "miiduoa.github.io", "www.kaggle.com"}
INLINE_LINK = re.compile(r"(!?)\[([^\]\n]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[tuple[str, str, bool]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and "href" in values:
            self.items.append((values["href"] or "", "", False))
        if tag == "img":
            self.items.append((values.get("src") or "", values.get("alt") or "", True))


def prose(text: str) -> str:
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", text)
    text = re.sub(r"(?ms)^~~~[^\n]*\n.*?^~~~[ \t]*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors(text: str) -> set[str]:
    result: set[str] = set()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", prose(text)):
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        slug, suffix = base, 0
        while slug in result:
            suffix += 1
            slug = f"{base}-{suffix}"
        result.add(slug)
    return result


def check_document(path: Path, root: Path) -> tuple[list[str], set[str]]:
    text = prose(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    remote: set[str] = set()
    if len(re.findall(r"(?m)^#\s+", text)) != 1:
        errors.append("expected exactly one top-level heading")
    parser = Links()
    parser.feed(text)
    items = [(url, label, bool(image)) for image, label, url in INLINE_LINK.findall(text)]
    items.extend(parser.items)
    for target, label, image in items:
        if image and not label.strip():
            errors.append(f"image needs descriptive alt text: {target}")
        if not target.strip() or any(ord(char) < 32 for char in target):
            errors.append("empty link or control character in URL")
            continue
        try:
            url = urlsplit(target)
            if url.scheme == "mailto":
                if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", url.path):
                    errors.append(f"invalid email link: {target}")
            elif url.scheme == "https":
                if not url.hostname or url.username or url.password or url.port not in (None, 443):
                    errors.append(f"invalid HTTPS URL: {target}")
                elif url.hostname not in ONLINE_HOSTS:
                    errors.append(f"add this public host to ONLINE_HOSTS before linking: {target}")
                else:
                    remote.add(urlunsplit((url.scheme, url.netloc, url.path or "/", url.query, "")))
            elif url.scheme or url.netloc:
                errors.append(f"unsupported link scheme: {target}")
            else:
                destination = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
                if not destination.is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f"missing or out-of-repository target: {target}")
                elif url.fragment and destination.suffix == ".md":
                    if unquote(url.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                        errors.append(f"missing Markdown heading: {target}")
        except ValueError as error:
            errors.append(f"invalid URL {target}: {error}")
    return errors, remote


def online_status(url: str) -> tuple[str, str | None]:
    # No credentials are sent. Fragments are checked only for local Markdown.
    for attempt in range(3):
        try:
            for method in ("HEAD", "GET"):
                try:
                    request = Request(url, method=method, headers={"User-Agent": "Miiduoa-profile-link-check/1.0"})
                    with urlopen(request, timeout=12) as response:
                        if response.status == 200:
                            return url, None
                        return url, f"HTTP {response.status}"
                except HTTPError as error:
                    if method == "HEAD" and error.code in (403, 404, 405, 410, 501):
                        continue
                    raise
        except (HTTPError, URLError, TimeoutError, OSError) as error:
            detail = f"{type(error).__name__}: {error}"
            if attempt < 2:
                time.sleep(attempt + 1)
    return url, detail


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="also check public HTTP destinations")
    args = parser.parse_args()
    errors: list[str] = []
    urls: set[str] = set()
    for name in DOCUMENTS:
        found, remote = check_document(ROOT / name, ROOT)
        errors.extend(f"{name}: {error}" for error in found)
        urls.update(remote)
    if args.online and not errors:
        with ThreadPoolExecutor(max_workers=3) as pool:
            for url, error in pool.map(online_status, sorted(urls)):
                print(f"{'FAIL' if error else 'OK'} {url}" + (f" — {error}" if error else ""))
                if error:
                    errors.append(f"{url}: {error}")
    for error in errors:
        print(f"ERROR: {error}")
    mode = "HTTP destinations checked; remote fragments are not checked" if args.online else "HTTP reachability not checked"
    print(f"{len(DOCUMENTS)} documents; {len(urls)} unique public URLs; {len(errors)} errors. {mode}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
