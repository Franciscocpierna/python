/*repl field_name with 'codigo',field_type with 'C',field_len  with 5,;
          field_dec  with 0               
     appe blan
     repl field_name with 'processo'  ,field_type with 'C',field_len  with 10,;
          field_dec  with 0
     appe blan
     repl field_name with 'junta',field_type with 'C',field_len  with 2,;
          field_dec  with 0
     appe blan
     repl field_name with 'cidade',field_type with 'C',field_len  with 5,;
          field_dec  with 0          
     appe blan
     repl field_name with 'd_distr',field_type with 'D',field_len  with 08,;
          field_dec  with 0          
     appe blan
     repl field_name with 'datainc',field_type with 'D',field_len  with 08,;
          field_dec  with 0                    
     appe blan
     repl field_name with 'd_valest',field_type with 'D',field_len  with 08,;
          field_dec  with 0                    
     appe blan
     repl field_name with 'dexev',field_type with 'D',field_len  with 08,;
          field_dec  with 0                    
     appe blan
     repl field_name with 'dexe',field_type with 'D',field_len  with 08,;
          field_dec  with 0                                        
     appe blan
     repl field_name with 'v_alcada',field_type with 'N',field_len  with 14,;
          field_dec  with 2          
     appe blan
     repl field_name with 'ganho',field_type with 'N',field_len  with 1,;
          field_dec  with 0
     appe blan
     repl field_name with 'dura',field_type with 'N',field_len  with 2,;
          field_dec  with 0          
     appe blan
     repl field_name with 'mens',field_type with 'C',field_len  with 1,;
          field_dec  with 0                    
     appe blan
     repl field_name with 'valest',field_type with 'N',field_len  with 14,;
          field_dec  with 2                    
     appe blan
     repl field_name with 'valesti',field_type with 'N',field_len  with 14,;
          field_dec  with 2                              
     appe blan
     repl field_name with 'valestf',field_type with 'N',field_len  with 14,;
          field_dec  with 2                                        
     appe blan
     repl field_name with 'vexe',field_type with 'N',field_len  with 14,;
          field_dec  with 2
     appe blan
     repl field_name with 'vexev',field_type with 'N',field_len  with 14,;
          field_dec  with 2                                        
     appe blan
     repl field_name with 'plurimo',field_type with 'C',field_len  with 1,;
          field_dec  with 0                                        
     appe blan
     repl field_name with 'locali',field_type with 'C',field_len  with 5,;
          field_dec  with 0                                                  
     appe blan
     repl field_name with 'vip',field_type with 'C',field_len  with 1,;
          field_dec  with 0                                                            
     appe blan
     repl field_name with 'codacao',field_type with 'C',field_len  with 2,;
          field_dec  with 0                                                                      
     appe blan
     repl field_name with 'situacao',field_type with 'C',field_len  with 1,;
          field_dec  with 0                                                                                
     appe blan
     repl field_name with 'datsys',field_type with 'D',field_len  with 8,;
          field_dec  with 0                                             
     appe blan
     repl field_name with 'portador',field_type with 'C',field_len  with 15,;
          field_dec  with  */
          
          
          
 create table if not exists pross (
     codigo   varchar(5) not null,
     processo varchar(10) not null,
     junta varchar(2) not null,
     cidade   varchar(5),
     d_distr date,
     datainc date,
     d_valest date,
     dexev date,
     dexe date,
     v_alcada decimal(14,2),
     ganho tinyint,
     dura tinyint,
     mens varchar(1),
     valest decimal(14,2),
	 valesti decimal(14,2),
	 valestf decimal(14,2),
     vexe decimal(14,2),
     vexev decimal(14,2),
     plurimo varchar(1),
     locali varchar(5),
     vip  varchar(1),
     codacao  varchar(2),
	 situacao  varchar(1),
	 datsys date,
     portador varchar(15)
 )default charset = utf8;  
 
/* crea tempo
   if !netuse("tempo",.t.,0)
     @23,03 say 'O arquivo tempo nao esta disponivel !'
     wait 'tecle <Enter>'
     retu .f.
    endif          
    append blank
    repl field_name with 'codigo',field_type with 'C',field_len with 5,;
         field_dec with 0
    append blank     
    repl field_name with 'cliente',field_type with 'C',field_len with 60,;
         field_dec with 0
    append blank
    repl field_name with 'endereco',field_type with 'C',field_len with 35,;
         field_dec with 0
    append blank
    repl field_name with 'cep',field_type with 'C',field_len with 8,;
         field_dec with 0
    append blank
    repl field_name with 'bairro',field_type with 'C',field_len with 15,;
         field_dec with 0                        
    append blank
    repl field_name with 'cidade',field_type with 'C',field_len with 20,;
         field_dec with 0                                 
    append blank
    repl field_name with 'estado',field_type with 'C',field_len with 2,;
         field_dec with 0                                 
    append blank
    repl field_name with 'numcgc',field_type with 'C',field_len with 14,;
         field_dec with 0                                 
    append blank
    repl field_name with 'inscest',field_type with 'C',field_len with 15,;
         field_dec with 0                                 
    append blank
    repl field_name with 'ddd',field_type with 'C',field_len with 4,;
         field_dec with 0                                 
    append blank
    repl field_name with 'fone',field_type with 'C',field_len with 8,;
         field_dec with 0                                 
    append blank
    repl field_name with 'ramal',field_type with 'C',field_len with 4,;
         field_dec with 0                                 
    append blank
    repl field_name with 'telex',field_type with 'C',field_len with 12,;
         field_dec with 0                                 
    append blank
    repl field_name with 'fax',field_type with 'C',field_len with 8,;
         field_dec with 0                                 
    append blank
    repl field_name with 'atencao',field_type with 'C',field_len with 35,;
         field_dec with 0                                 
    append blank
    repl field_name with 'coligada',field_type with 'C',field_len with 5,;
         field_dec with 0                                          
    append blank
    repl field_name with 'drec',field_type with 'D',field_len with 8,;
         field_dec with 0                                                   
    append blank
    repl field_name with 'grupo',field_type with 'N',field_len with 1,;
         field_dec with 0                                 
    append blank
    repl field_name with 'fixo',field_type with 'C',field_len with 1,;
         field_dec with 0                                          
    append blank
    repl field_name with 'email',field_type with 'C',field_len with 50,;
         field_dec with 0                                                   
     crea cliente from tempo         
     use
     erase tempo.dbf
     return .t.
*/
 create table  if not exists cliente(
    codigo varchar(5),
    cliente varchar(60),
	endereco varchar(35),
    cep varchar(8),
    bairro varchar(15),
    cidade varchar(20),
    estado varchar(2),
    numcgc varchar(14),
    inscest  varchar(15),
    ddd varchar(4),
    fone varchar(8),
    ramal varchar(4),
    telex varchar(12),
    fax varchar(8),
    atencao,varchar(35),
    coligada varchar(5),
    drec date,                                                  
    grupo tinyint,
    fixo varchar(1),
	email varchar(50)
   )default charset = utf8;  