<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AirQualityObserved  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Un'osservazione delle condizioni di qualità dell'aria in un determinato luogo e momento.**  
versione: 0.1.2  
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
- `airQualityIndex[number]`: L'indice di qualità dell'aria è un numero utilizzato per indicare la qualità dell'aria in un determinato giorno.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: Livello qualitativo complessivo di preoccupazione per la salute corrispondente alla qualità dell'aria osservata  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: Area di livello superiore a cui appartiene questa misurazione della qualità dell'aria  . Model: [https://schema.org/Text ](https://schema.org/Text )- `as[number]`: Arsenico rilevato  . Model: [https://schema.org/Number](https://schema.org/Number)- `c6h6[number]`: Benzene rilevato  - `cd[number]`: Cadmio rilevato  - `co[number]`: Rilevato monossido di carbonio  - `co2[number]`: Anidride carbonica rilevata  - `coLevel[string]`: Presenza qualitativa di monossido di carbonio  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateObserved[date-time]`: La data e l'ora di questa osservazione in formato ISO8601 UTC  . Model: [https://schema.org/Text ](https://schema.org/Text )- `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `ni[number]`: Rilevato il nichel  - `no[number]`: Rilevato monossido di azoto  - `no2[number]`: Rilevato biossido di azoto  - `nox[number]`: Altri ossidi di azoto rilevati  - `o3[number]`: Ozono rilevato  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pb[number]`: Piombo rilevato  - `pm1[number]`: Particolato di diametro pari o inferiore a 1 micrometro  - `pm10[number]`: Particolato di diametro pari o inferiore a 10 micrometri  - `pm25[number]`: Particolato di diametro pari o inferiore a 2,5 micrometri  - `precipitation[number]`: Quantità di acqua piovana  . Model: [https://schema.org/Number](https://schema.org/Number)- `refDevice[*]`: Un riferimento al dispositivo (o ai dispositivi) che ha catturato l'osservazione.  - `refPointOfInterest[*]`: Un riferimento a un punto di interesse (di solito una stazione di qualità dell'aria) associato a questa osservazione.  - `refWeatherObserved[*]`:  Tempo atmosferico osservato associato alle condizioni di qualità dell'aria descritte da questa entità  - `relativeHumidity[number]`: Umidità relativa dell'aria (un numero compreso tra 0 e 1 che rappresenta l'intervallo tra 0% e 100%)  - `reliability[number]`: Affidabilità (percentuale, espressa in parti per uno) corrispondente alla qualità dell'aria osservata  . Model: [https://schema.org/Number ](https://schema.org/Number )- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sh2[number]`: Rilevato idrogeno solforato  - `so2[number]`: Rilevato biossido di zolfo  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `temperature[number]`: Temperatura dell'articolo  - `type[string]`: Tipo di entità NGSI. Deve essere AirQualityObserved  - `typeofLocation[string]`: Tipo di ubicazione dell'articolo campionato  . Model: [https://schema.org/Text](https://schema.org/Text)- `volatileOrganicCompoundsTotal[number]`: Alcani <C10, chetoni <C6, aldeidi <C10, acidi carbossilici <C5, aspirati<C7, alcheni <C8, aromatici  - `windDirection[number]`: Direzione della banderuola  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: Intensità del vento  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Non tutti gli inquinanti sono inclusi in questo modello di dati. In caso di nuovi inquinanti per estendere il modello, si prega di fare riferimento a questa fonte http://dd.eionet.europa.eu/vocabulary/aq/pollutant/view?page=1#vocabularyConceptResults dove sono elencati la maggior parte degli inquinanti.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AirQualityObserved:    
  description: An observation of air quality conditions at a certain place and time.    
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
      description: Higher level area to which this air quality measurement belongs to    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    as:    
      description: Arsenic detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    c6h6:    
      description: Benzene detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    cd:    
      description: Cadmium detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co:    
      description: Carbon Monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co2:    
      description: Carbon Dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    coLevel:    
      description: Qualitative Carbon Monoxide presence    
      type: string    
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
    dateObserved:    
      description: The date and time of this observation in ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
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
    ni:    
      description: 'Nickel detected '    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no:    
      description: Nitrogen monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no2:    
      description: Nitrogen dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    nox:    
      description: Other Nitrogen oxides detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    o3:    
      description: 'Ozone detected '    
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
    pb:    
      description: 'Lead detected   '    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm1:    
      description: Particulate matter 1 micrometers or less in diameter    
      type: number    
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
    refDevice:    
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
      description: A reference to the device(s) which captured this observation    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
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
      description: A reference to a point of interest (usually an air quality station) associated to this observation    
      x-ngsi:    
        type: Relationship    
    refWeatherObserved:    
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
      description: ' Weather observed associated to the air quality conditions described by this entity'    
      x-ngsi:    
        type: Relationship    
    relativeHumidity:    
      description: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    reliability:    
      description: 'Reliability (percentage, expressed in parts per one) corresponding to the air quality observed'    
      maximum: 1.0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: 'https://schema.org/Number '    
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
    sh2:    
      description: Hydrogen sulfide detected    
      minimum: 0    
      type: number    
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
      description: NGSI Entity type. It has to be AirQualityObserved    
      enum:    
        - AirQualityObserved    
      type: string    
      x-ngsi:    
        type: Property    
    typeofLocation:    
      description: Type of location of the sampled item    
      enum:    
        - indoor    
        - outdoor    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    volatileOrganicCompoundsTotal:    
      description: 'Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    windDirection:    
      description: Direction of the weather vane    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
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
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.1.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave di AirQualityObserved NGSI-v2 Esempio  
Ecco un esempio di AirQualityObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Madrid",  
    "streetAddress": "Plaza de Espa\u00f1a"  
  },  
  "dateObserved": "2016-03-15T11:00:00",  
  "areaServed": "Brooklands",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.712247222222222,  
      40.423852777777775  
    ]  
  },  
  "source": "http://datos.madrid.es",  
  "typeOfLocation": "outdoor",  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "temperature": 12.2,  
  "windDirection": 176,  
  "windSpeed": 0.64,  
  "airQualityLevel": "moderate",  
  "airQualityIndex": 65,  
  "reliability": 0.7,  
  "co": 500,  
  "no": 45,  
  "co2": 69,  
  "nox": 139,  
  "so2": 11,  
  "coLevel": "moderate",  
  "refPointOfInterest": "28079004-Pza.deEspanya"  
}  
```  
</details>  
#### Qualità dell'aria osservata NGSI-v2 normalizzata Esempio  
Ecco un esempio di AirQualityObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2016-03-15T11:00:00"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Brooklands"  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "moderate"  
  },  
  "co": {  
    "type": "Number",  
    "value": 500,  
    "metadata": {  
      "unitCode": {  
        "value": "GP"  
      }  
    }  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 12.2  
  },  
  "no": {  
    "type": "Number",  
    "value": 45,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "refPointOfInterest": {  
    "type": "Text",  
    "value": "28079004-Pza.deEspanya"  
  },  
  "windDirection": {  
    "type": "Number",  
    "value": 176  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://datos.madrid.es"  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 0.64  
  },  
  "so2": {  
    "type": "Number",  
    "value": 11,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "nox": {  
    "type": "Number",  
    "value": 139,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.712247222222222,  
        40.423852777777775  
      ]  
    }  
  },  
  "typeOfLocation": {  
    "type": "Text",  
    "value": "outdoor"  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 65  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Madrid",  
      "streetAddress": "Plaza de Espa\u00f1a"  
    }  
  },  
  "reliability": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.54  
  },  
  "precipitation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "no2": {  
    "type": "Number",  
    "value": 69,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "coLevel": {  
    "type": "Text",  
    "value": "moderate"  
  }  
}  
```  
</details>  
#### Valori chiave di AirQualityObserved NGSI-LD Esempio  
Ecco un esempio di AirQualityObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "co": 500,  
  "coLevel": "moderate",  
  "no": 45,  
  "no2": 69,  
  "nox": 139,  
  "so2": 11,  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Madrid",  
    "streetAddress": "Plaza de Espa\u00f1a",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 65,  
  "airQualityLevel": "moderate",  
  "areaServed": "Brooklands",  
  "dateObserved": "2016-03-15T11:00:00",  
  "location": {  
    "coordinates": [  
      -3.712247222222222,  
      40.423852777777775  
    ],  
    "type": "Point"  
  },  
  "precipitation": 0,  
  "refPointOfInterest": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya",  
  "relativeHumidity": 0.54,  
  "reliability": 0.7,  
  "source": "http://datos.madrid.es",  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "windDirection": 180,  
  "windSpeed": 0.64,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Qualità dell'ariaOsservata NGSI-LD normalizzato Esempio  
