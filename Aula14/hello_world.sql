use bdxavier;

create table tipo (
	idTipo char(1) not null primary key,
    descTipo varchar(20) not null);
    
rename table tipo to tiposClientes;                                /*renomeia o nome da tabela*/
    
alter table tipo add column subTipo varchar(20) null;             /*cria uma nova coluna - função tem a capacidade de criar uma nova coluna*/

alter table tipo drop column subTipo;                   		  /*Apaga a coluna*/

create table clientes (
	IdCli tinyint not null check(IdCli > 0),           		      /*guarda um mini inteiro de 4 posições - só pode colacar cliente que o ID é maior que 0*/
    nomeCli varchar(30) not null unique,               			  /*varchar guardar um char e não é determinado o tamanho dele, é um tamanho variável. Um byte também é separado para dizer a quatidade de bits que tem no char. Nessa caso, o tamanho máximo do cahr é 30*/
															      /*unique - não pode cadastrar mais de um cliente com o mesmo nome*/
    sexoCli char(1) null,                               	      /*esse char pode ter apenas um byte, pois foi determinado isso.  Quando não digo se é null ou not null, será null.*/
    IdTipoCli  char(1) not null references tipo,        		  /*Cria uma relação entre as duas tabelas */
    vipCli bool null,
    primary key(idCli)                                  		  /*é uma chave primária*/
    );                                

alter table clientes 
add constraint chk_sexo check(sexoCli in ('m', 'f', 't', 'o'));    /*restringe o sexoCli a permitir apenas esses caracteres*/

alter table clientes 
drop constraint chk_sexo;

alter table clientes                                              /*Toda vez que eu altero a tabela, devo usar isso*/
modify sexoCli char(2) not null;                                  /*Aqui eu modifico como a variável foi declarada*/

drop table clientes;