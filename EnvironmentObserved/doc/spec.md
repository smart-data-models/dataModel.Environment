Entity: EnvironmentObserved  
===========================  
[Open License](https://github.com/smart-data-models//dataModel.Environment/blob/master/EnvironmentObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of the environmental conditions observed at a particular location and time. This entity is primarily associated with the vertical segment of the environment and agriculture but may also be used in smart home, smart cities, industry and related IoT applications.**  

## List of properties  

- `address`: The mailing address  - `airQualityObserved`: A reference to associated AirQualityObserved entities.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pointOfInterest`: A reference to associated Points of Interest (e.g. monitoring stations) that the associated observations are related to.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity identifier. It has to be EnvironmentObserved  - `waterQualityObserved`: A reference to associated WaterQualityObserved entities.  - `weatherObserved`: A reference to associated WeatherObserved entities.    
Required properties  
- `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EnvironmentObserved:    
  description: 'This entity contains a harmonised description of the environmental conditions observed at a particular location and time. This entity is primarily associated with the vertical segment of the environment and agriculture but may also be used in smart home, smart cities, industry and related IoT applications.'    
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
    airQualityObserved:    
      description: 'A reference to associated AirQualityObserved entities.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: '^[\w\-\.\{\}\$\+\*\[\]`|~^@!,: \\]+$'    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
        description: 'Relationship. A reference to associated AirQualityObserved entities.'    
      type: array    
      x-ngsi:    
        type: Relationship    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &environmentobserved_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *environmentobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pointOfInterest:    
      description: 'A reference to associated Points of Interest (e.g. monitoring stations) that the associated observations are related to.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
        description: 'Relationship. A reference to associated Points of Interest (e.g. monitoring stations) that the associated observations are related to.'    
      type: array    
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
    type:    
      description: 'NGSI Entity identifier. It has to be EnvironmentObserved'    
      enum:    
        - EnvironmentObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterQualityObserved:    
      description: 'A reference to associated WaterQualityObserved entities.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: '^[\w\-\.\{\}\$\+\*\[\]`|~^@!,: \\]+$'    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    weatherObserved:    
      description: 'A reference to associated WeatherObserved entities.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: '^[\w\-\.\{\}\$\+\*\[\]`|~^@!,: \\]+$'    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/EnvironmentObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/EnvironmentObserved/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Example payloads    
#### EnvironmentObserved NGSI-v2 key-values Example    
Here is an example of a EnvironmentObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
  "type": "EnvironmentObserved",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "pointOfInterest": [  
    "urn:ngsi-ld:POI:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:POI:42dcd5ea-46db-11e8-bea0-772aba733f93",  
    "urn:ngsi-ld:POI:4912d78e-46db-11e8-8572-ab2b8e55590b"  
  ],  
  "weatherObserved": [  
    "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
    "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
  ],  
  "airQualityObserved": [  
    "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
    "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
  ],  
  "waterQualityObserved": [  
    "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
    "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
  ]  
}  
```  
#### EnvironmentObserved NGSI-v2 normalized Example    
Here is an example of a EnvironmentObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
  "type": "EnvironmentObserved",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "pointOfInterest": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:POI:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:POI:42dcd5ea-46db-11e8-bea0-772aba733f93",  
      "urn:ngsi-ld:POI:4912d78e-46db-11e8-8572-ab2b8e55590b"  
    ]  
  },  
  "weatherObserved": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
      "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
    ]  
  },  
  "airQualityObserved": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
      "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
    ]  
  },  
  "waterQualityObserved": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
      "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
    ]  
  }  
}  
```  
#### EnvironmentObserved NGSI-LD key-values Example    
Here is an example of a EnvironmentObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.github.io/dataModel.Environment/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
  "type": "EnvironmentObserved",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "pointOfInterest": [  
    "urn:ngsi-ld:POI:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:POI:42dcd5ea-46db-11e8-bea0-772aba733f93",  
    "urn:ngsi-ld:POI:4912d78e-46db-11e8-8572-ab2b8e55590b"  
  ],  
  "weatherObserved": [  
    "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
    "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
  ],  
  "airQualityObserved": [  
    "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
    "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
  ],  
  "waterQualityObserved": [  
    "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
    "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
  ]  
}  
```  
#### EnvironmentObserved NGSI-LD normalized Example    
Here is an example of a EnvironmentObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
  "type": "EnvironmentObserved",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "pointOfInterest": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:POI:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:POI:42dcd5ea-46db-11e8-bea0-772aba733f93",  
      "urn:ngsi-ld:POI:4912d78e-46db-11e8-8572-ab2b8e55590b"  
    ]  
  },  
  "weatherObserved": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
      "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
    ]  
  },  
  "airQualityObserved": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
      "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
    ]  
  },  
  "waterQualityObserved": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
      "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
    ]  
  }  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units