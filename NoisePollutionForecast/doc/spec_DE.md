[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: NoisePollutionForecast  
===============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Vorhersage der Lärmbelastung speichert die Erwartung über die Lärmbelastung auf der Grundlage einiger Eingabeelemente und der vorhandenen Lärmelemente.**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `LANight`: Durchschnittlicher Schallpegel in der Nacht (8h)  - `LAeq`: Durchschnittlicher Schallpegel (Äquivalent), der während der Messzeit aufgezeichnet wurde  - `LAeq2`: Durchschnittlicher Schallpegel der letzten 2 Stunden  - `LAeq_d`: Durchschnittlicher Schallpegel während des Tages (8h)  - `LAmax`: Maximaler Schallpegel, der während der Messzeit aufgezeichnet wurde  - `LAmax2`: Maximal aufgezeichneter Schallpegel der letzten 2 Stunden  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateIssued`: Das Datum und die Uhrzeit, zu der die Vorhersage vom Diensteanbieter erstellt wurde, im Format ISO8601 UTC.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `noiseAnnoyanceIndex`: Index (1 bis 10) nach dem Grad der Lärmbelästigung  - `noiseOrigin`: Hauptursache (Quelle) des aufgezeichneten Lärms bei der Installation des Sensors  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type`: NGSI-Typ. Es muss NoisePollutionForecast sein  - `validFrom`: Beginn des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validTo`: Das Ende des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validity`: Enthält den Gültigkeitszeitraum für diese Prognose als ISO8601-Zeitintervall.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoisePollutionForecast:    
  description: 'Noise Pollution forecast stores the expectation about noise pollution based on some input elements and the noise elements present.'    
  properties:    
    LANight:    
      description: 'Average sound level recorded during the night (8h)'    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq:    
      description: 'Average sound level (equivalent) recorded during the measuring time'    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq2:    
      description: 'Average sound level over the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq_d:    
      description: 'Average sound level during the day (8h)'    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax:    
      description: 'Maximum sound level recorded during the measuring time'    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax2:    
      description: 'Maximum sound level recorded for the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
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
    dateIssued:    
      description: 'The date and time the forecast was issued by the service provider in ISO8601 UTC format.'    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &noisepollutionforecast_-_properties_-_owner_-_items_-_anyof    
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
    noiseAnnoyanceIndex:    
      description: 'Index (1 to 10) according to noise annoyance level'    
      max: 10    
      min: 1    
      type: number    
      x-ngsi:    
        type: Property    
    noiseOrigin:    
      description: 'Main origin (source) of the recorded noise at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *noisepollutionforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      description: 'NGSI type. It has to be NoisePollutionForecast'    
      enum:    
        - NoisePollutionForecast    
      type: string    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'The start of the validity period for this forecast as a ISO8601 format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validTo:    
      description: 'The end of the validity period for this forecast as a ISO8601 format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollutionForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### NoisePollutionForecast NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen NoisePollutionForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": "2022-07-22T17:37:38Z",  
  "dateModified": "2022-10-22T02:05:56Z",  
  "source": "",  
  "name": "forecast",  
  "alternateName": "",  
  "description": "forecast tomorrow",  
  "dataProvider": "service online Nice",  
  "owner": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
    "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
    "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ]  
  },  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "areaServed": "",  
  "noiseAnnoyanceIndex": 3.8,  
  "LANight": 32.9,  
  "LAmax2": 70.3,  
  "LAeq2": 67.8,  
  "noiseOrigin": "",  
  "LAeq": 39.2,  
  "LAeq_d": 66.2,  
  "LAmax": 74.7,  
  "validFrom": "2022-08-23T05:35:35Z",  
  "validTo": "2022-08-24T05:35:35Z",  
  "validity": "P1D",  
  "dateIssued": "2022-08-23T05:05:35Z"  
}  
```  
#### NoisePollutionForecast NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen NoisePollutionForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": {  
    "type": "date-time",  
    "value": "2022-07-22T17:37:38Z"  
  },  
  "dateModified": {  
    "type": "date-time",  
    "value": "2022-10-22T02:05:56Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "forecast"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "forecast tomorrow"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "service online Nice"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
      "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
      "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.2032497427380235,  
        43.68056738083439  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "France",  
      "addressLocality": "Nice",  
      "postalCode": "06200",  
      "type": "PostalAddress"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "noiseAnnoyanceIndex": {  
    "type": "Number",  
    "value": 3.8  
  },  
  "LANight": {  
    "type": "Number",  
    "value": 32.9  
  },  
  "LAmax2": {  
    "type": "Number",  
    "value": 70.3  
  },  
  "LAeq2": {  
    "type": "Number",  
    "value": 67.8  
  },  
  "noiseOrigin": {  
    "type": "Text",  
    "value": ""  
  },  
  "LAeq": {  
    "type": "Number",  
    "value": 39.2  
  },  
  "LAeq_d": {  
    "type": "Number",  
    "value": 66.2  
  },  
  "LAmax": {  
    "type": "Number",  
    "value": 74.7  
  },  
  "validFrom": {  
    "type": "date-time",  
    "value": "2022-08-23T05:35:35Z"  
  },  
  "validTo": {  
    "type":  "date-time",  
    "value": "2022-08-24T05:35:35Z"  
  },  
  "validity": {  
    "type": "Text",  
    "value": "P1D"  
  },  
  "dateIssued": {  
    "type": "date-time",  
    "value": "2022-08-23T05:05:35Z"  
  }  
}  
```  
#### NoisePollutionForecast NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen NoisePollutionForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": "2022-07-22T17:37:38Z",  
  "dateModified": "2022-10-22T02:05:56Z",  
  "source": "",  
  "name": "forecast",  
  "alternateName": "",  
  "description": "forecast tomorrow",  
  "dataProvider": "service online Nice",  
  "owner": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
    "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
    "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ]  
  },  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "areaServed": "",  
  "noiseAnnoyanceIndex": 3.8,  
  "LANight": 32.9,  
  "LAmax2": 70.3,  
  "LAeq2": 67.8,  
  "noiseOrigin": "",  
  "LAeq": 39.2,  
  "LAeq_d": 66.2,  
  "LAmax": 74.7,  
  "validFrom": "2022-08-23T05:35:35Z",  
  "validTo": "2022-08-24T05:35:35Z",  
  "validity": "P1D",  
  "dateIssued": "2022-08-23T05:05:35Z",  
  "@context": [  
    "https://smartdatamodels.org/dataModel.Environment/context.jsonld"  
  ]  
}  
```  
#### NoisePollutionForecast NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen NoisePollutionForecast im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-07-22T17:37:38Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-10-22T02:05:56Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "forecast"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "forecast tomorrow"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "service online Nice"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
      "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
      "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
    ]  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.2032497427380235,  
        43.68056738083439  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "France",  
      "addressLocality": "Nice",  
      "postalCode": "06200",  
      "type": "PostalAddress"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "noiseAnnoyanceIndex": {  
    "type": "Property",  
    "value": 3.8  
  },  
  "LANight": {  
    "type": "Property",  
    "value": 32.9  
  },  
  "LAmax2": {  
    "type": "Property",  
    "value": 70.3  
  },  
  "LAeq2": {  
    "type": "Property",  
    "value": 67.8  
  },  
  "noiseOrigin": {  
    "type": "Property",  
    "value": ""  
  },  
  "LAeq": {  
    "type": "Property",  
    "value": 39.2  
  },  
  "LAeq_d": {  
    "type": "Property",  
    "value": 66.2  
  },  
  "LAmax": {  
    "type": "Property",  
    "value": 74.7  
  },  
  "validFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-23T05:35:35Z"  
    }  
  },  
  "validTo": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-24T05:35:35Z"  
    }  
  },  
  "validity": {  
    "type": "Property",  
    "value": "P1D"  
  },  
  "dateIssued": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-23T05:05:35Z"  
    }  
  },  
  "@conProperty": [  
    "https://smartdatamodels.org/dataModel.Environment/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
