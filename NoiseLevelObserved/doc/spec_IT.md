Entità: NoiseLevelObserved  
==========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoiseLevelObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un'osservazione di quei parametri acustici che stimano i livelli di pressione acustica in un certo luogo e tempo. **  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateObserved`: La data e l'ora di questa osservazione rappresentata da un intervallo ISO8601.  - `dateObservedFrom`: Data e ora di inizio del periodo di osservazione.  - `dateObservedTo`: Data e ora di fine del periodo di osservazione. Vedere dateObserved.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `refDevice`: Un riferimento al dispositivo che ha catturato questa osservazione.  - `refPointOfInterest`: Un riferimento a un punto di interesse associato a questa osservazione.  - `refWeatherObserved`: Riferimento alle condizioni meteorologiche associate.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sonometerClass`: Classe del sonometro (0, 1, 2) secondo l'ANSI usato per prendere questa osservazione  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI    
Proprietà richieste  
- `dateObservedFrom`  - `dateObservedTo`  - `id`  - `location`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoiseLevelObserved:    
  description: 'An observation of those acoustic parameters that estimate noise pressure levels at a certain place and time. '    
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
      description: 'The date and time of this observation represented by an ISO8601 interval.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See dateObserved.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &noiselevelobserved_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *noiselevelobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A reference to the device which captured this observation.'    
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
    refWeatherObserved:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the associated weather conditions.'    
      x-ngsi:    
        type: Relationship    
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
    sonometerClass:    
      description: 'Class of sonometer (0, 1, 2) according to ANSI used for taking this observation'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - NoiseLevelObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObservedFrom    
    - dateObservedTo    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoiseLevelObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoiseLevelObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### Valori chiave NGSI-v2 NoiseLevelObserved Esempio  
Ecco un esempio di NoiseLevelObserved in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "type": "NoiseLevelObserved",  
  "LAS": 91.6,  
  "LAeq": 67.8,  
  "LAeq_d": 65.4,  
  "LAmax": 94.5,  
  "dateObservedFrom": "2016-12-28T11:00:00.00Z",  
  "dateObservedTo": "2016-12-28T12:00:00.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [-2.698, 42.8491]  
  }  
}  
```  
#### NoiseLevelObserved NGSI-v2 normalizzato Esempio  
Ecco un esempio di NoiseLevelObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-28T11:00:00.00Z"  
  },  
  "LAmax": {  
    "value": 94.5  
  },  
  "LAeq": {  
    "value": 67.8  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-28T12:00:00.00Z"  
  },  
  "LAeq_d": {  
    "value": 65.4  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-2.698, 42.8491]  
    }  
  },  
  "type": "NoiseLevelObserved",  
  "id": "Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "LAS": {  
    "value": 91.6  
  }  
}  
```  
#### Valori chiave NGSI-LD NoiseLevelObserved Esempio  
Ecco un esempio di NoiseLevelObserved in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:NoiseLevelObserved:Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "type": "NoiseLevelObserved",  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-28T11:00:00.00Z"  
    }  
  },  
  "LAmax": {  
    "type": "Property",  
    "value": 94.5  
  },  
  "LAeq": {  
    "type": "Property",  
    "value": 67.8  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-28T12:00:00.00Z"  
    }  
  },  
  "LAeq_d": {  
    "type": "Property",  
    "value": 65.4  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -2.698,  
        42.8491  
      ]  
    }  
  },  
  "LAS": {  
    "type": "Property",  
    "value": 91.6  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### NoiseLevelObserved NGSI-LD normalizzato Esempio  
Ecco un esempio di NoiseLevelObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "LAS": 91.6,  
  "LAeq": 67.8,  
  "LAeq_d": 65.4,  
  "LAmax": 94.5,  
  "dateObservedFrom": {  
    "@type": "DateTime",  
    "@value": "2016-12-28T11:00:00.00Z"  
  },  
  "dateObservedTo": {  
    "@type": "DateTime",  
    "@value": "2016-12-28T12:00:00.00Z"  
  },  
  "id": "urn:ngsi-ld:NoiseLevelObserved:Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "location": {  
    "coordinates": [  
      -2.698,  
      42.8491  
    ],  
    "type": "Point"  
  },  
  "type": "NoiseLevelObserved"  
}  
```  
