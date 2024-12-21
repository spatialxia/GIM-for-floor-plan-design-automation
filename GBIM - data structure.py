"""
Defining data structure of GIM based on a subset of the IFC schema
- Author: Yi Xia
- Affiliation: Chongqing University & Hong Kong University of Science and Technology (HKUST)
- Date: 2024-12-20
"""

from neomodel import (
    db,
    config,
    StructuredNode,
    StructuredRel,
    StringProperty,
    IntegerProperty,
    BooleanProperty,
    FloatProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    ArrayProperty,
    JSONProperty,
)
import ifcopenshell as ifc

""" Customized relationships """


# region Customized relationships
class GraphRelHosts(StructuredRel):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelHosts")
    Name = StringProperty()
    Description = StringProperty()

    IfcClass = StringProperty(default=None)  # IFC identifier


# endregion


""" Individual nodes """


# region 1. Relationship nodes
class GraphRelAggregates(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelAggregates")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcRelAggregates")
    Name = StringProperty(default="RelAggregates")
    Description = StringProperty()
    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")

    # IFC schema invese relationships
    from_GraphBuilding = RelationshipFrom("GraphBuilding", "RelatingObject")
    from_GraphProject = RelationshipFrom("GraphProject", "RelatingObject")
    from_GraphSite = RelationshipFrom("GraphSite", "RelatingObject")
    from_GraphBuildingStorey = RelationshipFrom("GraphBuildingStorey", "RelatingObject")

    to_GraphSite = RelationshipTo("GraphSite", "RelatedObjects")
    to_GraphBuilding = RelationshipTo("GraphBuilding", "RelatedObjects")
    to_GraphSpace = RelationshipTo("GraphSpace", "RelatedObjects")
    to_GraphBuildingStorey = RelationshipTo("GraphBuildingStorey", "RelatedObjects")


class GraphRelConnectsElements(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelConnectsElements")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcRelConnectsElements")
    Name = StringProperty(default="RelConnectsElements")
    Description = StringProperty(default="RelConnectsElements")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")

    # IFC schema invese relationships
    from_GraphSpace = RelationshipFrom("GraphSpace", "RelatingElement")
    to_GraphSpace = RelationshipFrom("GraphSpace", "RelatedElement")


class GraphRelContainedInSpatialStructure(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelContainedInSpatialStructure")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcRelContainedInSpatialStructure")
    Name = StringProperty(default="RelContainedInSpatialStructure")
    Description = StringProperty(default="RelContainedInSpatialStructure")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")

    # IFC schema invese relationships
    from_GraphSpace = RelationshipFrom("GraphSpace", "RelatingStructure")
    from_GraphBuildingStorey = RelationshipFrom("GraphBuildingStorey", "RelatingStructure")

    to_GraphColumn = RelationshipTo("GraphColumn", "RelatedElements")
    to_GraphBeam = RelationshipTo("GraphBeam", "RelatedElements")
    to_GraphWall = RelationshipTo("GraphWall", "RelatedElements")
    to_GraphWindow = RelationshipTo("GraphWindow", "RelatedElements")
    to_GraphDoor = RelationshipTo("GraphDoor", "RelatedElements")
    to_GraphSlab = RelationshipTo("GraphSlab", "RelatedElements")


class GraphRelVoidsElement(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelVoidsElement")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcRelVoidsElement")
    Name = StringProperty(default="RelVoidsElement")
    Description = StringProperty(default="RelVoidsElement")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")

    # IFC schema invese relationships
    from_GraphWall = RelationshipFrom("GraphWall", "RelatingBuildingElement")

    to_GraphOpeningElement = RelationshipTo("GraphOpeningElement", "RelatedOpeningElement")


class GraphRelFillsElement(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphRelFillsElement")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcRelFillsElement")
    Name = StringProperty(default="RelFillsElement")
    Description = StringProperty(default="RelFillsElement")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")

    # IFC schema invese relationships
    from_GraphWindow = RelationshipFrom("GraphWindow", "RelatedBuildingElement")
    from_GraphDoor = RelationshipFrom("GraphDoor", "RelatedBuildingElement")

    to_GraphOpeningElement = RelationshipTo("GraphOpeningElement", "RelatingOpeningElement")


