
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARR BOOL CHAR COMA CORCHDER CORCHIZQ CTEB CTEC CTEF CTEI CTESTRING DIFF DIV DO DOSPUN ELSE FLOAT FOR FUNC ID IF IGIG IGUAL INT LLAVDER LLAVIZQ MAIN MAS MAYIG MAYOR MENIG MENOR MENOS MOD OR PARDER PARIZQ POR PRINT PROGRAM PUNCOM RETURN TO VAR VOID WHILEprogram : PROGRAM ID PUNCOM VAR vars mainmain : MAIN PARIZQ PARDER bloquefuncion : FUNC TIPO insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN exp fin_declaracion_funcion\n               | FUNC VOID insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN fin_declaracion_funcioninsertar_nombre_funcion : guardar_param : fin_declaracion_funcion : acum_func : funcion acum_func\n                  | emptyparam : TIPO ID COMA param\n             | TIPO ID\n             | emptyid_lista : ID COMA id_lista\n               | IDvars : id_lista DOSPUN TIPO PUNCOM vars\n            | emptyTIPO : INT\n            | FLOAT\n            | CHAR\n            | BOOLbloque : LLAVIZQ multiples_estatutos LLAVDERestatuto : asignacion\n                 | condicion\n                 | escritura\n                 | while_condicionmultiples_estatutos : estatuto multiples_estatutos\n                       | emptyasignacion : ID IGUAL expresion PUNCOMescritura : PRINT PARIZQ print_expresion PARDER PUNCOMprint_expresion : expresion multiples_print\n                       | CTESTRING multiples_printmultiples_print : COMA  print_expresion\n                 | emptycondicion : IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM\n                 | IF PARIZQ expresion PARDER verificar_if bloque ELSE verificar_bloque_else bloque verificar_bloque_if PUNCOMwhile_condicion : WHILE PARIZQ guardar_posicion_while expresion verificar_expresion_while PARDER DO bloque llenar_cuadruplo_whileexpresion : expresion AND expresionexpresion : expresion OR expresionexpresion : exp \n                 | exp MAYOR exp\n                 | exp MENOR exp\n                 | exp DIFF exp\n                 | exp IGIG exp\n                 | exp MAYIG exp\n                 | exp MENIG expexp : termino exp_operacionexp_operacion : MAS termino exp_operacion\n                     | MENOS termino exp_operacion\n                     | emptytermino : factor termino_operadortermino_operador : POR factor termino_operador\n                        | DIV factor termino_operador\n                        | emptyfactor : PARIZQ expresion PARDER\n              | MAS var_cte\n              | MENOS var_cte\n              | var_cte\n              | emptyvar_cte : ID\n               | CTEI\n               | CTEF\n               | CTEC\n               | CTEBempty :verificar_if : verificar_bloque_if : verificar_bloque_else : guardar_posicion_while : verificar_expresion_while : llenar_cuadruplo_while : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,11,23,37,],[0,-1,-2,-21,]),'ID':([2,5,10,22,24,27,29,30,31,32,37,39,40,41,42,48,49,51,61,62,63,64,65,66,67,68,69,70,72,73,76,77,85,103,115,117,119,121,],[3,6,6,6,33,33,-22,-23,-24,-25,-21,43,43,43,-68,43,43,43,43,-28,43,43,43,43,43,43,43,43,43,43,43,43,43,-29,-34,-70,-36,-35,]),'PUNCOM':([3,16,17,18,19,20,37,39,43,44,45,46,47,50,52,53,54,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,83,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,110,112,118,120,],[4,22,-17,-18,-19,-20,-21,-64,-59,62,-39,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-64,-64,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,103,-37,-38,-40,-41,-42,-43,-44,-45,-64,-64,-64,-64,-54,-47,-48,-51,-52,-66,115,-66,121,]),'VAR':([4,],[5,]),'MAIN':([5,7,9,22,25,],[-64,12,-16,-64,-15,]),'COMA':([6,41,43,45,46,47,50,52,53,54,55,56,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,85,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[10,-64,-59,-39,-64,-64,-57,-58,-60,-61,-62,-63,85,85,-64,-64,-64,-64,-64,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-37,-38,-40,-41,-42,-43,-44,-45,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'DOSPUN':([6,8,14,],[-14,13,-13,]),'PARIZQ':([12,34,35,36,39,40,41,42,48,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[15,40,41,42,48,48,48,-68,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'INT':([13,],[17,]),'FLOAT':([13,],[18,]),'CHAR':([13,],[19,]),'BOOL':([13,],[20,]),'PARDER':([15,40,41,42,43,45,46,47,48,50,52,53,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,106,107,108,109,],[21,-64,-64,-68,-59,-39,-64,-64,-64,-57,-58,-60,-61,-62,-63,82,83,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,101,-55,-56,-30,-64,-33,-31,-69,-37,-38,-40,-41,-42,-43,-44,-45,-64,-64,-64,-64,-54,-32,111,-47,-48,-51,-52,]),'LLAVIZQ':([21,82,102,113,114,116,],[24,-65,24,-67,24,24,]),'LLAVDER':([24,26,27,28,29,30,31,32,37,38,62,103,115,117,119,121,],[-64,37,-64,-27,-22,-23,-24,-25,-21,-26,-28,-29,-34,-70,-36,-35,]),'IF':([24,27,29,30,31,32,37,62,103,115,117,119,121,],[34,34,-22,-23,-24,-25,-21,-28,-29,-34,-70,-36,-35,]),'PRINT':([24,27,29,30,31,32,37,62,103,115,117,119,121,],[35,35,-22,-23,-24,-25,-21,-28,-29,-34,-70,-36,-35,]),'WHILE':([24,27,29,30,31,32,37,62,103,115,117,119,121,],[36,36,-22,-23,-24,-25,-21,-28,-29,-34,-70,-36,-35,]),'IGUAL':([33,],[39,]),'ELSE':([37,110,],[-21,113,]),'MAS':([39,40,41,42,43,46,47,48,50,52,53,54,55,56,61,63,64,65,66,67,68,69,70,72,73,75,76,77,78,80,81,85,97,98,99,100,101,108,109,],[49,49,49,-68,-59,72,-64,49,-57,-58,-60,-61,-62,-63,49,49,49,49,49,49,49,49,49,49,49,-50,49,49,-53,-55,-56,49,72,72,-64,-64,-54,-51,-52,]),'MENOS':([39,40,41,42,43,46,47,48,50,52,53,54,55,56,61,63,64,65,66,67,68,69,70,72,73,75,76,77,78,80,81,85,97,98,99,100,101,108,109,],[51,51,51,-68,-59,73,-64,51,-57,-58,-60,-61,-62,-63,51,51,51,51,51,51,51,51,51,51,51,-50,51,51,-53,-55,-56,51,73,73,-64,-64,-54,-51,-52,]),'CTEI':([39,40,41,42,48,49,51,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[53,53,53,-68,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'CTEF':([39,40,41,42,48,49,51,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[54,54,54,-68,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'CTEC':([39,40,41,42,48,49,51,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[55,55,55,-68,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CTEB':([39,40,41,42,48,49,51,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[56,56,56,-68,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'POR':([39,40,41,42,43,47,48,50,52,53,54,55,56,61,63,64,65,66,67,68,69,70,72,73,76,77,80,81,85,99,100,101,],[-64,-64,-64,-68,-59,76,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-55,-56,-64,76,76,-54,]),'DIV':([39,40,41,42,43,47,48,50,52,53,54,55,56,61,63,64,65,66,67,68,69,70,72,73,76,77,80,81,85,99,100,101,],[-64,-64,-64,-68,-59,77,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-55,-56,-64,77,77,-54,]),'MAYOR':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,65,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'MENOR':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,66,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'DIFF':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,67,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'IGIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,68,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'MAYIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,69,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'MENIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,61,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,70,-64,-64,-64,-57,-58,-60,-61,-62,-63,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,-55,-56,-64,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'AND':([39,40,41,42,43,44,45,46,47,48,50,52,53,54,55,56,57,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,63,-39,-64,-64,-64,-57,-58,-60,-61,-62,-63,63,63,-64,-64,-64,-64,-64,-64,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,63,-55,-56,-64,63,63,63,-40,-41,-42,-43,-44,-45,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'OR':([39,40,41,42,43,44,45,46,47,48,50,52,53,54,55,56,57,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[-64,-64,-64,-68,-59,64,-39,-64,-64,-64,-57,-58,-60,-61,-62,-63,64,64,-64,-64,-64,-64,-64,-64,-64,-64,-64,-46,-64,-64,-49,-50,-64,-64,-53,64,-55,-56,-64,64,64,64,-40,-41,-42,-43,-44,-45,-64,-64,-64,-64,-54,-47,-48,-51,-52,]),'CTESTRING':([41,85,],[60,60,]),'DO':([111,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([5,22,],[7,25,]),'id_lista':([5,10,22,],[8,14,8,]),'empty':([5,22,24,27,39,40,41,46,47,48,59,60,61,63,64,65,66,67,68,69,70,72,73,76,77,85,97,98,99,100,],[9,9,28,28,52,52,52,74,78,52,86,86,52,52,52,52,52,52,52,52,52,52,52,52,52,52,74,74,78,78,]),'main':([7,],[11,]),'TIPO':([13,],[16,]),'bloque':([21,102,114,116,],[23,110,117,118,]),'multiples_estatutos':([24,27,],[26,38,]),'estatuto':([24,27,],[27,27,]),'asignacion':([24,27,],[29,29,]),'condicion':([24,27,],[30,30,]),'escritura':([24,27,],[31,31,]),'while_condicion':([24,27,],[32,32,]),'expresion':([39,40,41,48,61,63,64,85,],[44,57,59,79,88,89,90,59,]),'exp':([39,40,41,48,61,63,64,65,66,67,68,69,70,85,],[45,45,45,45,45,45,45,91,92,93,94,95,96,45,]),'termino':([39,40,41,48,61,63,64,65,66,67,68,69,70,72,73,85,],[46,46,46,46,46,46,46,46,46,46,46,46,46,97,98,46,]),'factor':([39,40,41,48,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,99,100,47,]),'var_cte':([39,40,41,48,49,51,61,63,64,65,66,67,68,69,70,72,73,76,77,85,],[50,50,50,50,80,81,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'print_expresion':([41,85,],[58,104,]),'guardar_posicion_while':([42,],[61,]),'exp_operacion':([46,97,98,],[71,106,107,]),'termino_operador':([47,99,100,],[75,108,109,]),'multiples_print':([59,60,],[84,87,]),'verificar_if':([82,],[102,]),'verificar_expresion_while':([88,],[105,]),'verificar_bloque_if':([110,118,],[112,120,]),'verificar_bloque_else':([113,],[116,]),'llenar_cuadruplo_while':([117,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID PUNCOM VAR vars main','program',6,'p_program','parser_1.py',161),
  ('main -> MAIN PARIZQ PARDER bloque','main',4,'p_main','parser_1.py',171),
  ('funcion -> FUNC TIPO insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN exp fin_declaracion_funcion','funcion',13,'p_funcion','parser_1.py',174),
  ('funcion -> FUNC VOID insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN fin_declaracion_funcion','funcion',12,'p_funcion','parser_1.py',175),
  ('insertar_nombre_funcion -> <empty>','insertar_nombre_funcion',0,'p_insertar_nombre_funcion','parser_1.py',183),
  ('guardar_param -> <empty>','guardar_param',0,'p_guardar_param','parser_1.py',203),
  ('fin_declaracion_funcion -> <empty>','fin_declaracion_funcion',0,'p_fin_declaracion_funcion','parser_1.py',227),
  ('acum_func -> funcion acum_func','acum_func',2,'p_acum_func','parser_1.py',240),
  ('acum_func -> empty','acum_func',1,'p_acum_func','parser_1.py',241),
  ('param -> TIPO ID COMA param','param',4,'p_param','parser_1.py',244),
  ('param -> TIPO ID','param',2,'p_param','parser_1.py',245),
  ('param -> empty','param',1,'p_param','parser_1.py',246),
  ('id_lista -> ID COMA id_lista','id_lista',3,'p_id_lista','parser_1.py',257),
  ('id_lista -> ID','id_lista',1,'p_id_lista','parser_1.py',258),
  ('vars -> id_lista DOSPUN TIPO PUNCOM vars','vars',5,'p_vars','parser_1.py',277),
  ('vars -> empty','vars',1,'p_vars','parser_1.py',278),
  ('TIPO -> INT','TIPO',1,'p_TIPO','parser_1.py',287),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','parser_1.py',288),
  ('TIPO -> CHAR','TIPO',1,'p_TIPO','parser_1.py',289),
  ('TIPO -> BOOL','TIPO',1,'p_TIPO','parser_1.py',290),
  ('bloque -> LLAVIZQ multiples_estatutos LLAVDER','bloque',3,'p_bloque','parser_1.py',299),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser_1.py',306),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser_1.py',307),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','parser_1.py',308),
  ('estatuto -> while_condicion','estatuto',1,'p_estatuto','parser_1.py',309),
  ('multiples_estatutos -> estatuto multiples_estatutos','multiples_estatutos',2,'p_multiples_estatutos','parser_1.py',313),
  ('multiples_estatutos -> empty','multiples_estatutos',1,'p_multiples_estatutos','parser_1.py',314),
  ('asignacion -> ID IGUAL expresion PUNCOM','asignacion',4,'p_asignacion','parser_1.py',320),
  ('escritura -> PRINT PARIZQ print_expresion PARDER PUNCOM','escritura',5,'p_escritura','parser_1.py',346),
  ('print_expresion -> expresion multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',350),
  ('print_expresion -> CTESTRING multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',351),
  ('multiples_print -> COMA print_expresion','multiples_print',2,'p_multiples_print','parser_1.py',355),
  ('multiples_print -> empty','multiples_print',1,'p_multiples_print','parser_1.py',356),
  ('condicion -> IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM','condicion',8,'p_condicion','parser_1.py',360),
  ('condicion -> IF PARIZQ expresion PARDER verificar_if bloque ELSE verificar_bloque_else bloque verificar_bloque_if PUNCOM','condicion',11,'p_condicion','parser_1.py',361),
  ('while_condicion -> WHILE PARIZQ guardar_posicion_while expresion verificar_expresion_while PARDER DO bloque llenar_cuadruplo_while','while_condicion',9,'p_while_condicion','parser_1.py',364),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_and','parser_1.py',372),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_or','parser_1.py',376),
  ('expresion -> exp','expresion',1,'p_expresion','parser_1.py',380),
  ('expresion -> exp MAYOR exp','expresion',3,'p_expresion','parser_1.py',381),
  ('expresion -> exp MENOR exp','expresion',3,'p_expresion','parser_1.py',382),
  ('expresion -> exp DIFF exp','expresion',3,'p_expresion','parser_1.py',383),
  ('expresion -> exp IGIG exp','expresion',3,'p_expresion','parser_1.py',384),
  ('expresion -> exp MAYIG exp','expresion',3,'p_expresion','parser_1.py',385),
  ('expresion -> exp MENIG exp','expresion',3,'p_expresion','parser_1.py',386),
  ('exp -> termino exp_operacion','exp',2,'p_exp','parser_1.py',407),
  ('exp_operacion -> MAS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',412),
  ('exp_operacion -> MENOS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',413),
  ('exp_operacion -> empty','exp_operacion',1,'p_exp_operacion','parser_1.py',414),
  ('termino -> factor termino_operador','termino',2,'p_termino','parser_1.py',426),
  ('termino_operador -> POR factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',431),
  ('termino_operador -> DIV factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',432),
  ('termino_operador -> empty','termino_operador',1,'p_termino_operador','parser_1.py',433),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','parser_1.py',443),
  ('factor -> MAS var_cte','factor',2,'p_factor','parser_1.py',444),
  ('factor -> MENOS var_cte','factor',2,'p_factor','parser_1.py',445),
  ('factor -> var_cte','factor',1,'p_factor','parser_1.py',446),
  ('factor -> empty','factor',1,'p_factor','parser_1.py',447),
  ('var_cte -> ID','var_cte',1,'p_var_cte','parser_1.py',451),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','parser_1.py',452),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','parser_1.py',453),
  ('var_cte -> CTEC','var_cte',1,'p_var_cte','parser_1.py',454),
  ('var_cte -> CTEB','var_cte',1,'p_var_cte','parser_1.py',455),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',478),
  ('verificar_if -> <empty>','verificar_if',0,'p_verificar_if','parser_1.py',519),
  ('verificar_bloque_if -> <empty>','verificar_bloque_if',0,'p_verificar_bloque_if','parser_1.py',526),
  ('verificar_bloque_else -> <empty>','verificar_bloque_else',0,'p_verificar_bloque_else','parser_1.py',533),
  ('guardar_posicion_while -> <empty>','guardar_posicion_while',0,'p_guardar_posicion_while','parser_1.py',541),
  ('verificar_expresion_while -> <empty>','verificar_expresion_while',0,'p_verificar_expresion_while','parser_1.py',546),
  ('llenar_cuadruplo_while -> <empty>','llenar_cuadruplo_while',0,'p_llenar_cuadruplo_while','parser_1.py',557),
]
