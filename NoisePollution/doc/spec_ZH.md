<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：噪音污染    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollution/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**噪声污染数据模型将具体和准时的噪声测量值（如来自噪声级观测实体的测量值）合并为城市地区的平均参数，提供更多与城市相关的噪声污染状况和演变数据。    
版本： 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `LAeq2[number]`: 过去 2 小时的平均声级  - `LAmax2[number]`: 最近 2 小时记录的最大声级  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `buildingsType[string]`: 安装传感器时测量区域内主要建筑物的类型  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObservedFrom[date-time]`: 观察期开始日期和时间  - `dateObservedTo[date-time]`: 观察期的结束日期和时间  - `description[string]`: 项目描述  - `groundType[string]`: 安装传感器时测量区域的主要地面类型  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `noiseAnnoyanceIndex[number]`: 根据噪音干扰程度划分的指数（1 至 10  - `noiseOrigin[string]`: 安装传感器时记录噪音的主要来源（源头  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须是 NoisePollution（噪声污染）类型。  - `wallsType[string]`: 安装传感器时测量区域的主要外墙材料类型  <!-- /30-PropertiesList -->    
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
NoisePollution:      
  description: 'Noise Pollution data model merges specific and punctual noise measurements (coming, e.g. from NoiseLevelObservation entities) into average parameters referred to city areas, providing a more city-related data about noise pollution status and evolution.'      
  properties:      
    LAeq2:      
      description: Average sound level over the last 2 hours      
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
    buildingsType:      
      description: Type of predominant buildings within the measurement area at installation of the sensor      
      type: string      
      x-ngsi:      
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
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObservedFrom:      
      description: Observation period start date and time      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObservedTo:      
      description: End date and time of the observation period      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    groundType:      
      description: Type of predominant ground in the measurement area at installation of the sensor      
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
        - bbox:      
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
        - bbox:      
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
        - bbox:      
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
        - bbox:      
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
        - bbox:      
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
        - bbox:      
            items:      
              type: number      
            minItems: 4      
            type: array      
          coordinates:      
            items:      
              items:      
                items:      
                  items:      
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
      description: NGSI type. it has to be NoisePollution      
      enum:      
        - NoisePollution      
      type: string      
      x-ngsi:      
        type: Property      
    wallsType:      
      description: Facade material types dominant in the measurement area at installation of the sensor      
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
  x-model-tags: GreenMov      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### 噪声污染 NGSI-v2 关键值示例    
下面是一个以 JSON-LD 格式作为键值的 NoisePollution 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
  "wallsType": "glass"  
}  
```  
</details>    
#### 噪声污染 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 NoisePollution 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
    "type": "Text",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
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
    "type": "Text",  
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
#### 噪声污染 NGSI-LD 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 NoisePollution 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 噪声污染 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 NoisePollution 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
