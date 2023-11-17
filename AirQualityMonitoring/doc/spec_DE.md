<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: AirQualityMonitoring    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/AirQualityMonitoring/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Datenmodell für die Überwachung der Luftqualität (AQM).**    
Version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `airQualityIndex[number]`: Gesamtluftqualitätsindex (AQI) für die beobachtete Luftqualität  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityLevel[string]`: Angabe der Luftqualitätskategorie. Qualitative Stufe, die von den örtlichen Gesundheitsbehörden festgelegt wird. Zum Beispiel "GUT", "MÄSSIG", "SCHLECHT", "GESUNDHEITLICHER Zustand", "SCHWER", "GEFÄHRLICH" usw.  . Model: [https://schema.org/Text](https://schema.org/Text)- `airTemperatureTSA[object]`: Aggregation von Lufttemperatur-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `ambientNoiseTSA[object]`: Aggregation von Umgebungslärm-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `aqiMajorPollutant[string]`: Hauptschadstoff im Luftqualitätsindex (AQI). Enum:'Arsen, bap, Benzol, co2, nh3, no, no2, o2, o3, so2, pb'  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arsenicTSA[object]`: Aggregation von Arsen-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `atmosphericPressure[number]`: Beobachteter (atmosphärischer oder barometrischer) Luftdruck  . Model: [https://schema.org/Number](https://schema.org/Number)- `atmosphericPressureTSA[object]`: Aggregation von Zeitreihen zum Atmosphärendruck  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `bapTSA[object]`: Benzo(a)pyren-Zeitreihenaggregation  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `benzeneTSA[object]`: Aggregation von Benzol-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `co2TSA[object]`: Aggregation von Kohlendioxid-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `coTSA[object]`: Aggregation von Kohlenmonoxid-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `deviceInfo[object]`: Informationen über das mit den Beobachtungen verbundene Gerät  	- `RFID[string]`: Gibt die ID des RFID-Lesegeräts an  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceBatteryStatus[string]`: Gibt den Batterieladestatus des meldenden Geräts an (verbunden, getrennt)  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceID[string]`: Geräte-ID des physischen Sensors/der Messstation, der/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceList[string]`: Informationen über die Teilenummer des Geräts und die Untergeräte, die dieser Beobachtung entsprechen  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: Beschreibt die Informationen über das betreffende Gerät, den Sensor oder das System      
	- `deviceName[string]`: Gerätename oder Stationsname des Sensorgeräts/der Station, das/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: Gibt die Sim-Nummer des Geräts im Entsorgungsfahrzeug an  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: Vom Gerät erfasste/beobachtete/gemessene Eigenschaft/Eigenschaften  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `deviceStatus[string]`: Zeigt den Status des physischen Geräts oder der physischen Geräte an.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `illuminance[number]`: Gemessene Beleuchtungsstärke  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `nh3TSA[object]`: Aggregation von Ammoniak-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `nickelTSA[object]`: Nickel-Zeitreihenaggregation  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `no2TSA[object]`: Aggregation von Stickstoffdioxid-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `noTSA[object]`: Aggregation von Stickstoffmonoxid-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `o2TSA[object]`: Aggregation von Sauerstoff-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `o3TSA[object]`: Aggregation von Ozonzeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `observationDateTime[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pbTSA[object]`: Aggregation von Vorlaufzeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `pm10TSA[object]`: Partikel in der Luft mit einem Durchmesser von 10 Mikrometern oder weniger Zeitreihenaggregation  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `pm25TSA[object]`: Partikel in der Luft mit einem Durchmesser von 25 Mikrometern oder weniger Zeitreihenaggregation  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `precipitation[number]`: Beobachteter Niederschlag/Niederschlagsmenge über einen bestimmten Zeitraum  . Model: [https://schema.org/Number](https://schema.org/Number)- `relativeHumidityTSA[object]`: Aggregation von Zeitreihen der relativen Luftfeuchtigkeit  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `so2TSA[object]`: Aggregation von Schwefeldioxid-Zeitreihen  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `solarRadiation[number]`: Momentane Sonneneinstrahlung gemessen in kW/m2  . Model: [http://schema.org/Number](http://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Typ. es muss AirQualityMonitoring sein  - `uvTSA[object]`: Aggregation von Zeitreihen der ultravioletten Strahlung  	- `averageValue[number]`: Durchschnittswert der zeitlichen Verarbeitung über die Zeit      
	- `instValue[number]`: Unmittelbarer Wert der zeitlichen Verarbeitung      
	- `maxOverTime[number]`: Maximaler Wert der zeitlichen Verarbeitung über die Zeit      
- `versionInfo[object]`: Informationen zur Version, die dieser Beobachtung entspricht  	- `comments[string]`: Entsprechende Benutzerkommentare zu dieser Beobachtung  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `endDateTime[date-time]`: Gemeldete Endzeit für diese Beobachtung  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)    
	- `startDateTime[date-time]`: Gemeldete Startzeit, die dieser Beobachtung entspricht  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)    
	- `versionName[string]`: Name der Version, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### AirQualityMonitoring NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein AirQualityMonitoring im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.    
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
#### AirQualityMonitoring NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein AirQualityMonitoring im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirQualityMonitoring:id:MUTW:63473748",  
  "type": "AirQualityMonitoring",  
  "dateCreated": {  
    "type": "DateTime",  
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
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AirQualityMonitoring:items:PDSP:96970072",  
      "urn:ngsi-ld:AirQualityMonitoring:items:FTKL:60685543"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
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
    "type": "Number",  
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
#### AirQualityMonitoring NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein AirQualityMonitoring im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.    
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
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AirQualityMonitoring NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein AirQualityMonitoring im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
