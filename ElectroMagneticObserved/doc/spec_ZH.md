<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。电磁波观测  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/ElectroMagneticObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该数据模型旨在根据空气中电磁场的暴露程度，测量工作或公共环境中过量的电场和磁场（EMF），或辐射。赫兹波的频率传统上低于300GHz，在空间传播时没有人工引导。它们在9千赫兹和300吉赫兹之间**。  
版本：0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 该观测的日期和时间，以ISO8601 UTC格式表示。它可以用一个特定的时间瞬间来表示，也可以用一个ISO8601间隔来分隔属性`dateObservedFrom`、`dateObservedTo`。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[string]`: 观察期。ISO8601 UTC格式的开始日期和时间。当该属性与要突出显示的时间间隔相对应时，可以与`dateObserved`属性一起使用。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: 观察期。ISO8601 UTC格式的结束日期和时间。当该属性与要突出显示的时间间隔相对应时，可以与`dateObserved`属性一起使用。  . Model: [https://schema.org/](https://schema.org/)- `description[string]`: 对这个项目的描述  - `eMF[number]`: 与观察调查相对应的水平。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MHz**代表百万赫兹。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refDevice[*]`: 参考一个[设备](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)，它记录了这一观察结果。  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: 参考与观察有关的[兴趣点](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)。  . Model: [https://schema.org/URL](https://schema.org/URL)- `reliability[number]`: 百分比为置信系数。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**P1**代表百分比。  . Model: [https://schema.org/](https://schema.org/)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 它必须是ElectroMagneticObserved  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `eMF`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ElectroMagneticObserved:    
  description: 'The Data Model is intended to measure excessive electric and magnetic fields (EMFs), or radiation in a work or public environment according to the level of exposure to electromagnetic fields on the air. The frequency of the hertzian waves is conventionally lower than 300 GHz, propagating in space without artificial guide. They are between 9 kHz and 300 GHz.'    
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
      description: 'Date and time of this observation represented by an ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval to separate attributes `dateObservedFrom`, `dateObservedTo`. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    eMF:    
      description: 'Level corresponding to the observed survey. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MHz** represents Mega Hertz. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &electromagneticobserved_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *electromagneticobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which captured this observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [Point Of Interest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reliability:    
      description: 'Percent for confidence Factor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent. '    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/    
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
      description: 'It has to be ElectroMagneticObserved'    
      enum:    
        - ElectroMagneticObserved    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - eMF    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/ElectroMagneticObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Environment/ElectroMagneticObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ElectroMagneticObserved NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的ElectroMagneticObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": "MNCA-EM-018",  
  "alternateName": "AirPort  global Observation",  
  "description": "EMF observation",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Terminal 2 - Parking 7"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-T2-P7-EM03",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "eMF": 950.12,  
  "observedAt": "2020-03-17TT08:45:00Z",  
  "measurementType": "Instant",  
  "measurementInterval": 1,  
  "reliability": 0.993  
}  
```  
</details>  
#### ElectroMagneticObserved NGSI-v2 normalized Example  
下面是一个以JSON-LD格式规范化的ElectroMagneticObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
  "type": "ElectroMagneticObserved",  
  "name": {  
    "type": "Property",  
    "value": "MNCA-EM-018"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort SPA global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "EMF observation"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Terminal 2 - Parking 7"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:NCE-T2-P7-EM03"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "eMF": {  
    "type": "Property",  
    "value": 950.12,  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "Instant"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "reliability": {  
    "type": "Property",  
    "value": 0.993  
  }  
}  
```  
</details>  
#### ElectroMagneticObserved NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的ElectroMagneticObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
    "type": "ElectroMagneticObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Terminal 2 - Parking 7"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort \u0096 global Observation"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "EMF observation"  
    },  
    "eMF": {  
        "type": "Property",  
        "value": 950.12,  
        "observedAt": "2020-03-17TT08:45:00Z",  
        "measurementType": {  
            "type": "Property",  
            "value": "Instant"  
        },  
        "measurementInterval": {  
            "type": "Property",  
            "value": 1  
        }  
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
    "name": {  
        "type": "Property",  
        "value": "MNCA-EM-018"  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:NCE-T2-P7-EM03"  
    },  
    "reliability": {  
        "type": "Property",  
        "value": 0.993  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ElectroMagneticObserved NGSI-LD normalized Example  
这里是一个以JSON-LD格式规范化的ElectroMagneticObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ElectroMagneticObserved:ElectroMagneticObserved:MNCA-EM-018",  
    "type": "ElectroMagneticObserved",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Terminal 2 - Parking 7"  
    },  
    "alternateName": "AirPort global Observation",  
    "areaServed": "Nice Aeroport",  
    "dateObserved": "2020-03-17T08:45:00Z",  
    "description": "EMF observation",  
    "eMF": 950.12,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "measurementInterval": 1,  
    "measurementType": "Instant",  
    "name": "MNCA-EM-018",  
    "observedAt": "2020-03-17TT08:45:00Z",  
    "refDevice": "urn:ngsi-ld:Device:NCE-T2-P7-EM03",  
    "reliability": 0.993,  
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
