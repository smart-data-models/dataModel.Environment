<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: AirQualityForecast    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Vorhersage der Luftqualitätsbedingungen für einen bestimmten Zeitraum**    
Version: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `airQualityIndex[number]`: Der Luftqualitätsindex ist eine Zahl, die die Qualität der Luft an einem bestimmten Tag angibt.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: Qualitatives Gesamtniveau der Gesundheitsbedenken entsprechend der beobachteten Luftqualität  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: Prognostiziertes Kohlendioxid  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `no2[number]`: Prognostiziertes Stickstoffdioxid  - `nox[number]`: Andere Stickstoffoxide prognostiziert  - `o3[number]`: Ozon vorhergesagt  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pm10[number]`: Feinstaub mit einem Durchmesser von 10 Mikrometern oder weniger  - `pm25[number]`: Partikel mit einem Durchmesser von 2,5 Mikrometern oder weniger  - `precipitation[number]`: Menge des Regenwassers  . Model: [https://schema.org/Number](https://schema.org/Number)- `relativeHumidity[number]`: Luftfeuchtigkeit  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `so2[number]`: Schwefeldioxid nachgewiesen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `temperature[number]`: Temperatur des Gegenstandes  - `type[string]`: NGSI Entity type: es muss AirQualityForecast sein  - `validFrom[date-time]`: Beginn des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validTo[date-time]`: Das Ende des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validity[string]`: Enthält den Gültigkeitszeitraum für diese Prognose als ISO8601-Zeitintervall  . Model: [https://schema.org/Text](https://schema.org/Text)- `windSpeed[number]`: Intensität des Windes  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AirQualityForecast:      
  description: A forecast of air quality conditions valid during a period      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    airQualityIndex:      
      description: Air quality index is a number used to report the quality of the air on any given day      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    airQualityLevel:      
      description: Overall qualitative level of health concern corresponding to the air quality observed      
      minLength: 2      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    co2:      
      description: Carbon Dioxide forecasted      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    no2:      
      description: Nitrogen dioxide forecasted      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    nox:      
      description: Other Nitrogen oxides forecasted      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    o3:      
      description: Ozone forecasted      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    pm10:      
      description: Particulate matter 10 micrometers or less in diameter      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    pm25:      
      description: Particulate matter 2.5 micrometers or less in diameter      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    precipitation:      
      description: Amount of water rain      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Liters per square meter      
    relativeHumidity:      
      description: Humidity in the Air      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
    so2:      
      description: Sulfur dioxide detected      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    temperature:      
      description: Temperature of the item      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: 'NGSI Entity type: it has to be AirQualityForecast'      
      enum:      
        - AirQualityForecast      
      type: string      
      x-ngsi:      
        type: Property      
    validFrom:      
      description: The start of the validity period for this forecast as a ISO8601 format      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    validTo:      
      description: The end of the validity period for this forecast as a ISO8601 format      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    validity:      
      description: Includes the validity period for this forecast as a ISO8601 time interval      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    windSpeed:      
      description: Intensity of the wind      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http//schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityForecast/schema.json      
  x-model-tags: GreenMov      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### AirQualityForecast NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 3,  
  "airQualityLevel": "moderate",  
  "co2": 45,  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateIssued": "2022-07-01T10:40:01.00Z",  
  "dateRetrieved": "2022-07-01T12:57:24.00Z",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "no2": 69,  
  "nox": 139,  
  "o3": 100,  
  "pm10": 19,  
  "pm25": 21,  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "so2": 11,  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "validFrom": "2022-07-01T17:00:00.00Z",  
  "validTo": "2022-07-01T18:00:00.00Z",  
  "validity": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00",  
  "windSpeed": 0.64  
}  
```  
</details>    
#### AirQualityForecast NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice"  
    }  
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
  "dataProvider": {  
    "type": "Text",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateIssued": {  
    "type": "DateTime",  
    "value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateRetrieved": {  
    "type": "DateTime",  
    "value": "2022-07-01T12:57:24.00Z"  
  },  
  "validFrom": {  
    "type": "DateTime",  
    "value": "2022-07-01T17:00:00.00Z"  
  },  
  "validTo": {  
    "type": "DateTime",  
    "value": "2022-07-01T18:00:00.00Z"  
  },  
  "validity": {  
    "type": "DateTime",  
    "value": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00"  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 3  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "moderate"  
  },  
  "co2": {  
    "type": "Number",  
    "value": 45  
  },  
  "no2": {  
    "type": "Number",  
    "value": 69  
  },  
  "o3": {  
    "type": "Number",  
    "value": 100  
  },  
  "nox": {  
    "type": "Number",  
    "value": 139  
  },  
  "so2": {  
    "type": "Number",  
    "value": 11  
  },  
  "pm10": {  
    "type": "Number",  
    "value": 19  
  },  
  "pm25": {  
    "type": "Number",  
    "value": 21  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 12.2  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.54  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 0.64  
  },  
  "precipitation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "typeOfLocation": {  
    "type": "Text",  
    "value": "outdoor"  
  }  
}  
```  
</details>    
#### AirQualityForecast NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 3,  
  "airQualityLevel": "moderate",  
  "co2": 45,  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateIssued": "2022-07-01T10:40:01.00Z",  
  "dateRetrieved": "2022-07-01T12:57:24.00Z",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "no2": 69,  
  "nox": 139,  
  "o3": 100,  
  "pm10": 19,  
  "pm25": 21,  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "so2": 11,  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "validFrom": "2022-07-01T17:00:00.00Z",  
  "validTo": "2022-07-01T18:00:00.00Z",  
  "validity": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00",  
  "windSpeed": 0.64,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AirQualityForecast NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice",  
      "type": "PostalAddress"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.2032497427380235,  
        43.68056738083439  
      ]  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateIssued": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T10:40:01.00Z"  
    }  
  },  
  "dateRetrieved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T12:57:24.00Z"  
    }  
  },  
  "validFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T17:00:00.00Z"  
    }  
  },  
  "validTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T18:00:00.00Z"  
    }  
  },  
  "validity": {  
    "type": "Property",  
    "value": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00"  
  },  
  "airQualityIndex": {  
    "type": "Property",  
    "value": 3  
  },  
  "airQualityLevel": {  
    "type": "Property",  
    "value": "moderate"  
  },  
  "co2": {  
    "type": "Property",  
    "value": 45,  
    "unitCode": "GQ"  
  },  
  "no2": {  
    "type": "Property",  
    "value": 69,  
    "unitCode": "GQ"  
  },  
  "o3": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "GQ"  
  },  
  "nox": {  
    "type": "Property",  
    "value": 139,  
    "unitCode": "GQ"  
  },  
  "so2": {  
    "type": "Property",  
    "value": 11,  
    "unitCode": "GQ"  
  },  
  "pm10": {  
    "type": "Property",  
    "value": 19,  
    "unitCode": "GQ"  
  },  
  "pm25": {  
    "type": "Property",  
    "value": 21,  
    "unitCode": "GQ"  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 12.2  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.54  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 0.64  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 0  
  },  
  "typeOfLocation": {  
    "type": "Property",  
    "value": "outdoor"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
