<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ大気質予報  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityForecast/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**ある期間に有効な大気の質の状態の予測**。  
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
- `airQualityIndex[number]`: 大気の質指数とは、その日の大気の質を表す数値。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: 観察された大気の質に対応する健康への懸念の全体的な質的レベル  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `co2[number]`: 二酸化炭素予測  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `no2[number]`: 二酸化窒素予測  - `nox[number]`: その他の窒素酸化物  - `o3[number]`: オゾン予想  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pm10[number]`: 直径10マイクロメートル以下の粒子状物質  - `pm25[number]`: 直径2.5マイクロメートル以下の粒子状物質  - `precipitation[number]`: 雨量  . Model: [https://schema.org/Number](https://schema.org/Number)- `relativeHumidity[number]`: 空気中の湿度  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `so2[number]`: 二酸化硫黄検出  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperature[number]`: 商品の温度  - `type[string]`: NGSIエンティティタイプ：AirQualityForecastでなければならない。  - `validFrom[date-time]`: この予報の有効期間の開始日をISO8601形式で表す。  - `validTo[date-time]`: ISO8601形式でのこの予報の有効期間の終了日  - `validity[string]`: この予測の有効期間をISO8601の時間間隔として含む。  . Model: [https://schema.org/Text](https://schema.org/Text)- `windSpeed[number]`: 風の強さ  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### 大気質予測 NGSI-v2 キー値の例  
以下は、JSON-LD形式のAirQualityForecastのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### 大気質予測 NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のAirQualityForecastの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
#### 大気質予測 NGSI-LD キー値の例  
JSON-LD形式のAirQualityForecastのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
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
#### 大気質予測 NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のAirQualityForecastの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
