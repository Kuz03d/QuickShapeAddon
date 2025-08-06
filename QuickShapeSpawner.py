bl_info = {
    "name": "QuickShape Spawner",
    "author": "Kuzo3D",
    "version": (1, 0),
    "blender": (3, 0, 0),  
    "location": "View3D > Sidebar > ShapeSpawner Tab",
    "warning": "fear the allmighty cube",
    "wiki_url": "https://github.com/Kuz03d/QuickShapeAddon",
    "category": "Add Mesh",
}

import bpy

class VIEW3D_PT_shape_spawner_main(bpy.types.Panel):
    bl_label = "QuickShape Spawner"
    bl_idname = "VIEW3D_PT_shape_spawner_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ShapeSpawner'

    def draw(self, context):
        layout = self.layout
        layout.scale_y=1.6
        layout.label(text="Choose an action below:")

class VIEW3D_PT_shape_spawner_cube(bpy.types.Panel):
    bl_label = "Cube"
    bl_idname = "VIEW3D_PT_shape_spawner_cube"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ShapeSpawner'
    bl_parent_id = "VIEW3D_PT_shape_spawner_main"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.scale_y=1.2
        layout.operator("mesh.primitive_cube_add", text="Cube", icon='CUBE')
        layout.label(text="Allmighty Cube")
        

        
        
class VIEW3D_PT_shape_spawner_others(bpy.types.Panel):
    bl_label = "Others"
    bl_idname = "VIEW3D_PT_shape_spawner_others"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ShapeSpawner'
    bl_parent_id = "VIEW3D_PT_shape_spawner_main"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row=layout.row()
        layout.scale_y=0.7
        row.operator("mesh.primitive_cylinder_add", text="Cylinder", icon='MESH_CYLINDER')
        row.operator("mesh.primitive_uv_sphere_add", text="UVsphere", icon='MESH_UVSPHERE')
        layout.operator("mesh.primitive_cone_add", text="Cone", icon='MESH_CONE')
        row=layout.row()
        row.operator("mesh.primitive_plane_add", text="Plane",icon='MESH_PLANE')
        row.operator("mesh.primitive_torus_add", text="Torus",icon='MESH_TORUS')
        layout.operator("mesh.primitive_ico_sphere_add", text="IcoSphere", icon='MESH_ICOSPHERE')

class OBJECT_OT_select(bpy.types.Operator):
    bl_idname="object.select"
    bl_label = "Select All Objects"
    bl_description="Selects all objects"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.ops.object.select_all(action="SELECT")
        return{'FINISHED'}  


class OBJECT_OT_delete_selected(bpy.types.Operator):
    bl_idname="object.delete_selected_objects"
    bl_label = "Delete Selected Objects"
    bl_description="Deletes all of the selected objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.object.delete()
        return{'FINISHED'}     
    
       
class OBJECT_OT_delete_all(bpy.types.Operator):
    bl_idname="object.delete_all_objects"
    bl_label = "Delete All Objects"
    bl_description="Deletes all of the objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()
        return{'FINISHED'}
        
        
class VIEW3D_PT_shape_spawner_shade(bpy.types.Panel):
    bl_label = "Special Operations"
    bl_idname = "VIEW3D_PT_shape_spawner_shade"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ShapeSpawner'
    bl_parent_id = "VIEW3D_PT_shape_spawner_main"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row=layout.row()
        layout.scale_y=0.7
        row.operator("object.shade_smooth")
        row.operator("object.shade_flat")
        row=layout.row()
        row.operator("object.shade_auto_smooth")
        obj=context.object
        mode=bpy.context.mode
        row=layout.row()
        
        if obj and obj.type=="MESH":
            mesh=obj.data
            layout.label(text=f"Selected Mesh: {obj.name}")
            col=layout.column()
            col.prop(context.object,"location")
            col.prop(context.object,"scale")
            col.prop(context.object,"rotation_euler",text="Rotation")

        else:
            layout.label(text="No objects selected")
        if mode =="OBJECT":
            layout.operator("object.select")
            layout.operator("object.delete_selected_objects",icon="TRASH")
            layout.operator("object.delete_all_objects", icon='TRASH')
        
            


classes = (
    OBJECT_OT_select,
    OBJECT_OT_delete_all,
    OBJECT_OT_delete_selected,
    VIEW3D_PT_shape_spawner_main,
    VIEW3D_PT_shape_spawner_cube,
    VIEW3D_PT_shape_spawner_others,
    VIEW3D_PT_shape_spawner_shade
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
     
    
