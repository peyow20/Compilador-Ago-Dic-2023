
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARR BOOL CHAR COMA CORCHDER CORCHIZQ CTEB CTEC CTEF CTEI CTESTRING DIFF DIV DO DOSPUN ELSE FLOAT FOR FUNC ID IF IGIG IGUAL INT LLAVDER LLAVIZQ MAIN MAS MAYIG MAYOR MENIG MENOR MENOS MOD OR PARDER PARIZQ POR PRINT PROGRAM PUNCOM RETURN TO VAR VOID WHILEprogram : PROGRAM ID PUNCOM VAR vars mainmain : MAIN PARIZQ PARDER bloqueid_lista : ID COMA id_lista\n               | IDvars : id_lista DOSPUN TIPO PUNCOM vars\n            | emptyTIPO : INT\n            | FLOAT\n            | CHAR\n            | BOOLbloque : LLAVIZQ multiples_estatutos LLAVDERestatuto : asignacion\n                 | condicion\n                 | escritura\n                 | while_condicionmultiples_estatutos : estatuto multiples_estatutos\n                       | emptyasignacion : ID IGUAL expresion PUNCOMescritura : PRINT PARIZQ print_expresion PARDER PUNCOMprint_expresion : expresion multiples_print\n                       | CTESTRING multiples_printmultiples_print : COMA  print_expresion\n                 | emptycondicion : IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOMverificar_if : verificar_bloque_if :  while_condicion : WHILE PARIZQ expresion PARDER DO bloqueexpresion : expresion AND expresionexpresion : expresion OR expresionexpresion : exp \n                 | exp MAYOR exp\n                 | exp MENOR exp\n                 | exp DIFF exp\n                 | exp IGIG exp\n                 | exp MAYIG exp\n                 | exp MENIG expexp : termino exp_operacionexp_operacion : MAS termino exp_operacion\n                     | MENOS termino exp_operacion\n                     | emptytermino : factor termino_operadortermino_operador : POR factor termino_operador\n                        | DIV factor termino_operador\n                        | emptyfactor : PARIZQ expresion PARDER\n              | MAS var_cte\n              | MENOS var_cte\n              | var_cte\n              | emptyvar_cte : ID\n               | CTEI\n               | CTEF\n               | CTEC\n               | CTEBempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,11,23,37,],[0,-1,-2,-11,]),'ID':([2,5,10,22,24,27,29,30,31,32,37,39,40,41,42,48,49,51,62,63,64,65,66,67,68,69,70,72,73,76,77,85,103,111,113,],[3,6,6,6,33,33,-12,-13,-14,-15,-11,43,43,43,43,43,43,43,-18,43,43,43,43,43,43,43,43,43,43,43,43,43,-19,-27,-24,]),'PUNCOM':([3,16,17,18,19,20,37,39,43,44,45,46,47,50,52,53,54,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,83,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,110,112,],[4,22,-7,-8,-9,-10,-11,-55,-50,62,-30,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-55,-55,-55,-55,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,103,-28,-29,-31,-32,-33,-34,-35,-36,-55,-55,-55,-55,-45,-38,-39,-42,-43,-26,113,]),'VAR':([4,],[5,]),'MAIN':([5,7,9,22,25,],[-55,12,-6,-55,-5,]),'COMA':([6,41,43,45,46,47,50,52,53,54,55,56,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,85,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[10,-55,-50,-30,-55,-55,-48,-49,-51,-52,-53,-54,85,85,-55,-55,-55,-55,-55,-55,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-28,-29,-31,-32,-33,-34,-35,-36,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'DOSPUN':([6,8,14,],[-4,13,-3,]),'PARIZQ':([12,34,35,36,39,40,41,42,48,63,64,65,66,67,68,69,70,72,73,76,77,85,],[15,40,41,42,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'INT':([13,],[17,]),'FLOAT':([13,],[18,]),'CHAR':([13,],[19,]),'BOOL':([13,],[20,]),'PARDER':([15,40,41,42,43,45,46,47,48,50,52,53,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,104,106,107,108,109,],[21,-55,-55,-55,-50,-30,-55,-55,-55,-48,-49,-51,-52,-53,-54,82,83,-55,-55,88,-55,-55,-55,-55,-55,-55,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,101,-46,-47,-20,-55,-23,-21,-28,-29,-31,-32,-33,-34,-35,-36,-55,-55,-55,-55,-45,-22,-38,-39,-42,-43,]),'LLAVIZQ':([21,82,102,105,],[24,-25,24,24,]),'LLAVDER':([24,26,27,28,29,30,31,32,37,38,62,103,111,113,],[-55,37,-55,-17,-12,-13,-14,-15,-11,-16,-18,-19,-27,-24,]),'IF':([24,27,29,30,31,32,37,62,103,111,113,],[34,34,-12,-13,-14,-15,-11,-18,-19,-27,-24,]),'PRINT':([24,27,29,30,31,32,37,62,103,111,113,],[35,35,-12,-13,-14,-15,-11,-18,-19,-27,-24,]),'WHILE':([24,27,29,30,31,32,37,62,103,111,113,],[36,36,-12,-13,-14,-15,-11,-18,-19,-27,-24,]),'IGUAL':([33,],[39,]),'MAS':([39,40,41,42,43,46,47,48,50,52,53,54,55,56,63,64,65,66,67,68,69,70,72,73,75,76,77,78,80,81,85,97,98,99,100,101,108,109,],[49,49,49,49,-50,72,-55,49,-48,-49,-51,-52,-53,-54,49,49,49,49,49,49,49,49,49,49,-41,49,49,-44,-46,-47,49,72,72,-55,-55,-45,-42,-43,]),'MENOS':([39,40,41,42,43,46,47,48,50,52,53,54,55,56,63,64,65,66,67,68,69,70,72,73,75,76,77,78,80,81,85,97,98,99,100,101,108,109,],[51,51,51,51,-50,73,-55,51,-48,-49,-51,-52,-53,-54,51,51,51,51,51,51,51,51,51,51,-41,51,51,-44,-46,-47,51,73,73,-55,-55,-45,-42,-43,]),'CTEI':([39,40,41,42,48,49,51,63,64,65,66,67,68,69,70,72,73,76,77,85,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'CTEF':([39,40,41,42,48,49,51,63,64,65,66,67,68,69,70,72,73,76,77,85,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'CTEC':([39,40,41,42,48,49,51,63,64,65,66,67,68,69,70,72,73,76,77,85,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CTEB':([39,40,41,42,48,49,51,63,64,65,66,67,68,69,70,72,73,76,77,85,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'POR':([39,40,41,42,43,47,48,50,52,53,54,55,56,63,64,65,66,67,68,69,70,72,73,76,77,80,81,85,99,100,101,],[-55,-55,-55,-55,-50,76,-55,-48,-49,-51,-52,-53,-54,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-46,-47,-55,76,76,-45,]),'DIV':([39,40,41,42,43,47,48,50,52,53,54,55,56,63,64,65,66,67,68,69,70,72,73,76,77,80,81,85,99,100,101,],[-55,-55,-55,-55,-50,77,-55,-48,-49,-51,-52,-53,-54,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-46,-47,-55,77,77,-45,]),'MAYOR':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,65,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'MENOR':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,66,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'DIFF':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,67,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'IGIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,68,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'MAYIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,69,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'MENIG':([39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,63,64,71,72,73,74,75,76,77,78,80,81,85,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,70,-55,-55,-55,-48,-49,-51,-52,-53,-54,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,-46,-47,-55,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'AND':([39,40,41,42,43,44,45,46,47,48,50,52,53,54,55,56,57,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,63,-30,-55,-55,-55,-48,-49,-51,-52,-53,-54,63,63,63,-55,-55,-55,-55,-55,-55,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,63,-46,-47,-55,63,63,-31,-32,-33,-34,-35,-36,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'OR':([39,40,41,42,43,44,45,46,47,48,50,52,53,54,55,56,57,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,],[-55,-55,-55,-55,-50,64,-30,-55,-55,-55,-48,-49,-51,-52,-53,-54,64,64,64,-55,-55,-55,-55,-55,-55,-55,-55,-37,-55,-55,-40,-41,-55,-55,-44,64,-46,-47,-55,64,64,-31,-32,-33,-34,-35,-36,-55,-55,-55,-55,-45,-38,-39,-42,-43,]),'CTESTRING':([41,85,],[60,60,]),'DO':([88,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([5,22,],[7,25,]),'id_lista':([5,10,22,],[8,14,8,]),'empty':([5,22,24,27,39,40,41,42,46,47,48,59,60,63,64,65,66,67,68,69,70,72,73,76,77,85,97,98,99,100,],[9,9,28,28,52,52,52,52,74,78,52,86,86,52,52,52,52,52,52,52,52,52,52,52,52,52,74,74,78,78,]),'main':([7,],[11,]),'TIPO':([13,],[16,]),'bloque':([21,102,105,],[23,110,111,]),'multiples_estatutos':([24,27,],[26,38,]),'estatuto':([24,27,],[27,27,]),'asignacion':([24,27,],[29,29,]),'condicion':([24,27,],[30,30,]),'escritura':([24,27,],[31,31,]),'while_condicion':([24,27,],[32,32,]),'expresion':([39,40,41,42,48,63,64,85,],[44,57,59,61,79,89,90,59,]),'exp':([39,40,41,42,48,63,64,65,66,67,68,69,70,85,],[45,45,45,45,45,45,45,91,92,93,94,95,96,45,]),'termino':([39,40,41,42,48,63,64,65,66,67,68,69,70,72,73,85,],[46,46,46,46,46,46,46,46,46,46,46,46,46,97,98,46,]),'factor':([39,40,41,42,48,63,64,65,66,67,68,69,70,72,73,76,77,85,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,99,100,47,]),'var_cte':([39,40,41,42,48,49,51,63,64,65,66,67,68,69,70,72,73,76,77,85,],[50,50,50,50,50,80,81,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'print_expresion':([41,85,],[58,104,]),'exp_operacion':([46,97,98,],[71,106,107,]),'termino_operador':([47,99,100,],[75,108,109,]),'multiples_print':([59,60,],[84,87,]),'verificar_if':([82,],[102,]),'verificar_bloque_if':([110,],[112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID PUNCOM VAR vars main','program',6,'p_program','parser_1.py',154),
  ('main -> MAIN PARIZQ PARDER bloque','main',4,'p_main','parser_1.py',162),
  ('id_lista -> ID COMA id_lista','id_lista',3,'p_id_lista','parser_1.py',192),
  ('id_lista -> ID','id_lista',1,'p_id_lista','parser_1.py',193),
  ('vars -> id_lista DOSPUN TIPO PUNCOM vars','vars',5,'p_vars','parser_1.py',212),
  ('vars -> empty','vars',1,'p_vars','parser_1.py',213),
  ('TIPO -> INT','TIPO',1,'p_TIPO','parser_1.py',222),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','parser_1.py',223),
  ('TIPO -> CHAR','TIPO',1,'p_TIPO','parser_1.py',224),
  ('TIPO -> BOOL','TIPO',1,'p_TIPO','parser_1.py',225),
  ('bloque -> LLAVIZQ multiples_estatutos LLAVDER','bloque',3,'p_bloque','parser_1.py',234),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser_1.py',241),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser_1.py',242),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','parser_1.py',243),
  ('estatuto -> while_condicion','estatuto',1,'p_estatuto','parser_1.py',244),
  ('multiples_estatutos -> estatuto multiples_estatutos','multiples_estatutos',2,'p_multiples_estatutos','parser_1.py',248),
  ('multiples_estatutos -> empty','multiples_estatutos',1,'p_multiples_estatutos','parser_1.py',249),
  ('asignacion -> ID IGUAL expresion PUNCOM','asignacion',4,'p_asignacion','parser_1.py',255),
  ('escritura -> PRINT PARIZQ print_expresion PARDER PUNCOM','escritura',5,'p_escritura','parser_1.py',281),
  ('print_expresion -> expresion multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',285),
  ('print_expresion -> CTESTRING multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',286),
  ('multiples_print -> COMA print_expresion','multiples_print',2,'p_multiples_print','parser_1.py',290),
  ('multiples_print -> empty','multiples_print',1,'p_multiples_print','parser_1.py',291),
  ('condicion -> IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM','condicion',8,'p_condicion','parser_1.py',295),
  ('verificar_if -> <empty>','verificar_if',0,'p_verificar_if','parser_1.py',299),
  ('verificar_bloque_if -> <empty>','verificar_bloque_if',0,'p_verificar_bloque_if','parser_1.py',307),
  ('while_condicion -> WHILE PARIZQ expresion PARDER DO bloque','while_condicion',6,'p_while_condicion','parser_1.py',314),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_and','parser_1.py',344),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_or','parser_1.py',348),
  ('expresion -> exp','expresion',1,'p_expresion','parser_1.py',352),
  ('expresion -> exp MAYOR exp','expresion',3,'p_expresion','parser_1.py',353),
  ('expresion -> exp MENOR exp','expresion',3,'p_expresion','parser_1.py',354),
  ('expresion -> exp DIFF exp','expresion',3,'p_expresion','parser_1.py',355),
  ('expresion -> exp IGIG exp','expresion',3,'p_expresion','parser_1.py',356),
  ('expresion -> exp MAYIG exp','expresion',3,'p_expresion','parser_1.py',357),
  ('expresion -> exp MENIG exp','expresion',3,'p_expresion','parser_1.py',358),
  ('exp -> termino exp_operacion','exp',2,'p_exp','parser_1.py',379),
  ('exp_operacion -> MAS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',384),
  ('exp_operacion -> MENOS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',385),
  ('exp_operacion -> empty','exp_operacion',1,'p_exp_operacion','parser_1.py',386),
  ('termino -> factor termino_operador','termino',2,'p_termino','parser_1.py',398),
  ('termino_operador -> POR factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',403),
  ('termino_operador -> DIV factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',404),
  ('termino_operador -> empty','termino_operador',1,'p_termino_operador','parser_1.py',405),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','parser_1.py',415),
  ('factor -> MAS var_cte','factor',2,'p_factor','parser_1.py',416),
  ('factor -> MENOS var_cte','factor',2,'p_factor','parser_1.py',417),
  ('factor -> var_cte','factor',1,'p_factor','parser_1.py',418),
  ('factor -> empty','factor',1,'p_factor','parser_1.py',419),
  ('var_cte -> ID','var_cte',1,'p_var_cte','parser_1.py',423),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','parser_1.py',424),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','parser_1.py',425),
  ('var_cte -> CTEC','var_cte',1,'p_var_cte','parser_1.py',426),
  ('var_cte -> CTEB','var_cte',1,'p_var_cte','parser_1.py',427),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',450),
]
