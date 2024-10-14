<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ大気質観測  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**ある場所と時間における大気の状態を観測すること。  
バージョン: 0.1.4  
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
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `airQualityIndex[number]`: 大気の質指数とは、その日の大気の質を表す数値。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: 観察された大気の質に対応する健康への懸念の全体的な質的レベル  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: この大気質測定が属する上位レベル地域  . Model: [https://schema.org/Text ](https://schema.org/Text )- `as[number]`: ヒ素検出  . Model: [https://schema.org/Number](https://schema.org/Number)- `c6h6[number]`: ベンゼン検出  - `cd[number]`: カドミウム検出  - `charge[number]`: 本機の入力充電電圧。  - `co[number]`: 一酸化炭素検出  - `co2[number]`: 二酸化炭素検出  - `coLevel[string]`: 質的な一酸化炭素の存在  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[date-time]`: ISO8601 UTCフォーマットによる観測日時  . Model: [https://schema.org/Text ](https://schema.org/Text )- `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `ni[number]`: ニッケル検出  - `no[number]`: 一酸化窒素検出  - `no2[number]`: 二酸化窒素検出  - `nox[number]`: 検出されたその他の窒素酸化物  - `o3[number]`: オゾン検出  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pb[number]`: 鉛検出  - `pm1[number]`: 直径1マイクロメートル以下の粒子状物質  - `pm10[number]`: 直径10マイクロメートル以下の粒子状物質  - `pm25[number]`: 直径2.5マイクロメートル以下の粒子状物質  - `pm4[number]`: 直径4マイクロメートル以下の粒子状物質  - `precipitation[number]`: 雨量  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[number]`: 観測された大気圧（hPa）。  - `refDevice[*]`: この観測を捕らえた機器へのリファレンス。  - `refPointOfInterest[*]`: この観測に関連する注目点（通常は大気質ステーション）への参照。  - `refWeatherObserved[*]`: このエンティティによって記述された大気質状況に関連して観測された天候  - `relativeHumidity[number]`: 空気の相対湿度（0％～100％の範囲を表す0～1の数値）  - `reliability[number]`: 観測された大気の質に対応する信頼性（パーセンテージ、単位：ppm  . Model: [https://schema.org/Number ](https://schema.org/Number )- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `sh2[number]`: 硫化水素検出  - `so2[number]`: 二酸化硫黄検出  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperature[number]`: 商品の温度  - `tpc[number]`: 総粒子カウンター（空気中に浮遊する粒子の総濃度。）  - `tsp[number]`: 総懸濁粒子（大きさや組成に関係なく、すべての空気中の粒子の濃度。）  - `type[string]`: NGSI エンティティタイプ。AirQualityObserved でなければならない。  - `typeofLocation[string]`: サンプルの場所の種類  . Model: [https://schema.org/Text](https://schema.org/Text)- `volatileOrganicCompoundsTotal[number]`: アルカン＜C10、ケトン＜C6、アルデヒド＜C10、カルボン酸＜C5、アスピリット＜C7、アルケン＜C8、芳香族  - `windDirection[number]`: 風見鶏の向き  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: 風の強さ  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
すべての汚染物質がこのデータモデルに含まれているわけではない。モデルを拡張するために新たな汚染物質が追加された場合は、http://dd.eionet.europa.eu/vocabulary/aq/pollutant/view?page=1#vocabularyConceptResults を参照してください。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AirQualityObserved:    
  description: An observation of air quality conditions at a certain place and time.    
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
      description: Higher level area to which this air quality measurement belongs to    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
        type: Property    
    as:    
      description: Arsenic detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    c6h6:    
      description: Benzene detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    cd:    
      description: Cadmium detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    charge:    
      description: Input charging voltage of the monitoring device.    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co:    
      description: Carbon Monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    co2:    
      description: Carbon Dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    coLevel:    
      description: Qualitative Carbon Monoxide presence    
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
    dateObserved:    
      description: The date and time of this observation in ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text '    
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
        type: Relationship    
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
    ni:    
      description: 'Nickel detected '    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no:    
      description: Nitrogen monoxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    no2:    
      description: Nitrogen dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    nox:    
      description: Other Nitrogen oxides detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    o3:    
      description: 'Ozone detected '    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    pb:    
      description: 'Lead detected   '    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    pm1:    
      description: Particulate matter 1 micrometers or less in diameter    
      type: number    
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
    pm4:    
      description: Particulate matter 4 micrometers or less in diameter    
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
    pressure:    
      description: Atmospheric pressure (hPa) observed.    
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
      description: A reference to a point of interest (usually an air quality station) associated to this observation    
      x-ngsi:    
        type: Relationship    
    refWeatherObserved:    
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
      description: ' Weather observed associated to the air quality conditions described by this entity'    
      x-ngsi:    
        type: Relationship    
    relativeHumidity:    
      description: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    reliability:    
      description: 'Reliability (percentage, expressed in parts per one) corresponding to the air quality observed'    
      maximum: 1.0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: 'https://schema.org/Number '    
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
    sh2:    
      description: Hydrogen sulfide detected    
      minimum: 0    
      type: number    
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
    tpc:    
      description: Total Particulate Counter (Total concentration of particles suspended in the air.)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    tsp:    
      description: Total Suspended Particles (Concentration of all airborne particles regardless of their size or composition.)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be AirQualityObserved    
      enum:    
        - AirQualityObserved    
      type: string    
      x-ngsi:    
        type: Property    
    typeofLocation:    
      description: Type of location of the sampled item    
      enum:    
        - indoor    
        - outdoor    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    volatileOrganicCompoundsTotal:    
      description: 'Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    windDirection:    
      description: Direction of the weather vane    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
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
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.1.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### AirQualityObserved NGSI-v2 キー値の例  
JSON-LD形式のAirQualityObservedのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Madrid",  
    "streetAddress": "Plaza de Espa\u00f1a"  
  },  
  "dateObserved": "2016-03-15T11:00:00",  
  "areaServed": "Brooklands",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.712247222222222,  
      40.423852777777775  
    ]  
  },  
  "source": "http://datos.madrid.es",  
  "typeOfLocation": "outdoor",  
  "precipitation": 0,  
  "relativeHumidity": 0.54,  
  "temperature": 12.2,  
  "windDirection": 176,  
  "windSpeed": 0.64,  
  "airQualityLevel": "moderate",  
  "airQualityIndex": 65,  
  "reliability": 0.7,  
  "co": 500,  
  "no": 45,  
  "co2": 69,  
  "nox": 139,  
  "so2": 11,  
  "coLevel": "moderate",  
  "pm4": 37,  
  "tpc": 108,  
  "tsp": 73.3,  
  "pressure": 1.1,  
  "charge": 5,  
  "refPointOfInterest": "28079004-Pza.deEspanya"  
}  
```  
</details>  
#### AirQualityObserved NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の AirQualityObserved の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2016-03-15T11:00:00"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Brooklands"  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "moderate"  
  },  
  "co": {  
    "type": "Number",  
    "value": 500,  
    "metadata": {  
      "unitCode": {  
        "value": "GP"  
      }  
    }  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 12.2  
  },  
  "no": {  
    "type": "Number",  
    "value": 45,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "refPointOfInterest": {  
    "type": "Text",  
    "value": "28079004-Pza.deEspanya"  
  },  
  "windDirection": {  
    "type": "Number",  
    "value": 176  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://datos.madrid.es"  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 0.64  
  },  
  "so2": {  
    "type": "Number",  
    "value": 11,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "nox": {  
    "type": "Number",  
    "value": 139,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.712247222222222,  
        40.423852777777775  
      ]  
    }  
  },  
  "typeOfLocation": {  
    "type": "Text",  
    "value": "outdoor"  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 65  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Madrid",  
      "streetAddress": "Plaza de Espa\u00f1a"  
    }  
  },  
  "reliability": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.54  
  },  
  "precipitation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "no2": {  
    "type": "Number",  
    "value": 69,  
    "metadata": {  
      "unitCode": {  
        "value": "GQ"  
      }  
    }  
  },  
  "coLevel": {  
    "type": "Text",  
    "value": "moderate"  
  },  
  "pm4": {  
      "type": "Number",  
      "value": 37  
    },  
    "tpc": {  
      "type": "Number",  
      "value": 108  
    },  
    "tsp": {  
      "type": "Number",  
      "value": 73.3  
    },  
    "pressure": {  
      "type": "Number",  
      "value": 1.1  
    },  
    "charge": {  
      "type": "Number",  
      "value": 5  
    }  
}  
```  
</details>  
#### NGSI-LD キー値の例  
AirQualityObservedをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "co": 500,  
  "coLevel": "moderate",  
  "no": 45,  
  "no2": 69,  
  "nox": 139,  
  "so2": 11,  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Madrid",  
    "streetAddress": "Plaza de Espa\u00f1a",  
    "type": "PostalAddress"  
  },  
  "airQualityIndex": 65,  
  "airQualityLevel": "moderate",  
  "areaServed": "Brooklands",  
  "dateObserved": "2016-03-15T11:00:00",  
  "location": {  
    "coordinates": [  
      -3.712247222222222,  
      40.423852777777775  
    ],  
    "type": "Point"  
  },  
  "precipitation": 0,  
  "refPointOfInterest": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya",  
  "relativeHumidity": 0.54,  
  "reliability": 0.7,  
  "source": "http://datos.madrid.es",  
  "temperature": 12.2,  
  "typeOfLocation": "outdoor",  
  "windDirection": 180,  
  "windSpeed": 0.64,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の AirQualityObserved の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityObserved:Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",  
  "type": "AirQualityObserved",  
  "co": {  
      "type": "Property",  
      "value": 500,  
      "unitCode": "GP"  
  },  
  "coLevel": {  
      "type": "Property",  
      "value": "moderate"  
  },  
  "no": {  
      "type": "Property",  
      "value": 45,  
      "unitCode": "GQ"  
  },  
  "no2": {  
      "type": "Property",  
      "value": 69,  
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
  "address": {  
      "type": "Property",  
      "value": {  
          "addressCountry": "ES",  
          "addressLocality": "Madrid",  
          "streetAddress": "Plaza de Espa\u00f1a",  
          "type": "PostalAddress"  
      }  
  },  
  "airQualityIndex": {  
      "type": "Property",  
      "value": 65  
  },  
  "airQualityLevel": {  
      "type": "Property",  
      "value": "moderate"  
  },  
  "areaServed": {  
      "type": "Property",  
      "value": "Brooklands"  
  },  
  "dateObserved": {  
      "type": "Property",  
      "value": "2016-03-15T11:00:00"  
  },  
  "location": {  
      "type": "GeoProperty",  
      "value": {  
          "type": "Point",  
          "coordinates": [  
              -3.712247222222222,  
              40.423852777777775  
          ]  
      }  
  },  
  "precipitation": {  
      "type": "Property",  
      "value": 0  
  },  
  "refPointOfInterest": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:PointOfInterest:28079004-Pza.deEspanya"  
  },  
  "relativeHumidity": {  
      "type": "Property",  
      "value": 0.54  
  },  
  "reliability": {  
      "type": "Property",  
      "value": 0.7  
  },  
  "source": {  
      "type": "Property",  
      "value": "http://datos.madrid.es"  
  },  
  "temperature": {  
      "type": "Property",  
      "value": 12.2  
  },  
  "typeOfLocation": {  
      "type": "Property",  
      "value": "outdoor"  
  },  
  "windDirection": {  
      "type": "Property",  
      "value": 186  
  },  
  "windSpeed": {  
      "type": "Property",  
      "value": 0.64  
  },  
  "pm4": {  
      "type": "Property",  
      "value": 37  
    },   
  "tpc": {  
      "type": "Property",  
      "value": 108  
    },  
  "tsp": {  
      "type": "Property",  
      "value": 73.3  
    },   
  "pressure": {  
      "type": "Property",  
      "value": 1.1  
    },  
  "charge": {  
      "type": "Property",  
      "value": 5  
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
