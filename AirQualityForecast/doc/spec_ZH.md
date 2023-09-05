<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：空气质量预报  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：空气质量状况预报** 在一段时期内有效**  
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
- `airQualityIndex[number]`: 空气质量指数是用来报告任何一天的空气质量的数字  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: 与观察到的空气质量相对应的健康问题的总体定性水平  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: 二氧化碳预测值  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `no2[number]`: 二氧化氮预测  - `nox[number]`: 其他氮氧化物预测  - `o3[number]`: 臭氧预报  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pm10[number]`: 直径为 10 微米或以下的颗粒物  - `pm25[number]`: 直径为 2.5 微米或以下的颗粒物  - `precipitation[number]`: 雨水量  . Model: [https://schema.org/Number](https://schema.org/Number)- `relativeHumidity[number]`: 空气湿度  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `so2[number]`: 检测到二氧化硫  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `temperature[number]`: 物品的温度  - `type[string]`: NGSI 实体类型：必须是 AirQualityForecast  - `validFrom[date-time]`: 该预报有效期的起始时间（ISO8601 格式  - `validTo[date-time]`: ISO8601 格式的预报有效期结束时间  - `validity[string]`: 包括作为 ISO8601 时间间隔的预报有效期  . Model: [https://schema.org/Text](https://schema.org/Text)- `windSpeed[number]`: 风的强度  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
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
AirQualityForecast:    
  description: A forecast of air quality conditions valid during a period    
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
    airQualityIndex:    
      description: Air quality index is a number used to report the quality of the air on any given day    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityLevel:    
      description: Overall qualitative level of health concern corresponding to the air quality observed    
      minLength: 2    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Carbon Dioxide forecasted    
      minimum: 0    
      type: number    
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
    no2:    
      description: Nitrogen dioxide forecasted    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    nox:    
      description: Other Nitrogen oxides forecasted    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    o3:    
      description: Ozone forecasted    
      minimum: 0    
      type: number    
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
    pm10:    
      description: Particulate matter 10 micrometers or less in diameter    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm25:    
      description: Particulate matter 2.5 micrometers or less in diameter    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: Amount of water rain    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter    
    relativeHumidity:    
      description: Humidity in the Air    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    so2:    
      description: Sulfur dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Temperature of the item    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type: it has to be AirQualityForecast'    
      enum:    
        - AirQualityForecast    
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
    windSpeed:    
      description: Intensity of the wind    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### AirQualityForecast NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 AirQualityForecast 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 3,  
  "airQualityLevel": "moderate",  
  "co2": 45,  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateIssued": "2022-07-01T10:40:01.00Z",  
  "dateRetrieved": "2022-07-01T12:57:24.00Z",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "no2": 69,  
  "nox": 139,  
  "o3": 100,  
  "pm10": 19,  
  "pm25": 21,  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "so2": 11,  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "validFrom": "2022-07-01T17:00:00.00Z",  
  "validTo": "2022-07-01T18:00:00.00Z",  
  "validity": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00",  
  "windSpeed": 0.64  
}  
```  
</details>  
#### AirQualityForecast NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 AirQualityForecast 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice"  
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
  "dateIssued": {  
    "type": "DateTime",  
    "value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateRetrieved": {  
    "type": "DateTime",  
    "value": "2022-07-01T12:57:24.00Z"  
  },  
  "validFrom": {  
    "type": "DateTime",  
    "value": "2022-07-01T17:00:00.00Z"  
  },  
  "validTo": {  
    "type": "DateTime",  
    "value": "2022-07-01T18:00:00.00Z"  
  },  
  "validity": {  
    "type": "Text",  
    "value": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00"  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 3  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "moderate"  
  },  
  "co2": {  
    "type": "Number",  
    "value": 45,  
    "unitCode": "GQ"  
  },  
  "no2": {  
    "type": "Number",  
    "value": 69,  
    "unitCode": "GQ"  
  },  
  "o3": {  
    "type": "Number",  
    "value": 100,  
    "unitCode": "GQ"  
  },  
  "nox": {  
    "type": "Number",  
    "value": 139,  
    "unitCode": "GQ"  
  },  
  "so2": {  
    "type": "Number",  
    "value": 11,  
    "unitCode": "GQ"  
  },  
  "pm10": {  
    "type": "Number",  
    "value": 19,  
    "unitCode": "GQ"  
  },  
  "pm25": {  
    "type": "Number",  
    "value": 21,  
    "unitCode": "GQ"  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 12.2  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.54  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 0.64  
  },  
  "precipitation": {  
    "type": "Number",  
    "value": 0  
  },  
  "typeOfLocation": {  
    "type": "Text",  
    "value": "outdoor"  
  }  
}  
```  
</details>  
#### AirQualityForecast NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 AirQualityForecast 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 3,  
  "airQualityLevel": "moderate",  
  "co2": 45,  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateIssued": "2022-07-01T10:40:01.00Z",  
  "dateRetrieved": "2022-07-01T12:57:24.00Z",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "no2": 69,  
  "nox": 139,  
  "o3": 100,  
  "pm10": 19,  
  "pm25": 21,  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "so2": 11,  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "validFrom": "2022-07-01T17:00:00.00Z",  
  "validTo": "2022-07-01T18:00:00.00Z",  
  "validity": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00",  
  "windSpeed": 0.64,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AirQualityForecast NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 AirQualityForecast 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "AirQualityForecast",  
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
  "dateIssued": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T10:40:01.00Z"  
    }  
  },  
  "dateRetrieved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T12:57:24.00Z"  
    }  
  },  
  "validFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T17:00:00.00Z"  
    }  
  },  
  "validTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T18:00:00.00Z"  
    }  
  },  
  "validity": {  
    "type": "Property",  
    "value": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00"  
  },  
  "airQualityIndex": {  
    "type": "Property",  
    "value": 3  
  },  
  "airQualityLevel": {  
    "type": "Property",  
    "value": "moderate"  
  },  
  "co2": {  
    "type": "Property",  
    "value": 45,  
    "unitCode": "GQ"  
  },  
  "no2": {  
    "type": "Property",  
    "value": 69,  
    "unitCode": "GQ"  
  },  
  "o3": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "GQ"  
  },  
  "nox": {  
    "type": "Property",  
    "value": 139,  
    "unitCode": "GQ"  
  },  
  "so2": {  
    "type": "Property",  
    "value": 11,  
    "unitCode": "GQ"  
  },  
  "pm10": {  
    "type": "Property",  
    "value": 19,  
    "unitCode": "GQ"  
  },  
  "pm25": {  
    "type": "Property",  
    "value": 21,  
    "unitCode": "GQ"  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 12.2  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.54  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 0.64  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 0  
  },  
  "typeOfLocation": {  
    "type": "Property",  
    "value": "outdoor"  
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
