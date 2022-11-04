<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。实验性的观察  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该数据模型旨在通过固定或移动监测系统，测量、观察和控制特定时间（T）的地下水位和质量。根据所使用的设备，也可以测量水的质量，如其电导率、盐含量、温度等。在这种情况下，测量的数值由数据模型`WaterObserved`和`WaterQualityObserved`处理。关于属性的附加信息。对于专用于水的属性，也可以使用MetaData属性。它包含以秒为单位的 "时间戳"，测量的 "资格 "和控制 "状态 "**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 该观察的日期和时间，采用ISO8601 UTC格式  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[string]`: 观察期 :开始日期和时间为ISO8601 UTC格式  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: 观察期 :结束日期和时间为ISO8601 UTC格式  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `depth[number]`: 饮用水的深度，自其识别`waterTable`。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。例如，<code>MTR</code>代表米。  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `investigationDepth[number]`: 进行调查的最大深度。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。例如，<code>MTR</code>代表米  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `isMobile[boolean]`: 使用的设备是固定式（假）或移动式（真）。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `measurementType[array]`: 观察期:处理的测量类型。Enum:'深度、体积、质量、其他'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pollutionRate[number]`: 污染率。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。例如，P1代表百分比。  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[number]`: 水压。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。例如，<code>BAR</code>代表Bar。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refDevice[array]`: 参考提供数据的设备  . Model: [https://scehma.org/URL](https://scehma.org/URL)- `residueLevel[number]`: 发现的残留物水平  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是PhreaticObserved  - `waterTable[number]`: 在本次调查中发现的水位。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。例如，<code>MTR</code>代表米。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `measurementType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhreaticObserved:    
  description: 'The Data Model is intended to measure, observe and control the level and quality of groundwater at a given time (T), by a fixed or mobile monitoring system. Depending on the device used, it is also possible to measure the quality of water such as its electrical conductivity, its salt content, its temperature, etc. In this case, the values measured are processed by the Data Model `WaterObserved` and `WaterQualityObserved`. Additional Information about Attributes: For attributes dedicated to water, a MetaData attribute can also be used. it contains the `TimeStamp` in seconds, the `qualification` and control `status` of the measurement.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    depth:    
      description: 'Depth of drinking water, since its identification `waterTable`. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code> MTR </code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &phreaticobserved_-_properties_-_owner_-_items_-_anyof    
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
    investigationDepth:    
      description: 'Maximum depth where the investigation was made. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: meters    
    isMobile:    
      description: 'The device used is Fixed (False) or Mobile (True)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    measurementType:    
      description: 'Observation period : Type of measurement processed. Enum:''depth, volume, quality, other'''    
      items:    
        enum:    
          - depth    
          - volume    
          - quality    
          - other    
        type: string    
      minItems: 0    
      type: array    
      uniqueItems: false    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pollutionRate:    
      description: 'Rate of pollution. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, P1 represents Percentage.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressure:    
      description: 'Water Pressure. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>BAR</code> represents Bar.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Bar    
    refDevice:    
      description: 'Reference to the devices providing data'    
      items:    
        anyOf: *phreaticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://scehma.org/URL    
        type: Relationship    
    residueLevel:    
      description: 'Residue level found'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
      description: 'NGSI Entity type. It has to be PhreaticObserved'    
      enum:    
        - PhreaticObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterTable:    
      description: 'Level at which water was found during this investigation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - measurementType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### PhreaticObserved NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的PhreaticObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": "STLRT-MNCA-NP-015",  
  "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Airport",  
  "dateObserved": "2020-07-07T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-NP-015"  
  ],  
  "isMobile": false,  
  "measurementType": [  
    "depth",  
    "volume"  
  ],  
  "investigationDepth": 22.35,  
  "waterTable": 12.75,  
  "depth": 20.45,  
  "pressure": 2.12  
}  
```  
</details>  
#### PhreaticObserved NGSI-v2归一化实例  
下面是一个以JSON-LD格式规范化的PhreaticObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
	"type": "PhreaticObserved",  
	"name": {  
		"type": "Property",  
		"value": "STLRT-MNCA-NP-015"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
	},  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [43.664810, 7.196545]  
        }  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Airport"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:Device:T1-NP-015"]  
	},  
	"isMobile": {  
		"type": "Property",  
		"value": false  
	},  
	"measurementType": {  
		"type": "Property",  
		"value": ["depth", "volume"]  
	},  
	"investigationDepth": {  
		"type": "Property",  
		"value": 22.35  
	},  
	"waterTable": {  
		"type": "Property",  
		"value": 12.75,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 2"  
		}  
	},  
	"depth": {  
		"type": "Property",  
		"value": 20.45,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"type": "Property",  
			"value": "Incorrect"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 1"  
		}  
	},  
	"pressure": {  
		"type": "Property",  
		"value": 2.12,  
		"observedAt": "2020-03-17TT08:45:00Z",  
		"qualification": {  
			"value": "Correct"  
		},  
		"status ": {  
			"type": "Property",  
			"value": "Level 3"  
		}  
	}  
}  
```  
</details>  
#### PhreaticObserved NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为key-values的PhreaticObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
    "type": "PhreaticObserved",  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Airport"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-07-07T15:05:59.408Z"  
        }  
    },  
    "depth": {  
        "type": "Property",  
        "value": 20.45,  
        "observedAt": "2020-03-17TT08:45:00Z",  
        "qualification": {  
            "type": "Property",  
            "value": "Incorrect"  
        },  
        "status ": {  
            "type": "Property",  
            "value": "Level 1"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
    },  
    "investigationDepth": {  
        "type": "Property",  
        "value": 22.35  
    },  
    "isMobile": {  
        "type": "Property",  
        "value": false  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "measurementType": {  
        "type": "Property",  
        "value": [  
            "depth",  
            "volume"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "STLRT-MNCA-NP-015"  
    },  
    "pressure": {  
        "type": "Property",  
        "value": 2.12,  
        "observedAt": "2020-03-17TT08:45:00Z",  
        "qualification": {  
            "value": "Correct"  
        },  
        "status ": {  
            "type": "Property",  
            "value": "Level 3"  
        }  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "Object": [  
            "urn:ngsi-ld:Device:T1-NP-015"  
        ]  
    },  
    "waterTable": {  
        "type": "Property",  
        "value": 12.75,  
        "observedAt": "2020-03-17TT08:45:00Z",  
        "qualification": {  
            "type": "Property",  
            "value": "Correct"  
        },  
        "status ": {  
            "type": "Property",  
            "value": "Level 2"  
        }  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PhreaticObserved NGSI-LD归一化实例  
下面是一个以JSON-LD格式规范化的PhreaticObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
    "type": "PhreaticObserved",  
    "areaServed": "Nice Airport",  
    "dateObserved": "2020-07-07T15:05:59.408Z",  
    "depth": 20.45,  
    "description": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var.",  
    "investigationDepth": 22.35,  
    "isMobile": false,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "measurementType": [  
        "depth",  
        "volume"  
    ],  
    "name": "STLRT-MNCA-NP-015",  
    "pressure": 2.12,  
    "refDevice": [  
        "urn:ngsi-ld:Device:T1-NP-015"  
    ],  
    "waterTable": 12.75,  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
