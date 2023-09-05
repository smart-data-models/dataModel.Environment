<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：蚊子密度  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**城市蚊子密度数据模型**。  
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
- `airTemperature[object]`: 气温观测值。值是一个对象，包含代表从过去数据中得出的统计总量的属性  - `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataDescriptor[uri]`: 指向数据描述符实体的 URI  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `deviceInfo[object]`: 与观测结果相关的设备信息  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: 显示报告设备的电池充电状态（连接、断开）  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceId[string]`: 与该观测值相对应的物理传感器/测量站的设备 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 描述有关设备、传感器或系统的信息  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: 该观测点对应的传感设备/站的设备名称或站名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 提供废物管理车上设备的模拟号码  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 设备感知/观测/测量的属性  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `mosquitoDensity[object]`: 蚊子种类的双名（或）动物学命名法，以及与此次观察相对应的装置所确定的蚊子数量  	- `femaleSpeciesCount[number]`: 设备识别出的雌蚊种类的总计数    
	- `maleSpeciesCount[number]`: 设备识别出的雄蚊种类的总计数    
	- `mosquitoSpecies[string]`: 装置识别的蚊子物种的双名/动物学命名法    
- `name[string]`: 该项目的名称  - `observationDateTime[date-time]`: 最后报告的观察时间  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `precipitation[number]`: 一定时间内的观测降水量/降雨量水平  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 MosquitoDensity  <!-- /30-PropertiesList -->  
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
## 有效载荷示例  
#### MosquitoDensity NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 MosquitoDensity 示例。当使用 "options=keyValues "时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 蚊子密度 NGSI-v2 标准化示例  
下面是一个以 JSON-LD 格式规范化的 MosquitoDensity 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 蚊子密度 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 MosquitoDensity 示例。当使用 "options=keyValues "时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### 蚊子密度 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 MosquitoDensity 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
