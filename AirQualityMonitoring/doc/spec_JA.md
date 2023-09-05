<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ大気品質モニタリング  
================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityMonitoring/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**大気質モニタリング（AQM）データモデル。  
バージョン: 0.0.3  
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
- `airQualityIndex[number]`: 観測された大気の質の総合指数（AQI）  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: 大気の質のカテゴリー表示。地域の保健機関に従って定義された質的レベル。例えば、「GOOD」、「MODERATE」、「POOR」、「UNHEALTHY」、「SEVERE」、「HAZARDOUS」など。  . Model: [https://schema.org/Text](https://schema.org/Text)- `airTemperatureTSA[object]`: 気温時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `alternateName[string]`: この項目の別名  - `ambientNoiseTSA[object]`: アンビエントノイズ時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `aqiMajorPollutant[string]`: 大気質指標（AQI）の主要汚染物質。列挙:'ヒ素、バップ、ベンゼン、CO2、NH3、NO、NO2、O2、O3、SO2、PB'  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arsenicTSA[object]`: ヒ素の時系列集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `atmosphericPressure[number]`: 大気圧または気圧の観測値  . Model: [https://schema.org/Number](https://schema.org/Number)- `atmosphericPressureTSA[object]`: 大気圧時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `bapTSA[object]`: ベンゾ(a)ピレンの時系列凝集  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `benzeneTSA[object]`: ベンゼン時系列集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `co2TSA[object]`: 二酸化炭素時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `coTSA[object]`: 一酸化炭素時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `deviceInfo[object]`: オブザベーションに関連するデバイスに関する情報  	- `RFID[string]`: RFIDリーダーのID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceBatteryStatus[string]`: 報告デバイスのバッテリ充電状態を表示（接続、切断）  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: この観測に対応する物理センサー/計測ステーションのデバイスID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceList[string]`: この観測に対応するデバイスの品番とサブデバイスの情報  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 対象となるデバイス、センサー、システムの情報を記述する。    
	- `deviceName[string]`: この観測に対応するセンサーデバイス/ステーションのデバイス名またはステーション名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 廃棄物管理車両に搭載されているデバイスのSIM番号を示す。  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 装置によって感知／観察／測定される特性／性質  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `deviceStatus[string]`: 物理デバイスのステータスを示す  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意識別子  - `illuminance[number]`: 測定照度  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nh3TSA[object]`: アンモニア時系列の集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `nickelTSA[object]`: ニッケル時系列集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `no2TSA[object]`: 二酸化窒素時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `noTSA[object]`: 一酸化窒素の時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `o2TSA[object]`: 酸素時系列の集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `o3TSA[object]`: オゾン時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `observationDateTime[date-time]`: 最終観測報告時刻  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pbTSA[object]`: リード時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `pm10TSA[object]`: 直径10μm以下の大気中の粒子状物質の時系列的凝集。  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `pm25TSA[object]`: 直径25μm以下の大気中の粒子状物質時系列凝集塊  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `precipitation[number]`: 一定期間の観測降水量／降雨量  . Model: [https://schema.org/Number](https://schema.org/Number)- `relativeHumidityTSA[object]`: 相対湿度時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `so2TSA[object]`: 二酸化硫黄の時系列集約  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `solarRadiation[number]`: 瞬時日射量（単位：kW/m2  . Model: [http://schema.org/Number](http://schema.org/Number)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: AirQualityMonitoringでなければならない。  - `uvTSA[object]`: 紫外線時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `versionInfo[object]`: この観測に対応するバージョン情報  	- `comments[string]`: この観察に対応するユーザーコメント  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `endDateTime[date-time]`: この観測に対応する報告終了時刻  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
	- `startDateTime[date-time]`: この観測に対応する報告された開始時間  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
	- `versionName[string]`: この観測に対応するバージョン名  . Model: [https://schema.org/Text](https://schema.org/Text)  
<!-- /30-PropertiesList -->  
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
AirQualityMonitoring:    
  description: Air Quality Monitoring (AQM) Data Model.    
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
      description: Overall Air Quality Index (AQI) for the observed air quality    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityLevel:    
      description: 'Air Quality Category Indication. Qualitative level defined according to the local health agencies. For example, ''GOOD'', ''MODERATE'', ''POOR'', ''UNHEALTHY'', ''SEVERE'', ''HAZARDOUS'' etc'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    airTemperatureTSA:    
      description: Air temperature time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    ambientNoiseTSA:    
      description: ambient Noise time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    aqiMajorPollutant:    
      description: 'Major pollutant in the Air Quality Index (AQI). Enum:''arsenic, bap, benzene, co2, nh3, no, no2, o2, o3, so2, pb'''    
      enum:    
        - arsenic    
        - bap    
        - benzene    
        - co2    
        - nh3    
        - no    
        - no2    
        - o2    
        - o3    
        - so2    
        - pb    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arsenicTSA:    
      description: Arsenic time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    atmosphericPressure:    
      description: Observed air (atmospheric or barometric) pressure    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    atmosphericPressureTSA:    
      description: Atmospheric pressure time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    bapTSA:    
      description: Benzo(a)Pyrene time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    benzeneTSA:    
      description: Benzene time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    co2TSA:    
      description: Carbon dioxide time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    coTSA:    
      description: Carbon monoxide time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
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
    deviceInfo:    
      description: Information about the device associated with the observations    
      properties:    
        RFID:    
          description: Gives the ID of the RFID reader    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceBatteryStatus:    
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceID:    
          description: Device ID of the physical sensor/ measurement station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceList:    
          description: Information of device part number and sub devices corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceModel:    
          description: 'Describes the information of the device, sensor or system in consideration'    
          properties:    
            areaServed:    
              description: 'Area served by the entity or a service. '    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
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
          description: Unique identifier of the entity    
          x-ngsi:    
            type: Relationship    
      type: object    
      x-ngsi:    
        type: Property    
    deviceStatus:    
      description: Indicates the status of physical device or devices    
      type: string    
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
    illuminance:    
      description: Measured illuminance    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - bbox:    
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
        - bbox:    
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
        - bbox:    
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
        - bbox:    
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
        - bbox:    
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
        - bbox:    
            items:    
              type: number    
            minItems: 4    
            type: array    
          coordinates:    
            items:    
              items:    
                items:    
                  items:    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nh3TSA:    
      description: Ammonia time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    nickelTSA:    
      description: Nickel time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    no2TSA:    
      description: Nitrogen dioxide time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    noTSA:    
      description: Nitrogen monoxide time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    o2TSA:    
      description: Oxygen time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    o3TSA:    
      description: 'Ozone time series aggregation '    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    pbTSA:    
      description: Lead time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    pm10TSA:    
      description: Particulate matter in the air with a diameter of 10 micrometers or less time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    pm25TSA:    
      description: Particulate matter in the air with a diameter of 25 micrometers or less time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: Observed precipitation/rainfall level over a given duration    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    relativeHumidityTSA:    
      description: Relative Humidity time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
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
    so2TSA:    
      description: Sulfur dioxide time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    solarRadiation:    
      description: Instantaneous solar radiation measured in kW/m2    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kW/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI type. it has to be AirQualityMonitoring    
      enum:    
        - AirQualityMonitoring    
      type: string    
      x-ngsi:    
        type: Property    
    uvTSA:    
      description: Ultra violet radiation time series aggregation    
      properties:    
        averageValue:    
          description: Average value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        instValue:    
          description: Instant value of temporal processing    
          type: number    
          x-ngsi:    
            type: Property    
        maxOverTime:    
          description: Maximum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
        minOverTime:    
          description: Minimum value of temporal processing over time    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    versionInfo:    
      description: Version information corresponding to this observation    
      properties:    
        comments:    
          description: User comments corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        endDateTime:    
          description: Reported end time corresponding to this observation    
          format: date-time    
          type: string    
          x-ngsi:    
            model: https://schema.org/DateTime    
            type: Property    
        startDateTime:    
          description: Reported start time corresponding to this observation    
          format: date-time    
          type: string    
          x-ngsi:    
            model: https://schema.org/DateTime    
            type: Property    
        versionName:    
          description: Version name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        windType:    
          description: Wind type dominate during the last 24 hours    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/AirQualityMonitoring/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/AirQualityMonitoring/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### AirQualityMonitoring NGSI-v2 キー値の例  
JSON-LD形式のAirQualityMonitoringのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
  "type": "AirQualityMonitoring",  
  "address": {  
    "addressCountry": "India",  
    "addressLocality": "Bangalore",  
    "addressRegion": "Karnataka",  
    "postOfficeBoxNumber": "",  
    "postalCode": "110001",  
    "streetAddress": "Avenue Road"  
  },  
  "airQualityIndex": 90,  
  "airQualityLevel": "SATISFACTORY",  
  "airTemperatureTSA": {  
    "avgOverTime": 23.1,  
    "instValue": 30.8,  
    "maxOverTime": 32.8,  
    "minOverTime": 12.7  
  },  
  "alternateName": "EnvAQM sampling",  
  "ambientNoiseTSA": {  
    "avgOverTime": 57.9,  
    "instValue": 57.6,  
    "maxOverTime": 59.2,  
    "minOverTime": 50.5  
  },  
  "aqiMajorPollutant": "No2",  
  "areaServed": "Bangalore",  
  "arsenicTSA": {  
    "avgOverTime": 0.4,  
    "instValue": 0.35,  
    "maxOverTime": 0.44,  
    "minOverTime": 0.29  
  },  
  "atmosphericPressure": 633.2,  
  "atmosphericPressureTSA": {  
    "avgOverTime": 968.3,  
    "instValue": 982.9,  
    "maxOverTime": 982.7,  
    "minOverTime": 961.9  
  },  
  "bapTSA": {  
    "avgOverTime": 492.1,  
    "instValue": 439.1,  
    "maxOverTime": 573.7,  
    "minOverTime": 398.7  
  },  
  "benzeneTSA": {  
    "avgOverTime": 266.7,  
    "instValue": 321.7,  
    "maxOverTime": 576.9,  
    "minOverTime": 210.1  
  },  
  "co2TSA": {  
    "avgOverTime": 318.51,  
    "instValue": 320.4,  
    "maxOverTime": 390.2,  
    "minOverTime": 302.6  
  },  
  "coTSA": {  
    "avgOverTime": 3.51,  
    "instValue": 4.0,  
    "maxOverTime": 8.9,  
    "minOverTime": 3.4  
  },  
  "dataProvider": "",  
  "dateCreated": "2017-12-31T03:39:27Z",  
  "dateModified": "2021-12-22T04:21:57Z",  
  "description": "Air quality monitoring",  
  "deviceInfo": {  
    "RFID": "AB463478",  
    "deviceBatteryStatus": "Connected",  
    "deviceID": "12345",  
    "deviceList": "12",  
    "deviceModel": {  
      "areaServed": "Agartala",  
      "brandName": "Climo",  
      "manufacturerName": "Bosch",  
      "modelName": "sensor",  
      "modelURL": "www.boschclimo.com"  
    },  
    "deviceName": "Climo",  
    "deviceSimNumber": "12345678",  
    "measurand": "",  
    "refDevice": "urn:ngsi-ld:device:12"  
  },  
  "deviceStatus": "ACTIVE",  
  "illuminance": 3319.41,  
  "location": {  
    "coordinates": [  
      12.979,  
      77.591  
    ],  
    "type": "Point"  
  },  
  "name": "",  
  "nh3TSA": {  
    "avgOverTime": 865.1,  
    "instValue": 900.2,  
    "maxOverTime": 990.8,  
    "minOverTime": 834.7  
  },  
  "nickelTSA": {  
    "avgOverTime": 434.0,  
    "instValue": 527.2,  
    "maxOverTime": 559.6,  
    "minOverTime": 132.2  
  },  
  "no2TSA": {  
    "avgOverTime": 409.7,  
    "instValue": 511.0,  
    "maxOverTime": 611.5,  
    "minOverTime": 242.4  
  },  
  "noTSA": {  
    "avgOverTime": 3.65,  
    "instValue": 3.6,  
    "maxOverTime": 4.8,  
    "minOverTime": 2.7  
  },  
  "o2TSA": {  
    "avgOverTime": 18.1,  
    "instValue": 18.0,  
    "maxOverTime": 18.2,  
    "minOverTime": 18.0  
  },  
  "o3TSA": {  
    "avgOverTime": 218.8,  
    "instValue": 173.1,  
    "maxOverTime": 236.4,  
    "minOverTime": 167.7  
  },  
  "observationDateTime": "2020-09-16T11:00:00+05:30",  
  "owner": [  
    "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
    "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
  ],  
  "pbTSA": {  
    "avgOverTime": 473.0,  
    "instValue": 391.0,  
    "maxOverTime": 542.1,  
    "minOverTime": 287.5  
  },  
  "pm10TSA": {  
    "avgOverTime": 847.3,  
    "instValue": 439.1,  
    "maxOverTime": 568.1,  
    "minOverTime": 54.3  
  },  
  "pm25TSA": {  
    "avgOverTime": 28.3,  
    "instValue": 56.6,  
    "maxOverTime": 56.8,  
    "minOverTime": 10.1  
  },  
  "precipitation": 846.0,  
  "relativeHumidityTSA": {  
    "avgOverTime": 326.3,  
    "instValue": 401.2,  
    "maxOverTime": 599.3,  
    "minOverTime": 211.6  
  },  
  "seeAlso": [  
    "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
    "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
  ],  
  "so2TSA": {  
    "avgOverTime": 3.65,  
    "instValue": 3.5,  
    "maxOverTime": 3.72,  
    "minOverTime": 2.9  
  },  
  "solarRadiation": 3.65,  
  "source": "Bangalore Smart city",  
  "uvTSA": {  
    "avgOverTime": 6.0,  
    "instValue": 8.2,  
    "maxOverTime": 8.3,  
    "minOverTime": 5.7  
  },  
  "versionInfo": {  
    "comments": "Version 1",  
    "endDateTime": "2020-09-16T11:00:00+05:30",  
    "startDateTime": "2020-09-16T11:00:00+05:30",  
    "versionName": "Version 1"  
  }  
}  
```  
</details>  
#### 大気品質モニタリング NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の AirQualityMonitoring の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirQualityMonitoring:id:MUTW:63473748",  
  "type": "AirQualityMonitoring",  
  "dateCreated": {  
    "type": "Datetime",  
    "value": "2017-12-31T03:39:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-12-22T04:21:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Bangalore Smart city"  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "EnvAQM sampling"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Air quality monitoring"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:AirQualityMonitoring:items:PDSP:96970072",  
      "urn:ngsi-ld:AirQualityMonitoring:items:FTKL:60685543"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:AirQualityMonitoring:items:SUXG:34385451",  
      "urn:ngsi-ld:AirQualityMonitoring:items:AEAM:62422977"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        12.979,  
        77.591  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Avenue Road",  
      "addressLocality": "Bangalore",  
      "addressRegion": "Karnataka",  
      "addressCountry": "India",  
      "postalCode": "110001",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Bangalore"  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "deviceList": "12",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": "Climo",  
      "deviceID": "12345",  
      "RFID": "AB463478",  
      "measurand": "",  
      "deviceSimNumber": "12345678",  
      "deviceModel": {  
        "brandName": "Climo",  
        "manufacturerName": "Bosch",  
        "modelName": "sensor",  
        "modelURL": "www.boschclimo.com",  
        "areaServed": "Agartala"  
      },  
      "refDevice": "urn:ngsi-ld:device:12"  
    }  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2020-09-16T11:00:00+05:30"  
  },  
  "deviceStatus": {  
    "type": "Text",  
    "value": "ACTIVE"  
  },  
  "atmosphericPressure": {  
    "type": "Number",  
    "value": 633.2  
  },  
  "airQualityIndex": {  
    "type": "Number",  
    "value": 90  
  },  
  "airQualityLevel": {  
    "type": "Text",  
    "value": "SATISFACTORY"  
  },  
  "aqiMajorPollutant": {  
    "type": "Text",  
    "value": "no2"  
  },  
  "airTemperatureTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 93.7,  
      "minOverTime": 710.0,  
      "maxOverTime": 741.9,  
      "instValue": 889.5  
    }  
  },  
  "ambientNoiseTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 729.1,  
      "minOverTime": 482.0,  
      "maxOverTime": 743.7,  
      "instValue": 813.9  
    }  
  },  
  "arsenicTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 0.4,  
      "minOverTime": 0.29,  
      "maxOverTime": 0.44,  
      "instValue": 0.35  
    }  
  },  
  "atmosphericPressureTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 0.92,  
      "minOverTime": 0.91,  
      "maxOverTime": 0.93,  
      "instValue": 0.92  
    }  
  },  
  "bapTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 109.2,  
      "minOverTime": 277.8,  
      "maxOverTime": 836.0,  
      "instValue": 9.7  
    }  
  },  
  "benzeneTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 312.6,  
      "minOverTime": 405.9,  
      "maxOverTime": 786.1,  
      "instValue": 323.0  
    }  
  },  
  "coTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.51,  
      "minOverTime": 3.4,  
      "maxOverTime": 8.9,  
      "instValue": 4.0  
    }  
  },  
  "co2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 318.51,  
      "minOverTime": 302.6,  
      "maxOverTime": 390.2,  
      "instValue": 320.4  
    }  
  },  
  "nh3TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 135.1,  
      "minOverTime": 834.7,  
      "maxOverTime": 790.8,  
      "instValue": 900.2  
    }  
  },  
  "nickelTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 434.0,  
      "minOverTime": 132.2,  
      "maxOverTime": 559.6,  
      "instValue": 527.2  
    }  
  },  
  "noTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.65,  
      "minOverTime": 2.7,  
      "maxOverTime": 4.8,  
      "instValue": 3.6  
    }  
  },  
  "no2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 409.7,  
      "minOverTime": 642.4,  
      "maxOverTime": 211.5,  
      "instValue": 511.0  
    }  
  },  
  "o2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 18.1,  
      "minOverTime": 18.0,  
      "maxOverTime": 18.2,  
      "instValue": 18.0  
    }  
  },  
  "o3TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 118.8,  
      "minOverTime": 667.7,  
      "maxOverTime": 36.4,  
      "instValue": 473.1  
    }  
  },  
  "pm10TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 847.3,  
      "minOverTime": 54.3,  
      "maxOverTime": 868.1,  
      "instValue": 439.1  
    }  
  },  
  "pm25TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 28.3,  
      "minOverTime": 10.1,  
      "maxOverTime": 56.8,  
      "instValue": 56.6  
    }  
  },  
  "relativeHumidityTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 326.3,  
      "minOverTime": 711.6,  
      "maxOverTime": 199.3,  
      "instValue": 401.2  
    }  
  },  
  "so2TSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 3.65,  
      "minOverTime": 2.9,  
      "maxOverTime": 3.72,  
      "instValue": 3.8  
    }  
  },  
  "pbTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 473.0,  
      "minOverTime": 287.5,  
      "maxOverTime": 42.1,  
      "instValue": 91.0  
    }  
  },  
  "uvTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 6.0,  
      "minOverTime": 5.7,  
      "maxOverTime": 8.3,  
      "instValue": 8.2  
    }  
  },  
  "illuminance": {  
    "type": "Number",  
    "value": 3319.41  
  },  
  "solarRadiation": {  
    "type": "Number",  
    "value": 3.65  
  },  
  "precipitation": {  
    "type": "StructuredValue",  
    "value": 846.0  
  },  
  "versionInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "startDateTime": "2020-09-16T11:00:00+05:30",  
      "endDateTime": "2020-09-16T11:00:00+05:30",  
      "versionName": "Version 1",  
      "comments": "Version 1"  
    }  
  }  
}  
```  
</details>  
#### AirQualityMonitoring NGSI-LD キー値の例  
JSON-LD形式のAirQualityMonitoringのkey-valuesの例です。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
    "type": "AirQualityMonitoring",  
    "address": {  
        "addressCountry": "India",  
        "addressLocality": "Bangalore",  
        "addressRegion": "Karnataka",  
        "postOfficeBoxNumber": "",  
        "postalCode": "110001",  
        "streetAddress": "Avenue Road"  
    },  
    "airQualityIndex": 90,  
    "airQualityLevel": "SATISFACTORY",  
    "airTemperatureTSA": {  
        "avgOverTime": 23.1,  
        "instValue": 30.8,  
        "maxOverTime": 32.8,  
        "minOverTime": 12.7  
    },  
    "alternateName": "EnvAQM sampling",  
    "ambientNoiseTSA": {  
        "avgOverTime": 57.9,  
        "instValue": 57.6,  
        "maxOverTime": 59.2,  
        "minOverTime": 50.5  
    },  
    "aqiMajorPollutant": "no2",  
    "areaServed": "Bangalore",  
    "arsenicTSA": {  
        "avgOverTime": 0.4,  
        "instValue": 0.35,  
        "maxOverTime": 0.44,  
        "minOverTime": 0.29  
    },  
    "atmosphericPressure": 633.2,  
    "atmosphericPressureTSA": {  
        "avgOverTime": 968.3,  
        "instValue": 982.9,  
        "maxOverTime": 982.7,  
        "minOverTime": 961.9  
    },  
    "bapTSA": {  
        "avgOverTime": 492.1,  
        "instValue": 439.1,  
        "maxOverTime": 573.7,  
        "minOverTime": 398.7  
    },  
    "benzeneTSA": {  
        "avgOverTime": 266.7,  
        "instValue": 321.7,  
        "maxOverTime": 576.9,  
        "minOverTime": 210.1  
    },  
    "co2TSA": {  
        "avgOverTime": 318.51,  
        "instValue": 320.4,  
        "maxOverTime": 390.2,  
        "minOverTime": 302.6  
    },  
    "coTSA": {  
        "avgOverTime": 3.51,  
        "instValue": 4.0,  
        "maxOverTime": 8.9,  
        "minOverTime": 3.4  
    },  
    "dataProvider": "",  
    "dateCreated": {  
        "@type": "DateTime",  
        "@value": "2017-12-31T03:39:27Z"  
    },  
    "dateModified": {  
        "@type": "DateTime",  
        "@value": "2021-12-22T04:21:57Z"  
    },  
    "description": "Air quality monitoring",  
    "deviceInfo": {  
        "RFID": "AB463478",  
        "deviceBatteryStatus": "Connected",  
        "deviceID": "12345",  
        "deviceList": "12",  
        "deviceModel": {  
            "areaServed": "Agartala",  
            "brandName": "Climo",  
            "manufacturerName": "Bosch",  
            "modelName": "sensor",  
            "modelURL": "www.boschclimo.com"  
        },  
        "deviceName": "Climo",  
        "deviceSimNumber": "12345678",  
        "measurand": "",  
        "refDevice": "urn:ngsi-ld:device:12"  
    },  
    "deviceStatus": "ACTIVE",  
    "illuminance": 3319.41,  
    "location": {  
        "coordinates": [  
            12.979,  
            77.591  
        ],  
        "type": "Point"  
    },  
    "name": "",  
    "nh3TSA": {  
        "avgOverTime": 865.1,  
        "instValue": 900.2,  
        "maxOverTime": 990.8,  
        "minOverTime": 834.7  
    },  
    "nickelTSA": {  
        "avgOverTime": 434.0,  
        "instValue": 527.2,  
        "maxOverTime": 559.6,  
        "minOverTime": 132.2  
    },  
    "no2TSA": {  
        "avgOverTime": 409.7,  
        "instValue": 511.0,  
        "maxOverTime": 611.5,  
        "minOverTime": 242.4  
    },  
    "noTSA": {  
        "avgOverTime": 3.65,  
        "instValue": 3.6,  
        "maxOverTime": 4.8,  
        "minOverTime": 2.7  
    },  
    "o2TSA": {  
        "avgOverTime": 18.1,  
        "instValue": 18.0,  
        "maxOverTime": 18.2,  
        "minOverTime": 18.0  
    },  
    "o3TSA": {  
        "avgOverTime": 218.8,  
        "instValue": 173.1,  
        "maxOverTime": 236.4,  
        "minOverTime": 167.7  
    },  
    "observationDateTime": {  
        "@type": "DateTime",  
        "@value": "2020-09-16T11:00:00+05:30"  
    },  
    "owner": [  
        "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
        "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
    ],  
    "pbTSA": {  
        "avgOverTime": 473.0,  
        "instValue": 391.0,  
        "maxOverTime": 542.1,  
        "minOverTime": 287.5  
    },  
    "pm10TSA": {  
        "avgOverTime": 847.3,  
        "instValue": 439.1,  
        "maxOverTime": 568.1,  
        "minOverTime": 54.3  
    },  
    "pm25TSA": {  
        "avgOverTime": 28.3,  
        "instValue": 56.6,  
        "maxOverTime": 56.8,  
        "minOverTime": 10.1  
    },  
    "precipitation": 846.0,  
    "relativeHumidityTSA": {  
        "avgOverTime": 326.3,  
        "instValue": 401.2,  
        "maxOverTime": 599.3,  
        "minOverTime": 211.6  
    },  
    "seeAlso": [  
        "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
        "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
    ],  
    "so2TSA": {  
        "avgOverTime": 3.65,  
        "instValue": 3.5,  
        "maxOverTime": 3.72,  
        "minOverTime": 2.9  
    },  
    "solarRadiation": 3.65,  
    "source": "Bangalore Smart city",  
    "uvTSA": {  
        "avgOverTime": 6.0,  
        "instValue": 8.2,  
        "maxOverTime": 8.3,  
        "minOverTime": 5.7  
    },  
    "versionInfo": {  
        "comments": "Version 1",  
        "endDateTime": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        },  
        "startDateTime": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        },  
        "versionName": "Version 1"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 大気品質モニタリング NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の AirQualityMonitoring の例です。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AirQualityMonitoring:id:ARET:00795717",  
    "type": "AirQualityMonitoring",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Avenue Road",  
            "addressLocality": "Bangalore",  
            "addressRegion": "Karnataka",  
            "addressCountry": "India",  
            "postalCode": "110001",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "airQualityIndex": {  
        "type": "Property",  
        "value": 90  
    },  
    "airQualityLevel": {  
        "type": "Property",  
        "value": "SATISFACTORY"  
    },  
    "airTemperatureTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 23.1,  
            "minOverTime": 12.7,  
            "maxOverTime": 32.8,  
            "instValue": 30.8  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "EnvAQM sampling"  
    },  
    "ambientNoiseTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 57.9,  
            "minOverTime": 50.5,  
            "maxOverTime": 59.2,  
            "instValue": 57.6  
        }  
    },  
    "aqiMajorPollutant": {  
        "type": "Property",  
        "value": "no2"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Bangalore"  
    },  
    "arsenicTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 0.4,  
            "minOverTime": 0.29,  
            "maxOverTime": 0.44,  
            "instValue": 0.35  
        }  
    },  
    "atmosphericPressure": {  
        "type": "Property",  
        "value": 633.2  
    },  
    "atmosphericPressureTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 968.3,  
            "minOverTime": 961.9,  
            "maxOverTime": 982.7,  
            "instValue": 982.9  
        }  
    },  
    "bapTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 492.1,  
            "minOverTime": 398.7,  
            "maxOverTime": 573.7,  
            "instValue": 439.1  
        }  
    },  
    "benzeneTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 266.7,  
            "minOverTime": 210.1,  
            "maxOverTime": 576.9,  
            "instValue": 321.7  
        }  
    },  
    "co2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 318.51,  
            "minOverTime": 302.6,  
            "maxOverTime": 390.2,  
            "instValue": 320.4  
        }  
    },  
    "coTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.51,  
            "minOverTime": 3.4,  
            "maxOverTime": 8.9,  
            "instValue": 4.0  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-12-31T03:39:27Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-12-22T04:21:57Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Air quality monitoring"  
    },  
    "deviceInfo": {  
        "type": "Property",  
        "value": {  
            "deviceList": "12",  
            "deviceBatteryStatus": "Connected",  
            "deviceName": "Climo",  
            "deviceID": "12345",  
            "RFID": "AB463478",  
            "measurand": "",  
            "deviceSimNumber": "12345678",  
            "deviceModel": {  
                "brandName": "Climo",  
                "manufacturerName": "Bosch",  
                "modelName": "sensor",  
                "modelURL": "www.boschclimo.com",  
                "areaServed": "Agartala"  
            },  
            "refDevice": "urn:ngsi-ld:device:12"  
        }  
    },  
    "deviceStatus": {  
        "type": "Property",  
        "value": "ACTIVE"  
    },  
    "illuminance": {  
        "type": "Property",  
        "value": 3319.41  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                12.979,  
                77.591  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": ""  
    },  
    "nh3TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 865.1,  
            "minOverTime": 834.7,  
            "maxOverTime": 990.8,  
            "instValue": 900.2  
        }  
    },  
    "nickelTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 434.0,  
            "minOverTime": 132.2,  
            "maxOverTime": 559.6,  
            "instValue": 527.2  
        }  
    },  
    "no2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 409.7,  
            "minOverTime": 242.4,  
            "maxOverTime": 611.5,  
            "instValue": 511.0  
        }  
    },  
    "noTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.65,  
            "minOverTime": 2.7,  
            "maxOverTime": 4.8,  
            "instValue": 3.6  
        }  
    },  
    "o2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 18.1,  
            "minOverTime": 18.0,  
            "maxOverTime": 18.2,  
            "instValue": 18.0  
        }  
    },  
    "o3TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 218.8,  
            "minOverTime": 167.7,  
            "maxOverTime": 236.4,  
            "instValue": 173.1  
        }  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-16T11:00:00+05:30"  
        }  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:AirQualityMonitoring:items:WCBR:34036943",  
            "urn:ngsi-ld:AirQualityMonitoring:items:PLLV:16542546"  
        ]  
    },  
    "pbTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 473.0,  
            "minOverTime": 287.5,  
            "maxOverTime": 542.1,  
            "instValue": 391.0  
        }  
    },  
    "pm10TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 847.3,  
            "minOverTime": 54.3,  
            "maxOverTime": 568.1,  
            "instValue": 439.1  
        }  
    },  
    "pm25TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 28.3,  
            "minOverTime": 10.1,  
            "maxOverTime": 56.8,  
            "instValue": 56.6  
        }  
    },  
    "precipitation": {  
        "type": "Property",  
        "value": 846.0  
    },  
    "relativeHumidityTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 326.3,  
            "minOverTime": 211.6,  
            "maxOverTime": 599.3,  
            "instValue": 401.2  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:AirQualityMonitoring:items:FCTF:59597941",  
            "urn:ngsi-ld:AirQualityMonitoring:items:JAYJ:76906163"  
        ]  
    },  
    "so2TSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 3.65,  
            "minOverTime": 2.9,  
            "maxOverTime": 3.72,  
            "instValue": 3.5  
        }  
    },  
    "solarRadiation": {  
        "type": "Property",  
        "value": 3.65  
    },  
    "source": {  
        "type": "Property",  
        "value": "Bangalore Smart city"  
    },  
    "uvTSA": {  
        "type": "Property",  
        "value": {  
            "avgOverTime": 6.0,  
            "minOverTime": 5.7,  
            "maxOverTime": 8.3,  
            "instValue": 8.2  
        }  
    },  
    "versionInfo": {  
        "type": "Property",  
        "value": {  
            "startDateTime": {  
                "@type": "DateTime",  
                "@value": "2020-09-16T11:00:00+05:30"  
            },  
            "endDateTime": {  
                "@type": "DateTime",  
                "@value": "2020-09-16T11:00:00+05:30"  
            },  
            "versionName": "Version 1",  
            "comments": "Version 1"  
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
