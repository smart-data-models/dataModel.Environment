Entité : FloodMonitoring  
========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/FloodMonitoring/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Modèle de données de capteur d'inondation destiné à représenter le niveau d'inondation par rapport au débit/niveau d'eau à une certaine masse d'eau (rivière, lac, etc.) **.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alertLevel`: Valeur seuil de niveau d'alerte de référence fixée pour la station de détection correspondant à cette observation. Un signal d'alerte est généré si le niveau actuel franchit la valeur seuil du niveau d'alerte.  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `currentLevel`: Niveau d'inondation actuel indiqué par la station de détection correspondant à cette observation, calculé à l'aide de referenceLevel et measuredDistance(currentLevel = referenceLevel - measuredDistance).  - `dangerLevel`: Valeur de référence du seuil de niveau de danger fixée pour la station de détection correspondant à cette observation. L'état du niveau d'inondation est marqué comme dangereux si le niveau actuel franchit la valeur seuil du niveau de danger.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `floodLevelStatus`: Indication de l'état du niveau d'inondation donné par le dispositif de détection d'inondation. L'état est marqué Danger si le niveau actuel est supérieur à la valeur seuil du niveau de danger.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `measuredDistance`: Décrit la distance mesurée par le capteur, de l'extrémité du capteur à la surface supérieure de l'eau.  - `name`: Le nom de cet élément.  - `observationDateTime`: Dernière heure d'observation signalée.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `referenceLevel`: Décrit la distance verticale entre le lit de la rivière et l'extrémité du capteur.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `stationID`: Un identifiant anonyme unique attribué à la station correspondant à cette observation.  - `type`: Il doit s'agir de FloodMonitoring. Type d'entité NGSI.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FloodMonitoring:    
  description: 'Flood Sensor Data Model intended to represent the level of flooding w.r.t water flow/level at a certain water mass(river, lake,etc.)..'    
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
    alertLevel:    
      description: 'Reference alert level threshold value set for the sensing station corresponding to this observation. An Alert signal is generated if the current level crosses the alert level threshold value.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    currentLevel:    
      description: 'Current flooding level indicated by the sensing station corresponding to this observation, computed using referenceLevel and measuredDistance(currentLevel = referenceLevel - measuredDistance).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dangerLevel:    
      description: 'Reference danger level threshold value set for the sensing station corresponding to this observation. Flood level status is marked danger if the current level crosses the danger level threshold value.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    floodLevelStatus:    
      description: 'Flood level status indication given by the flood sensing device. The status is marked Danger if the current level is higher than the danger level threshold value.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &floodmonitoring_-_properties_-_owner_-_items_-_anyof    
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
    measuredDistance:    
      description: 'Describes the distance measured by the sensor, from the sensor tip to the upper surface of water.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *floodmonitoring_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    referenceLevel:    
      description: 'Describes the vertical distance from river bed to sensor tip.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    stationID:    
      description: 'A unique anonymous identifier assigned to the station corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be FloodMonitoring. NGSI Entity type.'    
      enum:    
        - FloodMonitoring    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/FloodMonitoring/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/FloodMonitoring/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### FloodMonitoring NGSI-v2 valeurs-clés Exemple  
Voici un exemple de FloodMonitoring au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": 10.00,  
  "measuredDistance": 3.22,  
  "currentLevel": 0.98,  
  "dangerLevel": 25.00,  
  "observationDateTime": "2020-09-16T13:30:00+05:30",  
  "referenceLevel": 4.2,  
  "floodLevelStatus": "Normal",  
  "stationID": "FWR013"  
}  
```  
#### FloodMonitoring NGSI-v2 normalisé Exemple  
Voici un exemple de FloodMonitoring au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": {  
    "type": "Property",  
    "value": 11.00  
  },  
  "measuredDistance": {  
    "type": "Property",  
    "value": 4.22  
  },  
  "currentLevel": {  
    "type": "Property",  
    "value": 1.98  
  },  
  "dangerLevel": {  
    "type": "Property",  
    "value": 26.00  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": "2020-09-16T13:30:00+05:30"  
  },  
  "referenceLevel": {  
    "type": "Property",  
    "value": 4.2  
  },  
  "floodLevelStatus": {  
    "type": "Property",  
    "value": "Normal"  
  },  
  "stationID": {  
    "type": "Property",  
    "value": "FWR013"  
  }  
}  
```  
#### FloodMonitoring NGSI-LD key-values Exemple  
Voici un exemple d'un FloodMonitoring au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": {  
    "type": "Property",  
    "value": 11.0,  
    "unitCode": "MTR"  
  },  
  "measuredDistance": {  
    "type": "Property",  
    "value": 4.22,  
    "unitCode": "MTR"  
  },  
  "currentLevel": {  
    "type": "Property",  
    "value": 1.98,  
    "unitCode": "MTR"  
  },  
  "dangerLevel": {  
    "type": "Property",  
    "value": 26.0,  
    "unitCode": "MTR"  
  },  
  "observationDateTime": {  
    "type": "string",  
    "format": "date-time",  
    "value": "2020-09-16T13:30:00+05:30"  
  },  
  "referenceLevel": {  
    "type": "Property",  
    "value": 4.2,  
    "unitCode": "MTR"  
  },  
  "floodLevelStatus": {  
    "type": "string",  
    "value": "Normal"  
  },  
  "stationID": {  
    "type": "string",  
    "value": "FWR013"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Surveillance des crues NGSI-LD normalisé Exemple  
Voici un exemple de FloodMonitoring au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "alertLevel": 10.0,  
  "measuredDistance": 3.22,  
  "currentLevel": 0.98,  
  "dangerLevel": 25.0,  
  "observationDateTime": "2020-09-16T13:30:00+05:30",  
  "referenceLevel": 4.2,  
  "floodLevelStatus": "Normal",  
  "stationID": "FWR013"  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude