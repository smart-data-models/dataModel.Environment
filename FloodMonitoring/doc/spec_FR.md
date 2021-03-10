Entité : FloodMonitoring  
========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Environment/blob/master/FloodMonitoring/LICENSE.md)  
Description globale : **Modèle de données de capteur d'inondation destiné à représenter le niveau d'inondation du débit/niveau d'eau à une certaine masse d'eau (rivière, lac, etc.).  

## Liste des biens  

- `address`: L'adresse postale  - `alertLevel`: Valeur seuil du niveau d'alerte de référence fixée pour la station de détection correspondant à cette observation. Un signal d'alerte est généré si le niveau actuel franchit la valeur seuil du niveau d'alerte.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `currentLevel`: Niveau d'inondation actuel indiqué par la station de détection correspondant à cette observation, calculé en utilisant le Niveau de référence et la Distance mesurée (Niveau actuel = Niveau de référence - Distance mesurée).  - `dangerLevel`: Valeur seuil du niveau de danger de référence fixée pour la station de détection correspondant à cette observation. L'état du niveau d'inondation est considéré comme un danger marqué si le niveau actuel dépasse la valeur seuil du niveau de danger.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `floodLevelStatus`: Indication de l'état du niveau d'inondation donnée par le dispositif de détection des inondations. L'état est marqué Danger si le niveau actuel est supérieur à la valeur seuil du niveau de danger.  - `id`: Identifiant unique de l'entité  - `location`:   - `measuredDistance`: Décrit la distance mesurée par le capteur, de la pointe du capteur à la surface supérieure de l'eau.  - `name`: Le nom de cet article.  - `observationDateTime`: Dernière heure d'observation signalée.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `referenceLevel`: Décrit la distance verticale entre le lit de la rivière et la pointe du capteur.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `stationID`: Un identifiant anonyme unique attribué à la station correspondant à cette observation.  - `type`: Il doit s'agir d'un FloodMonitoring. Type d'entité NGSI.    
Propriétés requises  
- `id`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alertLevel:    
      description: 'Reference alert level threshold value set for the sensing station corresponding to this observation. An Alert signal is generated if the current level crosses the alert level threshold value.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    currentLevel:    
      description: 'Current flooding level indicated by the sensing station corresponding to this observation, computed using referenceLevel and measuredDistance(currentLevel = referenceLevel - measuredDistance).'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dangerLevel:    
      description: 'Reference danger level threshold value set for the sensing station corresponding to this observation. Flood level status is marked danger if the current level crosses the danger level threshold value.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    floodLevelStatus:    
      description: 'Flood level status indication given by the flood sensing device. The status is marked Danger if the current level is higher than the danger level threshold value.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    measuredDistance:    
      description: 'Describes the distance measured by the sensor, from the sensor tip to the upper surface of water.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *floodmonitoring_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    referenceLevel:    
      description: 'Describes the vertical distance from river bed to sensor tip.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    stationID:    
      description: 'A unique anonymous identifier assigned to the station corresponding to this observation.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'It has to be FloodMonitoring. NGSI Entity type.'    
      enum:    
        - FloodMonitoring    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### FloodMonitoring NGSI V2 key-values Exemple  
Voici un exemple de FloodMonitoring au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
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
#### FloodMonitoring NGSI V2 normalisé Exemple  
Voici un exemple de surveillance des inondations au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de FloodMonitoring au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
	"@context": ["https://schema.lab.fiware.org/ld/context",  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	],  
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
#### Surveillance des inondations NGSI-LD normalisé Exemple  
Voici un exemple d'un FloodMonitoring au format JSON-LD tel que normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FloodMonitoring:Pune-NoiseLevelObserved",  
  "type": "FloodMonitoring",  
  "alertLevel": {  
    "type": "Property",  
    "value": 11.00,  
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
    "value": 26.00,  
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
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
