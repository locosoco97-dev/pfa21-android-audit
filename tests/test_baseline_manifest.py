"""Tests Sprint 1 : le manifeste de base existe, est lisible et conforme a la fiche de cible."""
from pathlib import Path

import pytest
from defusedxml import ElementTree as ET

ANDROID = "{http://schemas.android.com/apk/res/android}"
ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "manifests" / "base" / "AndroidManifest.xml"
SOURCE = ROOT / "app" / "src" / "main" / "AndroidManifest.xml"


@pytest.fixture(scope="module")
def root():
    return ET.parse(BASE).getroot()


def test_base_identique_a_la_source():
    assert BASE.read_bytes() == SOURCE.read_bytes()


def test_package(root):
    assert root.get("package") == "ma.emsi.eventschedule"


def test_cinq_composants(root):
    app = root.find("application")
    noms = {e.get(ANDROID + "name") for e in app if e.tag in ("activity", "service", "receiver", "provider")}
    assert noms == {".MainActivity", ".SessionDetailActivity", ".SyncService", ".ReminderReceiver", ".ScheduleProvider"}


def test_seule_activite_launcher_exportee(root):
    app = root.find("application")
    exportes = [e.get(ANDROID + "name") for e in app if e.get(ANDROID + "exported") == "true"]
    assert exportes == [".MainActivity"]


def test_drapeaux_applicatifs_conformes(root):
    app = root.find("application")
    assert app.get(ANDROID + "debuggable") in (None, "false")
    assert app.get(ANDROID + "allowBackup") == "false"
    assert app.get(ANDROID + "usesCleartextTraffic") == "false"


def test_permissions_attendues(root):
    perms = {p.get(ANDROID + "name") for p in root.findall("uses-permission")}
    assert perms == {
        "android.permission.INTERNET",
        "android.permission.ACCESS_NETWORK_STATE",
        "android.permission.POST_NOTIFICATIONS",
    }
