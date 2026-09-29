import subprocess

server = r"\\10.31.1.42\podtrans"
user = "wks\\svcHDvorstufe"
password = "Pw-sh?2026"

import subprocess

try:
    result = subprocess.run(
        [
            "net",
            "use",
            "Z:",
            r"\\10.31.1.42\podtrans",
            r"/user:wks\svcHDvorstufe",
            "Pw-sh?2026"
        ],
        check=True,
        capture_output=True,
        text=True
    )

    print("Freigabe erfolgreich verbunden.")
    #print(result.stdout)

except subprocess.CalledProcessError as e:
    #print(f"Fehler beim Verbinden der Freigabe.")
    #print(f"Return-Code: {e.returncode}")

    if e.stdout:
        print("STDOUT:")
        print(e.stdout)

    if e.stderr:
        if "Systemfehler 85 aufgetreten" in e.stderr:
            print("Das Laufwerk Z wird bereits verwendet !")
        else:
            print(e.stderr)

except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
