Entità: IndoorEnvironmentObserved  
=================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/IndoorEnvironmentObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un'osservazione delle condizioni dell'aria e del clima per gli ambienti interni.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `atmosphericPressure`: Pressione atmosferica misurata  - `co2`: La concentrazione interna di C02 misurata nominalmente in mg/L  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateObserved`: Data e ora dell'osservazione in ISO8601  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `illuminance`: Illuminamento misurato  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `peopleCount`: Numero di persone nella stanza  - `refDevice`: Un riferimento al dispositivo o ai dispositivi che hanno catturato questa osservazione.  - `refPointOfInterest`: Un riferimento a un punto di interesse associato a questa osservazione.  - `relativeHumidity`: Umidità misurata  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sensorHeight`: Altezza del sensore (distanza dal pavimento)  - `sensorPlacement`: Posizione del sensore  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `temperature`: Temperatura misurata  - `type`: Tipo di entità NGSI    
Proprietà richieste  
- `dateObserved`  - `id`  - `location`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### Valori chiave NGSI-v2 di IndoorEnvironmentObserved Esempio  
Ecco un esempio di IndoorEnvironmentObserved in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### IndoorEnvironmentObserved NGSI-v2 normalizzato Esempio  
Ecco un esempio di un IndoorEnvironmentObserved in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Valori-chiave NGSI-LD osservati nell'ambiente interno Esempio  
Ecco un esempio di IndoorEnvironmentObserved in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
  "type": "IndoorEnvironmentObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
  },  
  "refPointOfInterest": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo"  
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
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "IT",  
      "addressLocality": "Demo city",  
      "streetAddress": "Demo address",  
      "type": "PostalAddress"  
    }  
  },  
  "peopleCount": {  
    "type": "Property",  
    "value": 10  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 12.2  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.54  
  },  
  "illuminance": {  
    "type": "Property",  
    "value": 1000  
  },  
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
  "NOx": {  
    "type": "Property",  
    "value": 139,  
    "unitCode": "GQ"  
  },  
  "NO2": {  
    "type": "Property",  
    "value": 69,  
    "unitCode": "GQ"  
  },  
  "SO2": {  
    "type": "Property",  
    "value": 11,  
    "unitCode": "GQ"  
  },  
  "@context": [  
    "https://fiware.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld"  
  ]  
}  
```  
#### IndoorEnvironmentObserved NGSI-LD normalizzato Esempio  
Ecco un esempio di un IndoorEnvironmentObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [40, 11]  
        }  
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
    "peopleCount": {  
        "type": "Property",  
        "value": 10  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 1000  
    },  
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
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "@context": [  
        "https://fiware.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld"  
    ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza