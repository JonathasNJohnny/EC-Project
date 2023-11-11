DROP TABLE IF EXISTS Enderecos CASCADE;
DROP TABLE IF EXISTS Consultas CASCADE;
DROP TABLE IF EXISTS Usuarios CASCADE;
DROP TABLE IF EXISTS Tipos_Usuarios CASCADE;

create table Tipos_Usuarios (
tipo_Usuario_ID SERIAL PRIMARY KEY,
tipo_Usuario_Nome varchar(50) not null
);

CREATE TABLE Enderecos (
    endereco_ID SERIAL PRIMARY KEY,
    cidade VARCHAR(50) NOT NULL,
    UF VARCHAR(2) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    rua VARCHAR(50) NOT NULL
);

CREATE TABLE Usuarios (
    user_ID SERIAL PRIMARY KEY,
    user_Name VARCHAR(50) NOT NULL,
    user_Senha VARCHAR(50) NOT NULL,
    user_Email VARCHAR(50) NOT NULL,
    user_Numero VARCHAR(50) NOT NULL,
    cpf VARCHAR(50) NOT NULL,
    tipo_Usuario_ID INT,
    endereco_ID INT, -- Adicione a chave estrangeira para a tabela Enderecos
    FOREIGN KEY (tipo_Usuario_ID) REFERENCES Tipos_Usuarios(tipo_Usuario_ID),
    FOREIGN KEY (endereco_ID) REFERENCES Enderecos(endereco_ID)
);

create table Consultas (
consultas_ID SERIAL PRIMARY KEY,
medico_ID int,
paciente_ID int,
data varchar(50) not null,
horario varchar(50) not null,
dados varchar(250),
FOREIGN KEY (medico_ID) references Usuarios(user_ID),
FOREIGN KEY (paciente_ID) references Usuarios(user_ID)
);

INSERT INTO Tipos_Usuarios (tipo_Usuario_Nome) VALUES
    ('Recepcionista'),
    ('Medico'),
    ('Administrador'),
    ('Paciente');

INSERT INTO Enderecos (cidade, UF, bairro, rua)
VALUES 
	('adminCity', 
	'AD', 
	'adminNeighborhood', 
	'adminStreet'
   );


INSERT INTO Usuarios (user_Name, user_Senha, user_Email, user_NUmero, cpf, tipo_Usuario_ID, endereco_ID)
VALUES (
	'ADMIN', 
	'admin', 
	'admin@admin.admin', 
	'(00) 00 00000-0000',
	'00000000000', 
	(SELECT tipo_Usuario_ID FROM Tipos_Usuarios WHERE tipo_Usuario_Nome = 'Administrador'),
	(SELECT endereco_ID FROM Enderecos where cidade = 'adminCity')
	);
