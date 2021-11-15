Entidad: AguaObservada  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Environment/blob/master/WaterObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: ** El modelo de datos de observación del agua está destinado a representar los parámetros de flujo, nivel y volumen de agua observados, así como la información sobre el oleaje, sobre un área fija o variable. Esta observación también incluye las masas de objetos flotantes en esta área. Los datos recogidos son proporcionados por Sensores, Cámaras, Estaciones de Agua posicionadas en lugares específicos o sensibles para ríos, arroyos, torrentes, lagos, mares, etc.**.  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: Fecha y hora de esta observación representada por un formato ISO8601 UTC.  - `dateObservedFrom`: Período de observación : Fecha y hora de inicio en formato ISO8601 UTC.  - `dateObservedTo`: Período de observación : Fecha y hora de finalización en formato ISO8601 UTC.  - `description`: Una descripción de este artículo  - `flow`: Flujo de agua observado. El código de la unidad (texto) de medida dado utilizando el UN/CEFACAT  - `height`: Altura del agua - Alcance del nivel en las costas de alerta.  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `measuredArea`: Referencia de la superficie medida. El código de la unidad (texto) de medida dado utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTK</código> representa M².  - `name`: El nombre de este artículo.  - `objectArea`: Porcentaje ocupado por el objeto flotante en la zona. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>P1</código> representa el Porcentaje.  - `objectHeightAverage`: Altura media elevada. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa el Metro.  - `objectHeightMax`: Altura máxima elevada. El código de la unidad (texto) de medida dado utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres). Por ejemplo, <código>MTR</código> representa el Metro.  - `objectVolume`: Volumen estimado recaudado. El código de la unidad (texto) de medida que se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máximo 3 caracteres). Por ejemplo, <código>MTQ</código> representa Metros Cúbicos  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: Una referencia a un punto de interés asociado a esta observación.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `swellDirection`: Dirección de las marejadas observadas.  - `swellHeight`: Altura del oleaje observada.  - `swellPeriod`: Periodo de oleaje observado.  - `type`: Tipo de entidad NGSI. Tiene que ser WaterObserved  - `waveLength`: Longitud de onda observada.    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `type`    
El modelo de datos de observación del agua tiene por objeto representar los parámetros de flujo, nivel y volumen de agua observados, así como la información sobre el oleaje, en una zona fija o variable. Esta observación también incluye las masas de objetos flotantes en esta área.  Los datos recogidos son proporcionados por [Sensores], [Cámaras], [Estaciones acuáticas] colocados en lugares específicos o sensibles para los ríos, arroyos, torrentes, lagos, mares, etc.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterObserved:    
  description: ' Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area. The data collected is provided by Sensors, Cameras,Water stations positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc.'    
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
      description: 'Date and time of this observation represented by an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    flow:    
      description: 'Water Flow observed. The unit code (text) of measurement given using the UN/CEFACAT'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    height:    
      description: 'Water height - Level reach on alert coasts.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
    id:    
      anyOf: &waterobserved_-_properties_-_owner_-_items_-_anyof    
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
    measuredArea:    
      description: 'Reference of the surface measured. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTK</code> represents M².'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'square meters'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    objectArea:    
      description: 'Percentage occupied by floating object in the area. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>P1</code> represents Percentage.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    objectHeightAverage:    
      description: 'Average height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    objectHeightMax:    
      description: 'Maximum height raised. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
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
        units: 'cubic meters'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A reference to a point of interest associated to this observation.'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    swellDirection:    
      description: 'Swells Direction observed.'    
      maximum: 360    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    swellHeight:    
      description: 'Swell height observed.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
    swellPeriod:    
      description: 'Swells period observed.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WaterObserved'    
      enum:    
        - WaterObserved    
      type: string    
      x-ngsi:    
        type: Property    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/WaterObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Environment/WaterObserved/schema.js    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## Ejemplo de carga útil  
#### WaterObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un WaterObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
      43.664810,  
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
  "objectVolume": 17.5  
}  
```  
#### AguaObservada NGSI-v2 normalizada Ejemplo  
Este es un ejemplo de un WaterObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Airport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
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
  }  
}  
```  
#### WaterObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un WaterObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "uri:ngsi:WaterObserved:MNCA-001",  
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
  "refDevice": "uri:ngsi:Device:T2-NP-018",  
  "dateObserved": "2020-03-17T08:45:00.209Z",  
  "flow": 12,  
  "height": 3.52,  
  "measuredArea": 250,  
  "objectArea": 35,  
  "objectHeightAverage": 1.75,  
  "objectHeightMax": 2.25,  
  "objectVolume": 17.5,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### AguaObservada NGSI-LD normalizada Ejemplo  
Este es un ejemplo de un WaterObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi:WaterObserved:MNCA-001",  
  "type": "WaterObserved",  
  "name": {  
    "type": "Property",  
    "value": "STLRT-MNCA-AP-WO-012"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Var River Alert for safety procedure for Airport"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Observation of Evolution of the water levels"  
  },  
  "location": {  
    "type": "Geoproperty",  
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
  "refDevice": {  
    "type": "Relationship",  
    "object": "uri:ngsi:Device:T2-NP-018"  
  },  
  "dateObserved": {  
    "type": "Relationship",  
    "object": "2020-03-17T08:45:00.209Z"  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
