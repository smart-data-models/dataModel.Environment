<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

TrafficEnvironmentImpactForecast:    
  description: Environmental Impact of traffic based on the vehicles traffic expectations and their emission characteristics    
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
    co2:    
      description: The expected C02 emission concentration    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/L    
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
    dateIssued:    
      description: The date and time the forecast was issued by the service provider in ISO8601 UTC format    
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
    traffic:    
      description: 'Array of objects containing the expected values for intensity, occupation an speed of the different vehicle types'    
      items:    
        properties:    
          averageVehicleSpeedExpected:    
            description: Average speed expected of the vehicles transiting during the observation period    
            minimum: 0    
            type: number    
            x-ngsi:    
              model: https://schema.org/Number    
              type: Property    
              units: Kilometer per hour (Km/h)    
          intensityExpected:    
            description: Total number of vehicles expected during this forecast period    
            minimum: 0    
            type: number    
            x-ngsi:    
              model: https://schema.org/Number    
              type: Property    
          occupancyExpected:    
            description: Fraction of the observation time where a vehicle has been occupying the observed lane    
            maximum: 1    
            minimum: 0    
            type: number    
            x-ngsi:    
              model: https://schema.org/Number    
              type: Property    
          vehicleClass:    
            description: Enumeration of the vehicle classes    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI type. It has to be TrafficEnvironmentImpactForecast    
      enum:    
        - TrafficEnvironmentImpact    
      type: string    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: The start of the validity period for this forecast as a ISO8601 format    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validTo:    
      description: The end of the validity period for this forecast as a ISO8601 format    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validity:    
      description: Includes the validity period for this forecast as a ISO8601 time interval    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/TrafficEnvironmentImpactForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
  "type": "TrafficEnvironmentImpact",  
  "dateCreated": "2022-08-17T05:21:50Z",  
  "dateModified": "2022-08-30T08:09:40Z",  
  "dateIssued": "2022-08-30T08:09:40Z",  
  "validFrom": "2022-08-30T08:19:40Z",  
  "validTo": "2022-08-31T08:19:40Z",  
  "validity": "P1D",  
  "source": "",  
  "name": "Environmental impact",  
  "alternateName": "",  
  "description": "",  
  "dataProvider": "City sensors",  
  "owner": [  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
    "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.7034,  
      7.2663  
    ]  
  },  
  "address": {  
    "streetAddress": "Rue Frédéric Mistral",  
    "addressLocality": "Valbonne",  
    "addressRegion": "Sophia Antipolis",  
    "addressCountry": "France",  
    "postalCode": "06550",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "",  
  "co2": 582.3,  
  "traffic": [  
    {  
      "vehicleClass": "A",  
      "intensityExpected": 23,  
      "occupancyExpected": 0.2,  
      "averageVehicleSpeedExpected": 45  
    },  
    {  
      "vehicleClass": "B",  
      "intensityExpected": 112,  
      "occupancyExpected": 0.15,  
      "averageVehicleSpeedExpected": 65  
    }  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
  "type": "TrafficEnvironmentImpact",  
  "dateCreated": {  
    "type": "date-time",  
    "value": "2022-08-17T05:21:50Z"  
  },  
  "dateModified": {  
    "type": "date-time",  
    "value": "2022-08-30T08:09:40Z"  
  },  
  "dateIssued": {  
    "type": "Date-Time",  
    "value": "2022-08-30T08:09:40Z"  
  },  
  "validFrom": {  
    "type": "Date-Time",  
    "value": "2022-08-30T08:19:40Z"  
  },  
  "validTo": {  
    "type": "Date-Time",  
    "value": "2022-08-31T08:19:40Z"  
  },  
  "validity": {  
    "type": "Text",  
    "value": "P1D"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Environmental impact"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "City sensors"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
      "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
    ]  
  },  
  "location": {  
    "type": "object",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Rue Frédéric Mistral",  
      "addressLocality": "Valbonne",  
      "addressRegion": "Sophia Antipolis",  
      "addressCountry": "France",  
      "postalCode": "06550",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "co2": {  
    "type": "Number",  
    "value": 582.3  
  },  
  "traffic": {  
    "type": "array",  
    "value": [  
       {  
      "vehicleClass": "A",  
      "intensityExpected": 23,  
      "occupancyExpected": 0.2,  
      "averageVehicleSpeedExpected": 45  
    },  
    {  
      "vehicleClass": "B",  
      "intensityExpected": 112,  
      "occupancyExpected": 0.15,  
      "averageVehicleSpeedExpected": 65  
    }  
    ]  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
    "type": "TrafficEnvironmentImpact",  
    "dateCreated": "2022-08-17T05:21:50Z",  
    "dateModified": "2022-08-30T08:09:40Z",  
    "dateIssued": "2022-08-30T08:09:40Z",  
    "validFrom": "2022-08-30T08:19:40Z",  
    "validTo": "2022-08-31T08:19:40Z",  
    "validity": "P1D",  
    "source": "",  
    "name": "Environmental impact",  
    "alternateName": "",  
    "description": "",  
    "dataProvider": "City sensors",  
    "owner": [  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
        "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.7034,  
            7.2663  
        ]  
    },  
    "address": {  
        "streetAddress": "Rue Fr\u00e9d\u00e9ric Mistral",  
        "addressLocality": "Valbonne",  
        "addressRegion": "Sophia Antipolis",  
        "addressCountry": "France",  
        "postalCode": "06550",  
        "postOfficeBoxNumber": ""  
    },  
    "areaServed": "",  
    "co2": 582.3,  
    "traffic": [  
        {  
            "vehicleClass": "A",  
            "intensityExpected": 23,  
            "occupancyExpected": 0.2,  
            "averageVehicleSpeedExpected": 45  
        },  
        {  
            "vehicleClass": "B",  
            "intensityExpected": 112,  
            "occupancyExpected": 0.15,  
            "averageVehicleSpeedExpected": 65  
        }  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:TrafficEnvironmentImpact:id:BGGK:76812356",  
    "type": "TrafficEnvironmentImpact",  
    "dateCreated": {  
        "type": "Property",  
        "value": "2022-08-17T05:21:50Z"  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": "2022-08-30T08:09:40Z"  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": "2022-08-30T08:09:40Z"  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": "2022-08-30T08:19:40Z"  
    },  
    "validTo": {  
        "type": "Property",  
        "value": "2022-08-31T08:19:40Z"  
    },  
    "validity": {  
        "type": "Property",  
        "value": "P1D"  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "name": {  
        "type": "Property",  
        "value": "Environmental impact"  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "description": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "City sensors"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:FAVE:94166126",  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:EWHQ:53940846"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:JSNF:11004684",  
            "urn:ngsi-ld:TrafficEnvironmentImpact:items:HURK:65683455"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.7034,  
                7.2663  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Rue Fr\u00e9d\u00e9ric Mistral",  
            "addressLocality": "Valbonne",  
            "addressRegion": "Sophia Antipolis",  
            "addressCountry": "France",  
            "postalCode": "06550",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "co2": {  
        "type": "Property",  
        "value": 582.3  
    },  
    "traffic": {  
        "type": "Property",  
        "value": [  
            {  
                "vehicleClass": "A",  
                "intensityExpected": 23,  
                "occupancyExpected": 0.2,  
                "averageVehicleSpeedExpected": 45  
            },  
            {  
                "vehicleClass": "B",  
                "intensityExpected": 112,  
                "occupancyExpected": 0.15,  
                "averageVehicleSpeedExpected": 65  
            }  
        ]  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
