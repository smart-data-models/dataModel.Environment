<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

====================
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
- `airTemperature[object]`: 관측된 기온 값입니다. 값은 과거 데이터에서 파생된 통계 집계를 나타내는 속성을 포함하는 개체입니다.  
	- `deviceId[string]`: 이 관측에 해당하는 물리적 센서/측정 스테이션의 장치 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 고려 중인 장치, 센서 또는 시스템의 정보를 설명합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: 이 관측에 해당하는 센서 장치/스테이션의 장치 이름 또는 스테이션 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 폐기물 관리 차량에 있는 기기의 심 번호를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 장치에서 감지/관찰/측정된 속성/특성  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: RFID 리더의 ID를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `id[*]`: 엔티티의 고유 식별자  
	- `maleSpeciesCount[number]`: 장치에서 식별한 종의 수컷 모기의 총 수입니다.    
	- `mosquitoSpecies[string]`: 장치에서 식별한 모기 종의 이항/동물학적 명명법    
	- `totalSpeciesCount[number]`: 장치가 감지한 특정 종의 총 개수입니다.    
- `name[string]`: 이 항목의 이름  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

MosquitoDensity:    
  description: A Data Model for density of mosquitoes in cities.    
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
    airTemperature:    
      description: Observed value of air temperature. Value is an object containing attributes representing statistical aggregates derived from past data    
      type: object    
      x-ngsi:    
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
    dataDescriptor:    
      description: URI pointing to the data-descriptor entity    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: Information about the device associated with the observations    
      properties:    
        deviceBatteryStatus:    
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceId:    
          description: Device ID of the physical sensor/ measurement station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceModel:    
          description: 'Describes the information of the device, sensor or system in consideration'    
          properties:    
            brandName:    
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            manufacturerName:    
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelName:    
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelURL:    
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
          type: object    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceName:    
          description: Device Name or Station name of the sensor device/station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceSimNumber:    
          description: Gives the sim number of the device in the waste management vehicle    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        measurand:    
          description: Property/properties sensed/observed/measured by the device    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        rfID:    
          description: Gives the ID of the RFID reader    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
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
    mosquitoDensity:    
      description: The binomial (or) zoological nomenclature of the mosquito species and its count as identified by the device corresponding to this observation    
      properties:    
        femaleSpeciesCount:    
          description: The total count of the female mosquitoes of the species identified by the device    
          type: number    
          x-ngsi:    
            type: Property    
        maleSpeciesCount:    
          description: The total count of the male mosquitoes of the species identified by the device    
          type: number    
          x-ngsi:    
            type: Property    
        mosquitoSpecies:    
          description: The binomial/ zoological nomenclature of the mosquito species as identified by the device    
          type: string    
          x-ngsi:    
            type: Property    
        totalSpeciesCount:    
          description: The total count of a particular species detected by the device    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
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
    precipitation:    
      description: Observed precipitation/rainfall level over a given duration    
      type: number    
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
    type:    
      description: NGSI Entity type. It has to be MosquitoDensity    
      enum:    
        - MosquitoDensity    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/MosquitoDensity/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "ngsi-ld:MosquitoDensity:001",  
  "type": "MosquitoDensity",  
  "deviceId": "VDFWitw@B",  
  "deviceSimNumber": "861123052561188",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      76.9578654,  
      8.487284  
    ]  
  },  
  "speciesName": "Culex quinquefasciatus",  
  "speciesTotal": 3,  
  "femaleTotal": 2,  
  "maleTotal": 1,  
  "observationDateTime": "2022-09-18T23:59:59+05:30",  
  "airTemperature": {  
    "instValue": 24.88  
  },  
  "precipitation": 0,  
  "deviceInfo": {  
    "rfID": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "deviceID": "43",  
    "measurand": "6",  
    "deviceSimNumber": "6755375727",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "ngsi-ld:MosquitoDensity:001",  
  "type":  
    "MosquitoDensity"  
  ,  
  "deviceId": {  
    "type": "Text",  
    "value": "VDFWitw@B"  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "861123052561188"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        76.9578654,  
        8.487284  
      ]  
    }  
  },  
  "speciesName": {  
    "type": "Text",  
    "value": "Culex quinquefasciatus"  
  },  
  "speciesTotal": {  
    "type": "Number",  
    "value": 3  
  },  
  "femaleTotal": {  
    "type": "Number",  
    "value": 2  
  },  
  "maleTotal": {  
    "type": "Boolean",  
    "value": true  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2022-09-18T23:59:59+05:30"  
  },  
  "airTemperature": {  
    "type": "StructuredValue",  
    "value": {  
      "instValue": 24.88  
    }  
  },  
  "precipitation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "deviceID": "43",  
      "measurand": "6",  
      "deviceSimNumber": "6755375727",  
      "deviceModel": {  
        "brandName": "abc",  
        "manufacturerName": "xyz",  
        "modelName": "SL1",  
        "modelURL": "www.abcstreetlight.com"  
      }  
    }  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "ngsi-ld:MosquitoDensity:001",  
  "type":  
    "MosquitoDensity"  
  ,  
  "deviceId": "VDFWitw@B",  
  "deviceSimNumber": "861123052561188",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      76.9578654,  
      8.487284  
    ]  
  },  
  "speciesName": "Culex quinquefasciatus",  
  "speciesTotal": 3,  
  "femaleTotal": 2,  
  "maleTotal": 1,  
  "observationDateTime": "2022-09-18T23:59:59+05:30",  
  "airTemperature": {  
    "instValue": 24.88  
  },  
  "precipitation": 0,  
  "deviceInfo": {  
    "rfID": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "deviceID": "43",  
    "measurand": "6",  
    "deviceSimNumber": "6755375727",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  },  
  "@context": [  
 "  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "ngsi-ld:MosquitoDensity:001",  
  "type": "MosquitoDensity",  
  "deviceId": {  
    "type": "Property",  
    "value": "VDFWitw@B"  
  },  
  "deviceSimNumber": {  
    "type": "Property",  
    "value": "861123052561188"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        76.9578654,  
        8.487284  
      ]  
    }  
  },  
  "speciesName": {  
    "type": "Property",  
    "value": "Culex quinquefasciatus"  
  },  
  "speciesTotal": {  
    "type": "Property",  
    "value": 3  
  },  
  "femaleTotal": {  
    "type": "Property",  
    "value": 2  
  },  
  "maleTotal": {  
    "type": "Property",  
    "value": true  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-18T23:59:59+05:30"  
    }  
  },  
  "airTemperature": {  
    "type": "Property",  
    "value": {  
      "instValue": 24.88  
    }  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": false  
  },  
  "deviceInfo": {  
    "type": "Property",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "deviceID": "43",  
      "measurand": "6",  
      "deviceSimNumber": "6755375727",  
      "deviceModel": {  
        "brandName": "abc",  
        "manufacturerName": "xyz",  
        "modelName": "SL1",  
        "modelURL": "www.abcstreetlight.com"  
      }  
    }  
  },  
  "@context": [  
 "  
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
