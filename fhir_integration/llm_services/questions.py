questions_organization = {
    "manufacturer": {
        "question": (
            "Suche nach dem Hersteller des Medikaments, und achte darauf den Hersteller und "
            "nicht den Vertreiber zu finden. "
            "Schreibe in deine Antwort den vollständigen Herstellernamen "
            "sowie die gesamte gefundene Adresse und weitere Kontaktdaten wenn vorhanden."
        ),
        "following": {
            "orgName": {
                "question": (
                    "Wie lautet der vollständige Name des Hersteller oder der Herstellerfirma. "
                    "Die Antwort sollte nur den Herstellernamen enthalten"
                )
            },
            "address_street_number": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Strasse und Türnummer, falls vorhanden. "
                    "Ist keine Strasse und Türnummer vorhanden antworte ausschliesslich mit None! "
                )
            },
            "address_city": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Stadt, falls vorhanden. "
                    "Ist keine Stadt angegeben antworte ausschliesslich mit None! "
                )
            },
            "address_zip": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Postleitzahl. "
                    "Die Antwort sollte nur die Postleitzahl enthalten!"
                )
            },
            "address_country": {
                "question": (
                    "Extrahiere das Land aus der Adresszeile. "
                    "Die Antwort sollte nur das Land enthalten!"
                )
            },
            "webAdress":{ 
                "question": (
                    "Suche nach der Webadresse des Herstellers. "
                    "Ist keine Webadresse angegeben so antworte ausschliesslich mit None! "
                )
            },
            "fax":{
                "question": (
                    "Suche nach der Faxnummer des Herstellers. "
                    "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                    "Ist keine Faxnummer angegeben so antworte ausschliesslich mit None! "
                )
            }
        }
    }
}

#TODO optimize, modeOfAction, indication evtl zusammenfassen in following question
# active und adjuvant auch aus einem abschnitt rauslesen
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
        "Sind verschiedene Anwendungsbereiche angegeben trenne diese mit einem Semikolon voneinander. "
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

questions_medical_knowledge = {
    "name_medication" : { 
        "question": (
            "Wie lautet der Handels- oder Markenname des Medikaments? "
            "Deine Antwort soll nur den Namen beinhalten!"
        )
       
    },
    "forgotten" : {
        "question": (
            "Suche nach dem Abschnitt was zu tun ist wenn die Einnahme des Medikaments vergessen wurde. "
            "Deine Antwort soll ausschliesslich die beschriebene Anleitung beinhalten ohne eine Überschrift zu erwähnen"
        )
        
    },
    "quit" : {
        "question": (
            "Suche nach dem Abschnitt zu hinweisen bezüglich Abbruch der Einnahme. "
            "Deine Antwort soll ausschliesslich die Hinweise und Anweisungen beinhalten ohne eine Überschrift zu erwähnen"
        )
    },
    "too_much" : {
        "question": (
            "Suche nach dem Abschnitt bezüglich Hinweise und Anweisungen wenn zu viel vom Medikament eingenommen wurde. "
            "Deine Anwort soll ausschliesslich die Hinweise und Anweisungen beinhalten ohne eine Überschrift zu erwähnen "
        )
    },
    
    "max_intake_duration": {
        "question": (
                "Welche Hinweise zur Anwendungsdauer sind zu finden? "
                "Deine Antwort soll nur Hinweise enthalten die auch im Beipackzettel zu finden sind. "
                "Schreibe in die Anwort wenn die Einnahme nicht limitiert ist und keine Hinweise existieren."
        )
    },
    "general_dosage": {
        "question": (
            "Suche nach dem Abschnitt in dem die Einnahmeart und Dosierung des Medikaments erklärt wird. "
            "Deine Antwort sollte den gesamten Abschnitt zur Dosierung und korrekten Einnahme beinhalten. "
        ),
        "following": {
            "patient_instruction": {
                "question": (
                    "Welche Hinweise zur Einnahme sind enthalten. "
                    "Oft ist dies der erste Absatz am Abschnitt 'Wie Medikamentenname einzunehmen ist:'. "
                    "Hänge dazu auch noch Informationen zur empfohlenen Dosis betreffend Tagesdosis und Abstand in Stunden bis zur nächsten Einnahme an. "
                    "Schreibe keine Anleitungen dazu wie das Medikament einzunehmen ist. "
                    "Antworte nur mit dem Hinweisen und schreibe keine Überschrift in die Antwort! "
                )
            },
            "additional_instruction": {
                "question": (
                    "Welche zusätzlichen Hinweise sind bezüglich der korrekten Einnahme zu finden? "
                    "Bsp. mit Wasser einnehmen"
                    "Antworte nur mit den Hinweisen zur Einnhame, findest du nichts so antworte mit None. " 
                )
            },
            "route": {
                "question": (
                    "Wie wird das Medikament dem Körper zugeführt? z.B. Zum Einnehmen"
                    "Welche Einnahmeroute ist angeführt? "
                    "Deine Antwort soll nur die Einnahmeroute enthalten! "
                )
            },
            "doseform": {
                "question": (
                    "Welche Dosierform ist für das Medikament angegeben "
                    "Deine Antwort soll nur die Dosierform enthalten!"
                )
            },
            "dose_and_rate": {
                "question": (
                    "Wie viele Tabletten/Einheiten werden pro Einnahme im Normalfall eingenommen? "
                    "Deine Antwort soll nur die Zahl enthalten! "
                )
            },
            "max_dose_per_intake": {
                "question": (
                    "Wie viele Tabletten/Einheiten dürfen maximal pro Einnhame eingenommen werden? "
                    "Deine Antwort soll nur die Anzahl enthalten. "
                )
            },
            "max_dose_per_period": {
                "question": (
                    "Wie viele Tabletten/Einheiten dürfen maximal pro Tag eingenommen werden. "
                    "Deine Antwort soll nur die Anzahl enthalten. Ist kein Hinweis zu finden antworte mit None. "
                )
            },
        }
    },
    "storage_guideline": {
        "question": (
            "Welche Hinweise und Anweisungen sind zur Aufbewahrung des Medikaments zu finden? "
            "Deine Antwort soll alle Hinweise zur Aufbewahrung inkl. Verfallsdatum beinhalten. "
            "Deine Antwort soll nur die Anweisungen zur Aufbewahrung und Hinweise zum Verfallsdatum beinhalten"
        )
    },
    "characteristics": {
        "question": (
            "Suche nach dem Abschnitt in dem das Aussehen des Medikaments beschrieben ist. "
            "Deine Antwort soll nur das beschriebenen Aussehen beinhalten. "
            "Findest du nichts so antworte mit None."
        )
    }
}

