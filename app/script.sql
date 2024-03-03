create table if not exists clientes (
    id int primary key generated always as identity,
    limite int,
    saldo_inicial int
);


create table if not exists transacoes (
    id int primary key generated always as identity,
    cliente_id int references clientes(id),
    tipo char(1),
    valor int,
    descricao varchar(10),
    realizada_em timestamptz default now()
);

insert into clientes (limite, saldo_inicial) values
(100000, 0),
(80000, 0),
(1000000, 0),
(10000000, 0),
(500000, 0);

