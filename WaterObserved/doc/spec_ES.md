<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: WaterObserved    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Environment/blob/master/WaterObserved/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: ** El modelo de datos de observación del agua pretende representar los parámetros de caudal, nivel y volumen de agua observados, así como la información de oleaje, sobre un área fija o variable. Esta observación incluye también las masas de objetos flotantes sobre esta zona. Los datos recogidos proceden de sensores, cámaras, estaciones acuáticas situadas en lugares específicos o sensibles de ríos, arroyos, torrentes, lagos, mares, etc.**.    
versión: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateObserved[date-time]`: Fecha y hora de esta observación representadas por un formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: Período de observación : Fecha y hora de inicio en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: Período de observación : Fecha y hora de finalización en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descripción de este artículo  - `flow[number]`: Caudal de agua observado. El código de unidad (texto) de medida dado utilizando el UN/CEFACAT  . Model: [https://schema.org/Number](https://schema.org/Number)- `height[number]`: Altura del agua - Alcance del nivel en las costas de alerta  . Model: [https://schema.org/height](https://schema.org/height)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `measuredArea[number]`: Referencia de la superficie medida. El código de unidad (texto) de medida dado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTK</code> representa M².  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo  - `objectArea[number]`: Porcentaje ocupado por objeto flotante en la zona. El código de unidad (texto) de medida dado utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>P1</code> representa Porcentaje  . Model: [https://schema.org/Number](https://schema.org/Number)- `objectHeightAverage[number]`: Altura media elevada. El código de unidad (texto) de medida dado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTR</code> representa Metro  . Model: [https://schema.org/Number](https://schema.org/Number)- `objectHeightMax[number]`: Altura máxima elevada. El código de unidad (texto) de medida dado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTR</code> representa Metro  . Model: [https://schema.org/Number](https://schema.org/Number)- `objectVolume[number]`: Volumen estimado recaudado. El código de unidad (texto) de medida dado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTQ</code> representa Metros Cúbicos.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `refDevice[*]`: Referencia a un punto de interés asociado a esta observación  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `swellDirection[number]`: Dirección del oleaje observado  . Model: [https://schema.org/Number](https://schema.org/Number)- `swellHeight[number]`: Altura de oleaje observada  . Model: [https://schema.org/height](https://schema.org/height)- `swellPeriod[number]`: Periodo de oleaje observado  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser WaterObserved  - `waterDischarge[number]`: Vertido al agua procedente de plantas de tratamiento de aguas pluviales y residuales. El código de unidad (texto) de medida indicado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTQ</code> representa el metro cúbico.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: Nivel actual del agua correspondiente a esta observación. El código de unidad (texto) de medida dado utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <code>MTR</code> representa Metros  . Model: [https://schema.org/Number](https://schema.org/Number)- `waveLength[number]`: Longitud de onda observada.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
El modelo de datos de observación del agua tiene por objeto representar los parámetros de caudal, nivel y volumen de agua observados, así como la información sobre el oleaje, en una zona fija o variable. Esta observación incluye también las masas de objetos flotantes sobre esta zona.  Los datos recogidos son proporcionados por [Sensores], [Cámaras], [Estaciones acuáticas] situados en lugares específicos o sensibles para ríos, arroyos, torrentes, lagos, mares, etc.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WaterObserved:      
  description: ' Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area. The data collected is provided by Sensors, Cameras,Water stations positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc.'      
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
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: Date and time of this observation represented by an ISO8601 UTC format      
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
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    flow:      
      description: Water Flow observed. The unit code (text) of measurement given using the UN/CEFACAT      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    height:      
      description: Water height - Level reach on alert coasts      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/height      
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
    measuredArea:      
      description: 'Reference of the surface measured. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTK</code> represents M²'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: square meters      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    objectArea:      
      description: 'Percentage occupied by floating object in the area. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>P1</code> represents Percentage'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    objectHeightAverage:      
      description: 'Average height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: meters      
    objectHeightMax:      
      description: 'Maximum height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: meters      
    objectVolume:      
      description: 'Estimated volume raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTQ</code> represents Cubic Meters'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: cubic meters      
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
      description: A reference to a point of interest associated to this observation      
      x-ngsi:      
        type: Relationship      
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
    swellDirection:      
      description: Swells Direction observed      
      maximum: 360      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    swellHeight:      
      description: Swell height observed      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/height      
        type: Property      
    swellPeriod:      
      description: Swells period observed      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be WaterObserved      
      enum:      
        - WaterObserved      
      type: string      
      x-ngsi:      
        type: Property      
    waterDischarge:      
      description: 'Discharge into the water from stormwater and wastewater treatment plants. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTQ</code> represents Cubic Metre'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: cubic metre      
    waterLevel:      
      description: 'Current water level corresponding to this observation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Metre'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metre      
    waveLength:      
      description: 'Wave Length observed. '      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
    - location      
    - dateObserved      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/WaterObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/data-models/Environment/WaterObserved/schema.js      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### WaterObserved NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un WaterObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "name": "STLRT-MNCA-AP-WO-012",  
  "alternateName": "Var River Alert for safety procedure for Airport",  
  "description": "Observation of Evolution of the water levels",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "refDevice": "Device:T2-NP-018",  
  "dateObserved": "2020-03-17T08:45:00.209Z",  
  "flow": 12,  
  "height": 3.52,  
  "measuredArea": 250,  
  "objectArea": 35,  
  "objectHeightAverage": 1.75,  
  "objectHeightMax": 2.25,  
  "objectVolume": 17.5,  
  "waterLevel": 2.4,  
  "waterDischarge": 3  
}  
```  
</details>    
#### WaterObserved NGSI-v2 normalized Ejemplo    
He aquí un ejemplo de WaterObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "name": {  
    "type": "Text",  
    "value": "STLRT-MNCA-AP-WO-012"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Var River Alert for safety procedure for Airport"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Observation of Evolution of the water levels"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Airport"  
  },  
  "refDevice": {  
    "type": "Text",  
    "value": "Device:T2-NP-018"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00.209Z"  
  },  
  "flow": {  
    "type": "Number",  
    "value": 12  
  },  
  "height": {  
    "type": "Number",  
    "value": 3.52  
  },  
  "measuredArea": {  
    "type": "Number",  
    "value": 250  
  },  
  "objectArea": {  
    "type": "Number",  
    "value": 35  
  },  
  "objectHeightAverage": {  
    "type": "Number",  
    "value": 1.75  
  },  
  "objectHeightMax": {  
    "type": "Number",  
    "value": 2.25  
  },  
  "objectVolume": {  
    "type": "Number",  
    "value": 17.5  
  },  
  "waterLevel": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 3  
  }  
}  
```  
</details>    
#### WaterObserved NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un WaterObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi:WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "alternateName": "Var River Alert for safety procedure for Airport",  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-03-17T08:45:00.209Z",  
  "description": "Observation of Evolution of the water levels",  
  "flow": 12,  
  "height": 3.52,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "measuredArea": 250,  
  "name": "STLRT-MNCA-AP-WO-012",  
  "objectArea": 35,  
  "objectHeightAverage": 1.75,  
  "objectHeightMax": 2.25,  
  "objectVolume": 17.5,  
  "refDevice": "uri:ngsi:Device:T2-NP-018",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AguaObservada NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de WaterObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi:WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "alternateName": {  
    "type": "Property",  
    "value": "Var River Alert for safety procedure for Airport"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateObserved": {  
    "type": "Relationship",  
    "object": "2020-03-17T08:45:00.209Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Observation of Evolution of the water levels"  
  },  
  "flow": {  
    "type": "Number",  
    "value": 12  
  },  
  "height": {  
    "type": "Number",  
    "value": 3.52  
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
  "measuredArea": {  
    "type": "Number",  
    "value": 250  
  },  
  "name": {  
    "type": "Property",  
    "value": "STLRT-MNCA-AP-WO-012"  
  },  
  "objectArea": {  
    "type": "Number",  
    "value": 35  
  },  
  "objectHeightAverage": {  
    "type": "Number",  
    "value": 1.75  
  },  
  "objectHeightMax": {  
    "type": "Number",  
    "value": 2.25  
  },  
  "objectVolume": {  
    "type": "Number",  
    "value": 17.5  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "uri:ngsi:Device:T2-NP-018"  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
