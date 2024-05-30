questions_organization = {
    "orgName": (
        "Wie lautet der vollständige Name des Hersteller oder der Herstellerfirma. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. Suche exakt den Hersteller"
        "Die Antwort sollte nur den Herstellernamen enthalten"
    ),
    "shortNameAsID" : (
        "Finde den Herstellernamen und generiere ein Kürzel mit welchen sich der Hersteller identifzieren lässt. "
        "Die Anwort sollte nur das Kürzel enthalten"
    ),
    
    "address_street_number": (
        "Suche die Adresszeile des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Aus der Adresszeile des Herstellers extrahiere die Strasse und Türnummer, falls vorhanden. "
        "Ist keine Strasse und Türnummer vorhanden antworte ausschliesslich mit None! "
    ),
    "address_city": (
        "Suche die Adresszeile des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Aus der Adresszeile des Herstellers extrahiere die Stadt, falls vorhanden. "
        "Ist keine Stadt angegeben antworte ausschliesslich mit None! "
    ),
    "address_zip": (
        "Suche die Adresszeile des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Aus der Adresszeile des Herstellers extrahiere die Postleitzahl. "
        "Die Antwort sollte nur die Postleitzahl enthalten!"
    ),
    "address_country": (
        "Suche die Adresszeile des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Extrahiere das Land aus der Adresszeile. "
        "Die Antwort sollte nur das Land enthalten!"
    ),
    "webAdress": (
        "Suche nach der Webadresse des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Ist keine Webadresse angegeben so antworte ausschliesslich mit None! "
    ),
    "fax":  (
        "Suche nach der Faxnummer des Herstellers. "
        "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
        "Ist keine Faxnummer angegeben so antworte ausschliesslich mit None! "
    )
}

questions_mpd = {
    "fullName": {
        "question": (
            "Suche nach dem vollständigen Produktnamen des Medikaments. "
            "Die Antwort sollte nur den vollständigen Produktnamen enthalten!"
            ),
        "following": {
            "nameDoseFormPart": {"question": (
                "Suche im Produktnamen nach der Dosierform. "
                "Deine Antwort sollte nur die Dosierform enthalten!"
            )},
            "nameStrengthPart": {"question": (
                "Suche im Produktnamen nach der Zusammensetzung/Stärke des Medikaments. "
                "Deine Antwort sollte nur die Zusammensetzung/Stärke als Zahl inklusive der Einheit enthalten."
            )},
            "namePopulationPart": {"question": (
                "Suche im Produktnamen nach der Population für die das Medikament gedacht ist. "
                "Ist keine Population zu finden antworte ausschliesslich mit None!"
            )},
        },
    },
    "admission_nr": {"question": (
        "Suche die Zulassungsnummer des Medikaments. "
        "Deine Antwort soll ausschliessliech die reine Zulassungsnummer beinhalten"
    )},
    "modeOfAction": {"question": (
        "Suche die Wirkungsweise des Medikaments. "
        "Gib die Wirkungsweise nur so zurück wie sie auch im Beipackzettel zu finden ist. "
    )},
    "indication": {"question": (
        "Suche nach den Anwendungsbereich des Medikaments. "
        "Sind verschiedene Anwendungsbereiche angegeben trenne diese mit einem Beistrich voneinander. "
        "Deine Antwort sollte nur die Anwendungsbereiche aufzählen"
    )},
    "creationDate": {"question": (
        "Suche nach dem Datum an dem die Packungsbeilage zuletzt überarbeitet oder erstellt wurde. "
        "Deine Antwort sollte nur das Datum im Format YYYY-MM--DD enthalten. "
    )},
    "blackTriangle": {"question": (
        "Suche nach Informationen ob das Medikament einer zusätzlichen Überwachung unterliegt. "
        "Der sogenannten Black-Triangle Informationen "
        "Extrahiere den Text betreffend der zusätzlichen (Black Triangle) Überwachung. "
        "Ist keine Black-Triangle Information zu finden antworde ausschliesslich mit None!"
    )},

    "activeIngredient": {
        "question": (
            "Suche nach dem Abschnitt in dem die Wirkstoffe des Medikaments beschrieben sind. "
            "Ignoriere die Hilfsstoffe oder sonstige Bestandteile. "
            "Die aktiven Wirkstoffe sind oft daran zu erkennen dass eine genaue Dosisangebe existiert. "
        ) ,
        "following": {
            "name_strength_active":  {"question": (
                "Suche im Abschnitt der Wirkstoffe die genaue Anzahl an aktiven Wirkstoffen im Medikament. "
                "Extrahiere jeden Wirkstoff inklusive Menge pro Dosiereinheit getrennt durch ein Komma. "
                "Wenn es mehrere Wirkstoffe gibt trenne diese mit einem Semikolon voneinander. "
                "Deine Antwort sollte nur Wirkstoff, Menge, Dosierform enthalten. "
            )},
        }
    },
    "adjuvantIngredient": {
        "question": (
            "Suche nach dem Abschnitt in dem die Hilfsstoffe oder sontige Bestandteile des Medikaments beschrieben sind. "
            "Ignoriere die aktiven Wirkstoffe. "
        ) ,
        "following": {
            "name_strength_adjuvant":  {"question": (
                "Finde im Abschnitt der Hilfsstoffe oder sonstigen Bestandteile die genaue Anzahl an verschiederen Stoffe heraus. "
                "Wenn es mehrere Stoffe gibt trenne diese mit einem Semikolon voneinander. "
                "Deine Antwort sollte nur die Stoffbezeichnungen enthalten!"
            )},
        }
    }
}

