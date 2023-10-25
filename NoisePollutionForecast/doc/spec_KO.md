<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: NoisePollutionForecast  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **소음 공해 예측은 일부 입력 요소와 존재하는 소음 요소를 기반으로 소음 공해에 대한 예상치를 저장합니다.**  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `LANight[number]`: 밤 동안 녹음된 평균 소음 수준(8시간)  - `LAeq[number]`: 측정 시간 동안 기록된 평균 소음 수준(등가)  - `LAeq2[number]`: 지난 2시간 동안의 평균 소음 수준  - `LAeq_d[number]`: 낮 동안의 평균 소음 수준(8시간)  - `LAmax[number]`: 측정 시간 동안 녹음된 최대 소음 수준  - `LAmax2[number]`: 지난 2시간 동안 녹음된 최대 소음 수준  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateIssued[date-time]`: 서비스 제공업체가 예보를 발행한 날짜와 시간(ISO8601 UTC 형식)  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `noiseAnnoyanceIndex[number]`: 소음 성가심 정도에 따른 지수(1~10)  - `noiseOrigin[string]`: 센서 설치 시 기록된 노이즈의 주요 발생지(소스)  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 유형. 노이즈 오염 예보 유형이어야 합니다.  - `validFrom[date-time]`: ISO8601 형식으로 이 예측의 유효 기간 시작일  - `validTo[date-time]`: ISO8601 형식으로 이 예측의 유효 기간 종료일  - `validity[string]`: 이 예측의 유효 기간을 ISO8601 시간 간격으로 포함합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoisePollutionForecast:    
  description: Noise Pollution forecast stores the expectation about noise pollution based on some input elements and the noise elements present.    
  properties:    
    LANight:    
      description: Average sound level recorded during the night (8h)    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq:    
      description: Average sound level (equivalent) recorded during the measuring time    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq2:    
      description: Average sound level over the last 2 hours    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq_d:    
      description: Average sound level during the day (8h)    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax:    
      description: Maximum sound level recorded during the measuring time    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax2:    
      description: Maximum sound level recorded for the last 2 hours    
      type: number    
      x-ngsi:    
        type: Property    
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
    noiseAnnoyanceIndex:    
      description: Index (1 to 10) according to noise annoyance level    
      maximum: 10    
      minimum: 1    
      type: number    
      x-ngsi:    
        type: Property    
    noiseOrigin:    
      description: Main origin (source) of the recorded noise at installation of the sensor    
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
    type:    
      description: NGSI type. It has to be NoisePollutionForecast    
      enum:    
        - NoisePollutionForecast    
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
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollutionForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollutionForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### NoisePollutionForecast NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 소음 오염 예보의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": "2022-07-22T17:37:38Z",  
  "dateModified": "2022-10-22T02:05:56Z",  
  "source": "",  
  "name": "forecast",  
  "alternateName": "",  
  "description": "forecast tomorrow",  
  "dataProvider": "service online Nice",  
  "owner": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
    "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
    "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ]  
  },  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "areaServed": "",  
  "noiseAnnoyanceIndex": 3.8,  
  "LANight": 32.9,  
  "LAmax2": 70.3,  
  "LAeq2": 67.8,  
  "noiseOrigin": "",  
  "LAeq": 39.2,  
  "LAeq_d": 66.2,  
  "LAmax": 74.7,  
  "validFrom": "2022-08-23T05:35:35Z",  
  "validTo": "2022-08-24T05:35:35Z",  
  "validity": "P1D",  
  "dateIssued": "2022-08-23T05:05:35Z"  
}  
```  
</details>  
#### NoisePollutionForecast NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 노이즈 오염 예보의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": {  
    "type": "date-time",  
    "value": "2022-07-22T17:37:38Z"  
  },  
  "dateModified": {  
    "type": "date-time",  
    "value": "2022-10-22T02:05:56Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "forecast"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "forecast tomorrow"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "service online Nice"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
      "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
      "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
    ]  
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
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "France",  
      "addressLocality": "Nice",  
      "postalCode": "06200",  
      "type": "PostalAddress"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "noiseAnnoyanceIndex": {  
    "type": "Number",  
    "value": 3.8  
  },  
  "LANight": {  
    "type": "Number",  
    "value": 32.9  
  },  
  "LAmax2": {  
    "type": "Number",  
    "value": 70.3  
  },  
  "LAeq2": {  
    "type": "Number",  
    "value": 67.8  
  },  
  "noiseOrigin": {  
    "type": "Text",  
    "value": ""  
  },  
  "LAeq": {  
    "type": "Number",  
    "value": 39.2  
  },  
  "LAeq_d": {  
    "type": "Number",  
    "value": 66.2  
  },  
  "LAmax": {  
    "type": "Number",  
    "value": 74.7  
  },  
  "validFrom": {  
    "type": "date-time",  
    "value": "2022-08-23T05:35:35Z"  
  },  
  "validTo": {  
    "type":  "date-time",  
    "value": "2022-08-24T05:35:35Z"  
  },  
  "validity": {  
    "type": "Text",  
    "value": "P1D"  
  },  
  "dateIssued": {  
    "type": "date-time",  
    "value": "2022-08-23T05:05:35Z"  
  }  
}  
```  
</details>  
#### NoisePollutionForecast NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 소음 오염 예보의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
    "type": "NoisePollutionForecast",  
    "dateCreated": "2022-07-22T17:37:38Z",  
    "dateModified": "2022-10-22T02:05:56Z",  
    "source": "",  
    "name": "forecast",  
    "alternateName": "",  
    "description": "forecast tomorrow",  
    "dataProvider": "service online Nice",  
    "owner": [  
        "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
        "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
        "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            7.2032497427380235,  
            43.68056738083439  
        ]  
    },  
    "address": {  
        "addressCountry": "France",  
        "addressLocality": "Nice",  
        "postalCode": "06200",  
        "type": "PostalAddress"  
    },  
    "areaServed": "",  
    "noiseAnnoyanceIndex": 3.8,  
    "LANight": 32.9,  
    "LAmax2": 70.3,  
    "LAeq2": 67.8,  
    "noiseOrigin": "",  
    "LAeq": 39.2,  
    "LAeq_d": 66.2,  
    "LAmax": 74.7,  
    "validFrom": "2022-08-23T05:35:35Z",  
    "validTo": "2022-08-24T05:35:35Z",  
    "validity": "P1D",  
    "dateIssued": "2022-08-23T05:05:35Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### NoisePollutionForecast NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 소음 오염 예보의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollutionForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollutionForecast",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-07-22T17:37:38Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-10-22T02:05:56Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "forecast"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "forecast tomorrow"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "service online Nice"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:IIZN:71750066",  
      "urn:ngsi-ld:NoisePollutionForecast:items:HKJD:09603525"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NoisePollutionForecast:items:UYHN:79392420",  
      "urn:ngsi-ld:NoisePollutionForecast:items:VCCQ:21243558"  
    ]  
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
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "France",  
      "addressLocality": "Nice",  
      "postalCode": "06200",  
      "type": "PostalAddress"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "noiseAnnoyanceIndex": {  
    "type": "Property",  
    "value": 3.8  
  },  
  "LANight": {  
    "type": "Property",  
    "value": 32.9  
  },  
  "LAmax2": {  
    "type": "Property",  
    "value": 70.3  
  },  
  "LAeq2": {  
    "type": "Property",  
    "value": 67.8  
  },  
  "noiseOrigin": {  
    "type": "Property",  
    "value": ""  
  },  
  "LAeq": {  
    "type": "Property",  
    "value": 39.2  
  },  
  "LAeq_d": {  
    "type": "Property",  
    "value": 66.2  
  },  
  "LAmax": {  
    "type": "Property",  
    "value": 74.7  
  },  
  "validFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-23T05:35:35Z"  
    }  
  },  
  "validTo": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-24T05:35:35Z"  
    }  
  },  
  "validity": {  
    "type": "Property",  
    "value": "P1D"  
  },  
  "dateIssued": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-08-23T05:05:35Z"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
