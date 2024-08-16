use aula16;
create table alunos(
	matricula smallint not null primary key,
    nome varchar(30) not null,
    curso varchar(10) null);

insert into alunos (matricula, nome, curso)
	values (1, 'Ana', 'DEV');
 
insert into alunos (matricula, nome, curso)
	values (2, 'Pedro', 'Fotografia');
    
