<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ交通環境影響予測  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述**自動車の交通量の予想とその排出ガス特性に基づく交通の環境影響**。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: 予想されるC02排出濃度  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateIssued[string]`: サービスプロバイダが予報を発行した日時。ISO8601 UTCフォーマット。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `traffic[array]`: 異なる車種の強度、職業、速度に関する期待値を含むオブジェクトの配列。  - `type[string]`: NGSIタイプ。TrafficEnvironmentImpactForecastでなければならない。  - `validFrom[string]`: ISO8601形式で表したこの予報の有効期間の開始日  - `validTo[string]`: ISO8601形式でのこの予報の有効期間の終了日  - `validity[string]`: この予測の有効期間をISO8601時間間隔として含む。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficEnvironmentImpactForecast:    
  description: 'Environmental Impact of traffic based on the vehicles traffic expectations and their emission characteristics'    
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
    co2:    
      description: 'The expected C02 emission concentration'    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/L    
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
    dateIssued:    
      description: 'The date and time the forecast was issued by the service provider in ISO8601 UTC format.'    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &trafficenvironmentimpactforecast_-_properties_-_owner_-_items_-_anyof    
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
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficenvironmentimpactforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
    traffic:    
      description: 'Array of objects containing the expected values for intensity, occupation an speed of the different vehicle types'    
      items:    
        properties:    
          averageVehicleSpeedExpected:    
            description: 'Property. Average speed expected of the vehicles transiting during the observation period. Model:''https://schema.org/Number''. Units:''Kilometer per hour (Km/h)'''    
            minimum: 0    
            type: number    
          intensityExpected:    
            description: 'Property. Total number of vehicles expected during this forecast period. Model:''https://schema.org/Number''.'    
            minimum: 0    
            type: number    
          occupancyExpected:    
            description: 'Property. Fraction of the observation time where a vehicle has been occupying the observed lane. Model:''https://schema.org/Number''.'    
            maximum: 1    
            minimum: 0    
            type: number    
          vehicleClass:    
            description: 'Property. Enumeration of the vehicle classes'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type. It has to be TrafficEnvironmentImpactForecast'    
      enum:    
        - TrafficEnvironmentImpact    
      type: string    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'The start of the validity period for this forecast as a ISO8601 format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validTo:    
      description: 'The end of the validity period for this forecast as a ISO8601 format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval.'    
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
## ペイロードの例  
#### TrafficEnvironmentImpactForecast NGSI-v2 key-value の例。  
以下は、TrafficEnvironmentImpactForecastをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用したときにNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### TrafficEnvironmentImpactForecast NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のTrafficEnvironmentImpactForecastの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### TrafficEnvironmentImpactForecast NGSI-LD キー値例  
TrafficEnvironmentImpactForecastをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
        "https://smartdatamodels.org/dataModel.Environment/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### トラフィック環境影響予測 NGSI-LD 正規化例  
以下は、TrafficEnvironmentImpactForecastをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
        "type": "Geoproperty",  
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
        "https://smartdatamodels.org/dataModel.Environment/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
