#-----------------------------------------------------------------------------
#
# Controladores de las funcionalidades de Gestion
#
# - Erick Flejan <12-1155@usb.ve>
# - Amanda Camacho <12-10644@usb.ve>
# - David Cabeza <13-10191@usb.ve>
# - Fabiola Martínez <13-10838@usb.ve>
# - Lautaro Villalon <12-10427@usb.ve>
# - Yarima Luciani <13-10770@usb.ve>
#-----------------------------------------------------------------------------

@auth.requires_login(otherwise=URL('modulos', 'login'))
def usuarios():
    if(auth.has_membership('ADMINISTRADOR PERSONAL') or auth.has_membership('WEBMASTER')\
       or auth.has_membership('DIRECTOR') or (auth.user.email == "ulab-calidad@usb.ve")):
        table = SQLFORM.smartgrid(db.auth_user,onupdate=auth.archive,links_in_grid=False,csv=False,user_signature=True,paginate=10)
    else:
        table = SQLFORM.smartgrid(db.auth_user,editable=False,deletable=False,csv=False,links_in_grid=False,create=False,paginate=10)
    return locals()

@auth.requires_login(otherwise=URL('modulos', 'login'))
def dependencias():
    if(auth.has_membership('ADMINISTRADOR PERSONAL') or auth.has_membership('WEBMASTER')\
       or auth.has_membership('DIRECTOR') or (auth.user.email == "ulab-calidad@usb.ve")):
        table = SQLFORM.smartgrid(db.dependencias,onupdate=auth.archive,links_in_grid=False,csv=False,user_signature=True,paginate=10)
    else:
        table = SQLFORM.smartgrid(db.dependencias,editable=False,deletable=False,csv=False,links_in_grid=False,create=False,paginate=10)
    return locals()

@auth.requires_login(otherwise=URL('modulos', 'login'))
def espacios_fisicos():
    if(auth.has_membership('ADMINISTRADOR PERSONAL') or auth.has_membership('WEBMASTER')\
       or auth.has_membership('DIRECTOR') or (auth.user.email == "ulab-calidad@usb.ve")):
        table = SQLFORM.smartgrid(db.espacios_fisicos,onupdate=auth.archive,links_in_grid=False,csv=False,user_signature=True,paginate=10)
    else:
        table = SQLFORM.smartgrid(db.espacios_fisicos,editable=False,deletable=False,csv=False,links_in_grid=False,create=False,paginate=10)
    return locals()