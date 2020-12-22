Entité : WaterQualityObserved  
=============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Environment/blob/master/WaterQualityObserved/LICENSE.md)  
Description globale : **Le modèle de données sur la qualité de l'eau est destiné à représenter les paramètres de qualité de l'eau pour une certaine masse d'eau (rivière, lac, mer, etc.) section**  

## Liste des biens  

- `Chla`: Concentration de chlorophylle A.  - `Cl-`: Concentration des chlorures.  - `NH3`: Concentration d'ammonium.  - `NH4`: Concentration d'ammonium.  - `NO3`: Concentration de nitrates.  - `O2`: Niveau d'oxygène libre, non composé, présent.  - `PC`: Concentration de phycocyanine pigmentaire qui peut être mesurée pour estimer spécifiquement les concentrations de cyanobactéries.  - `PE`: Concentration de phycoérythrine pigmentaire qui peut être mesurée pour estimer spécifiquement les concentrations de cyanobactéries.  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `conductance`: Conduite spécifique.  - `conductivity`: Conductivité électrique.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format UTC ISO8601. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `measurand`: Un ensemble de chaînes de caractères contenant des détails (voir le format ci-dessous) sur les mesurandes supplémentaires fournis par cette observation.  - `name`: Le nom de cet article.  - `orp`: Potentiel d'oxydation-réduction.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `pH`: Acidité ou basicité d'une solution aqueuse.  - `refPointOfInterest`: Une référence à un point d'intérêt associé à cette observation.  - `salinity`: Quantité de sels dissous dans l'eau.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tds`: Total des solides dissous.  - `temperature`: Température  - `tss`: Total des solides en suspension.  - `turbidity`: Quantité de lumière diffusée par les particules dans la colonne d'eau  - `type`: NGSI Type d'entité    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: 'Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section'    
  properties:    
    Chla:    
      description: 'Concentration of chlorophyll A.'    
      minimum: 0    
      type: Property    
    Cl-:    
      description: 'Concentration of chlorides.'    
      minimum: 0    
      type: Property    
    NH3:    
      description: 'Concentration of ammonium.'    
      minimum: 0    
      type: Property    
    NH4:    
      description: 'Concentration of ammonium.'    
      minimum: 0    
      type: Property    
    NO3:    
      description: 'Concentration of nitrates.'    
      minimum: 0    
      type: Property    
    O2:    
      description: 'Level of free, non-compound oxygen present.'    
      minimum: 0    
      type: Property    
    PC:    
      description: 'Concentration of pigment phycocyanin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: Property    
    PE:    
      description: 'Concentration of pigment phycoerythrin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: Property    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    conductance:    
      description: 'Specific Conductance.'    
      minimum: 0    
      type: Property    
    conductivity:    
      description: 'Electrical Conductivity.'    
      minimum: 0    
      type: Property    
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
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
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
    measurand:    
      description: 'An array of strings containing details (see format below) about extra measurands provided by this observation.'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    orp:    
      description: 'Oxidation-Reduction potential.'    
      minimum: 0    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pH:    
      description: 'Acidity or basicity of an aqueous solution.'    
      maximum: 14    
      minimum: 0    
      type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to a point of interest associated to this observation.'    
      type: Relationship    
    salinity:    
      description: 'Amount of salts dissolved in water.'    
      minimum: 0    
      type: Property    
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
    tds:    
      description: 'Total dissolved solids. '    
      minimum: 0    
      type: Property    
    temperature:    
      description: Temperature    
      type: Property    
    tss:    
      description: 'Total suspended solids.'    
      minimum: 0    
      type: Property    
    turbidity:    
      description: 'Amount of light scattered by particles in the water column'    
      minimum: 0    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WaterQualityObserved    
      type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WaterQualityObserved NGSI V2 key-values Exemple  
Voici un exemple d'une qualité de l'eau observée au format JSON en tant que valeurs clés. Ce format est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
  "location": {  
    "type": "Point",  
    "coordinates": [-5.993307, 37.362882]  
  },  
  "temperature": 24.4,  
  "conductivity": 0.005,  
  "pH": 7.4,  
  "NO3": 0.01  
}  
```  
#### WaterQualityObserved NGSI V2 normalisé Exemple  
Voici un exemple de qualité de l'eau observée au format JSON, telle qu'elle est normalisée. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2017-01-31T06:45:00Z"  
  },  
  "temperature": {  
    "value": 24.4  
  },  
  "NO3": {  
    "value": 0.01  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-5.993307, 37.362882]  
    }  
  },  
  "pH": {  
    "value": 7.4  
  },  
  "measurand": {  
    "value": ["NO3, 0.01, M1, Concentration of Nitrates"]  
  },  
  "conductivity": {  
    "value": 0.005  
  }  
}  
```  
#### WaterQualityObserved NGSI-LD key-values Example  
Voici un exemple de valeurs-clés de la qualité de l'eau observée au format JSON-LD. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "NO3": 0.01,  
 "conductivity": 0.005,  
 "dateObserved": {"@type": "DateTime", "@value": "2017-01-31T06:45:00Z"},  
 "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
 "location": {"coordinates": [-5.993307, 37.362882], "type": "Point"},  
 "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
 "pH": 7.4,  
 "temperature": 24.4,  
 "type": "WaterQualityObserved"}  
```  
#### WaterQualityObserved NGSI-LD normalisé Exemple  
Voici un exemple de qualité de l'eau observée en format JSON-LD, telle que normalisée. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
    "type": "WaterQualityObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-31T06:45:00Z"  
        }  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 24.4  
    },  
    "NO3": {  
        "type": "Property",  
        "value": 0.01  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -5.993307,  
                37.362882  
            ]  
        }  
    },  
    "pH": {  
        "type": "Property",  
        "value": 7.4  
    },  
    "measurand": {  
        "type": "Property",  
        "value": [  
            "NO3, 0.01, M1, Concentration of Nitrates"  
        ]  
    },  
    "conductivity": {  
        "type": "Property",  
        "value": 0.005  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
