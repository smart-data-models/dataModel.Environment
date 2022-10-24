<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: IndoorEnvironmentObserved  
==================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/IndoorEnvironmentObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Beobachtung der Luft- und Klimabedingungen für Innenräume**.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: Gemessener atmosphärischer Druck  - `co2[number]`: Die gemessene C02-Konzentration im Innenraum wird in mg/L angegeben.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateObserved[string]`: Datum und Uhrzeit der Beobachtung in ISO8601  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `illuminance[number]`: Gemessene Beleuchtungsstärke  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `peopleCount[number]`: Anzahl der Personen im Raum  - `refDevice[*]`: Ein Verweis auf das/die Gerät(e), das/die diese Beobachtung aufgezeichnet hat/haben.  - `refPointOfInterest[*]`: Ein Verweis auf einen Punkt von Interesse, der mit dieser Beobachtung verbunden ist.  - `relativeHumidity[number]`: Gemessene Luftfeuchtigkeit  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sensorHeight[number]`: Höhe des Sensors (Abstand vom Boden)  - `sensorPlacement[string]`: Position des Sensors  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `temperature[number]`: Gemessene Temperatur  - `type[string]`: NGSI Entitätstyp  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
IndoorEnvironmentObserved:    
  description: 'An observation of air and climate conditions for indoor environments.'    
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
    atmosphericPressure:    
      description: 'Measured atmospheric pressure'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co2:    
      description: 'The measured interior C02 concentration nominally in mg/L'    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'mg per liter'    
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
      description: 'Date and time of the observation in ISO8601'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &indoorenvironmentobserved_-_properties_-_owner_-_items_-_anyof    
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
    illuminance:    
      description: 'Measured illuminance'    
      minimum: 0    
      type: number    
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
        anyOf: *indoorenvironmentobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peopleCount:    
      description: 'Number of people in the room'    
      minimum: 0    
      type: number    
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
      description: 'A reference to the device(s) which captured this observation.'    
      x-ngsi:    
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
      description: 'A reference to a point of interest associated to this observation.'    
      x-ngsi:    
        type: Relationship    
    relativeHumidity:    
      description: 'Measured humidity'    
      minimum: 0    
      type: number    
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
    sensorHeight:    
      description: 'Height of the sensor (distance from the floor)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    sensorPlacement:    
      description: 'Position of the sensor'    
      enum:    
        - northWall    
        - southWall    
        - eastWall    
        - westWall    
        - center    
        - floor    
        - roof    
        - ceiling    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Measured temperature'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - IndoorEnvironmentObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/IndoorEnvironmentObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/dataModel.Environment/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### IndoorEnvironmentObserved NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein IndoorEnvironmentObserved im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
        "id": "urn:ngsi:MuseoDemo_Room_1",  
        "type": "IndoorEnvironmentObserved",  
        "dateObserved": "2020-06-08T17:54:00",  
        "refPointOfInterest": "urn:ngsi:MuseoDemo",  
        "address": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address"  
        },  
        "location": {  
            "type": "Point",  
            "coordinates": [  
                40,  
                11  
            ]  
        },  
        "peopleCount": 10,  
        "temperature": 12.2,  
        "relativeHumidity": 0.54,  
        "atmosphericPressure": 1013.52,  
        "illuminance": 1000,  
        "CO": 500,  
        "NO": 45,  
        "NO2": 69,  
        "NOx": 139,  
        "SO2": 11  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein IndoorEnvironmentObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "dateObserved": {  
        "value": "2020-06-08T17:54:00"  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "value": "urn:ngsi:MuseoDemo"  
    },  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [40, 11]  
        }  
    },  
    "address": {  
        "type": "PostalAddress",  
        "value": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address"  
        }  
    },  
    "peopleCount": {  
        "value": 10  
    },  
    "temperature": {  
        "value": 12.2,  
        "metadata": {  
            "unitCode": {  
                "value": "CEL"  
            }  
        }  
    },  
    "relativeHumidity": {  
        "value": 0.54,  
        "metadata": {  
            "unitCode": {  
                "value": "P1"  
            }  
        }  
    },  
    "illuminance": {  
        "value": 1000,  
        "metadata": {  
            "unitCode": {  
                "value": "LX"  
            }  
        }  
    },  
    "CO": {  
        "value": 500,  
        "metadata": {  
            "unitCode": {  
                "value": "GP"  
            }  
        }  
    },  
    "NO": {  
        "value": 45,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "NOx": {  
        "value": 139,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "NO2": {  
        "value": 69,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "SO2": {  
        "value": 11,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    }  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein IndoorEnvironmentObserved im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "CO": {  
        "type": "Property",  
        "value": 500,  
        "unitCode": "GP"  
    },  
    "NO": {  
        "type": "Property",  
        "value": 45,  
        "unitCode": "GQ"  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address",  
            "type": "PostalAddress"  
        }  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 1000  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                40,  
                11  
            ]  
        }  
    },  
    "peopleCount": {  
        "type": "Property",  
        "value": 10  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo"  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "@context": [  
        "https://fiware.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein IndoorEnvironmentObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "CO": {  
        "type": "Property",  
        "value": 500,  
        "unitCode": "GP"  
    },  
    "NO": {  
        "type": "Property",  
        "value": 45,  
        "unitCode": "GQ"  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address",  
            "type": "PostalAddress"  
        }  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 1000  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                40,  
                11  
            ]  
        }  
    },  
    "peopleCount": {  
        "type": "Property",  
        "value": 10  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo"  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "@context": [  
        "https://fiware.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld",  
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
