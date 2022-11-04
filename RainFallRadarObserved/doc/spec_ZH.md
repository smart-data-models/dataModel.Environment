<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。雨落雷达观测  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Environment/blob/master/RainFallRadarObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该数据模型旨在通过一组由地理属性格式表示的4个位置来测量预定区域的水滑坡。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: 观察到的大气压力以Hecto Pascals为单位。  . Model: [https://schema.org/Number](https://schema.org/Number)- `cellsSize[number]`: 构成雷达的每个单元的尺寸。测量的单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MTR**代表**米**。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 该观测的日期和时间，采用ISO8601 UTC格式。它可以由一个特定的时间瞬间或由一个ISO8601间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[string]`: 观察期的开始日期和时间。见dateObserved。它可以由一个特定的时间瞬间或由一个ISO8601间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: 观察期结束的日期和时间。见dateObserved。它可以由一个特定的时间瞬间或由一个ISO8601区间来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 对这个项目的描述  - `feelLikesTemperature[number]`: 项目的温度欣赏  - `gustSpeed[number]`: 突然爆发的高速风，超过观察到的平均风速，只持续了几秒钟。  - `id[*]`: 实体的唯一标识符  - `illuminance[number]`: (https://en.wikipedia.org/wiki/Illuminance)观察，以勒克斯(lx)或每平方米流明(cd-sr-m-2)衡量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mapScale[string]`: 地图比例尺。cellSize的长度与它在地图上的表示之间的关系  . Model: [https://schema.org/Text](https://schema.org/Text)- `measuredArea[number]`: 被测面的参考。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MTK**代表平方米。  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `numberOfCol[number]`: 允许读取 "rainFallradarContent "属性的栏目数  . Model: [https://schema.org/Number](https://schema.org/Number)- `numberOfRow[number]`: 允许读取 "rainFallradarContent "属性的行数  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `rainFallRadarContent[string]`: 提供观察到的信息的路径和文件名  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: 参考一个[设备](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)，它记录了这一观察结果  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: 对与观测有关的[兴趣点](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)的引用。  . Model: [https://schema.org/URL](https://schema.org/URL)- `relativeHumidity[number]`: 空气中的湿度。观测到的瞬时相对湿度（空气中的水蒸气）。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `temperature[number]`: 项目的温度  - `type[string]`: NGSI实体类型。它必须是RainFallRadarObserved。  - `visibility[*]`: 能见度的类别  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: 天气的文字描述  . Model: [http://schema.org/Text.](http://schema.org/Text.)- `windDirection[number]`: 赌风的方向  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: 风的强度  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `rainFallRadarContent`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RainFallRadarObserved:    
  description: 'The Data Model is intended to measure the water slides on a predefined area by a set of 4 Location represented by a Geo property format.'    
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
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Hecto pascals'    
    cellsSize:    
      description: 'Size of each cell constituting the radar. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents **Meters**'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See dateObserved. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: 'A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &rainfallradarobserved_-_properties_-_owner_-_items_-_anyof    
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
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    mapScale:    
      description: 'Map Scale. Relationship between the length of the cellSize and its representation on the map'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    measuredArea:    
      description: 'Reference of the surface measured. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTK** represents Square Meters'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'square meters'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberOfCol:    
      description: 'Number of Cols allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    numberOfRow:    
      description: 'Number of Rows allowing the reading of the `rainFallradarContent` attribute'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *rainfallradarobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rainFallRadarContent:    
      description: 'Path and filename which provided the information observed'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Reference to a [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which captured this observation'    
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
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    relativeHumidity:    
      description: 'Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
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
    temperature:    
      description: 'Temperature of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RainFallRadarObserved'    
      enum:    
        - RainFallRadarObserved    
      type: string    
      x-ngsi:    
        type: Property    
    visibility:    
      anyOf:    
        - enum:    
            - veryPoor    
            - poor    
            - moderate    
            - good    
            - veryGood    
            - excellent    
          type: string    
        - minimum: 0    
          type: number    
      description: 'Categories of visibility'    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    weatherType:    
      description: 'Text description of the weather'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text.    
        type: Property    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 360    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - rainFallRadarContent    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/RainFallRadarObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/RainFallRadarObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### RainFallRadarObserved NGSI-v2 key-values 示例  
这里有一个RainFallRadarObserved的例子，以JSON-LD格式作为key-values。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
  "type": "RainFallRadarObserved",  
  "name": "MNCA-RFRO-018",  
  "alternateName": "AirPort global Observation",  
  "description": "Rain fall Radar Observation",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[  
      [43.66,7.19],  
      [44.66,7.19],  
      [44.66,7.21],  
      [43.66,7.21],  
      [43.66,7.19]  
    ]]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport Area Coverage + 4 km distance"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:NCE-RFRO-018",  
  "dateObserved": "2020-03-17T08:30:00Z",  
  "dateObservedFrom": "2020-03-17T08:30:00Z",  
  "dateObservedTo": "2020-03-17T08:45:00Z",  
  "rainFallRadarContent": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00",  
  "numberOfRow": 25,  
  "numberOfCol": 48,  
  "cellsSize": 1,  
  "mapScale": "1/10.000",  
  "measuredArea": 250  
}  
```  
</details>  
#### RainFallRadarObserved NGSI-v2 normalized Example  
下面是一个以JSON-LD格式规范化的RainFallRadarObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
	"type": "RainFallRadarObserved",  
	"name": {  
		"type": "Property",  
		"value": "MNCA-RFRO-018"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "AirPort  global Observation"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Rain fall Radar Observation"  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "polygon",  
			"coordinates": [[  
				[43.66, 7.19],  
				[44.66, 7.19],  
				[44.66, 7.21],  
				[43.66, 7.21],  
				[43.66, 7.19]  
			]]  
		}  
	},  
	"address": {  
		"type": "Property",  
		"value": {  
			"addressCountry": "FR",  
			"addressLocality": "Nice",  
			"streetAddress": "Airport Area Coverage + 4 km distance"  
		}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Aeroport"  
	},  
	"refDevice": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Device:NCE-RFRO-018"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:30:00Z"  
		}  
	},  
	"dateObservedFrom": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:30:00Z"  
		}  
	},  
	"dateObservedTo": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-03-17T08:45:00Z"  
		}  
	},  
	"rainFallRadarContent": {  
		"type": "Property",  
		"value": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00"  
	},  
	"numberOfRow": {  
		"type": "Property",  
		"value": 25  
	},  
	"numberOfCol": {  
		"type": "Property",  
		"value": 48  
	},  
	"cellsSize": {  
		"type": "Property",  
		"value": 1  
	},  
	"mapScale": {  
		"type": "Property",  
		"value": "1/10.000"  
	},  
	"measuredArea": {  
		"type": "Property",  
		"value": 250  
	}  
}  
```  
</details>  
#### RainFallRadarObserved NGSI-LD关键值示例  
这里是一个RainFallRadarObserved的例子，以JSON-LD格式作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
    "type": "RainFallRadarObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Airport Area Coverage + 4 km distance"  
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
    "cellsSize": {  
        "type": "Property",  
        "value": 1  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-03-17T08:30:00Z"  
        }  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-03-17T08:30:00Z"  
        }  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Rain fall Radar Observation"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "polygon",  
            "coordinates": [  
                [  
                    [  
                        43.66,  
                        7.19  
                    ],  
                    [  
                        44.66,  
                        7.19  
                    ],  
                    [  
                        44.66,  
                        7.21  
                    ],  
                    [  
                        43.66,  
                        7.21  
                    ],  
                    [  
                        43.66,  
                        7.19  
                    ]  
                ]  
            ]  
        }  
    },  
    "mapScale": {  
        "type": "Property",  
        "value": "1/10.000"  
    },  
    "measuredArea": {  
        "type": "Property",  
        "value": 250  
    },  
    "name": {  
        "type": "Property",  
        "value": "MNCA-RFRO-018"  
    },  
    "numberOfCol": {  
        "type": "Property",  
        "value": 48  
    },  
    "numberOfRow": {  
        "type": "Property",  
        "value": 25  
    },  
    "rainFallRadarContent": {  
        "type": "Property",  
        "value": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00"  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:NCE-RFRO-018"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RainFallRadarObserved NGSI-LD 归一化示例  
这里有一个RainFallRadarObserved的例子，是以JSON-LD格式规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RainFallRadarObserved:RainFallRadarObserved:MNCA-RFRO-018",  
    "type": "RainFallRadarObserved",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Airport Area Coverage + 4 km distance"  
    },  
    "alternateName": "AirPort global Observation",  
    "areaServed": "Nice Aeroport",  
    "cellsSize": 1,  
    "dateObserved": "2020-03-17T08:30:00Z",  
    "dateObservedFrom": "2020-03-17T08:30:00Z",  
    "dateObservedTo": "2020-03-17T08:45:00Z",  
    "description": "Rain fall Radar Observation",  
    "location": {  
        "type": "Polygon",  
        "coordinates": [  
            [  
                [  
                    43.66,  
                    7.19  
                ],  
                [  
                    44.66,  
                    7.19  
                ],  
                [  
                    44.66,  
                    7.21  
                ],  
                [  
                    43.66,  
                    7.21  
                ],  
                [  
                    43.66,  
                    7.19  
                ]  
            ]  
        ]  
    },  
    "mapScale": "1/10.000",  
    "measuredArea": 250,  
    "name": "MNCA-RFRO-018",  
    "numberOfCol": 48,  
    "numberOfRow": 25,  
    "rainFallRadarContent": "https://particuliers/rainFallRadar/NCE-RFRO-018-2020-03-17T08:30:00",  
    "refDevice": "urn:ngsi-ld:Device:NCE-RFRO-018",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
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
