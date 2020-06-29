# Water Observation

## Description
Water observation data model is intended to represent the parameters of flow, level and volume of water observed, as well as the swell information, over a fixed or variable area. This observation also includes the masses of floating objects on this area.
The data collected is provided by [Sensors], [Cameras], [Water stations] positioned at specific or sensitive locations for rivers, streams, torrent, lakes, seas, etc..

Link to the [specification](/doc/spec.md)

## Examples of use

### Normalized Example

Normalized NGSI response

{{Provide a JSON example in NGSIv2 Normalized Format}}

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

{{Provide a JSON example in NGSIv2 keyValues Format}}

### LD Example

Sample uses the NGSI-LD representation

{{Provide a JSON example in NGSI-LD Format}}

## Use it with a real service

{{Provide a link to a real service providing data following the harmonized data format}}

## Open Issues
{{Describe here any open issue}}
i.e. This data model is being adapted to the (guidelines)[https://github.com/smart-data-models/data-models/blob/master/guidelines.md]




### Common Water Observed parameters – identification data

- `id` : Unique identifier.

- `type` : Entity type. It must be equal to `WaterObserved`.

- `dataProvider` : Specifies the URL to information about the provider of this information.
    - Attribute type: Property. [URL](https://schema.org/URL)
    - Optional

- `source` : A sequence of characters giving the source of the entity data.
    - Attribute type: Property. [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    - Optional

- `name` : Name given to the observation.
    - Attribute type: Property. [Text](https://schema.org/Text)
    - Normative References: [https://schema.org/name](https://schema.org/name)
    - Optional
    
- `alternateName` : Alternative Name given to the observation.
    - Attribute type: Property. [Text](https://schema.org/Text)
    - Normative References: [https://schema.org/alternateName](https://schema.org/alternateName)
    - Optional
    
- `description` : Description given to the observation.
    - Attribute type: Property. [Text](https://schema.org/Text)
    - Normative References: [https://schema.org/description](https://schema.org/description)
    - Optional
    
- `seeAlso` : Text  Link can provide additional information.
    - Attribute type: Property. [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    - Optional

### Information related to the location of the observation

- `location` : Location of this observation represented by a GeoJSON geometry.
    - Attribute type: GeoProperty. `geo:json`.
    - Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946) 
    - Mandatory if `address` is not present.
    
- `address`: Civic address where the Water Observed measurement is taken.
    - Attribute type: Property. [Address](https://schema.org/address)
    - Normative References: [https://schema.org/address](https://schema.org/address)
    - Mandatory if `location` is not present.
    
- `areaServed`: Zone of level higher to the attributes Location & Address to gather and cross information (ex district, etc).
    - Attribute type: Property. List of [Text](https://schema.org/Text)
    - Normative References: [https://schema.org/areaServed](https://schema.org/areaServed)
    - Optional

### Information related to a reference to another Data Model

- `refDevice` : A reference to the device which captured this observation.
    - Attribute type: Relationship. Reference to an entity of type `Device`
    - Optional

### Information related to the date / period of the observation

- `dateObserved` : Date and time of this observation represented by an ISO8601 UTCformat.
    It can be represented by an specific time instant or by an ISO8601 interval to separate attributes `dateObservedFrom`,`dateObservedTo`.
    - Attribute type: Property. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text).
    - Mandatory

- `dateObservedFrom` : Observation period : Start date and time in an ISO8601 UTCformat.
    - Attribute type: Property. [DateTime](https://schema.org/DateTime) 
    - Mandatory if `dateObserved` is not present

- `dateObservedTo` : Observation period : End date and time in an ISO8601 UTCformat.
    - Attribute type: Property. [DateTime](https://schema.org/DateTime) 
    - Mandatory if `dateObserved` is not present

### Representing quantitative Water Observation information

- `flow` : Water Flow observed.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MQS</code> represents Cubic Meter per Second. 
    - Optional    
    
- `height` : Water height - Level reach on alert coasts.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.
    - Optional

### Representing quantitative Sea Observation information

- `swellHeight` : Swell height observed.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.
    - Optional

- `swellPeriod` : Swells period
    - Attribute type: Property. [Number](https://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>SEC</code> represents Second.
    - Optional

- `swellDirection` : Swells Direction.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit:  The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>DD</code> represents  Degree. If entered, the value must be between 0 and 360.
    - Optional

- `waveLength` : Wave Length.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.
    - Optional

### Representing quantitative Floating Object on an area 

- `measuredArea` : Reference of the surface measured
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTK</code> represents M².
    - Optional   
- `objectArea` : Percentage occupied by floating object in the area.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>P1</code> represents Percentage.
    - Optional   
- `objectHeightAverage` : Average height raised.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.
    - Optional
- `objectHeightMax` : Average height raised.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTR</code> represents Meter.
    - Optional
- `objectVolume` : Estimated volume raised.
    - Attribute type: Property. [Number](http://schema.org/Number)
    - Default unit: The unit code (text) of measurement given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters). For instance, <code>MTQ</code> represents Cubic Meters.
    - Optional

