<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: MosquitoDensity    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Environment/blob/master/MosquitoDensity/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Datenmodell für die Dichte von Stechmücken in Städten.**    
Version: 0.0.1    
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
- `airTemperature[object]`: Beobachteter Wert der Lufttemperatur. Value ist ein Objekt, das Attribute enthält, die statistische Aggregate darstellen, die aus vergangenen Daten abgeleitet wurden  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataDescriptor[uri]`: URI, die auf die Daten-Deskriptor-Entität verweist  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `deviceInfo[object]`: Informationen über das mit den Beobachtungen verbundene Gerät  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: Gibt den Batterieladestatus des meldenden Geräts an (verbunden, getrennt)  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceId[string]`: Geräte-ID des physischen Sensors/der Messstation, der/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: Beschreibt die Informationen über das betreffende Gerät, den Sensor oder das System  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceName[string]`: Gerätename oder Stationsname des Sensorgeräts/der Station, das/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: Gibt die Sim-Nummer des Geräts im Entsorgungsfahrzeug an  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: Vom Gerät erfasste/beobachtete/gemessene Eigenschaft/Eigenschaften  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mosquitoDensity[object]`: Die binomiale (oder) zoologische Nomenklatur der Stechmückenart und ihre Anzahl, wie sie von dem Gerät identifiziert wurde, das dieser Beobachtung entspricht  	- `femaleSpeciesCount[number]`: Die Gesamtzahl der weiblichen Stechmücken der vom Gerät identifizierten Art      
	- `maleSpeciesCount[number]`: Die Gesamtzahl der männlichen Stechmücken der vom Gerät identifizierten Art      
	- `mosquitoSpecies[string]`: Die binomische/zoologische Nomenklatur der mit dem Gerät identifizierten Mückenart      
- `name[string]`: Der Name dieses Artikels  - `observationDateTime[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `precipitation[number]`: Beobachteter Niederschlag/Niederschlagsmenge über einen bestimmten Zeitraum  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Entitätstyp. Es muss MosquitoDensity sein  <!-- /30-PropertiesList -->    
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
## Beispiel-Nutzlasten    
#### MosquitoDensity NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine MosquitoDensity im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### MosquitoDensity NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine MosquitoDensity im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "ngsi-ld:MosquitoDensity:001",  
  "type": "MosquitoDensity",  
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
#### MosquitoDensity NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine MosquitoDensity im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### MosquitoDensity NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine MosquitoDensity im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
