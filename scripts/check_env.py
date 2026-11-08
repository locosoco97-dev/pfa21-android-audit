"""Verification de l'environnement (Sprint 1) : versions, dependances, manifeste de base."""
import importlib
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifests" / "base" / "AndroidManifest.xml"


def main() -> int:
    ok = True
    print(f"[env] Python {platform.python_version()} sur {platform.system()} {platform.machine()}")
    for mod in ("pytest", "defusedxml"):
        try:
            m = importlib.import_module(mod)
            print(f"[env] {mod} OK ({getattr(m, '__version__', 'version inconnue')})")
        except ImportError:
            print(f"[env] {mod} MANQUANT")
            ok = False
    if MANIFEST.is_file():
        try:
            from defusedxml import ElementTree as ET
            root = ET.parse(MANIFEST).getroot()
            print(f"[env] manifeste de base lisible (package={root.get('package')})")
        except Exception as exc:
            print(f"[env] manifeste invalide : {exc}")
            ok = False
    else:
        print(f"[env] manifeste introuvable : {MANIFEST}")
        ok = False
    print("[env] RESULTAT :", "OK" if ok else "ECHEC")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
