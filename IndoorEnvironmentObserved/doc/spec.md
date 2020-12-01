# Indoor Environment Observed

**Note: The latest version of this Data Model can be found at
[https://github.com/smart-data-models/FIXME](https://github.com/smart-data-models/FIXME)**

## Description

An observation of air and climate conditions and people count for indoor use and closed environment as rooms, classrooms, halls, laboratories. This data model is based on and can be considered a specialization of the [Air Quality Observed Data Model](https://github.com/smart-data-models/dataModel.Environment/tree/master/AirQualityObserved). Some fields are also derived from [Weather Observed Data Model](https://github.com/smart-data-models/dataModel.Weather/tree/master/WeatherObserved) and [CrowdFlowObserved](https://github.com/smart-data-models/dataModel.Transportation/tree/master/CrowdFlowObserved).

## Data Model

A JSON Schema corresponding to this data model can be found
[here](http://fiware.github.io/data-models/specs/FIXME/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `IndoorEnvironmentObserved`.

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Location of the air quality observation represented by a
    GeoJSON geometry.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not defined.

-   `address` : Civic address of the air quality observation. Sometimes it
    corresponds to the air quality station address.

    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Mandatory if `location` is not present

-   `dateObserved` : The date and time of this observation in ISO8601 UTCformat.
    It can be represented by an specific time instant or by an ISO8601 interval.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) or an
        ISO8601 interval represented as [Text](https://schema.org/Text).
    -   Mandatory

-   `refDevice` : A reference to the device(s) which captured this observation.

    -   Attribute type: Relationship. Reference to an entity of type `Device`
    -   Optional

-  `refPointOfInterest` : A reference to a point of interest (a Building, a Museum...) associated to this indoor or closed environment.

    -   Attribute type: Relationship. Reference to an entity of type PointOfInterest
    -   Optional
- `sensorPlacement`	: Location where the sensor is
    placed.

    -   Attribute type: Property. Text.
    -   Allowed values: oneOf (`northWall`, `southWall`, `eastWall`, `westWall`, `center`, `floor`, `roof`, `ceiling`)
        -   Or any other value with semantics not covered by the above list.

- `sensorHeight`	: Sensor's height.

    -   Attribute type: Property. Number.
    -   Default unit: Meters.
    -   Optional

-   `peopleCount` : Total number of people detected in the room during this observation period.

    -   Attribute type: Property. Number. Positive integer.
    -   Optional

### Representing air pollutants

The description of attributes related to air pollutants and gases follows the specifications of the [Air Quality Observed Data Model](https://github.com/smart-data-models/dataModel.Environment/tree/master/AirQualityObserved):

-   Attribute name: Equal to the name of the measurand, for instance `CO`.

-   Attribute type: Property. [Number](https://schema.org/Number)

-   Attribute value: corresponds to the value for the measurand as a number.

-   Attribute metadata:
    -   `timestamp` : optional timestamp for the observed value in ISO8601
        format. It can be omitted if the observation time is the same as the one
        captured by the `dateObserved` attribute at entity level.
        -   Type: [DateTime](https://schema.org/DateTime)
    -   `unitCode` : The unit code (text) of measurement given using the
        [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)
        (max. 3 characters). For instance, `GP` represents milligrams per cubic
        meter and `GQ` represents micrograms per cubic meter.
        -   Type: [Text](https://schema.org/Text)
        -   Mandatory
    -   `description` : short description of the measurand
        -   Attribute type: Property. [Text](https://schema.org/Text)
        -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
            equivalent to [description](https://schema.org/description)
        -   Optional

A minimal set of air pollutants that can be monitored in indoor environments (workshops, laboratories, hospital's rooms) can be:

-    *CO*
-    *O2*
-    *H2*
-    *CH4*
-    *C4H10*
-    *CO2*
-    *PM25*
-    *PM10*

### Representing indoor environmental conditions

The description of environmental attributes of the air follows the specifications of the [Weather Observed Data Model](https://github.com/smart-data-models/dataModel.Weather/tree/master/WeatherObserved):

- `temperature` : Air's temperature observed. Celsius degrees
	- 	Attribute type: Property. Number.
	-	Optional
- `relativeHumidity` : Air's relative humidity observed (percentage, expressed in parts per one).
	- 	Attribute type: Property. Number.
		-  	minimum: 0
		-  maximum: 1 (100%)
	-	Optional

- `atmosphericPressure` : The atmospheric pressure observed measured in Hecto Pascals or millibar
	- 	Attribute type: Property. Number.
	-	Optional

- `illuminance`	: Illuminance observed measured in lux (lx) or lumens per square metre (cd·sr·m−2) 
	- 	Attribute type: Property. Number.
	-	Optional

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "urn:ngsi:MuseoDemo_Room_1",
    "type": "IndoorEnvironmentObserved",
    "dateObserved": {
        "value": "2020-06-08T17:54:00"
    },
    "refPointOfInterest": {
        "type": "Relationship",
        "value": "urn:ngsi:MuseoDemo"
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [40, 11]
        }
    },
    "address": {
        "type": "PostalAddress",
        "value": {
            "addressCountry": "IT",
            "addressLocality": "Demo city",
            "streetAddress": "Demo address"
        }
    },
    "peopleCount": {
    	"value": 10
  	},
    "temperature": {
        "value": 12.2,
        "metadata": {
            "unitCode": {
                "value": "CEL"
            }
        }
    },
    "relativeHumidity": {
        "value": 0.54,
        "metadata": {
            "unitCode": {
                "value": "P1"
            }
        }
    },
    "illuminance": {
        "value": 1000,
        "metadata": {
            "unitCode": {
                "value": "LX"
            }
        }
    },
    "CO": {
        "value": 500,
        "metadata": {
            "unitCode": {
                "value": "GP"
            }
        }
    },
    "NO": {
        "value": 45,
        "metadata": {
            "unitCode": {
                "value": "GQ"
            }
    },
    "NOx": {
        "value": 139,
        "metadata": {
            "unitCode": {
                "value": "GQ"
            }
        }
    },
    "NO2": {
        "value": 69,
        "metadata": {
            "unitCode": {
                "value": "GQ"
            }
        }
    },
    "SO2": {
        "value": 11,
        "metadata": {
            "unitCode": {
                "value": "GQ"
            }
        }
    }
}
```

### key-value pairs Example

```json
{
        "id": "urn:ngsi:MuseoDemo_Room_1",
        "type": "IndoorEnvironmentObserved",
        "CO": 500,
        "NO": 45,
        "NO2": 69,
        "NOx": 139,
        "SO2": 11,
        "address": {
            "addressCountry": "IT",
            "addressLocality": "Demo city",
            "streetAddress": "Demo address"
        },
        "peopleCount": 10,
        "atmosphericPressure": 1013.52,
        "dateObserved": "2020-06-08T17:54:00",
        "illuminance": 1000,
        "location": {
            "type": "Point",
            "coordinates": [
                40,
                11
            ]
        },
        "refPointOfInterest": "urn:ngsi:MuseoDemo",
        "relativeHumidity": 0.54,
        "temperature": 12.2
}    
```

### LD Example

TBD