<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `LAeq2[number]`: 过去2小时的平均声级  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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
      maximum: 10    
      minimum: 1    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollution/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollution/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details><!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
