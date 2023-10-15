create table Tipos_Usuarios (
tipo_Usuario_ID SERIAL PRIMARY KEY,
tipo_Usuario_Nome varchar(50) not null
);

create table Usuarios (
user_ID SERIAL PRIMARY KEY,
user_Name varchar(50) not null,
user_Senha varchar(50) not null,
tipo_Usuario_ID int,
FOREIGN KEY (tipo_Usuario_ID) references Tipos_Usuarios(tipo_Usuario_ID)
);

select * from Usuarios