Ecco un esempio di AirQualityObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "co": {  
      "type": "Property",  
      "value": 500,  
      "unitCode": "GP"  
  },  
  "coLevel": {  
      "type": "Property",  
      "value": "moderate"  
  },  
  "no": {  
      "type": "Property",  
      "value": 45,  
      "unitCode": "GQ"  
  },  
  "no2": {  
      "type": "Property",  
      "value": 69,  
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
  "address": {  
      "type": "Property",  
      "value": {  
          "addressCountry": "ES",  
          "addressLocality": "Madrid",  
          "streetAddress": "Plaza de Espa\u00f1a",  
          "type": "PostalAddress"  
      }  
  },  
  "airQualityIndex": {  
      "type": "Property",  
      "value": 65  
  },  
  "airQualityLevel": {  
      "type": "Property",  
      "value": "moderate"  
  },  
  "areaServed": {  
      "type": "Property",  
      "value": "Brooklands"  
  },  
  "dateObserved": {  
      "type": "Property",  
      "value": "2016-03-15T11:00:00"  
  },  
  "location": {  
      "type": "GeoProperty",  
      "value": {  
          "type": "Point",  
          "coordinates": [  
              -3.712247222222222,  
              40.423852777777775  
          ]  
      }  
  },  
  "precipitation": {  
      "type": "Property",  
      "value": 0  
  },  
  "refPointOfInterest": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya"  
  },  
  "relativeHumidity": {  
      "type": "Property",  
      "value": 0.54  
  },  
  "reliability": {  
      "type": "Property",  
      "value": 0.7  
  },  
  "source": {  
      "type": "Property",  
      "value": "http://datos.madrid.es"  
  },  
  "temperature": {  
      "type": "Property",  
      "value": 12.2  
  },  
  "typeOfLocation": {  
      "type": "Property",  
      "value": "outdoor"  
  },  
  "windDirection": {  
      "type": "Property",  
      "value": 186  
  },  
  "windSpeed": {  
      "type": "Property",  
      "value": 0.64  
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
