[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Monitoraggio della qualità dell'aria  
============================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityMonitoring/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Modello di dati per il monitoraggio della qualità dell'aria (AQM).  
versione: 0.0.1  

## Elenco delle proprietà  

- `airQualityIndex`: Indice complessivo di qualità dell'aria (AQI) per la qualità dell'aria osservata.  - `airQualityLevel`: Indicazione della categoria di qualità dell'aria. Livello qualitativo definito in base alle agenzie sanitarie locali. Ad esempio, "BUONO", "MODERATO", "POVERO", "INSALUBRE", "GRAVE", "PERICOLOSO" ecc.  - `airTemperatureTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `alternateName`: Un nome alternativo per questa voce  - `ambientNoiseTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `aqiMajorPollutant`: Inquinante principale nell'Indice di qualità dell'aria (AQI). Enum:'arsenico, bap, benzene, co2, nh3, no, no2, o2, o3, so2, pb'  - `arsenicTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `atmosphericPressure`: Pressione atmosferica (o barometrica) osservata.  - `atmosphericPressureTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `bapTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `benzeneTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `co2TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `coTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description`: Descrizione dell'articolo  - `deviceInfo`: Informazioni sul dispositivo associato alle osservazioni.  - `deviceStatus`: Indica lo stato del dispositivo o dei dispositivi fisici.  - `id`: Identificatore univoco dell'entità  - `illuminance`: Illuminamento misurato  - `name`: Il nome di questo elemento.  - `nh3TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `nickelTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `no2TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `noTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `o2TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `o3TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `observationDateTime`: Ultimo momento di osservazione segnalato.  - `owner`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pbTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `pm10TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `pm25TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `precipitation`: Livello di precipitazione/precipitazione osservato per una determinata durata.  - `relativeHumidityTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `so2TSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `solarRadiation`: Radiazione solare istantanea misurata in kW/m2  - `source`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type`: Tipo NGSI. deve essere Monitoraggio della qualità dell'aria.  - `uvTSA`: Oggetto che definisce l'elaborazione temporale di una proprietà di base durante un periodo. Fornisce il massimo, il minimo, il valore istantaneo e la media.  - `versionInfo`: Informazioni sulla versione corrispondente a questa osservazione.    
Proprietà richieste  
- `id`  - `type`  ## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AirQualityMonitoring:    
  description: 'Air Quality Monitoring (AQM) Data Model.'    
  properties:    
    airQualityIndex:    
      description: 'Overall Air Quality Index (AQI) for the observed air quality.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityLevel:    
      description: 'Air Quality Category Indication. Qualitative level defined according to the local health agencies. For example, ''GOOD'', ''MODERATE'', ''POOR'', ''UNHEALTHY'', ''SEVERE'', ''HAZARDOUS'' etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    airTemperatureTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: &airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
        instValue:    
          type: number    
        instvalue:    
          type: number    
        maxOverTime:    
          type: number    
        minOverTime:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    ambientNoiseTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    aqiMajorPollutant:    
      description: 'Major pollutant in the Air Quality Index (AQI). Enum:''arsenic, bap, benzene, co2, nh3, no, no2, o2, o3, so2, pb'''    
      enum:    
        - arsenic    
        - bap    
        - benzene    
        - co2    
        - nh3    
        - no    
        - no2    
        - o2    
        - o3    
        - so2    
        - pb    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arsenicTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    atmosphericPressure:    
      description: 'Observed air (atmospheric or barometric) pressure.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    atmosphericPressureTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    bapTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    benzeneTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    co2TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    coTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
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
    deviceInfo:    
      description: 'Information about the device associated with the observations.'    
      properties:    
        RFID:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceID:    
          description: 'Property. Model:''https://schema.org/Text''. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceList:    
          description: 'Property. Model:''https://schema.org/Text''. Information of device part number and sub devices corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            areaServed:    
              description: 'Property. Model:''https://schema.org/Text''. Area served by the entity or a service. '    
              type: string    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text''. URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text''. Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text''. Property/properties sensed/observed/measured by the device.'    
          type: string    
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
          description: 'Relationship. Unique identifier of the entity'    
      type: object    
      x-ngsi:    
        type: Property    
    deviceStatus:    
      description: 'Indicates the status of physical device or devices.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &airqualitymonitoring_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nh3TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    nickelTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    no2TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    noTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    o2TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    o3TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *airqualitymonitoring_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pbTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    pm10TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    pm25TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: 'Observed precipitation/rainfall level over a given duration.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    relativeHumidityTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
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
    so2TSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    solarRadiation:    
      description: 'Instantaneous solar radiation measured in kW/m2'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kW/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type. it has to be AirQualityMonitoring'    
      enum:    
        - AirQualityMonitoring    
      type: string    
      x-ngsi:    
        type: Property    
    uvTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties: *airqualitymonitoring_-_properties_-_ambientnoisetsa_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    versionInfo:    
      description: 'Version information corresponding to this observation.'    
      properties:    
        comments:    
          description: 'Property. Model:''https://schema.org/Text''. User comments corresponding to this observation.'    
          type: string    
        endDateTime:    
          description: 'Property. Model:''https://schema.org/DateTime''. Reported end time corresponding to this observation.'    
          format: date-time    
          type: string    
        startDateTime:    
          description: 'Property. Model:''https://schema.org/DateTime''. Reported start time corresponding to this observation.'    
          format: date-time    
          type: string    
        versionName:    
          description: 'Property. Model:''https://schema.org/Text''. Version name corresponding to this observation'    
          type: string    
        windType:    
          description: 'Property. Wind type dominate during the last 24 hours.'    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityMonitoring/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityMonitoring/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempi di payload  
#### Valori-chiave di AirQualityMonitoring NGSI-v2 Esempio  
Ecco un esempio di AirQualityMonitoring in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
  "type": "AirQualityMonitoring",  
  "address": {  
    "addressCountry": "India",  
    "addressLocality": "Bangalore",  
    "addressRegion": "Karnataka",  
    "postOfficeBoxNumber": "",  
    "postalCode": "110001",  
    "streetAddress": "Avenue Road"  
  },  
  "airQualityIndex": 90,  
  "airQualityLevel": "SATISFACTORY",  
  "airTemperatureTSA": {  
    "avgOverTime": 23.1,  
    "instValue": 30.8,  
    "maxOverTime": 32.8,  
    "minOverTime": 12.7  
  },  
  "alternateName": "EnvAQM sampling",  
  "ambientNoiseTSA": {  
    "avgOverTime": 57.9,  
    "instValue": 57.6,  
    "maxOverTime": 59.2,  
    "minOverTime": 50.5  
  },  
  "aqiMajorPollutant": "No2",  
  "areaServed": "Bangalore",  
  "arsenicTSA": {  
    "avgOverTime": 0.4,  
    "instValue": 0.35,  
    "maxOverTime": 0.44,  
    "minOverTime": 0.29  
  },  
  "atmosphericPressure": 633.2,  
  "atmosphericPressureTSA": {  
    "avgOverTime": 968.3,  
    "instValue": 982.9,  
    "maxOverTime": 982.7,  
    "minOverTime": 961.9  
  },  
  "bapTSA": {  
    "avgOverTime": 492.1,  
    "instValue": 439.1,  
    "maxOverTime": 573.7,  
    "minOverTime": 398.7  
  },  
  "benzeneTSA": {  
    "avgOverTime": 266.7,  
    "instValue": 321.7,  
    "maxOverTime": 576.9,  
    "minOverTime": 210.1  
  },  
  "co2TSA": {  
    "avgOverTime": 318.51,  
    "instValue": 320.4,  
    "maxOverTime": 390.2,  
    "minOverTime": 302.6  
  },  
  "coTSA": {  
    "avgOverTime": 3.51,  
    "instValue": 4.0,  
    "maxOverTime": 8.9,  
    "minOverTime": 3.4  
  },  
  "dataProvider": "",  
  "dateCreated": {  
    "@type": "DateTime",  
    "@value": "2017-12-31T03:39:27Z"  
  },  
  "dateModified": {  
    "@type": "DateTime",  
    "@value": "2021-12-22T04:21:57Z"  
  },  
  "description": "Air quality monitoring",  
  "deviceInfo": {  
    "RFID": "AB463478",  
    "deviceBatteryStatus": "Connected",  
    "deviceID": "12345",  
    "deviceList": "12",  
    "deviceModel": {  
      "areaServed": "Agartala",  
      "brandName": "Climo",  
      "manufacturerName": "Bosch",  
      "modelName": "sensor",  
      "modelURL": "www.boschclimo.com"  
    },  
    "deviceName": "Climo",  
    "deviceSimNumber": "12345678",  
    "measurand": "",  
    "refDevice": "urn:ngsi-ld:device:12"  
  },  
  "deviceStatus": "ACTIVE",  
  "illuminance": 3319.41,  
  "location": {  
    "coordinates": [  
      12.979,  
      77.591  
    ],  
    "type": "Point"  
  },  
  "name": "",  
  "nh3TSA": {  
    "avgOverTime": 865.1,  
    "instValue": 900.2,  
    "maxOverTime": 990.8,  
    "minOverTime": 834.7  
  },  
  "nickelTSA": {  
    "avgOverTime": 434.0,  
    "instValue": 527.2,  
    "maxOverTime": 559.6,  
    "minOverTime": 132.2  
  },  
  "no2TSA": {  
    "avgOverTime": 409.7,  
    "instValue": 511.0,  
    "maxOverTime": 611.5,  
    "minOverTime": 242.4  
  },  
  "noTSA": {  
    "avgOverTime": 3.65,  
    "instValue": 3.6,  
    "maxOverTime": 4.8,  
    "minOverTime": 2.7  
  },  
  "o2TSA": {  
    "avgOverTime": 18.1,  
    "instValue": 18.0,  
    "maxOverTime": 18.2,  
    "minOverTime": 18.0  
  },  
  "o3TSA": {  
    "avgOverTime": 218.8,  
    "instValue": 173.1,  
    "maxOverTime": 236.4,  
    "minOverTime": 167.7  
  },  
  "observationDateTime": {  
    "@type": "DateTime",  
    "@value": "2020-09-16T11:00:00+05:30"  
  },  
  "owner": [  
    "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
    "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
  ],  
  "pbTSA": {  
    "avgOverTime": 473.0,  
    "instValue": 391.0,  
    "maxOverTime": 542.1,  
    "minOverTime": 287.5  
  },  
  "pm10TSA": {  
    "avgOverTime": 847.3,  
    "instValue": 439.1,  
    "maxOverTime": 568.1,  
    "minOverTime": 54.3  
  },  
  "pm25TSA": {  
    "avgOverTime": 28.3,  
    "instValue": 56.6,  
    "maxOverTime": 56.8,  
    "minOverTime": 10.1  
  },  
  "precipitation": 846.0,  
  "relativeHumidityTSA": {  
    "avgOverTime": 326.3,  
    "instValue": 401.2,  
    "maxOverTime": 599.3,  
    "minOverTime": 211.6  
  },  
  "seeAlso": [  
    "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
    "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
  ],  
  "so2TSA": {  
    "avgOverTime": 3.65,  
    "instValue": 3.5,  
    "maxOverTime": 3.72,  
    "minOverTime": 2.9  
  },  
  "solarRadiation": 3.65,  
  "source": "Bangalore Smart city",  
  "uvTSA": {  
    "avgOverTime": 6.0,  
    "instValue": 8.2,  
    "maxOverTime": 8.3,  
    "minOverTime": 5.7  
  },  
  "versionInfo": {  
    "comments": "Version 1",  
    "endDateTime": {  
      "@type": "DateTime",  
      "@value": "2020-09-16T11:00:00+05:30"  
    },  
    "startDateTime": {  
      "@type": "DateTime",  
      "@value": "2020-09-16T11:00:00+05:30"  
    },  
    "versionName": "Version 1"  
  }  
}  
```  
#### Monitoraggio della qualità dell'aria NGSI-v2 normalizzato Esempio  
Ecco un esempio di AirQualityMonitoring in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:AirQualityMonitoring:id:MUTW:63473748",  
  "type": "AirQualityMonitoring",  
  "dateCreated": {  
    "type": "Datetime",  
    "value": "2017-12-31T03:39:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-12-22T04:21:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Bangalore Smart city"  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "EnvAQM sampling"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Air quality monitoring"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:AirQualityMonitoring:items:PDSP:96970072",  
      "urn:ngsi-ld:AirQualityMonitoring:items:FTKL:60685543"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:AirQualityMonitoring:items:SUXG:34385451",  
      "urn:ngsi-ld:AirQualityMonitoring:items:AEAM:62422977"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        12.979,  
        77.591  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Avenue Road",  
      "addressLocality": "Bangalore",  
      "addressRegion": "Karnataka",  
      "addressCountry": "India",  
      "postalCode": "110001",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Bangalore"  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "deviceList": "12",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "Climo",  
      "deviceID": "12345",  
      "RFID": "AB463478",  
      "measurand": "",  
      "deviceSimNumber": "12345678",  
      "deviceModel": {  
        "brandName": "Climo",  
        "manufacturerName": "Bosch",  
        "modelName": "sensor",  
        "modelURL": "www.boschclimo.com",  
        "areaServed": "Agartala"  
      },  
      "refDevice": "urn:ngsi-ld:device:12"  
    }  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2020-09-16T11:00:00+05:30"  
  },  
  "deviceStatus": {  
    "type": "Text",  
    "value": "ACTIVE"  
  },  
  "atmosphericPressure": {  
    "type": "Number",  
    "value": 633.2  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 90  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "SATISFACTORY"  
  },  
  "aqiMajorPollutant": {  
    "type": "Text",  
    "value": "no2"  
  },  
  "airTemperatureTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 93.7,  
      "minOverTime": 710.0,  
      "maxOverTime": 741.9,  
      "instValue": 889.5  
    }  
  },  
  "ambientNoiseTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 729.1,  
      "minOverTime": 482.0,  
      "maxOverTime": 743.7,  
      "instValue": 813.9  
    }  
  },  
  "arsenicTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 0.4,  
      "minOverTime": 0.29,  
      "maxOverTime": 0.44,  
      "instValue": 0.35  
    }  
  },  
  "atmosphericPressureTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 0.92,  
      "minOverTime": 0.91,  
      "maxOverTime": 0.93,  
      "instValue": 0.92  
    }  
  },  
  "bapTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 109.2,  
      "minOverTime": 277.8,  
      "maxOverTime": 836.0,  
      "instValue": 9.7  
    }  
  },  
  "benzeneTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 312.6,  
      "minOverTime": 405.9,  
      "maxOverTime": 786.1,  
      "instValue": 323.0  
    }  
  },  
  "coTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.51,  
      "minOverTime": 3.4,  
      "maxOverTime": 8.9,  
      "instValue": 4.0  
    }  
  },  
  "co2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 318.51,  
      "minOverTime": 302.6,  
      "maxOverTime": 390.2,  
      "instValue": 320.4  
    }  
  },  
  "nh3TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 135.1,  
      "minOverTime": 834.7,  
      "maxOverTime": 790.8,  
      "instValue": 900.2  
    }  
  },  
  "nickelTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 434.0,  
      "minOverTime": 132.2,  
      "maxOverTime": 559.6,  
      "instValue": 527.2  
    }  
  },  
  "noTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.65,  
      "minOverTime": 2.7,  
      "maxOverTime": 4.8,  
      "instValue": 3.6  
    }  
  },  
  "no2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 409.7,  
      "minOverTime": 642.4,  
      "maxOverTime": 211.5,  
      "instValue": 511.0  
    }  
  },  
  "o2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 18.1,  
      "minOverTime": 18.0,  
      "maxOverTime": 18.2,  
      "instValue": 18.0  
    }  
  },  
  "o3TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 118.8,  
      "minOverTime": 667.7,  
      "maxOverTime": 36.4,  
      "instValue": 473.1  
    }  
  },  
  "pm10TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 847.3,  
      "minOverTime": 54.3,  
      "maxOverTime": 868.1,  
      "instValue": 439.1  
    }  
  },  
  "pm25TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 28.3,  
      "minOverTime": 10.1,  
      "maxOverTime": 56.8,  
      "instValue": 56.6  
    }  
  },  
  "relativeHumidityTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 326.3,  
      "minOverTime": 711.6,  
      "maxOverTime": 199.3,  
      "instValue": 401.2  
    }  
  },  
  "so2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.65,  
      "minOverTime": 2.9,  
      "maxOverTime": 3.72,  
      "instValue": 3.8  
    }  
  },  
  "pbTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 473.0,  
      "minOverTime": 287.5,  
      "maxOverTime": 42.1,  
      "instValue": 91.0  
    }  
  },  
  "uvTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 6.0,  
      "minOverTime": 5.7,  
      "maxOverTime": 8.3,  
      "instValue": 8.2  
    }  
  },  
  "illuminance": {  
    "type": "Number",  
    "value": 3319.41  
  },  
  "solarRadiation": {  
    "type": "Number",  
    "value": 3.65  
  },  
  "precipitation": {  
    "type": "StructuredValue",  
    "value": 846.0  
  },  
  "versionInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "startDateTime": "2020-09-16T11:00:00+05:30",  
      "endDateTime": "2020-09-16T11:00:00+05:30",  
      "versionName": "Version 1",  
      "comments": "Version 1"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Monitoraggio della qualità dell'aria Valori chiave NGSI-LD Esempio  
Ecco un esempio di AirQualityMonitoring in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
    "type": "AirQualityMonitoring",  
    "address": {  
        "addressCountry": "India",  
        "addressLocality": "Bangalore",  
        "addressRegion": "Karnataka",  
        "postOfficeBoxNumber": "",  
        "postalCode": "110001",  
        "streetAddress": "Avenue Road"  
    },  
    "airQualityIndex": 90,  
    "airQualityLevel": "SATISFACTORY",  
    "airTemperatureTSA": {  
        "avgOverTime": 23.1,  
        "instValue": 30.8,  
        "maxOverTime": 32.8,  
        "minOverTime": 12.7  
    },  
    "alternateName": "EnvAQM sampling",  
    "ambientNoiseTSA": {  
        "avgOverTime": 57.9,  
        "instValue": 57.6,  
        "maxOverTime": 59.2,  
        "minOverTime": 50.5  
    },  
    "aqiMajorPollutant": "No2",  
    "areaServed": "Bangalore",  
    "arsenicTSA": {  
        "avgOverTime": 0.4,  
        "instValue": 0.35,  
        "maxOverTime": 0.44,  
        "minOverTime": 0.29  
    },  
    "atmosphericPressure": 633.2,  
    "atmosphericPressureTSA": {  
        "avgOverTime": 968.3,  
        "instValue": 982.9,  
        "maxOverTime": 982.7,  
        "minOverTime": 961.9  
    },  
    "bapTSA": {  
        "avgOverTime": 492.1,  
        "instValue": 439.1,  
        "maxOverTime": 573.7,  
        "minOverTime": 398.7  
    },  
    "benzeneTSA": {  
        "avgOverTime": 266.7,  
        "instValue": 321.7,  
        "maxOverTime": 576.9,  
        "minOverTime": 210.1  
    },  
    "co2TSA": {  
        "avgOverTime": 318.51,  
        "instValue": 320.4,  
        "maxOverTime": 390.2,  
        "minOverTime": 302.6  
    },  
    "coTSA": {  
        "avgOverTime": 3.51,  
        "instValue": 4.0,  
        "maxOverTime": 8.9,  
        "minOverTime": 3.4  
    },  
    "dataProvider": "",  
    "dateCreated": {  
        "@type": "DateTime",  
        "@value": "2017-12-31T03:39:27Z"  
    },  
    "dateModified": {  
        "@type": "DateTime",  
        "@value": "2021-12-22T04:21:57Z"  
    },  
    "description": "Air quality monitoring",  
    "deviceInfo": {  
        "RFID": "AB463478",  
        "deviceBatteryStatus": "Connected",  
        "deviceID": "12345",  
        "deviceList": "12",  
        "deviceModel": {  
            "areaServed": "Agartala",  
            "brandName": "Climo",  
            "manufacturerName": "Bosch",  
            "modelName": "sensor",  
            "modelURL": "www.boschclimo.com"  
        },  
        "deviceName": "Climo",  
        "deviceSimNumber": "12345678",  
        "measurand": "",  
        "refDevice": "urn:ngsi-ld:device:12"  
    },  
    "deviceStatus": "ACTIVE",  
    "illuminance": 3319.41,  
    "location": {  
        "coordinates": [  
            12.979,  
            77.591  
        ],  
        "type": "Point"  
    },  
    "name": "",  
    "nh3TSA": {  
        "avgOverTime": 865.1,  
        "instValue": 900.2,  
        "maxOverTime": 990.8,  
        "minOverTime": 834.7  
    },  
    "nickelTSA": {  
        "avgOverTime": 434.0,  
        "instValue": 527.2,  
        "maxOverTime": 559.6,  
        "minOverTime": 132.2  
    },  
    "no2TSA": {  
        "avgOverTime": 409.7,  
        "instValue": 511.0,  
        "maxOverTime": 611.5,  
        "minOverTime": 242.4  
    },  
    "noTSA": {  
        "avgOverTime": 3.65,  
        "instValue": 3.6,  
        "maxOverTime": 4.8,  
        "minOverTime": 2.7  
    },  
    "o2TSA": {  
        "avgOverTime": 18.1,  
        "instValue": 18.0,  
        "maxOverTime": 18.2,  
        "minOverTime": 18.0  
    },  
    "o3TSA": {  
        "avgOverTime": 218.8,  
        "instValue": 173.1,  
        "maxOverTime": 236.4,  
        "minOverTime": 167.7  
    },  
    "observationDateTime": {  
        "@type": "DateTime",  
        "@value": "2020-09-16T11:00:00+05:30"  
    },  
    "owner": [  
        "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
        "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
    ],  
    "pbTSA": {  
        "avgOverTime": 473.0,  
        "instValue": 391.0,  
        "maxOverTime": 542.1,  
        "minOverTime": 287.5  
    },  
    "pm10TSA": {  
        "avgOverTime": 847.3,  
        "instValue": 439.1,  
        "maxOverTime": 568.1,  
        "minOverTime": 54.3  
    },  
    "pm25TSA": {  
        "avgOverTime": 28.3,  
        "instValue": 56.6,  
        "maxOverTime": 56.8,  
        "minOverTime": 10.1  
    },  
    "precipitation": 846.0,  
    "relativeHumidityTSA": {  
        "avgOverTime": 326.3,  
        "instValue": 401.2,  
        "maxOverTime": 599.3,  
        "minOverTime": 211.6  
    },  
    "seeAlso": [  
        "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
        "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
    ],  
    "so2TSA": {  
        "avgOverTime": 3.65,  
        "instValue": 3.5,  
        "maxOverTime": 3.72,  
        "minOverTime": 2.9  
    },  
    "solarRadiation": 3.65,  
    "source": "Bangalore Smart city",  
    "uvTSA": {  
        "avgOverTime": 6.0,  
        "instValue": 8.2,  
        "maxOverTime": 8.3,  
        "minOverTime": 5.7  
    },  
    "versionInfo": {  
        "comments": "Version 1",  
        "endDateTime": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        },  
        "startDateTime": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        },  
        "versionName": "Version 1"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
#### Monitoraggio della qualità dell'aria NGSI-LD normalizzato Esempio  
Ecco un esempio di AirQualityMonitoring in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
    "type": "AirQualityMonitoring",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Avenue Road",  
            "addressLocality": "Bangalore",  
            "addressRegion": "Karnataka",  
            "addressCountry": "India",  
            "postalCode": "110001",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "airQualityIndex": {  
        "type": "Property",  
        "value": 90  
    },  
    "airQualityLevel": {  
        "type": "Property",  
        "value": "SATISFACTORY"  
    },  
    "airTemperatureTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 23.1,  
            "minOverTime": 12.7,  
            "maxOverTime": 32.8,  
            "instValue": 30.8  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "EnvAQM sampling"  
    },  
    "ambientNoiseTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 57.9,  
            "minOverTime": 50.5,  
            "maxOverTime": 59.2,  
            "instValue": 57.6  
        }  
    },  
    "aqiMajorPollutant": {  
        "type": "Property",  
        "value": "no2"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Bangalore"  
    },  
    "arsenicTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 0.4,  
            "minOverTime": 0.29,  
            "maxOverTime": 0.44,  
            "instValue": 0.35  
        }  
    },  
    "atmosphericPressure": {  
        "type": "Property",  
        "value": 633.2  
    },  
    "atmosphericPressureTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 968.3,  
            "minOverTime": 961.9,  
            "maxOverTime": 982.7,  
            "instValue": 982.9  
        }  
    },  
    "bapTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 492.1,  
            "minOverTime": 398.7,  
            "maxOverTime": 573.7,  
            "instValue": 439.1  
        }  
    },  
    "benzeneTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 266.7,  
            "minOverTime": 210.1,  
            "maxOverTime": 576.9,  
            "instValue": 321.7  
        }  
    },  
    "co2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 318.51,  
            "minOverTime": 302.6,  
            "maxOverTime": 390.2,  
            "instValue": 320.4  
        }  
    },  
    "coTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.51,  
            "minOverTime": 3.4,  
            "maxOverTime": 8.9,  
            "instValue": 4.0  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-12-31T03:39:27Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-12-22T04:21:57Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Air quality monitoring"  
    },  
    "deviceInfo": {  
        "type": "Property",  
        "value": {  
            "deviceList": "12",  
            "deviceBatteryStatus": "Connected",  
            "deviceName": "Climo",  
            "deviceID": "12345",  
            "RFID": "AB463478",  
            "measurand": "",  
            "deviceSimNumber": "12345678",  
            "deviceModel": {  
                "brandName": "Climo",  
                "manufacturerName": "Bosch",  
                "modelName": "sensor",  
                "modelURL": "www.boschclimo.com",  
                "areaServed": "Agartala"  
            },  
            "refDevice": "urn:ngsi-ld:device:12"  
        }  
    },  
    "deviceStatus": {  
        "type": "Property",  
        "value": "ACTIVE"  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 3319.41  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                12.979,  
                77.591  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": ""  
    },  
    "nh3TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 865.1,  
            "minOverTime": 834.7,  
            "maxOverTime": 990.8,  
            "instValue": 900.2  
        }  
    },  
    "nickelTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 434.0,  
            "minOverTime": 132.2,  
            "maxOverTime": 559.6,  
            "instValue": 527.2  
        }  
    },  
    "no2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 409.7,  
            "minOverTime": 242.4,  
            "maxOverTime": 611.5,  
            "instValue": 511.0  
        }  
    },  
    "noTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.65,  
            "minOverTime": 2.7,  
            "maxOverTime": 4.8,  
            "instValue": 3.6  
        }  
    },  
    "o2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 18.1,  
            "minOverTime": 18.0,  
            "maxOverTime": 18.2,  
            "instValue": 18.0  
        }  
    },  
    "o3TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 218.8,  
            "minOverTime": 167.7,  
            "maxOverTime": 236.4,  
            "instValue": 173.1  
        }  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        }  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
            "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
        ]  
    },  
    "pbTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 473.0,  
            "minOverTime": 287.5,  
            "maxOverTime": 542.1,  
            "instValue": 391.0  
        }  
    },  
    "pm10TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 847.3,  
            "minOverTime": 54.3,  
            "maxOverTime": 568.1,  
            "instValue": 439.1  
        }  
    },  
    "pm25TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 28.3,  
            "minOverTime": 10.1,  
            "maxOverTime": 56.8,  
            "instValue": 56.6  
        }  
    },  
    "precipitation": {  
        "type": "Property",  
        "value": 846.0  
    },  
    "relativeHumidityTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 326.3,  
            "minOverTime": 211.6,  
            "maxOverTime": 599.3,  
            "instValue": 401.2  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
            "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
        ]  
    },  
    "so2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.65,  
            "minOverTime": 2.9,  
            "maxOverTime": 3.72,  
            "instValue": 3.5  
        }  
    },  
    "solarRadiation": {  
        "type": "Property",  
        "value": 3.65  
    },  
    "source": {  
        "type": "Property",  
        "value": "Bangalore Smart city"  
    },  
    "uvTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 6.0,  
            "minOverTime": 5.7,  
            "maxOverTime": 8.3,  
            "instValue": 8.2  
        }  
    },  
    "versionInfo": {  
        "type": "Property",  
        "value": {  
            "startDateTime": {  
                "@type": "DateTime",  
                "@value": "2020-09-16T11:00:00+05:30"  
            },  
            "endDateTime": {  
                "@type": "DateTime",  
                "@value": "2020-09-16T11:00:00+05:30"  
            },  
            "versionName": "Version 1",  
            "comments": "Version 1"  
        }  
    },  
    "@context": []  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
