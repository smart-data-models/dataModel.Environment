<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

NightSkyQuality:    
  description: Data regarding the observed sky quality and the status of the measuring device.    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    ambientTemperature:    
      description: 'Property. Temperature measurement. Units:''degrees Celsius (C)'''    
      type: number    
      x-ngsi:    
        type: Property    
        units: degrees Celsius (C)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    battery:    
      description: 'Property. Voltage provided by the battery. Changes relative to the  Units:''millivolts (mV)'''    
      type: number    
      x-ngsi:    
        type: Property    
        units: Changes relative to the  millivolts (mV)    
    batteryLevel:    
      description: 'Property. Model:''https://schema.org/Number''. Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - maximum: -1    
          minimum: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    clouds:    
      description: Property. Qualitative indicator of the amount of cloud cover.    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      anyOf: &nightskyquality_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *nightskyquality_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
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
    sigmaMagnitude:    
      description: 'Property. Unitless parameter, expressing the Standard Deviation corresponding to the measurement of sky magnitude.'    
      type: number    
      x-ngsi:    
        type: Property    
    skyMagnitude:    
      description: 'Property. Unitless parameter: the measurement taken by the device, corresponding to the apparent magnitude of the night sky (that is, its brightness).'    
      type: number    
      x-ngsi:    
        type: Property    
    skyTemperature:    
      description: 'Property. Direct measurement of the sky temperature, as taken by the device. Units:''degrees Celsius (C)'''    
      type: number    
      x-ngsi:    
        type: Property    
        units: degrees Celsius (C)    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NightSkyQuality/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.NightSkyQuality/NightSkyQuality/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "DTI-036",  
  "type": "NightSkyQuality",  
  "ambientTemperature": 10.17,  
  "battery": 3691,  
  "clouds": "Despejado",  
  "dateCreated": "2023-03-15T14:00:00.000Z",  
  "dateModified": "2023-03-15T14:10:00.000Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "sigmaMagnitude": 0.003,  
  "skyMagnitude": 19.4,  
  "skyTemperature": -6.23  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "DTI-036",  
  "type": "NightSkyQuality"  
  "ambientTemperature": {  
    "type": "Number",  
    "value": 10.17  
  },  
  "battery": {  
    "type": "Number",  
    "value": 3691  
  },  
  "clouds": {  
    "type": "string",  
    "value": "Despejado"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-03-15T14:00:00.000Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-03-15T14:10:00.000Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "sigmaMagnitude": {  
    "type": "number",  
    "value": 0.003  
  },  
  "skyMagnitude": {  
    "type": "number",  
    "value": 19.4  
  },  
  "skyTemperature": {  
    "type": "number",  
    "value": -6.23  
  }  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "DTI-036",  
  "type": "NightSkyQuality",  
  "ambientTemperature": 10.17,  
  "battery": 3691,  
  "clouds": "Despejado",  
  "dateCreated": "2023-03-15T14:00:00.000Z",  
  "dateModified": "2023-03-15T14:10:00.000Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "sigmaMagnitude": 0.003,  
  "skyMagnitude": 19.4,  
  "skyTemperature": -6.23,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Environment/NightSkyQuality/schema.json"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "DTI-036",  
  "type": "NightSkyQuality",  
  "ambientTemperature": {  
    "type": "Property",  
    "value": 10.17  
  },  
  "battery": {  
    "type": "Property",  
    "value": 3691  
  },  
  "clouds": {  
    "type": "Property",  
    "value": "Despejado"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-03-15T14:00:00.000Z"  
    }  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-03-15T14:10:00.000Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "sigmaMagnitude": {  
    "type": "Property",  
    "value": 0.003  
  },  
  "skyMagnitude": {  
    "type": "Property",  
    "value": 19.4  
  },  
  "skyTemperature": {  
    "type": "Property",  
    "value": -6.23  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Environment/NightSkyQuality/schema.json"  
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
