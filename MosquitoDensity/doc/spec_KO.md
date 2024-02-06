<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: MosquitoDensity  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **도시 내 모기 밀도에 대한 데이터 모델**.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `airTemperature[object]`: 관측된 기온 값입니다. 값은 과거 데이터에서 파생된 통계 집계를 나타내는 속성을 포함하는 개체입니다.  - `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataDescriptor[uri]`: 데이터 설명자 엔티티를 가리키는 URI  - `dataProvider[string]`: 조율된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceInfo[object]`: 관찰과 관련된 장치에 대한 정보  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: 보고 디바이스의 배터리 충전 상태(연결됨, 연결 끊김)를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceId[string]`: 이 관측에 해당하는 물리적 센서/측정 스테이션의 장치 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 고려 중인 장치, 센서 또는 시스템의 정보를 설명합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: 이 관측에 해당하는 센서 디바이스/스테이션의 디바이스 이름 또는 스테이션 이름입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 폐기물 관리 차량에 있는 기기의 심 번호를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 디바이스가 감지/관찰/측정하는 속성/특성  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: RFID 리더의 ID를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `femaleTotal[number]`: 장치에서 식별한 특정 종의 암컷 총 개수입니다.  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maleTotal[number]`: 장치에서 식별한 특정 종의 수컷 총 개수입니다.  - `mosquitoDensity[object]`: 이 관찰에 해당하는 장치로 식별한 모기 종의 이항 (또는) 동물학적 명명법과 그 수입니다.  	- `femaleSpeciesCount[number]`: 장치에서 식별한 종의 암컷 모기의 총 개수입니다.    
	- `maleSpeciesCount[number]`: 장치에서 식별한 종의 수컷 모기의 총 개수입니다.    
	- `mosquitoSpecies[string]`: 기기에 의해 식별된 모기 종의 이항/동물학적 명명법    
	- `totalSpeciesCount[number]`: 장치가 감지한 특정 종의 총 개수입니다.    
- `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `precipitation[number]`: 주어진 기간 동안 관측된 강수량/강우량 수준  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 일련의 문자입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `speciesName[string]`: 장치에서 식별한 종의 이항식/동물학적 명명법.  - `speciesTotal[number]`: 장치에서 감지한 특정 종의 총 개수입니다.  - `type[string]`: NGSI 엔티티 유형. MosquitoDensity여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
      averageValue:    
        description: Property. Average value of temporal processing over time    
        type: number    
      description: Observed value of air temperature. Value is an object containing attributes representing statistical aggregates derived from past data    
      instValue:    
        description: Property. Instant value of temporal processing    
        type: number    
      maxOverTime:    
        description: Property. Maximum value of temporal processing over time    
        type: number    
      minOverTime:    
        description: Property. Minimum value of temporal processing over time    
        type: number    
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
    deviceId:    
      description: Device ID of the physical sensor/ measurement station corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deviceSimNumber:    
      description: Gives the sim number of the device in the waste management vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    femaleTotal:    
      description: 'The total count of females of a particular species, as identified by the device.'    
      type: number    
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
    maleTotal:    
      description: 'The total count of males of a particular species, as identified by the device.'    
      type: number    
      x-ngsi:    
        type: Property    
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
    speciesName:    
      description: The binomial/ zoological nomenclature of the species identified by the device.    
      type: string    
      x-ngsi:    
        type: Property    
    speciesTotal:    
      description: 'The total count of a particular species, as detected by the device.'    
      type: number    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/MosquitoDensity/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### MosquitoDensity NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 모기 밀도 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": "VDFWitw@B",  
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
    "measurand": "6",  
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
#### MosquitoDensity NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 모기 밀도 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": {  
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
    "type": "Number",  
    "value": 1  
  },  
  "observationDateTime": {  
    "type": "Date-Time",  
    "value": "2022-09-18T23:59:59+05:30"  
  },  
  "airTemperature": {  
    "type": "StructuredValue",  
    "value": {  
      "instValue": 24.88  
    }  
  },  
  "precipitation": {  
    "type": "Number",  
    "value": 0  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "measurand": "6",  
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
#### MosquitoDensity NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 모기 밀도를 키 값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": "VDFWitw@B",  
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
    "measurand": "6",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MosquitoDensity NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 모기 밀도 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/MosquitoDensity/schema.json",  
  "type": "MosquitoDensity",  
  "deviceID": {  
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
    "value": 1  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
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
    "value": 0  
  },  
  "deviceInfo": {  
    "type": "Property",  
    "value": {  
      "rfID": "5634684",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "SL1",  
      "measurand": "6",  
      "deviceModel": {  
        "brandName": "abc",  
        "manufacturerName": "xyz",  
        "modelName": "SL1",  
        "modelURL": "www.abcstreetlight.com"  
      }  
    }  
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
크기 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
