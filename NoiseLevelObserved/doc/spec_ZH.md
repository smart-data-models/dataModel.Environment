<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。观察到的噪音水平（NoiseLevelObserved  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/NoiseLevelObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**对那些估计某一地点和时间的噪声压力水平的声学参数的观察。**  
版本：0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `LAS[number]`: 缓慢声音的频率加权声级(A-weighting)，一秒钟m更多的向上和向下。  - `LAeq[number]`: 频率加权的Leq声级（A加权）。  - `LAeq_d[number]`: 一天的声级频率权重（A-weghting）当量  - `LAmax[number]`: 声级频率称量（A-weghting）最大声级  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 该观察的日期和时间由ISO8601区间表示。  - `dateObservedFrom[string]`: 观察期的开始日期和时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: 观察期结束的日期和时间。见dateObserved。  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: 对这个项目的描述  - `distanceAverage[string]`: 传感器与潜在噪声源之间的平均距离  - `heightAverage[string]`: 传感器和噪声源之间的潜在障碍物的类型  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `obstacles[string]`: 传感器和噪声源之间的潜在障碍物的类型。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refDevice[*]`: 指的是捕获这一观察结果的设备。  - `refPointOfInterest[*]`: 对与该观察相关的兴趣点的参考。  - `refWeatherObserved[*]`: 参考相关的天气状况。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `sonometerClass[string]`: 根据美国国家标准协会（ANSI）的规定，用于观察的声波仪的等级（0，1，2）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI 实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObservedFrom`  - `dateObservedTo`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NoiseLevelObserved:    
  description: 'An observation of those acoustic parameters that estimate noise pressure levels at a certain place and time. '    
  properties:    
    LAS:    
      description: 'The frequency weighted sound level (A-weighting) for a slow sound, one second mor more up and down.'    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq:    
      description: 'The frequency weighted Leq sound level (A-weighting).'    
      type: number    
      x-ngsi:    
        type: Property    
    LAeq_d:    
      description: 'Acoustic Level frequency weigthed (A-weghting) equivalent for  a day'    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax:    
      description: 'Acoustic level frequency weigthed (A-weghting) maximum sound level'    
      type: number    
      x-ngsi:    
        type: Property    
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
      description: 'The date and time of this observation represented by an ISO8601 interval.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See dateObserved.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    distanceAverage:    
      description: 'Average distance between sensor and potential noise sources'    
      type: string    
      x-ngsi:    
        type: Property    
        units: meters    
    heightAverage:    
      description: 'Type of potential obstacles between the sensor and the noise source'    
      type: string    
      x-ngsi:    
        type: Property    
        units: meters    
    id:    
      anyOf: &noiselevelobserved_-_properties_-_owner_-_items_-_anyof    
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
    obstacles:    
      description: 'Type of potential obstacles between the sensor and the noise source.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *noiselevelobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A reference to the device which captured this observation.'    
      x-ngsi:    
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
      description: 'A reference to a point of interest associated to this observation.'    
      x-ngsi:    
        type: Relationship    
    refWeatherObserved:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the associated weather conditions.'    
      x-ngsi:    
        type: Relationship    
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
    sonometerClass:    
      description: 'Class of sonometer (0, 1, 2) according to ANSI used for taking this observation'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - NoiseLevelObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObservedFrom    
    - dateObservedTo    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoiseLevelObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoiseLevelObserved/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.2.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### NoiseLevelObserved NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为关键值的NoiseLevelObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "type": "NoiseLevelObserved",  
  "LAS": 91.6,  
  "LAeq": 67.8,  
  "LAeq_d": 65.4,  
  "LAmax": 94.5,  
  "dateObservedFrom": "2016-12-28T11:00:00.00Z",  
  "dateObservedTo": "2016-12-28T12:00:00.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [-2.698, 42.8491]  
  }  
}  
```  
</details>  
#### NoiseLevelObserved NGSI-v2 normalized 示例  
下面是一个以JSON-LD格式规范化的NoiseLevelObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "type": "NoiseLevelObserved",  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-28T11:00:00.00Z"  
  },  
  "LAmax": {  
    "type": "Number",  
    "value": 94.5  
  },  
  "LAeq": {  
    "type": "Number",  
    "value": 67.8  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-28T12:00:00.00Z"  
  },  
  "LAeq_d": {  
    "type": "Number",  
    "value": 65.4  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -2.698,  
        42.8491  
      ]  
    }  
  },  
  "LAS": {  
    "type": "Number",  
    "value": 91.6  
  }  
}  
```  
</details>  
#### NoiseLevelObserved NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为关键值的NoiseLevelObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:NoiseLevelObserved:Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
    "type": "NoiseLevelObserved",  
    "LAS": 91.6,  
    "LAeq": 67.8,  
    "LAeq_d": 65.4,  
    "LAmax": 94.5,  
    "dateObservedFrom": {  
        "@type": "DateTime",  
        "@value": "2016-12-28T11:00:00.00Z"  
    },  
    "dateObservedTo": {  
        "@type": "DateTime",  
        "@value": "2016-12-28T12:00:00.00Z"  
    },  
    "location": {  
        "coordinates": [  
            -2.698,  
            42.8491  
        ],  
        "type": "Point"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### NoiseLevelObserved NGSI-LD归一化示例  
下面是一个以JSON-LD格式规范化的NoiseLevelObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NoiseLevelObserved:Vitoria-NoiseLevelObserved-2016-12-28T11:00:00_2016-12-28T12:00:00",  
  "type": "NoiseLevelObserved",  
  "LAS": {  
    "type": "Property",  
    "value": 91.6  
  },  
  "LAeq": {  
    "type": "Property",  
    "value": 67.8  
  },  
  "LAeq_d": {  
    "type": "Property",  
    "value": 65.4  
  },  
  "LAmax": {  
    "type": "Property",  
    "value": 94.5  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-28T11:00:00.00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-28T12:00:00.00Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -2.698,  
        42.8491  
      ]  
    }  
  },  
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
