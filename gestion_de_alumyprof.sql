-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-08-2024 a las 04:49:53
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_de_alumyprof`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `documento_identidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`id`, `nombre`, `documento_identidad`) VALUES
(1, 'Deysi Day Aguirre', '45678901D'),
(2, 'Marcelo Páez Aracena', '56789012E'),
(3, 'Rodolfo Barraza Campos', '67890123F'),
(4, 'Eduardo Chuy-Kan Goic', '78901234G'),
(5, 'Luis Espejo Tapia', '89012345H'),
(6, 'Sebastián Toledo Rojas', '90123456I'),
(7, 'Héctor Torres Espejo', '01234567J'),
(8, 'Nelson Tapia González', '12345678K');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaturas`
--

CREATE TABLE `asignaturas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `id_profesor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asignaturas`
--

INSERT INTO `asignaturas` (`id`, `nombre`, `id_profesor`) VALUES
(1, 'Herramientas De Desarrollo', 1),
(2, 'Lenguaje De Programación II', 1),
(3, 'Base De Datos', 2),
(4, 'Estructura De Datos', 2),
(5, 'Lenguaje De Programación I', 3),
(6, 'Programación Y Algoritmo', 3),
(7, 'Taller De Programación', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaturas_alumnos`
--

CREATE TABLE `asignaturas_alumnos` (
  `id` int(11) NOT NULL,
  `id_alumno` int(11) DEFAULT NULL,
  `id_asignatura` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asignaturas_alumnos`
--

INSERT INTO `asignaturas_alumnos` (`id`, `id_alumno`, `id_asignatura`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 3, 2),
(5, 4, 2),
(6, 5, 2),
(7, 2, 2),
(8, 2, 3),
(9, 3, 3),
(10, 5, 3),
(11, 1, 4),
(12, 4, 4),
(13, 3, 5),
(14, 4, 5),
(15, 6, 6),
(16, 7, 6),
(17, 8, 7),
(18, 6, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `id` int(11) NOT NULL,
  `id_asignatura_alumno` int(11) DEFAULT NULL,
  `nota1` float DEFAULT NULL,
  `nota2` float DEFAULT NULL,
  `nota3` float DEFAULT NULL,
  `promedio` float GENERATED ALWAYS AS ((`nota1` + `nota2` + `nota3`) / 3) STORED
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `notas`
--

INSERT INTO `notas` (`id`, `id_asignatura_alumno`, `nota1`, `nota2`, `nota3`) VALUES
(1, 1, 6.5, 7, 6),
(2, 2, 5, 6, 7),
(3, 3, 6, 6.5, 6.5),
(4, 4, 7, 7, 6),
(5, 5, 5.5, 6.5, 6),
(6, 6, 6.5, 6, 7),
(7, 7, 6, 5.5, 6.5),
(8, 8, 5, 5.5, 6),
(9, 9, 6.5, 6, 7),
(10, 10, 7, 6.5, 6.5),
(11, 11, 6, 6, 6.5),
(12, 12, 5.5, 6.5, 6),
(13, 13, 7, 7, 7),
(14, 14, 6, 5.5, 6.5),
(15, 15, 6.5, 6, 5.5),
(16, 16, 7, 7, 7),
(17, 17, 5.5, 6, 6.5),
(18, 18, 6, 6.5, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `documento_identidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id`, `nombre`, `documento_identidad`) VALUES
(1, 'Andrés Alfaro', '12345678A'),
(2, 'Servando Campillay', '23456789B'),
(3, 'Jacqueline Manríquez', '34567890C');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_profesor` (`id_profesor`);

--
-- Indices de la tabla `asignaturas_alumnos`
--
ALTER TABLE `asignaturas_alumnos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_alumno` (`id_alumno`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_asignatura_alumno` (`id_asignatura_alumno`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `asignaturas_alumnos`
--
ALTER TABLE `asignaturas_alumnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `notas`
--
ALTER TABLE `notas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD CONSTRAINT `asignaturas_ibfk_1` FOREIGN KEY (`id_profesor`) REFERENCES `profesores` (`id`);

--
-- Filtros para la tabla `asignaturas_alumnos`
--
ALTER TABLE `asignaturas_alumnos`
  ADD CONSTRAINT `asignaturas_alumnos_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id`),
  ADD CONSTRAINT `asignaturas_alumnos_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id`);

--
-- Filtros para la tabla `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`id_asignatura_alumno`) REFERENCES `asignaturas_alumnos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
