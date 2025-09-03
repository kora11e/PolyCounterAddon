bl_info = {
    "name": "Poly Counter",
    "author": "Canicule",
    "version": (1,0,0),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > Poly Counter",
    "description": "Poly Counter",
    "category": "Development"
}

import bpy 


class MESH_OT_poly_count(bpy.types.Operator):
    bl_idname = "mesh.poly_count"
    bl_label = "Count objects' polycount"
    
    def execute(self, context):
        list_of_objects = {}

        for x in bpy.data.objects:
            if x.type == 'MESH':

                list_of_objects[x.name] = (len(x.data.vertices))
                print(x.name)
                
                print(list_of_objects)
                
        list_of_objects = sorted(list_of_objects, key=list_of_objects.get, reverse=True)
        
        bpy.context.view_layer.objects.active = bpy.data.objects[list_of_objects[0]]
        bpy.data.objects[list_of_objects[0]].select_set(True)
        print(list_of_objects)
        
        #return list_of_objects or not xD
        return {"FINISHED"}
        

class VIEW3D_PT_custom_ui(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bl_category = "Poly Counter"
    bl_label = "Poly Counter"
    
    def draw(self, context):
        row = self.layout.row()
        row.operator("mesh.poly_count", text="Find heaviest Mesh")
        self.layout.separator()


def register():
    bpy.utils.register_class(VIEW3D_PT_custom_ui)
    bpy.utils.register_class(MESH_OT_poly_count)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_custom_ui)
    bpy.utils.unregister_class(MESH_OT_poly_count)
    
if __name__ == "__main__":
    register()
