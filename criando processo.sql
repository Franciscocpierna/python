
          
          
          
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
