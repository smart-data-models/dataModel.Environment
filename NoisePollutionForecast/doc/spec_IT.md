<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: RumoreInquinamentoPrevisione  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **La previsione dell'inquinamento acustico memorizza l'aspettativa sull'inquinamento acustico in base ad alcuni elementi di input e agli elementi di rumore presenti.**  
versione: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `LANight[number]`: Livello sonoro medio registrato durante la notte (8 ore)  - `LAeq[number]`: Livello sonoro medio (equivalente) registrato durante il tempo di misurazione  - `LAeq2[number]`: Livello sonoro medio nelle ultime 2 ore  - `LAeq_d[number]`: Livello sonoro medio durante il giorno (8 ore)  - `LAmax[number]`: Livello sonoro massimo registrato durante il tempo di misurazione  - `LAmax2[number]`: Livello sonoro massimo registrato nelle ultime 2 ore  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateIssued[date-time]`: La data e l'ora in cui la previsione è stata emessa dal fornitore di servizi in formato ISO8601 UTC.  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `noiseAnnoyanceIndex[number]`: Indice (da 1 a 10) in base al livello di fastidio del rumore  - `noiseOrigin[string]`: Origine principale (fonte) del rumore registrato al momento dell'installazione del sensore  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo NGSI. Deve essere NoisePollutionForecast (Previsione di inquinamento acustico)  - `validFrom[date-time]`: L'inizio del periodo di validità di questa previsione in formato ISO8601.  - `validTo[date-time]`: La fine del periodo di validità di questa previsione in formato ISO8601.  - `validity[string]`: Include il periodo di validità di questa previsione come intervallo di tempo ISO8601.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoisePollutionForecast:    
  description: Noise Pollution forecast stores the expectation about noise pollution based on some input elements and the noise elements present.    
  properties:    
    LANight:    
      description: Average sound level recorded during the night (8h)    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq:    
      description: Average sound level (equivalent) recorded during the measuring time    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq2:    
      description: Average sound level over the last 2 hours    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq_d:    
      description: Average sound level during the day (8h)    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax:    
      description: Maximum sound level recorded during the measuring time    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax2:    
      description: Maximum sound level recorded for the last 2 hours    
      type: number    
      x-ngsi:    
        type: Property    
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
    dateIssued:    
      description: The date and time the forecast was issued by the service provider in ISO8601 UTC format    
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
    noiseAnnoyanceIndex:    
      description: Index (1 to 10) according to noise annoyance level    
      maximum: 10    
      minimum: 1    
      type: number    
      x-ngsi:    
        type: Property    
    noiseOrigin:    
      description: Main origin (source) of the recorded noise at installation of the sensor    
      type: string    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI type. It has to be NoisePollutionForecast    
      enum:    
        - NoisePollutionForecast    
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
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollutionForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave di NoisePollutionForecast NGSI-v2 Esempio  
Ecco un esempio di NoisePollutionForecast in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Previsione dell'inquinamento acustico NGSI-v2 normalizzata Esempio  
Ecco un esempio di NoisePollutionForecast in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Previsione dell'inquinamento acustico Valori chiave NGSI-LD Esempio  
Ecco un esempio di NoisePollutionForecast in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Previsione di inquinamento acustico NGSI-LD normalizzato Esempio  
Ecco un esempio di NoisePollutionForecast in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "type": "GeoProperty",  
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
  "@context": [  
       "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
