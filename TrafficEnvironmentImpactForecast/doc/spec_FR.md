[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : TrafficEnvironmentImpactForecast  
=========================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/TrafficEnvironmentImpactForecast/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Incidence environnementale du trafic basée sur les prévisions de trafic des véhicules et leurs caractéristiques d'émission**.  
version : 0.0.1  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `co2`: La concentration attendue des émissions de C02  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateIssued`: La date et l'heure auxquelles la prévision a été émise par le prestataire de services, au format ISO8601 UTC.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `traffic`: propriété  - `type`: Type de NGSI. Il doit s'agir de TrafficEnvironmentImpactForecast.  - `validFrom`: Le début de la période de validité de cette prévision au format ISO8601.  - `validTo`: La fin de la période de validité de cette prévision au format ISO8601.  - `validity`: Comprend la période de validité de cette prévision sous forme d'intervalle de temps ISO8601.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      description: property    
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
    type:    
      description: 'NGSI type. it has to be TrafficEnvironmentImpactForecast'    
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
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### Prévision de l'impact sur l'environnement du trafic (TrafficEnvironmentImpactForecast) Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de TrafficEnvironmentImpactForecast au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Prévision de l'impact du trafic sur l'environnement NGSI-v2 normalisée Exemple  
Voici un exemple de TrafficEnvironmentImpactForecast au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Prévision de l'impact sur l'environnement et le trafic - Valeurs clés NGSI-LD Exemple  
Voici un exemple de TrafficEnvironmentImpactForecast au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  ],  
  "@context": [  
    "https://smartdatamodels.org/dataModel.Environment/context.jsonld"  
  ]  
}  
```  
#### Prévision de l'impact sur le trafic et l'environnement NGSI-LD normalisé Exemple  
Voici un exemple de TrafficEnvironmentImpactForecast au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
      "streetAddress": "Rue Frédéric Mistral",  
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
    "https://smartdatamodels.org/dataModel.Environment/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
