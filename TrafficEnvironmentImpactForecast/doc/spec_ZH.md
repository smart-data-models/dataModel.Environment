<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：交通环境影响预测  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：基于车辆交通预期及其排放特征的**交通对环境的影响**  
版本： 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: 预计的二氧化碳排放浓度  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateIssued[date-time]`: 服务提供商以 ISO8601 UTC 格式发布预报的日期和时间  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `traffic[array]`: 包含不同车辆类型的强度、占用率和速度预期值的对象数组  - `type[string]`: NGSI 类型。必须是 TrafficEnvironmentImpactForecast  - `validFrom[date-time]`: 该预报有效期的起始时间（ISO8601 格式  - `validTo[date-time]`: ISO8601 格式的预报有效期结束时间  - `validity[string]`: 包括作为 ISO8601 时间间隔的预报有效期  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
## 有效载荷示例  
#### 交通环境影响预测 NGSI-v2 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 TrafficEnvironmentImpactForecast 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 交通环境影响预测 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 TrafficEnvironmentImpactForecast 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 交通环境影响预测 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的交通环境影响预测示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 交通环境影响预测 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 TrafficEnvironmentImpactForecast 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
