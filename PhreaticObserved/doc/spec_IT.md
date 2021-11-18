Entità: PhreaticObserved  
========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Il modello di dati è destinato a misurare, osservare e controllare il livello e la qualità delle acque sotterranee in un dato momento (T), tramite un sistema di monitoraggio fisso o mobile. A seconda del dispositivo utilizzato, è anche possibile misurare la qualità dell'acqua come la sua conducibilità elettrica, il suo contenuto di sale, la sua temperatura, ecc. In questo caso, i valori misurati sono trattati dal modello di dati `WaterObserved` e `WaterQualityObserved`. Informazioni aggiuntive sugli attributi: Per gli attributi dedicati all'acqua, si può anche usare un attributo MetaData che contiene il `TimeStamp` in secondi, la `qualificazione` e il controllo `status` della misurazione.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateObserved`: La data e l'ora di questa osservazione nel formato ISO8601 UTC  - `dateObservedFrom`: Periodo di osservazione : Data e ora di inizio in formato ISO8601 UTC  - `dateObservedTo`: Periodo di osservazione : Data e ora di fine in un formato ISO8601 UTC  - `depth`: Profondità dell'acqua potabile, dalla sua identificazione `waterTable`. Il codice dell'unità (testo) di misura dato usando il [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 caratteri). Per esempio, <code> MTR </code> rappresenta Meter.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `investigationDepth`: Profondità massima in cui è stata fatta l'indagine. Il codice dell'unità (testo) di misura dato usando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (massimo 3 caratteri). Per esempio, <code>MTR</code> rappresenta Meter  - `isMobile`: Il dispositivo utilizzato è Fisso (Falso) o Mobile (Vero)  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `measurementType`: Periodo di osservazione : Tipo di misurazione trattata. Enum:'profondità, volume, qualità, altro'.  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `pollutionRate`: Tasso di inquinamento. Il codice dell'unità (testo) di misura dato usando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (massimo 3 caratteri). Per esempio, P1 rappresenta la Percentuale.  - `pressure`: Pressione dell'acqua. Il codice dell'unità (testo) di misura dato usando il [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 caratteri). Per esempio, <code>BAR</code> rappresenta Bar.  - `refDevice`: Riferimento ai dispositivi che forniscono dati  - `residueLevel`: Livello di residuo trovato  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI. Deve essere PhreaticObserved  - `waterTable`: Livello al quale è stata trovata l'acqua durante l'indagine. Il codice dell'unità (testo) di misura dato usando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (massimo 3 caratteri). Per esempio, <code>MTR</code> rappresenta il metro.    
Proprietà richieste  
- `dateObserved`  - `id`  - `location`  - `measurementType`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhreaticObserved:    
  description: 'The Data Model is intended to measure, observe and control the level and quality of groundwater at a given time (T), by a fixed or mobile monitoring system. Depending on the device used, it is also possible to measure the quality of water such as its electrical conductivity, its salt content, its temperature, etc. In this case, the values measured are processed by the Data Model `WaterObserved` and `WaterQualityObserved`. Additional Information about Attributes: For attributes dedicated to water, a MetaData attribute can also be used. it contains the `TimeStamp` in seconds, the `qualification` and control `status` of the measurement.'    
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
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    depth:    
      description: 'Depth of drinking water, since its identification `waterTable`. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code> MTR </code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &phreaticobserved_-_properties_-_owner_-_items_-_anyof    
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
    investigationDepth:    
      description: 'Maximum depth where the investigation was made. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: meters    
    isMobile:    
      description: 'The device used is Fixed (False) or Mobile (True)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    measurementType:    
      description: 'Observation period : Type of measurement processed. Enum:''depth, volume, quality, other'''    
      items:    
        enum:    
          - depth    
          - volume    
          - quality    
          - other    
        type: string    
      minItems: 0    
      type: array    
      uniqueItems: false    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pollutionRate:    
      description: 'Rate of pollution. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, P1 represents Percentage.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressure:    
      description: 'Water Pressure. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>BAR</code> represents Bar.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Bar    
    refDevice:    
      description: 'Reference to the devices providing data'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://scehma.org/URL    
        type: Relationship    
    residueLevel:    
      description: 'Residue level found'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
      description: 'NGSI Entity type. It has to be PhreaticObserved'    
      enum:    
        - PhreaticObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterTable:    
      description: 'Level at which water was found during this investigation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - measurementType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### PhreaticObserved NGSI-v2 key-values Esempio  
Ecco un esempio di un PhreaticObserved in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": "STLRT-MNCA-NP-015",  
  "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-07-07T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-NP-015"  
  ],  
  "isMobile": false,  
  "measurementType": [  
    "depth",  
    "volume"  
  ],  
  "investigationDepth": 22.35,  
  "waterTable": 12.75,  
  "depth": 20.45,  
  "pressure": 2.12  
}  
```  
#### PhreaticObserved NGSI-v2 normalizzato Esempio  
Ecco un esempio di un PhreaticObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
	"id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
	"type": "PhreaticObserved",  
	"name": {  
		"type": "Property",  
		"value": "STLRT-MNCA-NP-015"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
	},  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [43.664810, 7.196545]  
        }  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Airport"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:Device:T1-NP-015"]  
	},  
	"isMobile": {  
		"type": "Property",  
		"value": false  
	},  
	"measurementType": {  
		"type": "Property",  
		"value": ["depth", "volume"]  
	},  
	"investigationDepth": {  
		"type": "Property",  
		"value": 22.35  
	},  
	"waterTable": {  
		"type": "Property",  
		"value": 12.75,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 2"  
		}  
	},  
	"depth": {  
		"type": "Property",  
		"value": 20.45,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Incorrect"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 1"  
		}  
	},  
	"pressure": {  
		"type": "Property",  
		"value": 2.12,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 3"  
		}  
	}  
}  
```  
#### Esempio di valori chiave NGSI-LD freatici osservati  
Ecco un esempio di un PhreaticObserved in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": {  
    "type": "Property",  
    "value": "STLRT-MNCA-NP-015"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
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
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-07-07T15:05:59.408Z"  
    }  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "Object": [  
      "urn:ngsi-ld:Device:T1-NP-015"  
    ]  
  },  
  "isMobile": {  
    "type": "Property",  
    "value": false  
  },  
  "measurementType": {  
    "type": "Property",  
    "value": [  
      "depth",  
      "volume"  
    ]  
  },  
  "investigationDepth": {  
    "type": "Property",  
    "value": 22.35  
  },  
  "waterTable": {  
    "type": "Property",  
    "value": 12.75,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "qualification": {  
      "type": "Property",  
      "value": "Correct"  
    },  
    "status ": {  
      "type": "Property",  
      "value": "Level 2"  
    }  
  },  
  "depth": {  
    "type": "Property",  
    "value": 20.45,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "qualification": {  
      "type": "Property",  
      "value": "Incorrect"  
    },  
    "status ": {  
      "type": "Property",  
      "value": "Level 1"  
    }  
  },  
  "pressure": {  
    "type": "Property",  
    "value": 2.12,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "qualification": {  
      "value": "Correct"  
    },  
    "status ": {  
      "type": "Property",  
      "value": "Level 3"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### FreaticObserved NGSI-LD normalizzato Esempio  
Ecco un esempio di un PhreaticObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": "STLRT-MNCA-NP-015",  
  "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-07-07T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-NP-015"  
  ],  
  "isMobile": false,  
  "measurementType": [  
    "depth",  
    "volume"  
  ],  
  "investigationDepth": 22.35,  
  "waterTable": 12.75,  
  "depth": 20.45,  
  "pressure": 2.12,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
