<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：室内环境观测  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/IndoorEnvironmentObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**观测室内环境的空气和气候条件。  
版本： 0.0.1  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: 测量的大气压力  - `co2[number]`: 测得的室内 C02 浓度（单位：毫克/升  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[string]`: ISO8601 中的观测日期和时间  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `illuminance[number]`: 测量照度  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `peopleCount[number]`: 房间人数  - `refDevice[*]`: 捕捉这一观测结果的设备的参考信息  - `refPointOfInterest[*]`: 与该观测点相关的兴趣点参考文献  - `relativeHumidity[number]`: 测量湿度  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `sensorHeight[number]`: 传感器高度（与地面的距离）  - `sensorPlacement[string]`: 传感器的位置  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `temperature[number]`: 测量温度  - `type[string]`: NGSI 实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
IndoorEnvironmentObserved:    
  description: An observation of air and climate conditions for indoor environments.    
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
    atmosphericPressure:    
      description: Measured atmospheric pressure    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co2:    
      description: The measured interior C02 concentration nominally in mg/L    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg per liter    
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
    dateObserved:    
      description: Date and time of the observation in ISO8601    
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
    illuminance:    
      description: Measured illuminance    
      minimum: 0    
      type: number    
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
    peopleCount:    
      description: Number of people in the room    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    refDevice:    
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
      description: A reference to the device(s) which captured this observation    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
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
      description: A reference to a point of interest associated to this observation    
      x-ngsi:    
        type: Relationship    
    relativeHumidity:    
      description: Measured humidity    
      minimum: 0    
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
    sensorHeight:    
      description: Height of the sensor (distance from the floor)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    sensorPlacement:    
      description: Position of the sensor    
      enum:    
        - northWall    
        - southWall    
        - eastWall    
        - westWall    
        - center    
        - floor    
        - roof    
        - ceiling    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Measured temperature    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type    
      enum:    
        - IndoorEnvironmentObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/IndoorEnvironmentObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/dataModel.Environment/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### IndoorEnvironmentObserved NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 IndoorEnvironmentObserved 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
        "id": "urn:ngsi:MuseoDemo_Room_1",  
        "type": "IndoorEnvironmentObserved",  
        "dateObserved": "2020-06-08T17:54:00",  
        "refPointOfInterest": "urn:ngsi:MuseoDemo",  
        "address": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address"  
        },  
        "location": {  
            "type": "Point",  
            "coordinates": [  
                40,  
                11  
            ]  
        },  
        "peopleCount": 10,  
        "temperature": 12.2,  
        "relativeHumidity": 0.54,  
        "atmosphericPressure": 1013.52,  
        "illuminance": 1000,  
        "CO": 500,  
        "NO": 45,  
        "NO2": 69,  
        "NOx": 139,  
        "SO2": 11  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-v2 normalized 示例  
下面是一个规范化 JSON-LD 格式的 IndoorEnvironmentObserved 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "dateObserved": {  
        "value": "2020-06-08T17:54:00"  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "value": "urn:ngsi:MuseoDemo"  
    },  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [40, 11]  
        }  
    },  
    "address": {  
        "type": "PostalAddress",  
        "value": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address"  
        }  
    },  
    "peopleCount": {  
        "value": 10  
    },  
    "temperature": {  
        "value": 12.2,  
        "metadata": {  
            "unitCode": {  
                "value": "CEL"  
            }  
        }  
    },  
    "relativeHumidity": {  
        "value": 0.54,  
        "metadata": {  
            "unitCode": {  
                "value": "P1"  
            }  
        }  
    },  
    "illuminance": {  
        "value": 1000,  
        "metadata": {  
            "unitCode": {  
                "value": "LX"  
            }  
        }  
    },  
    "CO": {  
        "value": 500,  
        "metadata": {  
            "unitCode": {  
                "value": "GP"  
            }  
        }  
    },  
    "NO": {  
        "value": 45,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "NOx": {  
        "value": 139,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "NO2": {  
        "value": 69,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    },  
    "SO2": {  
        "value": 11,  
        "metadata": {  
            "unitCode": {  
                "value": "GQ"  
            }  
        }  
    }  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-LD 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 IndoorEnvironmentObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
  "type": "IndoorEnvironmentObserved",  
  "CO": 500,  
  "NO": 45,  
  "NO2": 69,  
  "NOx": 139,  
  "SO2": 11,  
  "address": {  
    "addressCountry": "IT",  
    "addressLocality": "Demo city",  
    "streetAddress": "Demo address",  
    "type": "PostalAddress"  
  },  
  "dateObserved": "2016-03-15T11:00:00/2016-03-15T12:00:00",  
  "illuminance": 1000,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40,  
      11  
    ]  
  },  
  "peopleCount": 10,  
  "refPointOfInterest": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo",  
  "relativeHumidity": 0.54,  
  "temperature": 12.2,  
  "@context": [  
    "https://fiware.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### IndoorEnvironmentObserved NGSI-LD normalized 示例  
下面是一个规范化的 JSON-LD 格式的 IndoorEnvironmentObserved 示例。在不使用选项的情况下，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:IndoorEnvironmentObserved:urn:ngsi:MuseoDemo_Room_1",  
    "type": "IndoorEnvironmentObserved",  
    "CO": {  
        "type": "Property",  
        "value": 500,  
        "unitCode": "GP"  
    },  
    "NO": {  
        "type": "Property",  
        "value": 45,  
        "unitCode": "GQ"  
    },  
    "NO2": {  
        "type": "Property",  
        "value": 69,  
        "unitCode": "GQ"  
    },  
    "NOx": {  
        "type": "Property",  
        "value": 139,  
        "unitCode": "GQ"  
    },  
    "SO2": {  
        "type": "Property",  
        "value": 11,  
        "unitCode": "GQ"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "IT",  
            "addressLocality": "Demo city",  
            "streetAddress": "Demo address",  
            "type": "PostalAddress"  
        }  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-03-15T11:00:00/2016-03-15T12:00:00"  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 1000  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                40,  
                11  
            ]  
        }  
    },  
    "peopleCount": {  
        "type": "Property",  
        "value": 10  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:PointOfInterest:urn:ngsi:MuseoDemo"  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.54  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12.2  
    },  
    "@context": [  
        "https://fiware.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld",  
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
