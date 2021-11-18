Entität: ElectroMagneticObserved  
================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/ElectroMagneticObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Das Datenmodell dient zur Messung übermäßiger elektrischer und magnetischer Felder (EMF) oder Strahlung am Arbeitsplatz oder in der Öffentlichkeit entsprechend dem Grad der Exposition gegenüber elektromagnetischen Feldern in der Luft. Die Frequenz der Hertz'schen Wellen liegt üblicherweise unter 300 GHz und breitet sich im Raum ohne künstliche Führung aus. Sie liegen zwischen 9 kHz und 300 GHz.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateObserved`: Datum und Uhrzeit dieser Beobachtung, dargestellt im ISO8601 UTC-Format. Sie können durch einen bestimmten Zeitpunkt oder durch ein ISO8601-Intervall dargestellt werden, um die Attribute "dateObservedFrom" und "dateObservedTo" zu trennen.  - `dateObservedFrom`: Beobachtungszeitraum: Anfangsdatum und -zeit im ISO8601 UTC-Format. Das Attribut kann zusätzlich zum Attribut "Beobachtungsdatum" verwendet werden, wenn es einem hervorzuhebenden Zeitintervall entspricht.  - `dateObservedTo`: Beobachtungszeitraum: Enddatum und -zeit im ISO8601 UTC-Format. Das Attribut kann zusätzlich zum Attribut "Beobachtungsdatum" verwendet werden, wenn es einem hervorzuhebenden Zeitintervall entspricht.  - `description`: Eine Beschreibung dieses Artikels  - `eMF`: Ebene, die der beobachteten Erhebung entspricht. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MHz** für Mega Hertz.  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refDevice`: Verweis auf ein [Gerät](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md), das diese Beobachtung aufgezeichnet hat.  - `refPointOfInterest`: Verweis auf einen [Point of Interest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit der Beobachtung verknüpft ist.  - `reliability`: Prozentsatz für den Konfidenzfaktor. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: Es muss ElectroMagneticObserved sein    
Erforderliche Eigenschaften  
- `dateObserved`  - `eMF`  - `id`  - `location`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ElectroMagneticObserved:    
  description: 'The Data Model is intended to measure excessive electric and magnetic fields (EMFs), or radiation in a work or public environment according to the level of exposure to electromagnetic fields on the air. The frequency of the hertzian waves is conventionally lower than 300 GHz, propagating in space without artificial guide. They are between 9 kHz and 300 GHz.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'Date and time of this observation represented by an ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval to separate attributes `dateObservedFrom`, `dateObservedTo`. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    eMF:    
      description: 'Level corresponding to the observed survey. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MHz** represents Mega Hertz. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &electromagneticobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *electromagneticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which captured this observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Point Of Interest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reliability:    
      description: 'Percent for confidence Factor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent. '    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be ElectroMagneticObserved'    
      enum:    
        - ElectroMagneticObserved    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - eMF    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/ElectroMagneticObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Environment/ElectroMagneticObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## Beispiel-Nutzlasten  
#### ElectroMagneticObserved NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein ElectroMagneticObserved im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": "MNCA-EM-018",  
  "alternateName": "AirPort  global Observation",  
  "description": "EMF observation",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Terminal 2 - Parking 7"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-T2-P7-EM03",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "eMF": 950.12,  
  "observedAt": "2020-03-17TT08:45:00Z",  
  "measurementType": "Instant",  
  "measurementInterval": 1,  
  "reliability": 0.993  
}  
```  
#### ElectroMagneticObserved NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein ElectroMagneticObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": {  
    "type": "Property",  
    "value": "MNCA-EM-018"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort SPA global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "EMF observation"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Terminal 2 - Parking 7"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:NCE-T2-P7-EM03"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "eMF": {  
    "type": "Property",  
    "value": 950.12,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "Instant"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "reliability": {  
    "type": "Property",  
    "value": 0.993  
  }  
}  
```  
#### ElectroMagneticObserved NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein ElectroMagneticObserved im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": {  
    "type": "Property",  
    "value": "MNCA-EM-018"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort \u0096 global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "EMF observation"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Terminal 2 - Parking 7"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:NCE-T2-P7-EM03"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "eMF": {  
    "type": "Property",  
    "value": 950.12,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "Instant"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "reliability": {  
    "type": "Property",  
    "value": 0.993  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### ElectroMagneticObserved NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein ElectroMagneticObserved im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": "MNCA-EM-018",  
  "alternateName": "AirPort global Observation",  
  "description": "EMF observation",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Terminal 2 - Parking 7"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-T2-P7-EM03",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "eMF": 950.12,  
  "observedAt": "2020-03-17TT08:45:00Z",  
  "measurementType": "Instant",  
  "measurementInterval": 1,  
  "reliability": 0.993,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
