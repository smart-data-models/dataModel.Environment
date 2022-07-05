[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: AirQualityForecast  
===========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Vorhersage der Luftqualitätsbedingungen für einen bestimmten Zeitraum**  
Version: 0.0.1  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `airQualityIndex`: Der Luftqualitätsindex ist eine Zahl, die die Qualität der Luft an einem bestimmten Tag angibt.  - `airQualityLevel`: Qualitatives Gesamtniveau der Gesundheitsbedenken entsprechend der beobachteten Luftqualität  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `co2`: Prognostiziertes Kohlendioxid  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `no2`: Prognostiziertes Stickstoffdioxid  - `nox`: Andere Stickstoffoxide prognostiziert  - `o3`: Ozon vorhergesagt  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pm10`: Feinstaub mit einem Durchmesser von 10 Mikrometern oder weniger  - `pm25`: Partikel mit einem Durchmesser von 2,5 Mikrometern oder weniger  - `precipitation`: Wassermenge Regen  - `relativeHumidity`: Luftfeuchtigkeit  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `so2`: Schwefeldioxid nachgewiesen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `temperature`: Temperatur des Gegenstandes  - `type`: NGSI Entity type: es muss AirQualityForecast sein  - `validFrom`: Beginn des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `windSpeed`: Intensität des Windes    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AirQualityForecast:    
  description: 'A forecast of air quality conditions valid during a period'    
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
    airQualityIndex:    
      description: 'Air quality index is a number used to report the quality of the air on any given day.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityLevel:    
      description: 'Overall qualitative level of health concern corresponding to the air quality observed'    
      minLength: 2    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Tex '    
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
    co2:    
      description: 'Carbon Dioxide forecasted'    
      minimum: 0    
      type: number    
      x-ngsi:    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &airqualityforecast_-_properties_-_owner_-_items_-_anyof    
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
    no2:    
      description: 'Nitrogen dioxide forecasted'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    nox:    
      description: 'Other Nitrogen oxides forecasted'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    o3:    
      description: 'Ozone forecasted'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *airqualityforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pm10:    
      description: 'Particulate matter 10 micrometers or less in diameter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm25:    
      description: 'Particulate matter 2.5 micrometers or less in diameter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: 'Amount of water rain'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Liters per square meter.'    
    relativeHumidity:    
      description: 'Humidity in the Air'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    so2:    
      description: 'Sulfur dioxide detected'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the item'    
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
      description: 'The start of the validity period for this forecast as a ISO8601 format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    windSpeed:    
      description: 'Intensity of the wind'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### AirQualityForecast NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "dateIssued": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateRetrieved": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T12:57:24.00Z"  
  },  
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
#### AirQualityForecast NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "type": "PostalAddress",  
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
    "type": "Text",  
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
    "value": 45,  
    "unitCode": "GQ"  
  },  
  "no2": {  
    "type": "Number",  
    "value": 69,  
    "unitCode": "GQ"  
  },  
  "o3": {  
    "type": "Number",  
    "value": 100,  
    "unitCode": "GQ"  
  },  
  "nox": {  
    "type": "Number",  
    "value": 139,  
    "unitCode": "GQ"  
  },  
  "so2": {  
    "type": "Number",  
    "value": 11,  
    "unitCode": "GQ"  
  },  
  "pm10": {  
    "type": "Number",  
    "value": 19,  
    "unitCode": "GQ"  
  },  
  "pm25": {  
    "type": "Number",  
    "value": 21,  
    "unitCode": "GQ"  
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
    "type": "Number",  
    "value": 0  
  },  
  "typeOfLocation": {  
    "type": "Text",  
    "value": "outdoor"  
  }  
}  
```  
#### AirQualityForecast NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "dateIssued": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateRetrieved": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T12:57:24.00Z"  
  },  
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
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
#### AirQualityForecast NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen AirQualityForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
