from pathlib import Path
import re
import sys

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "_templates"
PARTIALS = ROOT / "_partials"


def build():
    disclaimer_tpl = (PARTIALS / "disclaimer.html").read_text(encoding="utf-8")
    footer_tpl = (PARTIALS / "footer.html").read_text(encoding="utf-8")
    check_mode = "--check" in sys.argv
    out_of_sync = []
    written = 0
    unchanged = 0

    for tpl in sorted(TEMPLATES.rglob("*.html")):
        rel = tpl.relative_to(TEMPLATES)
        depth = len(rel.parts) - 1
        base = "../" * depth

        raw = tpl.read_text(encoding="utf-8")

        if '<aside class="disclaimer">' in raw:
            raise ValueError(
                f"{tpl.relative_to(ROOT)}: contains hard-coded disclaimer — "
                f"use {{{{disclaimer}}}} instead"
            )

        content = raw.replace("{{disclaimer}}", disclaimer_tpl.replace("{{base}}", base))
        content = content.replace("{{footer}}", footer_tpl.replace("{{base}}", base))

        leftover = re.findall(r"\{\{[^}]+\}\}", content)
        if leftover:
            raise ValueError(f"{tpl.relative_to(ROOT)}: unresolved placeholders: {leftover}")

        out = ROOT / "index.html" if rel == Path("index.html") else ROOT / rel.parent / "index.html"

        gen_comment = (
            f"<!-- GENERATED FILE - edit _templates/{rel.as_posix()},"
            f" then run: python build.py -->\n"
        )
        final = gen_comment + content

        if check_mode:
            if not out.exists() or out.read_text(encoding="utf-8") != final:
                out_of_sync.append(str(out.relative_to(ROOT)))
        else:
            if not out.exists() or out.read_text(encoding="utf-8") != final:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(final, encoding="utf-8")
                print(f"  wrote     {out.relative_to(ROOT)}")
                written += 1
            else:
                print(f"  unchanged {out.relative_to(ROOT)}")
                unchanged += 1

    if check_mode:
        if out_of_sync:
            print("OUT OF SYNC (edit templates, not generated files):")
            for p in out_of_sync:
                print(f"  {p}")
            sys.exit(1)
        else:
            count = len(list(TEMPLATES.rglob("*.html")))
            print(f"All {count} generated files are in sync.")
    else:
        print(f"\nBuild complete: {written} written, {unchanged} unchanged.")


if __name__ == "__main__":
    build()
