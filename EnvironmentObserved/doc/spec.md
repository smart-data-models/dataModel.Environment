<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: EnvironmentObserved  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Environment/blob/master/EnvironmentObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised description of the environmental conditions observed at a particular location and time. This entity is primarily associated with the vertical segment of the environment and agriculture but may also be used in smart home, smart cities, industry and related IoT applications.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `airQualityObserved[array]`: A reference to associated AirQualityObserved entities.  - `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pointOfInterest[array]`: A reference to associated Points of Interest (e.g. monitoring stations) that the associated observations are related to.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type[string]`: NGSI Entity identifier. It has to be EnvironmentObserved  - `waterQualityObserved[array]`: A reference to associated WaterQualityObserved entities.  - `weatherObserved[array]`: A reference to associated WeatherObserved entities.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### EnvironmentObserved NGSI-v2 key-values Example    
Here is an example of a EnvironmentObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EnvironmentObserved NGSI-v2 normalized Example    
Here is an example of a EnvironmentObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EnvironmentObserved NGSI-LD key-values Example    
Here is an example of a EnvironmentObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
    "type": "EnvironmentObserved",  
    "airQualityObserved": [  
        "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
        "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
    ],  
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
    "source": "https://source.example.com",  
    "waterQualityObserved": [  
        "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
        "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
    ],  
    "weatherObserved": [  
        "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
        "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
    ],  
    "@context": [  
        "https://smartdatamodels.github.io/dataModel.Environment/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EnvironmentObserved NGSI-LD normalized Example    
Here is an example of a EnvironmentObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EnvironmentObserved:33f02632-74f4-4c96-9ba1-e26945de9481",  
    "type": "EnvironmentObserved",  
    "airQualityObserved": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AirQualityObserved:4b8b09c9-ce54-46de-8067-5591e02d8f29",  
            "urn:ngsi-ld:WeatherObserved:08a14933-b44d-4297-b2d2-2c3f3844012e"  
        ]  
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
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "waterQualityObserved": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WeatherObserved:68a83e68-61e6-4e3c-975c-5b301c184ca6",  
            "urn:ngsi-ld:WeatherObserved:b01518e3-2b60-4bbd-9783-3af0d660349e"  
        ]  
    },  
    "weatherObserved": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WeatherObserved:fae29f4c-0691-4bab-bef8-ad1cd165cc28",  
            "urn:ngsi-ld:WeatherObserved:1c7a2711-ae38-4ea9-8f9f-627067067d53"  
        ]  
    },  
    "@context": [  
        "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
