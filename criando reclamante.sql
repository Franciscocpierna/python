 /*function reclac
 crea tempo
 if !netuse("tempo",.t.,0)
  @23,03 say 'O arquivo tempo nao esta disponivel !'
  wait 'tecle <Enter>'
  retu .f.
 endif
 appe blan
 repl field_name with 'processo',field_type with 'C',field_len  with 10,;
      field_dec  with 0
 appe blan
 repl field_name with 'junta'   ,field_type with 'C',field_len  with 2,;
      field_dec  with 0
 appe blan
 repl field_name with 'situacao'   ,field_type with 'C',field_len  with 1,;
      field_dec  with 0      
 appe blan
 repl field_name with 'cidade'   ,field_type with 'C',field_len  with 5,;
      field_dec  with 0         
 appe blan
 repl field_name with 'reclamante' ,field_type with 'C',field_len  with 40,;
       field_dec  with 0
 appe blan
 repl field_name with 'admissao',field_type with 'D',field_len  with 08,;
          field_dec  with 0                    
 appe blan
 repl field_name with 'demissao',field_type with 'D',field_len  with 08,;
          field_dec  with 0                              
 appe blan
 repl field_name with 'datsal',field_type with 'D',field_len  with 08,;
          field_dec  with 0                                        
 appe blan
 repl field_name with 'd_base',field_type with 'D',field_len  with 08,;
          field_dec  with 0                                                  
 appe blan
 repl field_name with 'd_basev',field_type with 'D',field_len  with 08,;
          field_dec  with 0                                                            
 appe blan
 repl field_name with 'salario',field_type with 'N',field_len  with 14,;
          field_dec  with 2        
 appe blan
 repl field_name with 'sallanc',field_type with 'N',field_len  with 14,;
          field_dec  with 2                  
 appe blan
 repl field_name with 'nrecla',field_type with 'N',field_len  with 5,;
          field_dec  with 0                  
appe blan
repl field_name with 'datsys',field_type with 'D',field_len  with 8,;
     field_dec  with 0                                             
appe blan
repl field_name with 'portador',field_type with 'C',field_len  with 15,;
     field_dec  with 0      
appe blan                                                                                                                                      
repl field_name with 'fisico',field_type with 'C',field_len  with 12,;
     field_dec  with 0                                                                                                                                                           
 crea recla  from tempo
 use
 eras tempo.dbf
 retu .t.*/
 create table   recla(
     processo varchar(10) not null,
     junta varchar(2) not null,
     cidade   varchar(5),
 'nrecla',field_type with 'N',field_len  with 5,
 'situacao'   ,field_type with 'C',field_len  with 1,
 'reclamante' ,field_type with 'C',field_len  with 40,
 'admissao',field_type with 'D',field_len  with 08,
 'demissao',field_type with 'D',field_len  with 08,
  `datsal`,field_type with 'D',field_len  with 08,
  'd_base',field_type with 'D',field_len  with 08,
  'd_basev',field_type with 'D',field_len  with 08,
  'salario',field_type with 'N',field_len  with 14,
  'sallanc',field_type with 'N',field_len  with 14,
  'datsys',field_type with 'D',field_len  with 8,
  'portador',field_type with 'C',field_len  with 15,
  'fisico',field_type with 'C',field_len  with 12,
 )default charset = utf8;  
 
 
 