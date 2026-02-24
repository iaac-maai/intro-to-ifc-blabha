# IFC Quick Reference Guide

## Loading an IFC File

```python
import ifcopenshell

# Open the file
ifc = ifcopenshell.open("assets/duplex.ifc")

# Check schema
print(ifc.schema)  # e.g., "IFC2x3", "IFC4"
```

## Querying Entities

```python
# Get all entities of a specific type
spaces = ifc.by_type("IfcSpace")
windows = ifc.by_type("IfcWindow")
doors = ifc.by_type("IfcDoor")
walls = ifc.by_type("IfcWall")

# Get entity by ID
entity = ifc.by_id(12345)

# Get entities by attribute value
kitchens = ifc.by_attribute("Name", "Kitchen")
```

## Common Entity Types

```
IfcProject          # Project container
IfcBuilding         # Building entity
IfcBuildingStorey   # Floors/stories
IfcSpace            # Rooms, zones
IfcWindow           # Windows
IfcDoor             # Doors, openings
IfcWall             # Wall elements
IfcSlab             # Floors, roofs
IfcMaterial         # Material definitions
IfcPropertySet      # Property containers
```

## Accessing Properties

```python
space = ifc.by_type("IfcSpace")[0]

# Basic attributes
space.Name                          # Entity name
space.Description                   # Description text
space.GlobalId                      # Unique identifier

# Geometry and positioning
space.ObjectPlacement              # Location/coordinates
space.Representation               # Shape geometry

# Quantities and properties
space.Quantities                    # Geometric quantities
space.HasProperties                # Custom properties
space.BoundedBy                     # Boundary elements
```

## Working with Quantities

```python
space = ifc.by_type("IfcSpace")[0]

if space.Quantities:
    for quantity in space.Quantities.Quantities:
        # Quantity types include:
        # IfcQuantityArea: AreaValue
        # IfcQuantityVolume: VolumeValue
        # IfcQuantityLength: LengthValue
        # IfcQuantityCount: CountValue
        
        print(f"Name: {quantity.Name}")
        
        if hasattr(quantity, 'AreaValue'):
            print(f"Area: {quantity.AreaValue} m²")
        elif hasattr(quantity, 'VolumeValue'):
            print(f"Volume: {quantity.VolumeValue} m³")
```

## Working with Properties

```python
entity = ifc.by_type("IfcSpace")[0]

if hasattr(entity, 'HasProperties') and entity.HasProperties:
    for prop_set in entity.HasProperties:
        for prop in prop_set.HasProperties:
            if hasattr(prop, 'Name') and hasattr(prop, 'NominalValue'):
                name = prop.Name
                value = prop.NominalValue
                print(f"{name}: {value}")
```

## Checking Entity Type

```python
entity = ifc.by_type("IfcWindow")[0]

# Check if entity is of specific type
if entity.is_a("IfcWindow"):
    print("This is a window")

# Get the entity type
entity_type = entity.is_a()  # Returns "IfcWindow"
```

## Useful Patterns

### Loop Through All Entities
```python
for entity in ifc.entities:
    if entity.is_a("IfcSpace"):
        print(entity.Name)
```

### Count Entity Types
```python
from collections import Counter

entity_types = [e.is_a() for e in ifc.entities]
type_counts = Counter(entity_types)

for entity_type, count in type_counts.most_common():
    print(f"{entity_type}: {count}")
```

### Filter with Conditions
```python
# Get all spaces with area > 20 m²
large_spaces = [
    s for s in ifc.by_type("IfcSpace")
    if get_space_area(s) and get_space_area(s) > 20
]

def get_space_area(space):
    if space.Quantities:
        for qty in space.Quantities.Quantities:
            if hasattr(qty, 'Name') and qty.Name == "NetFloorArea":
                return qty.AreaValue
    return None
```

### Print All Attributes of an Entity
```python
entity = ifc.by_type("IfcSpace")[0]

print("All attributes:")
for attr in dir(entity):
    if not attr.startswith('_'):
        try:
            value = getattr(entity, attr)
            if not callable(value):
                print(f"  {attr}: {value}")
        except:
            pass
```

## Debugging Tips

