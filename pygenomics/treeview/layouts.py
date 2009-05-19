import numpy
import faces

def basic(node):
  if node.is_leaf():
     faces.add_face(node, 0, faces.AttrFace("name","Arial",10,"#24416d",None) )

def phylogeny(node):
        leaf_color = "#24416d"
        if hasattr(node,"evoltype"):
                if node.evoltype == 'D':
                    node.img_style["fgcolor"] = "#0000FF"
                    node.img_style["hz_line_color"] = "#0000FF"
                    node.img_style["vt_line_color"] = "#0000FF"
                elif node.evoltype == 'S':
                    node.img_style["fgcolor"] = "#FF0000"
                    node.img_style["line_color"] = "#FF0000"
                elif node.evoltype == 'L':
                    node.img_style["fgcolor"] = "#999999"
                    node.img_style["vt_line_color"] = "#999999"
                    node.img_style["hz_line_color"] = "#999999"
                    node.img_style["line_type"] = 1
                    leaf_color = "#999999"

        if node.is_leaf():
            faces.add_face(node, 0, faces.AttrFace("name","Arial",12,leaf_color,None) )
            if hasattr(node,"sequence"):
                SequenceFace =  faces.SequenceFace(node.sequence,"aa",17)
                faces.add_face(node, 1, SequenceFace, aligned=True)

def cluster_heatmap(node):
        # Extras node info
        node.collapsed = False
        # Color and style
        node.img_style["fgcolor"] = "#3333FF"
        node.img_style["size"] =  0

        matrix_max = numpy.max(node.arraytable.matrix)
        matrix_min = numpy.min(node.arraytable.matrix)
        matrix_avg = matrix_min+((matrix_max-matrix_min)/2)
        ProfileFace = faces.ProfileFace(\
                                            matrix_max,\
                                            matrix_min,\
                                            matrix_avg,\
                                            200,\
                                            2,\
                                            "heatmap")
        ProfileFace.ymargin=0
        if node.is_leaf():
            # Set colors
            faces.add_face(node,0, ProfileFace, aligned=True )
          
def cluster_cbars(node):
        # Extras node info
        node.collapsed = False
        # Color and style
        node.img_style["fgcolor"] = "#3333FF"
        node.img_style["size"] =  4
        matrix_max = numpy.max(node.arraytable.matrix)
        matrix_min = numpy.min(node.arraytable.matrix)
        matrix_avg = matrix_min+((matrix_max-matrix_min)/2)
        ProfileFace = faces.ProfileFace(\
                                            matrix_max,\
                                            matrix_min,\
                                            matrix_avg,\
                                            200,\
                                            60,\
                                            "cbars")

        if node.is_leaf():
            nameFace = faces.AttrFace("name",fsize=6 )
            faces.add_face(node, 1, nameFace, aligned=True ) 
            faces.add_face(node,0, ProfileFace, aligned=True )
        else:
            # Set custom faces
            faces.add_face(node,0, ProfileFace, aligned=True )

def cluster_lines(node):
        # Extras node info
        node.collapsed = False
        # Color and style
        node.img_style["fgcolor"] = "#3333FF"
        node.img_style["size"] = 4
        matrix_max = numpy.max(node.arraytable.matrix)
        matrix_min = numpy.min(node.arraytable.matrix)
        matrix_avg = matrix_min+((matrix_max-matrix_min)/2)
        ProfileFace = faces.ProfileFace(\
          matrix_max,\
            matrix_min,\
            matrix_avg,\
            200,\
            50,\
            "lines")

        if node.is_leaf():
            nameFace = faces.AttrFace("name",fsize=6 )
            faces.add_face(node, 1, nameFace, aligned=True ) 
            faces.add_face(node,0, ProfileFace, aligned=True )
        else:
            # Set custom faces
            faces.add_face(node,0, ProfileFace, aligned=True )

def cluster_bars(node):
        # Extras node info
        node.collapsed = False
        # Color and style
        node.img_style["fgcolor"] = "#3333FF"
        node.img_style["size"] = 4
     
        if node.is_leaf():
          matrix_max = numpy.max(node.arraytable.matrix)
          matrix_min = numpy.min(node.arraytable.matrix)
          matrix_avg = matrix_min+((matrix_max-matrix_min)/2)
          ProfileFace = faces.ProfileFace(\
            matrix_max,\
              matrix_min,\
              matrix_avg,\
              200,\
              40,\
              "bars")
          nameFace = faces.AttrFace("name",fsize=6 )
          faces.add_face(node, 1, nameFace, aligned=True ) 
          faces.add_face(node,0, ProfileFace, aligned=True )

def large(node):
        # Color and style
        node.img_style["fgcolor"] = "#3333FF"
        node.img_style["size"] = 0
       

# Labels to show in qt application menu
layout_functions = {
        "Basic": basic, 
        "Phylogenetic tree": phylogeny, 
        "Clustering heatmap": cluster_heatmap, 
        "Clustering validation (bars)": cluster_bars, 
        "Clustering validation (profiles)": cluster_cbars, 
        "Very large topology": large
        }

