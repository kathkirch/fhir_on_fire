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
            "patientInstruction": {
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

questions_side_effects = {
    "sideEffects": {
        "question": (
            "Suche nach den Abschnitt in dem die Nebenwirkungen beschrieben sind: "
            "Deine Antwort soll den gesamten Abschnitt der Nebenwirkungen beinhalten!"
        ),
        "following": {
            "frequency_categories": {
                "question": (
                    "Zähle die beschriebenen Häufigkeitskategorien und schreib sie in die Antwort. "
                    "Deine Antwort soll nur aus der Zahl bestehen!"
                )
            } ,
            "side_effects_list": {
                "question":  (
                    "Extrahiere alle möglichen Nebenwirkungen und zähle sie kategorisiert nach Häufigkeit auf. "
                    "Formatiere deine Antwort folgend: Häufigkeit_A: Aufzählung1 | Aufzählung2 ; HäufigkeitB: Aufzählung3 | usw. "
                    "Wenn zur Häufigkeit genaue Angaben wie oft etwas auftritt bekannt sind, führe dies bei der Häufigkeit mit an. "
                ) 
            }
        }
    }
}

questions_contraindications = {
    "contraindications": (
        "Unter welchen Umständen oder wann darf das Medikament nicht eingenommen werden? "
        "Nenne alle Umstände/Kontraindikationen getrennt durch ein ';' in eine Liste auf. "
        "Deine Antwort sollte nur diese Liste enthalten!"
    )
}

questions_interactions = {
    "interactions": {
        "question": (
            "Suche nach dem Abschnitt in dem Wechselwirkungen oder Einnahme des Medikaments mit anderen Medikamenten beschrieben sind: "
            "Dazu gehört auch die Einnhame gemeinsam mit Alkohol oder anderen Lebensmitteln, sowie etwaige Auswirkungen auf Labortests etc. "
            "Deine Antwort soll den gesamten Abschnitt über diese Wechselwirkungen beinhalten!"
        ),
        "following": {
            "alcohol": {
                "question": (
                    "Such nach dem Abschnitt in dem die Einnhame mit Alkohol beschrieben ist. "
                    "Deine Antwort soll nur die beschriebene Wirkung beinhalten. "
                    "Findest du keine Hinweise so antworte mit None."
                )
            } ,
            "medications": {
                "question":  (
                    "Suche nach dem Abschnitt in dem die Einnahme mit anderen Medikamenten beschrieben sind.  "
                    "Nenne alle beschriebenen Wechselwirkungen oder Hinweise zu Wechselwirkungen, trenne die einzelnen Aufzählungen mit einem ; voneinander. "
                    "Deine Antwort soll nur die Liste der Aufzählungen beinhalten!"
                ) 
            },
            "other": {
                "question": (
                    "Suche danach ob Beeinflussungen beschrieben sind, die nicht die Wirkung mit anderen Medikamente oder Alkohol betreffen.  "
                    "Nenne die gefundenen Wirkungen und ordne sie einem Thema zu. "
                    "Deine Antwort sollte dann wie folgt formatiert sein: Thema, Inhalt; Thema2, Inhalt2; usw. "
                    "Wenn keine anderen Wechselwirkungen die nicht Alkohol oder Medikamente betreffen beschrieben sind, antworte mit None"
                )
            }
        }
    }
}

questions_warnings = {
    "precautios_warning": {
        "question": (
            "Suche nach dem Abschnitt 'Warnhinweise und Vorsichtsmaßnahmen' " 
            "dieser ist im oft im Kapitel was vor der Einnahme des Medikaments zu beachten' ist. "
            "Schreibe den Abschnitt in deine Antwort" 
        ),
        "following": {
            "warning_hints": {
                "question": (
                    "Extrahiere alle Anweisungen und Warnhinweise aus diesem Abschnitt. "
                    "Einzelne Einträge stehen meist in einem eigenen Absatz, und sind thematisch voneinander getrennt. "
                    "Antworte mit allen relevanten Anweisungen und Warnhinweisen und strukturiere diese so, "
                    "dass jeder Eintrag thematisch voneinander abgegrenzt wird. Trenne Einträge mit einem | voneinander."
              
                )
            }
        }
    },
    # "special_warnings": {
        # "question": (
        #     "Suche nach dem Kapitel was vor der Einnahme des Medikaments zu beachten ist. "
        #     "Dieses Kapitel beinhaltet, Kontraindikationen, Warnhinweise und Vorichtsmaßnahmen, Wechselwirkungen und Spezielle Warnungen. "
        #     "Entferne die Inhalte vor den speziellen Warnungen, heißt alles von Anfang bis inklusive Wechselwirkungen"
        #     "Extrahiere den Rest in deine Antwort"
        # ),
        # "following": {
            "roadworthiness": {
                "question": (
                    "Such nach Hinweisen die die Verkehrstüchtigkeit oder das Bedienen von Maschinen betreffen. "
                    "Deine Antwort soll nur die Hinweise dazu enthalten. Findest du nichts antworte mit None."
                )
            },
            "pregnancy": {
                "question": (
                    "Suche nach Hinweisen die Schwangerschaft und Stillen betreffen"
                    "Deine Antwort soll nur die Hinweise dazu enthalten. Findest du nichts antworte mit None. "
                )
            },
            # "other": {
            #     "question": (
            #         "Such nach anderen besonderen Hinweisen die nicht Schwangerschaft, Stillen oder Verkehrstüchtigkeit bzw. das Bedienen schwerer Maschinen betreffen.  "
            #         "und Hinweise die nicht unter Warnungen und Vorsichtsmaßnahmen zu finden sind. "
            #         "Findest du verschiedene Trenne einzelne Einträge mit einem ; voneinander."
            #         "Deine Antwort sollte nur diese besonderen Warnungen enthalten. "
            #     )
            # }   
        # }
    # }
}