questions_undesirable_effects ={
    "undesirable_effects": (
        "Suche nach den Abschnitt in dem die Nebenwirkungen beschrieben sind und"
        "extrahiere alle möglichen Nebenwirkungen und zähle sie kategorisiert nach Häufigkeit auf. "
        "Formatiere deine Antwort folgend: Häufigkeit_A: Aufzählung1 | Aufzählung2 ; HäufigkeitB: Aufzählung3 | usw. "
        "Wenn zur Häufigkeit genaue Angaben wie oft etwas auftritt bekannt sind, führe dies bei der Häufigkeit mit an. "
        "Deine Antwort soll nur die Liste mit den Häufigkeiten und Nebenwirkungen beinhalten! "
    )
}

questions_icw = {
    "precautious": {
        "question": (
                "Suche das Kapitel Was vor der Einnhame des Medikaments zu beachten ist. " 
                "Dieses Kapitel beinhaltet Informationen wann das Medikament nicht eingenommen werden darf, "
                "Warnhinweise und Vorsichtsmaßnahmen, Informationen zu Wechselwirkungen mit anderen Medikamenten, und weitere Hinweise und Warnungen "
                "Schreibe das Kapitel inklusive der Abschnittsüberschriften in deine Antwort. "
            ),
        "following": {
            "interaction_medications": {
                "question":  (
                    "Suche den Abschnitt in dem die Einnahme mit anderen Medikamenten (Wechselwirkungen) beschrieben sind.  "
                    "Nenne alle beschriebenen Wechselwirkungen oder Hinweise zu Wechselwirkungen mit anderen Medikamenten die im Abschnitt vorkommen und "
                    "trenne die einzelnen Aufzählungen mit einem | voneinander. "
                    "Es ist wichtig dass in den einzelnen Einträgen auch immer die mögliche Wechselwirkung genannt wird"
                    "Deine Antwort soll die Liste der extrahierten Wechselwirkungen beinhalten! "
                ) 
            },
            "contraindications": {
                "question": (
                    "Suche den Abschnitt wann das Medikament nicht eingenommen werden darf! "
                    "Nenne in deiner Antwort nur die Umstände wann das Medikament nicht eingenommen werden darf "
                    "ohne eine Einleitung, in der Antwort darf nicht sowas stehen wie ''Das Medikament XZY darf nicht eingenommen werden'"
                    "trenne die einzelnen Situationen mit einer | . "
                )  
            },
            "warning_other": {
                "question": (
                    "Suche Warnungen/Hinweisen die nach dem Abschnitt zur Einnahme des Medikaments mit anderen Arzneimitteln (den Wechselwirkungen) beschrieben werden "
                    "Beispiele sind Informationen zur Verkehrstüchtigkeit, Einnahme mit Alkohol, Beeinflussung von Labortests ..."
                    "Diese Warnungen sind meist mit einer eigenen Überschrift versehen "
                    "Deine Antwort sollte dann wie folgt formatiert sein: Überschrift, Inhalt| Überschrift2, Inhalt2| usw. "
                    "Stelle sicher dass du Hinweise zu Wechselwirkungen mit anderen Medikamenten von deiner Antwort ausschliesst. "
                    "Stelle sicher keine Warnungen zu nennen die im Abschnitt 'Warnhinweise und Vorsichtsmaßnahmen' vorkommen"
                    "Wenn keine anderen Warnungen beschrieben sind, antworte mit None"
                )
            },
            "hints" : {
                "question": (
                    "Suche den Abschnitt 'Warnhinweise und Vorsichtsmaßnahmen'"
                    "Dieser Abschnitt beinhaltet Anweisungen welche Informationen mit einem Arzt abgeklärt werden muss und was während der Einnhame zu beachten ist"
                    "Hinweise enthalten entweder eine Anweisungen mit mehreren Aufzählungen oder beschreiben eine einzelne Anweisung/Hinweis. "
                    "Schreibe diese Anweisungen oder Anweisungen mit Aufzählungen in eine Liste und trenne unabhängige Anweisungen mit einem | voneinander."
                )
            },
        }
    }
}