### Explore Unknown Entities
```python
# When you don't know what data is available:
entity = ifc.by_type("IfcSpace")[0]

print("Type:", entity.is_a())
print("Global ID:", entity.GlobalId)
print("\nAll non-method attributes:")
for attr in sorted(dir(entity)):
    if not attr.startswith('_'):
        try:
            val = getattr(entity, attr)
            if not callable(val):
                print(f"  {attr} = {val}")
        except:
            pass
```

### Check if Attribute Exists
```python
entity = ifc.by_type("IfcWindow")[0]

if hasattr(entity, 'OverallHeight'):
    height = entity.OverallHeight
    print(f"Height: {height}")
else:
    print("Height attribute not available")
```

### Safe Property Access
```python
def safe_get(entity, attr, default=None):
    """Safely get an attribute with fallback."""
    try:
        return getattr(entity, attr, default)
    except:
        return default

name = safe_get(entity, 'Name', 'Unnamed')
area = safe_get(entity, 'Area', 0)
```

## Common Issues and Solutions

### Issue: "Module not found: ifcopenshell"
```bash
pip install ifcopenshell
```

### Issue: IFC File Won't Load
```python
# Check if file exists
from pathlib import Path
if Path("assets/duplex.ifc").exists():
    ifc = ifcopenshell.open("assets/duplex.ifc")
else:
    print("File not found!")
```

### Issue: Quantities Are None
```python
# Some entities don't have quantities
# Check before accessing:
if space.Quantities:
    # Process quantities
else:
    print("No quantities available for this space")
```

### Issue: Properties Are Complex
```python
# Properties might be nested, use try/except:
try:
    area = space.Quantities.Quantities[0].AreaValue
except (AttributeError, IndexError):
    area = None
    print("Could not extract area")
```

## Real-World Workflows

### Extract All Rooms with Areas
```python
rooms = []
for space in ifc.by_type("IfcSpace"):
    name = space.Name or "Unnamed"
    area = None
    
    if space.Quantities:
        for qty in space.Quantities.Quantities:
            if hasattr(qty, 'Name') and qty.Name == "NetFloorArea":
                area = qty.AreaValue
    
    rooms.append({"name": name, "area": area})

# Print results
for room in rooms:
    print(f"{room['name']}: {room['area']} m²")
```

### Find All Elements of a Type
```python
def get_all_of_type(ifc_model, entity_type):
    """Get all entities of specified type."""
    entities = ifc_model.by_type(entity_type)
    return [{
        'name': e.Name,
        'id': e.GlobalId,
        'type': e.is_a()
    } for e in entities]

windows = get_all_of_type(ifc, "IfcWindow")
print(f"Found {len(windows)} windows")
```

### Build Element Hierarchy
```python
def print_hierarchy(entity, indent=0):
    """Print entity and related elements."""
    print("  " * indent + f"- {entity.is_a()}: {entity.Name}")
    
    if hasattr(entity, 'HasOpenings'):
        for opening in entity.HasOpenings:
            print_hierarchy(opening.RelatedOpeningElement, indent + 1)

building = ifc.by_type("IfcBuilding")[0]
print_hierarchy(building)
```

## Performance Tips

### For Large Files
```python
# Get only what you need
spaces = ifc.by_type("IfcSpace")  # Fast - indexed

# Avoid iterating all entities
# Instead of:
for entity in ifc.entities:
    if entity.is_a("IfcSpace"):
        # process

# Do this:
for entity in ifc.by_type("IfcSpace"):
    # process (much faster)
```

### Cache Results
```python
# If you query the same thing multiple times, cache it:
_spaces_cache = None

def get_spaces():
    global _spaces_cache
    if _spaces_cache is None:
        _spaces_cache = ifc.by_type("IfcSpace")
    return _spaces_cache
```

---

## Helpful Resources

- **IfcOpenShell Docs**: https://docs.ifcopenshell.org/ifcopenshell-python.html
- **IFC Schema Browser**: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
- **Entity Documentation**: Check the IFC standard for each entity type

## Common Mistakes to Avoid

- ❌ Assuming all properties are always present
- ❌ Forgetting to check if collections are None
- ❌ Not handling string encoding properly
- ❌ Trying to modify IFC objects directly
- ✅ Always check before accessing nested attributes
- ✅ Use try/except for robustness
- ✅ Print entity attributes when exploring
- ✅ Read the IFC standard documentation
