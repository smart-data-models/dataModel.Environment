Entidad: FloodMonitoring  
========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Environment/blob/master/FloodMonitoring/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Modelo de datos de sensores de inundación destinado a representar el nivel de inundación en relación con el flujo/nivel de agua en una determinada masa de agua (río, lago, etc.).  

## Lista de propiedades  

- `address`: La dirección postal  - `alertLevel`: Valor umbral de nivel de alerta de referencia establecido para la estación de detección correspondiente a esta observación. Se genera una señal de alerta si el nivel actual cruza el valor de umbral de nivel de alerta.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `currentLevel`: Nivel de inundación actual indicado por la estación de detección correspondiente a esta observación, calculado utilizando ReferenceLevel y measuredDistance(currentLevel = referenceLevel - measuredDistance).  - `dangerLevel`: Valor umbral de nivel de peligro de referencia fijado para la estación de detección correspondiente a esta observación. El estado del nivel de inundación se marca como peligroso si el nivel actual cruza el valor del umbral de nivel de peligro.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `floodLevelStatus`: Indicación del estado del nivel de inundación dado por el dispositivo de detección de inundaciones. El estado se marca como Peligro si el nivel actual es superior al valor del umbral de nivel de peligro.  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `measuredDistance`: Describe la distancia medida por el sensor, desde la punta del sensor hasta la superficie superior del agua.  - `name`: El nombre de este artículo.  - `observationDateTime`: Última hora de observación comunicada.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `referenceLevel`: Describe la distancia vertical desde el lecho del río hasta la punta del sensor.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `stationID`: Un identificador anónimo único asignado a la estación correspondiente a esta observación.  - `type`: Tiene que ser FloodMonitoring. Tipo de entidad NGSI.    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FloodMonitoring:    
  description: 'Flood Sensor Data Model intended to represent the level of flooding w.r.t water flow/level at a certain water mass(river, lake,etc.)..'    
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
    alertLevel:    
      description: 'Reference alert level threshold value set for the sensing station corresponding to this observation. An Alert signal is generated if the current level crosses the alert level threshold value.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    currentLevel:    
      description: 'Current flooding level indicated by the sensing station corresponding to this observation, computed using referenceLevel and measuredDistance(currentLevel = referenceLevel - measuredDistance).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dangerLevel:    
      description: 'Reference danger level threshold value set for the sensing station corresponding to this observation. Flood level status is marked danger if the current level crosses the danger level threshold value.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    floodLevelStatus:    
      description: 'Flood level status indication given by the flood sensing device. The status is marked Danger if the current level is higher than the danger level threshold value.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &floodmonitoring_-_properties_-_owner_-_items_-_anyof    
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
    measuredDistance:    
      description: 'Describes the distance measured by the sensor, from the sensor tip to the upper surface of water.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
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
        anyOf: *floodmonitoring_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    referenceLevel:    
      description: 'Describes the vertical distance from river bed to sensor tip.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    stationID:    
      description: 'A unique anonymous identifier assigned to the station corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be FloodMonitoring. NGSI Entity type.'    
      enum:    
        - FloodMonitoring    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/FloodMonitoring/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/FloodMonitoring/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### FloodMonitoring NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un FloodMonitoring en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": 10.00,  
  "measuredDistance": 3.22,  
  "currentLevel": 0.98,  
  "dangerLevel": 25.00,  
  "observationDateTime": "2020-09-16T13:30:00+05:30",  
  "referenceLevel": 4.2,  
  "floodLevelStatus": "Normal",  
  "stationID": "FWR013"  
}  
```  
#### FloodMonitoring NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un FloodMonitoring en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": {  
    "type": "Property",  
    "value": 11.00  
  },  
  "measuredDistance": {  
    "type": "Property",  
    "value": 4.22  
  },  
  "currentLevel": {  
    "type": "Property",  
    "value": 1.98  
  },  
  "dangerLevel": {  
    "type": "Property",  
    "value": 26.00  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": "2020-09-16T13:30:00+05:30"  
  },  
  "referenceLevel": {  
    "type": "Property",  
    "value": 4.2  
  },  
  "floodLevelStatus": {  
    "type": "Property",  
    "value": "Normal"  
  },  
  "stationID": {  
    "type": "Property",  
    "value": "FWR013"  
  }  
}  
```  
#### FloodMonitoring NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un FloodMonitoring en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": {  
    "type": "Property",  
    "value": 11.0,  
    "unitCode": "MTR"  
  },  
  "measuredDistance": {  
    "type": "Property",  
    "value": 4.22,  
    "unitCode": "MTR"  
  },  
  "currentLevel": {  
    "type": "Property",  
    "value": 1.98,  
    "unitCode": "MTR"  
  },  
  "dangerLevel": {  
    "type": "Property",  
    "value": 26.0,  
    "unitCode": "MTR"  
  },  
  "observationDateTime": {  
    "type": "string",  
    "format": "date-time",  
    "value": "2020-09-16T13:30:00+05:30"  
  },  
  "referenceLevel": {  
    "type": "Property",  
    "value": 4.2,  
    "unitCode": "MTR"  
  },  
  "floodLevelStatus": {  
    "type": "string",  
    "value": "Normal"  
  },  
  "stationID": {  
    "type": "string",  
    "value": "FWR013"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### FloodMonitoring NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de FloodMonitoring en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "alertLevel": 10.0,  
  "measuredDistance": 3.22,  
  "currentLevel": 0.98,  
  "dangerLevel": 25.0,  
  "observationDateTime": "2020-09-16T13:30:00+05:30",  
  "referenceLevel": 4.2,  
  "floodLevelStatus": "Normal",  
  "stationID": "FWR013"  
}  
```  
