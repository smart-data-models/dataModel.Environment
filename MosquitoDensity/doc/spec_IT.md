<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: MosquitoDensity  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Un modello di dati per la densità delle zanzare nelle città.**  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `airTemperature[object]`: Valore osservato della temperatura dell'aria. Valore è un oggetto contenente attributi che rappresentano aggregati statistici derivati da dati passati.  - `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataDescriptor[uri]`: URI che punta all'entità descrittore di dati  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `deviceInfo[object]`: Informazioni sul dispositivo associato alle osservazioni  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: Indica lo stato di carica della batteria del dispositivo segnalato (collegato, scollegato).  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceId[string]`: ID dispositivo del sensore fisico/stazione di misura corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: Descrive le informazioni del dispositivo, del sensore o del sistema in esame.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: Nome del dispositivo o della stazione del dispositivo/stazione del sensore corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: Indica il numero di sim del dispositivo nel veicolo per la gestione dei rifiuti.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: Proprietà/percezioni rilevate/osservate/misurate dal dispositivo  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: Fornisce l'ID del lettore RFID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `femaleTotal[number]`: Il conteggio totale delle femmine di una particolare specie, come identificate dal dispositivo.  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maleTotal[number]`: Il conteggio totale dei maschi di una particolare specie, come identificati dal dispositivo.  - `mosquitoDensity[object]`: La nomenclatura binomiale (o) zoologica della specie di zanzara e la sua conta, come identificata dal dispositivo corrispondente a questa osservazione.  	- `femaleSpeciesCount[number]`: Il conteggio totale delle zanzare femmine della specie identificata dal dispositivo    
	- `maleSpeciesCount[number]`: Il conteggio totale dei maschi di zanzara della specie identificata dal dispositivo    
	- `mosquitoSpecies[string]`: Nomenclatura binomiale/zoologica delle specie di zanzare identificate dal dispositivo.    
	- `totalSpeciesCount[number]`: Il conteggio totale di una particolare specie rilevata dal dispositivo    
- `name[string]`: Il nome di questo elemento  - `observationDateTime[date-time]`: Ultima ora di osservazione segnalata  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `precipitation[number]`: Livello di precipitazione/precipitazione osservato per un determinato periodo di tempo  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `speciesName[string]`: La nomenclatura binomiale/zoologica delle specie identificate dal dispositivo.  - `speciesTotal[number]`: Il conteggio totale di una particolare specie, come rilevato dal dispositivo.  - `type[string]`: Tipo di entità NGSI. Deve essere MosquitoDensity  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MosquitoDensity:    
  description: A Data Model for density of mosquitoes in cities.    
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
    airTemperature:    
      averageValue:    
        description: Property. Average value of temporal processing over time    
        type: number    
      description: Observed value of air temperature. Value is an object containing attributes representing statistical aggregates derived from past data    
      instValue:    
        description: Property. Instant value of temporal processing    
        type: number    
      maxOverTime:    
        description: Property. Maximum value of temporal processing over time    
        type: number    
      minOverTime:    
        description: Property. Minimum value of temporal processing over time    
        type: number    
      type: object    
      x-ngsi:    
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
    dataDescriptor:    
      description: URI pointing to the data-descriptor entity    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    deviceId:    
      description: Device ID of the physical sensor/ measurement station corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceInfo:    
      description: Information about the device associated with the observations    
      properties:    
        deviceBatteryStatus:    
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceModel:    
          description: 'Describes the information of the device, sensor or system in consideration'    
          properties:    
            brandName:    
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            manufacturerName:    
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelName:    
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelURL:    
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
          type: object    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceName:    
          description: Device Name or Station name of the sensor device/station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        measurand:    
          description: Property/properties sensed/observed/measured by the device    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        rfID:    
          description: Gives the ID of the RFID reader    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: Gives the sim number of the device in the waste management vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    femaleTotal:    
      description: 'The total count of females of a particular species, as identified by the device.'    
      type: number    
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
    maleTotal:    
      description: 'The total count of males of a particular species, as identified by the device.'    
      type: number    
      x-ngsi:    
        type: Property    
    mosquitoDensity:    
      description: The binomial (or) zoological nomenclature of the mosquito species and its count as identified by the device corresponding to this observation    
      properties:    
        femaleSpeciesCount:    
          description: The total count of the female mosquitoes of the species identified by the device    
          type: number    
          x-ngsi:    
            type: Property    
        maleSpeciesCount:    
          description: The total count of the male mosquitoes of the species identified by the device    
          type: number    
          x-ngsi:    
            type: Property    
        mosquitoSpecies:    
          description: The binomial/ zoological nomenclature of the mosquito species as identified by the device    
          type: string    
          x-ngsi:    
            type: Property    
        totalSpeciesCount:    
          description: The total count of a particular species detected by the device    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
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
    precipitation:    
      description: Observed precipitation/rainfall level over a given duration    
      type: number    
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
    speciesName:    
      description: The binomial/ zoological nomenclature of the species identified by the device.    
      type: string    
      x-ngsi:    
        type: Property    
    speciesTotal:    
      description: 'The total count of a particular species, as detected by the device.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be MosquitoDensity    
      enum:    
        - MosquitoDensity    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/MosquitoDensity/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### MosquitoDensity NGSI-v2 valori-chiave Esempio  
