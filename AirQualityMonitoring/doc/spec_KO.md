<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

===============
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `airQualityIndex[number]`: 관측된 공기질에 대한 종합 공기질 지수(AQI)  . Model: [https://schema.org/Number](https://schema.org/Number)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `alternateName[string]`: 이 항목의 대체 이름  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `aqiMajorPollutant[string]`: 대기질 지수(AQI)의 주요 오염 물질. 열거형:'비소, bap, 벤젠, co2, nh3, no, no2, o2, o3, so2, pb'  . Model: [https://schema.org/Text](https://schema.org/Text)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `atmosphericPressure[number]`: 관측된 공기(대기압 또는 기압) 압력  . Model: [https://schema.org/Number](https://schema.org/Number)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `bapTSA[object]`: 벤조(a)피렌 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `benzeneTSA[object]`: 벤젠 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `co2TSA[object]`: 이산화탄소 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `coTSA[object]`: 일산화탄소 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  
	- `deviceBatteryStatus[string]`: 보고 장치의 배터리 충전 상태(연결됨, 연결 해제됨)를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: 이 관측에 해당하는 물리적 센서/측정 스테이션의 장치 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceList[string]`: 이 관찰에 해당하는 장치 부품 번호 및 하위 장치 정보  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 고려 중인 장치, 센서 또는 시스템의 정보를 설명합니다.    
	- `deviceName[string]`: 이 관측에 해당하는 센서 장치/스테이션의 장치 이름 또는 스테이션 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 폐기물 관리 차량에 있는 기기의 심 번호를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 장치에서 감지/관찰/측정된 속성/특성  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `refDevice[*]`: 엔티티의 고유 식별자    
- `deviceStatus[string]`: 물리적 장치의 상태를 나타냅니다.  . Model: [https://schema.org/Text](https://schema.org/Text)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `nickelTSA[object]`: 니켈 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `no2TSA[object]`: 이산화질소 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `noTSA[object]`: 일산화질소 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `o2TSA[object]`: 산소 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `o3TSA[object]`: 오존 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `pm10TSA[object]`: 직경 10마이크로미터 이하의 대기 중 미립자 물질 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `pm25TSA[object]`: 직경 25마이크로미터 이하의 대기 중 미립자 물질 시계열 집계  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `precipitation[number]`: 주어진 기간 동안 관측된 강수량/강우량 수준  . Model: [https://schema.org/Number](https://schema.org/Number)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `solarRadiation[number]`: 순간 일사량 측정(kW/m2)  . Model: [http://schema.org/Number](http://schema.org/Number)
	- `instValue[number]`: 시간적 처리의 즉각적인 가치    
	- `maxOverTime[number]`: 시간 경과에 따른 시간 처리의 최대값    
	- `minOverTime[number]`: 시간 경과에 따른 시간 처리의 최소값    
- `versionInfo[object]`: 이 관찰에 해당하는 버전 정보  
	- `endDateTime[date-time]`: 이 관측에 해당하는 보고된 종료 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
	- `startDateTime[date-time]`: 이 관측에 해당하는 보고된 시작 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
	- `versionName[string]`: 이 관찰에 해당하는 버전 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `windType[string]`: 지난 24시간 동안 지배적인 바람 유형    
<!-- /30-PropertiesList -->
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
