<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: TrafficEnvironmentImpactForecast  
=========================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Umweltauswirkungen des Verkehrs auf der Grundlage der Verkehrserwartungen der Fahrzeuge und ihrer Emissionsmerkmale**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: Die erwartete C02-Emissionskonzentration  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateIssued[string]`: Das Datum und die Uhrzeit, zu der die Vorhersage vom Diensteanbieter erstellt wurde, im Format ISO8601 UTC.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `traffic[array]`: Array von Objekten, die die erwarteten Werte für Intensität, Besetzung und Geschwindigkeit der verschiedenen Fahrzeugtypen enthalten  - `type[string]`: NGSI-Typ. Es muss TrafficEnvironmentImpactForecast sein  - `validFrom[string]`: Beginn des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validTo[string]`: Das Ende des Gültigkeitszeitraums dieser Prognose im ISO8601-Format  - `validity[string]`: Enthält den Gültigkeitszeitraum für diese Prognose als ISO8601-Zeitintervall.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
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
TrafficEnvironmentImpactForecast:    
  description: 'Environmental Impact of traffic based on the vehicles traffic expectations and their emission characteristics'    
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
    co2:    
      description: 'The expected C02 emission concentration'    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/L    
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
      anyOf: &trafficenvironmentimpactforecast_-_properties_-_owner_-_items_-_anyof    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficenvironmentimpactforecast_-_properties_-_owner_-_items_-_anyof    
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
    traffic:    
      description: 'Array of objects containing the expected values for intensity, occupation an speed of the different vehicle types'    
      items:    
        properties:    
          averageVehicleSpeedExpected:    
            description: 'Property. Average speed expected of the vehicles transiting during the observation period. Model:''https://schema.org/Number''. Units:''Kilometer per hour (Km/h)'''    
            minimum: 0    
            type: number    
          intensityExpected:    
            description: 'Property. Total number of vehicles expected during this forecast period. Model:''https://schema.org/Number''.'    
            minimum: 0    
            type: number    
          occupancyExpected:    
            description: 'Property. Fraction of the observation time where a vehicle has been occupying the observed lane. Model:''https://schema.org/Number''.'    
            maximum: 1    
            minimum: 0    
            type: number    
          vehicleClass:    
            description: 'Property. Enumeration of the vehicle classes'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type. It has to be TrafficEnvironmentImpactForecast'    
      enum:    
        - TrafficEnvironmentImpact    
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
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/TrafficEnvironmentImpactForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### TrafficEnvironmentImpactForecast NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen TrafficEnvironmentImpactForecast im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
  "type": "TrafficEnvironmentImpact",  
  "dateCreated": "2022-08-17T05:21:50Z",  
  "dateModified": "2022-08-30T08:09:40Z",  
  "dateIssued": "2022-08-30T08:09:40Z",  
  "validFrom": "2022-08-30T08:19:40Z",  
  "validTo": "2022-08-31T08:19:40Z",  
  "validity": "P1D",  
  "source": "",  
  "name": "Environmental impact",  
  "alternateName": "",  
  "description": "",  
  "dataProvider": "City sensors",  
  "owner": [  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.7034,  
      7.2663  
    ]  
  },  
  "address": {  
    "streetAddress": "Rue Frédéric Mistral",  
    "addressLocality": "Valbonne",  
    "addressRegion": "Sophia Antipolis",  
    "addressCountry": "France",  
    "postalCode": "06550",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "",  
  "co2": 582.3,  
  "traffic": [  
    {  
      "vehicleClass": "A",  
      "intensityExpected": 23,  
      "occupancyExpected": 0.2,  
      "averageVehicleSpeedExpected": 45  
    },  
    {  
      "vehicleClass": "B",  
      "intensityExpected": 112,  
      "occupancyExpected": 0.15,  
      "averageVehicleSpeedExpected": 65  
    }  
  ]  
}  
```  
</details>  
#### TrafficEnvironmentImpactForecast NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen TrafficEnvironmentImpactForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
  "type": "TrafficEnvironmentImpact",  
  "dateCreated": {  
    "type": "date-time",  
    "value": "2022-08-17T05:21:50Z"  
  },  
  "dateModified": {  
    "type": "date-time",  
    "value": "2022-08-30T08:09:40Z"  
  },  
  "dateIssued": {  
    "type": "Date-Time",  
    "value": "2022-08-30T08:09:40Z"  
  },  
  "validFrom": {  
    "type": "Date-Time",  
    "value": "2022-08-30T08:19:40Z"  
  },  
  "validTo": {  
    "type": "Date-Time",  
    "value": "2022-08-31T08:19:40Z"  
  },  
  "validity": {  
    "type": "Text",  
    "value": "P1D"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Environmental impact"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "City sensors"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
    ]  
  },  
  "location": {  
    "type": "object",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Rue Frédéric Mistral",  
      "addressLocality": "Valbonne",  
      "addressRegion": "Sophia Antipolis",  
      "addressCountry": "France",  
      "postalCode": "06550",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "co2": {  
    "type": "Number",  
    "value": 582.3  
  },  
  "traffic": {  
    "type": "array",  
    "value": [  
       {  
      "vehicleClass": "A",  
      "intensityExpected": 23,  
      "occupancyExpected": 0.2,  
      "averageVehicleSpeedExpected": 45  
    },  
    {  
      "vehicleClass": "B",  
      "intensityExpected": 112,  
      "occupancyExpected": 0.15,  
      "averageVehicleSpeedExpected": 65  
    }  
    ]  
  }  
}  
```  
</details>  
#### TrafficEnvironmentImpactForecast NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen TrafficEnvironmentImpactForecast im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
    "type": "TrafficEnvironmentImpact",  
    "dateCreated": "2022-08-17T05:21:50Z",  
    "dateModified": "2022-08-30T08:09:40Z",  
    "dateIssued": "2022-08-30T08:09:40Z",  
    "validFrom": "2022-08-30T08:19:40Z",  
    "validTo": "2022-08-31T08:19:40Z",  
    "validity": "P1D",  
    "source": "",  
    "name": "Environmental impact",  
    "alternateName": "",  
    "description": "",  
    "dataProvider": "City sensors",  
    "owner": [  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.7034,  
            7.2663  
        ]  
    },  
    "address": {  
        "streetAddress": "Rue Fr\u00e9d\u00e9ric Mistral",  
        "addressLocality": "Valbonne",  
        "addressRegion": "Sophia Antipolis",  
        "addressCountry": "France",  
        "postalCode": "06550",  
        "postOfficeBoxNumber": ""  
    },  
    "areaServed": "",  
    "co2": 582.3,  
    "traffic": [  
        {  
            "vehicleClass": "A",  
            "intensityExpected": 23,  
            "occupancyExpected": 0.2,  
            "averageVehicleSpeedExpected": 45  
        },  
        {  
            "vehicleClass": "B",  
            "intensityExpected": 112,  
            "occupancyExpected": 0.15,  
            "averageVehicleSpeedExpected": 65  
        }  
    ],  
    "@context": [  
        "https://smartdatamodels.org/dataModel.Environment/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TrafficEnvironmentImpactForecast NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen TrafficEnvironmentImpactForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
    "type": "TrafficEnvironmentImpact",  
    "dateCreated": {  
        "type": "Property",  
        "value": "2022-08-17T05:21:50Z"  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": "2022-08-30T08:09:40Z"  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": "2022-08-30T08:09:40Z"  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": "2022-08-30T08:19:40Z"  
    },  
    "validTo": {  
        "type": "Property",  
        "value": "2022-08-31T08:19:40Z"  
    },  
    "validity": {  
        "type": "Property",  
        "value": "P1D"  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "name": {  
        "type": "Property",  
        "value": "Environmental impact"  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "description": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "City sensors"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.7034,  
                7.2663  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Rue Fr\u00e9d\u00e9ric Mistral",  
            "addressLocality": "Valbonne",  
            "addressRegion": "Sophia Antipolis",  
            "addressCountry": "France",  
            "postalCode": "06550",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "co2": {  
        "type": "Property",  
        "value": 582.3  
    },  
    "traffic": {  
        "type": "Property",  
        "value": [  
            {  
                "vehicleClass": "A",  
                "intensityExpected": 23,  
                "occupancyExpected": 0.2,  
                "averageVehicleSpeedExpected": 45  
            },  
            {  
                "vehicleClass": "B",  
                "intensityExpected": 112,  
                "occupancyExpected": 0.15,  
                "averageVehicleSpeedExpected": 65  
            }  
        ]  
    },  
    "@context": [  
        "https://smartdatamodels.org/dataModel.Environment/context.jsonld",  
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
