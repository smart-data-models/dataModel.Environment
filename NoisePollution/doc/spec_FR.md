<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entité : NoisePollution  
=======================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licence ouverte] (https://github.com/smart-data-models//dataModel.Environment/blob/master/NoisePollution/LICENSE.md)  

[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Description globale : **Le modèle de données sur la pollution sonore fusionne des mesures de bruit spécifiques et ponctuelles (provenant, par exemple, d'entités NoiseLevelObservation) en paramètres moyens se rapportant aux zones urbaines, fournissant des données plus liées à la ville sur l'état et l'évolution de la pollution sonore**.  

version : 0.0.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste des propriétés  


<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `LAeq2[number]`: Niveau sonore moyen sur les 2 dernières heures  
- `LAmax2[number]`: Niveau sonore maximal enregistré au cours des 2 dernières heures  
- `alternateName[string]`: Un nom alternatif pour cet élément  
- `buildingsType[string]`: Type de bâtiments prédominants dans la zone de mesure au moment de l'installation du capteur.  
- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  
- `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  
- `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  
- `dateObservedFrom[string]`: Date et heure de début de la période d'observation  
- `dateObservedTo[string]`: Date et heure de fin de la période d'observation  
- `description[string]`: Une description de cet article  
- `groundType[string]`: Type de sol prédominant dans la zone de mesure lors de l'installation du capteur  
- `id[*]`: Identifiant unique de l'entité  
- `name[string]`: Le nom de cet élément.  
- `noiseAnnoyanceIndex[number]`: Indice (1 à 10) selon le niveau de gêne sonore  
- `noiseOrigin[string]`: Origine principale (source) du bruit enregistré lors de l'installation du capteur  
- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  
- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  
- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  
- `type[string]`: Type de NGSI. Il doit s'agir de NoisePollution.  
- `wallsType[string]`: Types de matériaux de façade dominants dans la zone de mesure lors de l'installation du capteur  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Propriétés requises  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Description des propriétés du modèle de données  

Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
NoisePollution:    
  description: 'Noise Pollution data model merges specific and punctual noise measurements (coming, e.g. from NoiseLevelObservation entities) into average parameters referred to city areas, providing a more city-related data about noise pollution status and evolution.'    
  properties:    
    LAeq2:    
      description: 'Average sound level over the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
    LAmax2:    
      description: 'Maximum sound level recorded for the last 2 hours'    
      type: number    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    buildingsType:    
      description: 'Type of predominant buildings within the measurement area at installation of the sensor'    
      type: string    
      x-ngsi:    
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
    dateObservedFrom:    
      description: 'Observation period start date and time'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'End date and time of the observation period'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    groundType:    
      description: 'Type of predominant ground in the measurement area at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &noisepollution_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    noiseAnnoyanceIndex:    
      description: 'Index (1 to 10) according to noise annoyance level'    
      maximum: 10    
      minimum: 1    
      type: number    
      x-ngsi:    
        type: Property    
    noiseOrigin:    
      description: 'Main origin (source) of the recorded noise at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *noisepollution_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI type. it has to be NoisePollution'    
      enum:    
        - NoisePollution    
      type: string    
      x-ngsi:    
        type: Property    
    wallsType:    
      description: 'Facade material types dominant in the measurement area at installation of the sensor'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Environment/blob/master/NoisePollution/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/NoisePollution/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Exemples de charges utiles  

#### NoisePollution Valeurs-clés NGSI-v2 Exemple  

Voici un exemple de NoisePollution au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "Laeq2": 85,  
  "Lamax2": 75,  
  "Lanight": 45,  
  "NoiseAnnoyanceIndex": 3,  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "buildingsType": "residential",  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateObservedFrom": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateObservedTo": {  
    "@type": "DateTime",  
    "@value": "2022-07-01T12:40:01.00Z"  
  },  
  "exposureType": "short term exposure",  
  "groundType": "concrete",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "noiseOrigin": "traffic",  
  "wallsType": "glass"  
}  
```  
</details>  

#### NoisePollution NGSI-v2 normalisé Exemple  

Voici un exemple de NoisePollution au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "France",  
      "postalCode": "06200",  
      "addressLocality": "Nice",  
      "type": "PostalAddress"  
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
    "type": "Property",  
    "value": "IMREDD_UCA_Nice"  
  },  
  "dateObservedFrom": {  
    "type":  "DateTime",  
      "value": "2022-07-01T10:40:01.00Z"  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
      "value": "2022-07-01T12:40:01.00Z"  
  },  
  "NoiseAnnoyanceIndex": {  
    "type": "Number",  
    "value": 3  
  },  
  "Lanight": {  
    "type": "Number",  
    "value": 45  
  },  
  "noiseOrigin": {  
    "type": "Text",  
    "value": "traffic"  
  },  
  "exposureType": {  
    "type": "Property",  
    "value": "short term exposure"  
  },  
  "buildingsType": {  
    "type": "Text",  
    "value": "residential"  
  },  
  "groundType": {  
    "type": "Text",  
    "value": "concrete"  
  },  
  "wallsType": {  
    "type": "Text",  
    "value": "glass"  
  },  
  "Lamax2": {  
    "type": "Number",  
    "value": 75  
  },  
  "Laeq2": {  
    "type": "Number",  
    "value": 85  
  }  
}  
```  
</details>  

#### NoisePollution Valeurs-clés NGSI-LD Exemple  

Voici un exemple de NoisePollution au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
  "Laeq2": 85,  
  "Lamax2": 75,  
  "Lanight": 45,  
  "NoiseAnnoyanceIndex": 3,  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "postalCode": "06200",  
    "type": "PostalAddress"  
  },  
  "buildingsType": "residential",  
  "dataProvider": "IMREDD_UCA_Nice",  
  "dateObservedFrom": "2022-07-01T10:40:01.00Z",  
  "dateObservedTo": "2022-07-01T12:40:01.00Z",  
  "exposureType": "short term exposure",  
  "groundType": "concrete",  
  "location": {  
    "coordinates": [  
      7.2032497427380235,  
      43.68056738083439  
    ],  
    "type": "Point"  
  },  
  "noiseOrigin": "traffic",  
  "wallsType": "glass",  
  "@context": [  
  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"  
  ]  
}  
```  
</details>  

#### BruitPollution NGSI-LD normalisé Exemple  

Voici un exemple de NoisePollution au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:NoisePollution:France-NoisePollution-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",  
  "type": "NoisePollution",  
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
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T10:40:01.00Z"  
    }  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-07-01T12:40:01.00Z"  
    }  
  },  
  "NoiseAnnoyanceIndex": {  
    "type": "Property",  
    "value": 3  
  },  
  "Lanight": {  
    "type": "Property",  
    "value": 45  
  },  
  "noiseOrigin": {  
    "type": "Property",  
    "value": "traffic"  
  },  
  "exposureType": {  
    "type": "Property",  
    "value": "short term exposure"  
  },  
  "buildingsType": {  
    "type": "Property",  
    "value": "residential"  
  },  
  "groundType": {  
    "type": "Property",  
    "value": "concrete"  
  },  
  "wallsType": {  
    "type": "Property",  
    "value": "glass"  
  },  
  "Lamax2": {  
    "type": "Property",  
    "value": 75  
  },  
  "Laeq2": {  
    "type": "Property",  
    "value": 85  
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
  

Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
