CREATE DATABASE repuestos;


CREATE TABLE clientes (
  id_cliente INT PRIMARY KEY AUTO_INCREMENT,
  fk_id_tipo_cliente INT NOT NULL,
  nombre_apellido VARCHAR(70) NOT NULL,
  cuit VARCHAR(30) NOT NULL,
  direccion VARCHAR(50) NOT NULL,
  fk_id_localidad INT NOT NULL, 
  FOREIGN KEY (fk_id_tipo_cliente) REFERENCES tipos_clientes(id_tipo_cliente),
  FOREIGN KEY (fk_id_localidad) REFERENCES localidades(id_localidad)
);


CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    fk_id_venta INT NOT NULL,
    fk_id_articulo INT NOT NULL,
    FOREIGN KEY (fk_id_venta) REFERENCES ventas(id_ventas),
    FOREIGN KEY (fk_id_articulo) REFERENCES articulos(id_articulo)
);

CREATE TABLE ventas (
    id_ventas INT PRIMARY KEY AUTO_INCREMENT,
    nro_comprobante int NOT NULL, 
    fk_id_cliente INT NOT NULL,
         INT NOT NULL,
    FOREIGN KEY (fk_id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (fk_id_canal_de_ventas) REFERENCES canales_de_ventas(id_canal_de_ventas)
);
CREATE TABLE articulos (
    id_articulo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    fk_id_grupo INT NOT NULL,
    FOREIGN KEY (fk_id_grupo) REFERENCES grupos(id_grupo)
);
CREATE TABLE compatibilidades (
    id_compatibilidad INT PRIMARY KEY AUTO_INCREMENT,
    fk_id_articulo INT NOT NULL,
    fk_id_modelo INT NOT NULL,
    FOREIGN KEY (fk_id_articulo) REFERENCES articulos(id_articulo),
    FOREIGN KEY (fk_id_modelo) REFERENCES modelos(id_modelo)

);

CREATE TABLE canales_de_ventas (
    id_canal_de_ventas INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
);
CREATE TABLE tipos_clientes (
    id_tipo_cliente INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL
);
CREATE TABLE provincias (
    id_provincia INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL
);
CREATE TABLE localidades (
    id_localidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    fk_id_provincia INT,
    FOREIGN KEY (fk_id_provincia) REFERENCES provincias(id_provincia)
);


CREATE TABLE grupos (
    id_grupo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL
);
clientes, pedidos,ventas,articulos, canales_de_ventas, tipos_clientes, provincias, localidades,grupos,modelos,marcas


CREATE TABLE modelos (
    id_modelo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    fk_id_marca INT NOT NULL,
    FOREIGN KEY (fk_id_marca) REFERENCES marcas(id_marca)

);

CREATE TABLE marcas (
    id_marca INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL
);
INSERT INTO tabla (columnas) VALUES (VALORES),(OTROS CAMPOS)


ALTER TABLE clientes DROP COLUMN apellido;


INSERT INTO `provincias` (`id_provincia`, `nombre`) VALUES (NULL, 'Capital Federal');
INSERT INTO `localidades` (`id_localidad`, `nombre`, `fk_id_provincia`) VALUES (NULL, 'Capital Federal', 1), (NULL, 'Lanus', 3), (NULL, 'Belen', 2); 

INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Golf','1');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Virtus','1');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Ka','2');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Ranger','2');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Corsa','3');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Meriva','3');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Hilux','4');
INSERT INTO modelos (nombre,fk_id_marca) VALUES ('Etios','4');

INSERT INTO `grupos` (`id_grupo`, `nombre`) VALUES (NULL, ''), (NULL, 'Tren Trasero'),(NULL, 'Motor'),(NULL, 'Laterales'); 


INSERT INTO clientes (fk_id_tipo_cliente,nombre_apellido,cuit,direccion,fk_id_localidad) VALUES (2,'ConsumidorFinal','1000000000','Calle Belgrano 123',2);
INSERT INTO clientes (fk_id_tipo_cliente,nombre_apellido,cuit,direccion,fk_id_localidad) VALUES (1,'El Salvanti','3030948576','Avenida Mitre 456',5);
INSERT INTO clientes (fk_id_tipo_cliente,nombre_apellido,cuit,direccion,fk_id_localidad) VALUES (1,'Roberto Levi','2020229385','Calle San Martín 789',3);
INSERT INTO clientes (fk_id_tipo_cliente,nombre_apellido,cuit,direccion,fk_id_localidad) VALUES (2,'Camila Salerno','2739888403','Avenida Sarmiento 234',4);
INSERT INTO clientes (fk_id_tipo_cliente,nombre_apellido,cuit,direccion,fk_id_localidad) VALUES (2,'Gabriela Pari','2739040043','Calle Moreno 567',1);



SELECT * FROM clientes;
SELECT * FROM pedidos;
SELECT * FROM ventas;
SELECT * FROM articulos;
SELECT * FROM compatibilidades;
SELECT * FROM canales_de_ventas;
SELECT * FROM tipos_clientes;
SELECT * FROM provincias;
SELECT * FROM localidades;
SELECT * FROM grupos;
SELECT * FROM modelos;
SELECT * FROM marcas;


#inner join 

Select * from tipos_clientes inner join clientes on tipos_clientes.id_tipo_cliente = clientes.fk_id_tipo_cliente; 

