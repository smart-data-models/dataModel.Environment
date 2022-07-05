[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: NoisePollution  
======================  
[Open License](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollution/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Noise Pollution data model merges specific and punctual noise measurements (coming, e.g. from NoiseLevelObservation entities) into average parameters referred to city areas, providing a more city-related data about noise pollution status and evolution.**  
version: 0.0.1  

## List of properties  

- `LAeq2`: Average sound level over the last 2 hours  - `LAmax2`: Maximum sound level recorded for the last 2 hours  - `alternateName`: An alternative name for this item  - `buildingsType`: Type of predominant buildings within the measurement area at installation of the sensor  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObservedFrom`: Observation period start date and time  - `dateObservedTo`: End date and time of the observation period  - `description`: A description of this item  - `groundType`: Type of predominant ground in the measurement area at installation of the sensor  - `id`: Unique identifier of the entity  - `name`: The name of this item.  - `noiseAnnoyanceIndex`: Index (1 to 10) according to noise annoyance level  - `noiseOrigin`: Main origin (source) of the recorded noise at installation of the sensor  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI type. it has to be NoisePollution  - `wallsType`: Facade material types dominant in the measurement area at installation of the sensor    
Required properties  
- `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoisePollution:    
  description: 'Noise Pollution data model merges specific and punctual noise measurements (coming, e.g. from NoiseLevelObservation entities) into average parameters referred to city areas, providing a more city-related data about noise pollution status and evolution.'    
  properties:    
    LAeq2:    
      description: 'Average sound level over the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax2:    
      description: 'Maximum sound level recorded for the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    buildingsType:    
      description: 'Type of predominant buildings within the measurement area at installation of the sensor'    
      type: string    
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
    dateObservedFrom:    
      description: 'Observation period start date and time'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'End date and time of the observation period'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    groundType:    
      description: 'Type of predominant ground in the measurement area at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &noisepollution_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    noiseAnnoyanceIndex:    
      description: 'Index (1 to 10) according to noise annoyance level'    
      max: 10    
      min: 1    
      type: number    
      x-ngsi:    
        type: Property    
    noiseOrigin:    
      description: 'Main origin (source) of the recorded noise at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *noisepollution_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type. it has to be NoisePollution'    
      enum:    
        - NoisePollution    
      type: string    
      x-ngsi:    
        type: Property    
    wallsType:    
      description: 'Facade material types dominant in the measurement area at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollution/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollution/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Example payloads    
#### NoisePollution NGSI-v2 key-values Example    
Here is an example of a NoisePollution in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "Laeq2": 85,  
  "Lamax2": 75,  
  "Lanight": 45,  
  "NoiseAnnoyanceIndex": 3,  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "buildingsType": "residential",  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateObservedFrom": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateObservedTo": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T12:40:01.00Z"  
  },  
  "exposureType": "short term exposure",  
  "groundType": "concrete",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "noiseOrigin": "traffic",  
  "wallsType": "glass"  
}  
```  
#### NoisePollution NGSI-v2 normalized Example    
Here is an example of a NoisePollution in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice",  
      "type": "PostalAddress"  
    }  
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
  "dataProvider": {  
    "type": "Property",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateObservedFrom": {  
    "type":  "DateTime",  
      "value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
      "value": "2022-07-01T12:40:01.00Z"  
  },  
  "NoiseAnnoyanceIndex": {  
    "type": "Number",  
    "value": 3  
  },  
  "Lanight": {  
    "type": "Number",  
    "value": 45  
  },  
  "noiseOrigin": {  
    "type": "Text",  
    "value": "traffic"  
  },  
  "exposureType": {  
    "type": "Property",  
    "value": "short term exposure"  
  },  
  "buildingsType": {  
    "type": "Text",  
    "value": "residential"  
  },  
  "groundType": {  
    "type": "Text",  
    "value": "concrete"  
  },  
  "wallsType": {  
    "type": "Text",  
    "value": "glass"  
  },  
  "Lamax2": {  
    "type": "Number",  
    "value": 75  
  },  
  "Laeq2": {  
    "type": "Number",  
    "value": 85  
  }  
}  
```  
#### NoisePollution NGSI-LD key-values Example    
Here is an example of a NoisePollution in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "Laeq2": 85,  
  "Lamax2": 75,  
  "Lanight": 45,  
  "NoiseAnnoyanceIndex": 3,  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "buildingsType": "residential",  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateObservedFrom": "2022-07-01T10:40:01.00Z",  
  "dateObservedTo": "2022-07-01T12:40:01.00Z",  
  "exposureType": "short term exposure",  
  "groundType": "concrete",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "noiseOrigin": "traffic",  
  "wallsType": "glass",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
#### NoisePollution NGSI-LD normalized Example    
Here is an example of a NoisePollution in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice",  
      "type": "PostalAddress"  
    }  
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
  "dataProvider": {  
    "type": "Property",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T10:40:01.00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T12:40:01.00Z"  
    }  
  },  
  "NoiseAnnoyanceIndex": {  
    "type": "Property",  
    "value": 3  
  },  
  "Lanight": {  
    "type": "Property",  
    "value": 45  
  },  
  "noiseOrigin": {  
    "type": "Property",  
    "value": "traffic"  
  },  
  "exposureType": {  
    "type": "Property",  
    "value": "short term exposure"  
  },  
  "buildingsType": {  
    "type": "Property",  
    "value": "residential"  
  },  
  "groundType": {  
    "type": "Property",  
    "value": "concrete"  
  },  
  "wallsType": {  
    "type": "Property",  
    "value": "glass"  
  },  
  "Lamax2": {  
    "type": "Property",  
    "value": 75  
  },  
  "Laeq2": {  
    "type": "Property",  
    "value": 85  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
