# comp-storage-webui

### Category

Layout:
- id: unique id
- name: A string
- parentCategory: 

Category example: 
- Diodes
    - Xener-diodes
    - LEDs
        - red, green, blue
        - RGB LEDs
            - common anode
            - common cathode



### Drawers
A drawer contains one or more components

Layout:
- id: Unique key for the Drawer table
- location: A number which is a physical label printed on the drawer, e.g. "81"
- size: dropdown list "wide 1", "wide 2", "narrow", "large", "largest"
- category: ManyToOne field linking to any number of categories.

Drawer example
- id: 1
- location: "101"
- size: "wide, 1 high"    
- category: LED's, red LED's, green LED's, common-cathode-leds



### Component
A component is a simple electrical component

Layout:
- component_id: PRIMARY KEY
- name: String
- manufacturer_id: FOREIGN KEY (Manufacturer.ManufacturerID)
- stock
- drawer: FOREIGN KEY (drawer.drawerID)
- image: Link to an url containing an image? #TODO Figure this shit out


### Manufacturer
Manufacturers of components, related by ManufacturerID

Layout:
- manufacturer_id: PRIMARY KEY
- name


## TODO
- [ ] Payment due by end of project: 100 rigsdalere betalt til Frida
- [ ] When making a new component, drawer, category and manufacturer is created if they dont already exist.