Ecco un esempio di MosquitoDensity in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": "VDFWitw@B",  
  "deviceSimNumber": "861123052561188",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      76.9578654,  
      8.487284  
    ]  
  },  
  "speciesName": "Culex quinquefasciatus",  
  "speciesTotal": 3,  
  "femaleTotal": 2,  
  "maleTotal": 1,  
  "observationDateTime": "2022-09-18T23:59:59+05:30",  
  "airTemperature": {  
    "instValue": 24.88  
  },  
  "precipitation": 0,  
  "deviceInfo": {  
    "rfID": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "measurand": "6",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  }  
}  
```  
</details>  
#### MosquitoDensity NGSI-v2 normalizzato Esempio  
Ecco un esempio di MosquitoDensity in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": {  
    "type": "Text",  
    "value": "VDFWitw@B"  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "861123052561188"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        76.9578654,  
        8.487284  
      ]  
    }  
  },  
  "speciesName": {  
    "type": "Text",  
    "value": "Culex quinquefasciatus"  
  },  
  "speciesTotal": {  
    "type": "Number",  
    "value": 3  
  },  
  "femaleTotal": {  
    "type": "Number",  
    "value": 2  
  },  
  "maleTotal": {  
    "type": "Number",  
    "value": 1  
  },  
  "observationDateTime": {  
    "type": "Date-Time",  
    "value": "2022-09-18T23:59:59+05:30"  
  },  
  "airTemperature": {  
    "type": "StructuredValue",  
    "value": {  
      "instValue": 24.88  
    }  
  },  
  "precipitation": {  
    "type": "Number",  
    "value": 0  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "measurand": "6",  
      "deviceModel": {  
        "brandName": "abc",  
        "manufacturerName": "xyz",  
        "modelName": "SL1",  
        "modelURL": "www.abcstreetlight.com"  
      }  
    }  
  }  
}  
```  
</details>  
#### MosquitoDensity Valori chiave NGSI-LD Esempio  
Ecco un esempio di MosquitoDensity in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": "VDFWitw@B",  
  "deviceSimNumber": "861123052561188",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      76.9578654,  
      8.487284  
    ]  
  },  
  "speciesName": "Culex quinquefasciatus",  
  "speciesTotal": 3,  
  "femaleTotal": 2,  
  "maleTotal": 1,  
  "observationDateTime": "2022-09-18T23:59:59+05:30",  
  "airTemperature": {  
    "instValue": 24.88  
  },  
  "precipitation": 0,  
  "deviceInfo": {  
    "rfID": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "measurand": "6",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MosquitoDensity NGSI-LD normalizzato Esempio  
Ecco un esempio di MosquitoDensity in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": {  
    "type": "Property",  
    "value": "VDFWitw@B"  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "861123052561188"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        76.9578654,  
        8.487284  
      ]  
    }  
  },  
  "speciesName": {  
    "type": "Property",  
    "value": "Culex quinquefasciatus"  
  },  
  "speciesTotal": {  
    "type": "Property",  
    "value": 3  
  },  
  "femaleTotal": {  
    "type": "Property",  
    "value": 2  
  },  
  "maleTotal": {  
    "type": "Property",  
    "value": 1  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2022-09-18T23:59:59+05:30"  
    }  
  },  
  "airTemperature": {  
    "type": "Property",  
    "value": {  
      "instValue": 24.88  
    }  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 0  
  },  
  "deviceInfo": {  
    "type": "Property",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "measurand": "6",  
      "deviceModel": {  
        "brandName": "abc",  
        "manufacturerName": "xyz",  
        "modelName": "SL1",  
        "modelURL": "www.abcstreetlight.com"  
      }  
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
