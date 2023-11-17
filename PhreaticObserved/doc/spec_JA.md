<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ水蒸気観測    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このデータモデルは、固定または移動式のモニタリングシステムによって、ある時間（T）における地下水の水位と水質を測定、観測、管理することを目的としている。使用する装置によっては、電気伝導度、塩分、温度などの水質を測定することも可能である。この場合、測定された値はデータモデル `WaterObserved` と `WaterQualityObserved` によって処理される。属性に関する追加情報：水専用の属性については、MetaData 属性を使用することもできます。MetaData 属性には、秒単位の `TimeStamp` 、測定の `qualification` と制御 `status` が含まれます。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[date-time]`: ISO8601 UTCフォーマットでの観測日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: 観測期間 ：ISO8601UTCフォーマットによる開始日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: 観測期間：ISO8601 UTCフォーマットによる終了日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `depth[number]`: 識別 `waterTable` 以降の飲料水の深さ。UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる測定の単位コード(テキスト)(最大3文字)。例えば、<code> MTR </code> は Meter を表す。  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `investigationDepth[number]`: 調査が行われた最大深度。UN/CEFACT共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる測定の単位コード(テキスト)(最大3文字)。例えば、<code>MTR</code>はメートルを表す。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `isMobile[boolean]`: 使用デバイスが固定（偽）またはモバイル（真）  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `measurementType[array]`: 観測期間：処理された測定の種類。Enum:'深度、体積、品質、その他'  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pollutionRate[number]`: 汚染率。UN/CEFACT共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる測定の単位コード（テキスト）（最大3文字）。例えば、P1 はパーセンテージを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[number]`: 水圧。UN/CEFACT共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与えられる測定の単位コード(テキスト)(最大3文字)。例えば、<code>BAR</code>はBarを表す。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refDevice[array]`: データ提供機器に関する言及  . Model: [https://scehma.org/URL](https://scehma.org/URL)- `residueLevel[number]`: 残留レベル発見  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIエンティティタイプ。PhreaticObservedでなければならない。  - `waterTable[number]`: 今回の調査で水が検出された水位。UN/CEFACT共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して与えられた測定の単位コード（テキスト）（最大3文字）。例えば、<code>MTR</code>はメートルを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `dateObserved`  - `id`  - `location`  - `measurementType`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
PhreaticObserved:      
  description: 'The Data Model is intended to measure, observe and control the level and quality of groundwater at a given time (T), by a fixed or mobile monitoring system. Depending on the device used, it is also possible to measure the quality of water such as its electrical conductivity, its salt content, its temperature, etc. In this case, the values measured are processed by the Data Model `WaterObserved` and `WaterQualityObserved`. Additional Information about Attributes: For attributes dedicated to water, a MetaData attribute can also be used. it contains the `TimeStamp` in seconds, the `qualification` and control `status` of the measurement.'      
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
      description: The date and time of this observation in ISO8601 UTC format      
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
      description: 'Depth of drinking water, since its identification `waterTable`. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code> MTR </code> represents Meter'      
      type: number      
      x-ngsi:      
        model: https://schema.org/depth      
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
    investigationDepth:      
      description: 'Maximum depth where the investigation was made. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'      
      type: number      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
        units: meters      
    isMobile:      
      description: The device used is Fixed (False) or Mobile (True)      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
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
    measurementType:      
      description: 'Observation period : Type of measurement processed. Enum:''depth, volume, quality, other'''      
      items:      
        enum:      
          - depth      
          - other      
          - quality      
          - volume      
        type: string      
      minItems: 0      
      type: array      
      uniqueItems: false      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
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
    pollutionRate:      
      description: 'Rate of pollution. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, P1 represents Percentage'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    pressure:      
      description: 'Water Pressure. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>BAR</code> represents Bar'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
        units: Bar      
    refDevice:      
      description: Reference to the devices providing data      
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
        model: https://scehma.org/URL      
        type: Relationship      
    residueLevel:      
      description: Residue level found      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be PhreaticObserved      
      enum:      
        - PhreaticObserved      
      type: string      
      x-ngsi:      
        type: Property      
    waterTable:      
      description: 'Level at which water was found during this investigation. The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter'      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/PhreaticObserved/LICENSE.md      
  x-model-schema: ""      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### PhreaticObserved NGSI-v2 キー値の例    
JSON-LD形式のPhreaticObservedのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
      43.66481,  
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
#### PhreaticObserved NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のPhreaticObservedの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhreaticObserved:PhreaticObserved:MNCA-001",  
  "type": "PhreaticObserved",  
  "name": {  
    "type": "Text",  
    "value": "STLRT-MNCA-NP-015"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Measurement corresponding to the level and quality of groundwater closed from Airport River Saint Laurent du Var."  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Airport"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-07-07T15:05:59.408Z"  
  },  
  "refDevice": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Device:T1-NP-015"  
    ]  
  },  
  "isMobile": {  
    "type": "Boolean",  
    "value": false  
  },  
  "measurementType": {  
    "type": "StructuredValue",  
    "value": [  
      "depth",  
      "volume"  
    ]  
  },  
  "investigationDepth": {  
    "type": "Number",  
    "value": 22.35  
  },  
  "waterTable": {  
    "type": "Number",  
    "value": 12.75  
  },  
  "depth": {  
    "type": "Number",  
    "value": 20.45  
  },  
  "pressure": {  
    "type": "Number",  
    "value": 2.12  
  }  
}  
```  
</details>    
#### PhreaticObserved NGSI-LD キー値の例    
以下はPhreaticObservedをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。    
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 水蒸気観測 NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のPhreaticObservedの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