# endregion

""" Individual nodes """


# region 2. Individual nodes
class GraphProject(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphProject")

    # IFC schema attributes
    IfcClass = StringProperty(default="IfcProject")
    Name = StringProperty()
    Description = StringProperty()
    ObjectType = StringProperty()
    LongName = StringProperty()
    Phase = StringProperty()

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")


class GraphSite(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphSite")

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcSite")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")

    # entity relationships


class GraphBuilding(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphBuilding")

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcBuilding")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")

    # entity relationships


class GraphBuildingStorey(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphBuildingStorey")

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcBuildingStorey")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")


class GraphSpace(StructuredNode):  ######## Here #########
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphSpace")
    SpaceType = StringProperty()

    # Customized relationships
    GraphSpace_adj = Relationship("GraphSpace", "GraphRelAdjoinsSpaces")
    GraphSpace_con = Relationship("GraphSpace", "GraphRelConnectsSpaces")

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcSpace")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")


class GraphColumn(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphColumn")
    existance = BooleanProperty(default=True)

    # basic geometry data
    location_start = ArrayProperty(default=[])
    location_end = ArrayProperty(default=[])
    size_x = FloatProperty(default=None)
    size_y = FloatProperty(default=None)
    index = StringProperty(default=None)
    length = FloatProperty(default=None)

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcColumn")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphBeam(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphBeam")
    existance = BooleanProperty(default=True)
    location_start = ArrayProperty(default=[])
    location_end = ArrayProperty(default=[])
    size_x = FloatProperty(default=None)
    size_y = FloatProperty(default=None)
    index = StringProperty(default=None)

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcBeam")

    # IFC schema invese relationships
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphWall(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphWall")
    existance = BooleanProperty(default=True)
    location_start = ArrayProperty(default=[])
    location_end = ArrayProperty(default=[])
    size_x = FloatProperty(default=None)  # thickness
    size_y = FloatProperty(default=None)  # height
    index = StringProperty(default=None)

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcWall")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphWindow(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphWindow")
    existance = BooleanProperty(default=True)
    size_x = FloatProperty(default=None)  # length
    size_y = FloatProperty(default=None)  # height_bottom
    size_z = FloatProperty(default=None)  # height_top
    index = StringProperty(default=None)
    hosted_wall_index = StringProperty(default=None)
    placement_ratio = FloatProperty(default=None)

    # Customize relationships
    GraphWall = RelationshipFrom("GraphWall", "GraphRelHosts", model=GraphRelHosts)

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcWindow")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphDoor(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphDoor")
    existance = BooleanProperty(default=True)
    size_x = FloatProperty(default=None)  # length
    size_y = FloatProperty(default=None)  # height
    index = StringProperty(default=None)
    hosted_wall_index = StringProperty(default=None)
    placement_ratio = FloatProperty(default=None)

    # Customize relationships
    GraphWall = RelationshipFrom("GraphWall", "GraphRelHosts", model=GraphRelHosts)

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcDoor")
    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphSlab(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphSlab")
    existance = BooleanProperty(default=True)
    slabtype = StringProperty(default=None)
    index = StringProperty(default=None)
    location_x = ArrayProperty(default=[])
    location_y = ArrayProperty(default=[])
    location_z = ArrayProperty(default=[])
    size_x = FloatProperty(default=None)  # Thickness

    # IFC schema attributes
    Name = StringProperty()
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcSlab")
    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


class GraphOpeningElement(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphOpeningElement")
    existance = BooleanProperty(default=True)

    # IFC schema attributes
    Name = StringProperty(default="OpeningElement")
    Description = StringProperty()
    IfcClass = StringProperty(default="IfcOpeningElement")

    # IFC schema attributes (other instance)
    GraphOwnerHistory = RelationshipTo("GraphOwnerHistory", "OwnerHistory")
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "ObjectPlacement")
    GraphProductDefinitionShape = RelationshipTo("GraphProductDefinitionShape", "Representation")


# endregion

""" Bridging nodes """


# region Bridging entity
class GraphLocalPlacement(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphLocalPlacement")
    IfcClass = StringProperty(default="IfcLocalPlacement")
    Name = StringProperty(default="LocalPlacement")

    # IFC schema attributes (other instance)
    GraphLocalPlacement = RelationshipTo("GraphLocalPlacement", "PlacementRelTo")
    GraphAxis2Placement3D = RelationshipTo("GraphAxis2Placement3D", "RelativePlacement")


class GraphArbitraryClosedProfileDef(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphArbitraryClosedProfileDef")
    Name = StringProperty(default="ArbitraryClosedProfileDef")
    IfcClass = StringProperty(default="IfcArbitraryClosedProfileDef")

    # IFC schema attributes
    ProfileType = StringProperty(default="AREA")
    ProfileName = StringProperty(default=None)
    # IFC schema attributes (other instance)
    GraphPolyline = RelationshipTo("GraphPolyline", "OuterCurve")
    GraphIndexedPolyCurve = RelationshipTo("GraphIndexedPolyCurve", "OuterCurve")


class GraphExtrudedAreaSolid(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphExtrudedAreaSolid")
    Name = StringProperty(default="ExtrudedAreaSolid")
    IfcClass = StringProperty(default="IfcExtrudedAreaSolid")

    # IFC schema attributes
    ExtrudedDirection = ArrayProperty(default=[])
    Depth = FloatProperty(default=None)
    # IFC schema attributes (other instance)
    GraphArbitraryClosedProfileDef = RelationshipTo("GraphArbitraryClosedProfileDef", "SweptArea")
    GraphAxis2Placement3D = RelationshipTo("GraphAxis2Placement3D", "Position")


class GraphShapeRepresentation(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphShapeRepresentation")
    Name = StringProperty(default="ShapeRepresentation")
    IfcClass = StringProperty(default="IfcShapeRepresentation")

    # IFC schema attributes
    ContextOfItems = StringProperty(default=None)
    RepresentationIdentifier = StringProperty(default="BODY")
    RepresentationType = StringProperty(default="SweptSolid")

    # IFC schema attributes (other instance)
    GraphExtrudedAreaSolid = RelationshipTo("GraphExtrudedAreaSolid", "Items")
    GraphPolygonalFaceSet = RelationshipTo("GraphPolygonalFaceSet", "Items")
    GraphIndexedPolyCurve = RelationshipTo("GraphIndexedPolyCurve", "Items")
    GraphMappedItem = RelationshipTo("GraphMappedItem", "Items")


class GraphProductDefinitionShape(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphProductDefinitionShape")
    IfcClass = StringProperty(default="IfcProductDefinitionShape")

    # IFC schema attributes
    Name = StringProperty(default="ProductDefinitionShape")
    Description = StringProperty(default=None)

    # IFC schema attributes (other instance)
    GraphShapeRepresentation = RelationshipTo("GraphShapeRepresentation", "Representations")


# endregion

""" Attribute nodes """


# region Attribute nodes
class GraphAxis2Placement3D(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphAxis2Placement3D")
    Name = StringProperty(default="Axis2Placement3D")
    IfcClass = StringProperty(default="IfcAxis2Placement3D")

    # IFC schema attributes
    Location = ArrayProperty(FloatProperty())
    Axis = ArrayProperty(FloatProperty())
    RefDirection = ArrayProperty(FloatProperty())


class GraphPolyline(StructuredNode):
    GlobalId = UniqueIdProperty()
    GraphClass = StringProperty(default="GraphPolyline")
    Name = StringProperty(default="Polyline")
    IfcClass = StringProperty(default="IfcPolyline")

    # IFC schema attributes
    Points = JSONProperty(default={})

# endregion
