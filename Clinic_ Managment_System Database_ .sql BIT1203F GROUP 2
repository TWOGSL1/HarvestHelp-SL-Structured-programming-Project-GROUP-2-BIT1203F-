-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2026 at 04:53 PM
-- Server version: 8.0.46
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic managment system`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL,
  `patient_id` int NOT NULL,
  `staff_id` int NOT NULL,
  `appt_date` datetime NOT NULL,
  `status` enum('Scheduled','Completed','Cancelled') DEFAULT 'Scheduled'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` (`appointment_id`, `patient_id`, `staff_id`, `appt_date`, `status`) VALUES
(1, 1, 1, '2026-06-20 10:00:00', 'Completed'),
(2, 2, 3, '2026-06-22 11:30:00', 'Scheduled'),
(3, 9, 3, '2026-06-29 16:25:08', 'Completed'),
(4, 1, 2, '2026-06-29 16:25:08', 'Scheduled'),
(5, 6, 3, '2026-06-29 16:30:53', 'Cancelled'),
(6, 7, 2, '2026-06-29 16:30:53', 'Completed'),
(7, 7, 1, '2026-07-05 23:38:29', 'Scheduled'),
(8, 8, 2, '2026-06-30 12:00:00', 'Scheduled'),
(9, 9, 3, '2026-07-05 23:40:35', 'Scheduled'),
(10, 10, 1, '2026-07-07 23:40:35', 'Scheduled'),
(11, 11, 2, '2026-07-06 04:00:00', 'Scheduled'),
(12, 12, 2, '2026-07-10 05:00:00', 'Scheduled');

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `bill_id` int NOT NULL,
  `record_id` int NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` enum('Pending','Paid','Overdue') DEFAULT 'Pending'
) ;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`bill_id`, `record_id`, `total_amount`, `status`) VALUES
(1, 1, 50.00, 'Pending'),
(2, 1, 90.00, 'Paid'),
(3, 1, 100.00, 'Paid'),
(4, 1, 50.00, 'Pending'),
(5, 1, 300.00, 'Overdue'),
(6, 1, 150.00, 'Paid'),
(7, 1, 120.00, 'Paid'),
(8, 1, 150.00, 'Paid'),
(9, 5, 120.00, 'Paid'),
(11, 6, 100.00, 'Paid'),
(12, 1, 300.00, 'Overdue');

-- --------------------------------------------------------

--
-- Table structure for table `cliniccenter`
--

CREATE TABLE `cliniccenter` (
  `clinic_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cliniccenter`
--

INSERT INTO `cliniccenter` (`clinic_id`, `name`, `location`, `phone`) VALUES
(1, 'City Health Clinic', '123 Main St, Freetown', '232-77-123456'),
(2, 'Wellness Center', '456 Oak Ave, Bo', '232-78-789012');

-- --------------------------------------------------------

--
-- Table structure for table `medicalrecords`
--

CREATE TABLE `medicalrecords` (
  `record_id` int NOT NULL,
  `appointment_id` int NOT NULL,
  `diagnosis` text,
  `treatment` text,
  `record_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `medicalrecords`
--

INSERT INTO `medicalrecords` (`record_id`, `appointment_id`, `diagnosis`, `treatment`, `record_date`) VALUES
(1, 1, 'Common Cold', 'Rest and fluids', '2026-06-20'),
(2, 2, 'Common Cold', 'Rest and fluids', '2026-06-21'),
(3, 5, 'Common Cold', 'Rest and fluids', '2026-06-26'),
(4, 4, 'Common Cold', 'Rest', '2026-07-01'),
(5, 6, 'Malaria', 'Full treatment', '2026-06-30'),
(6, 3, 'Toothache', 'Full treatment', '2026-06-22');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `patient_id` int NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `dob` date DEFAULT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`patient_id`, `first_name`, `last_name`, `dob`, `gender`, `address`, `phone`) VALUES
(1, 'Alice', 'Smith', '1990-05-15', 'Female', '888 New Rd, Freetown', '232-77-111222'),
(2, 'Bob', 'Johnson', '1985-11-20', 'Male', '101 Elm St, Bo', '232-78-333444'),
(3, 'Charlie', 'Brown', '1992-03-01', 'Male', '202 Maple Dr, Freetown', '232-77-555666'),
(4, 'Hawa', 'Bah', '2000-05-15', 'Female', '1 foday dr,Bo', '232-77-111222'),
(5, 'Karim', 'sesay', '1992-03-01', 'Male', '2 sorie ln, Freetown', '23279 -883 556'),
(6, 'Williams', 'Kanu', '1980-08-20', 'Male', '13 Williams st, Freetown.', '232-78-884-221'),
(7, 'Musa', 'Kamara', '1985-01-20', 'Male', '27 immat street, Freetown', '23279 -883 654'),
(8, 'Joshu', 'Bangura', '1999-08-20', 'Male', '1 yam farm sch, Waterloo', '232-77-889-456'),
(9, 'Mary', 'Mansaray', '1985-01-20', 'Female', '1 Mansaray st, Waterloo', '23279 -908-765'),
(10, 'Mohamed ', 'Mansaray', '1995-09-30', 'Male', '1 Mansaray Street, Devil Hole', '232-33-445-990'),
(11, 'Elvera', 'Smith', '1990-07-15', 'Female', '26 SS CAMP junction, Freetown', '232-31-315-887'),
(12, 'Emmanuel', 'Turay', '2003-01-20', 'Male', '45 SS CAMP, Freetown', '23279 -789-654'),
(13, 'Santigie', 'Sesay', '1990-07-15', 'Male', '1 Susu Town, Devil Hole', '232-31-315-8777'),
(14, 'Yeano', 'Kalokoh', '1997-01-20', 'Female', '23 susu town, devil hole', '23279 -89756'),
(15, 'Alie', 'Kanu', '1990-08-15', 'Male', '111 Mansaray dr', '232-31-315-700'),
(16, 'Sarah', 'Sesay', '1997-09-20', 'Female', '33 Davies dr', '23279 -134-323'),
(17, 'Lucida', 'Kamara', '1990-05-15', 'Female', '555 junction, waterloo', '232-77-878-456'),
(18, 'Hawanatu', 'Kamara', '2012-10-20', 'Female', '90 Devil hole', '23279 -908-765'),
(19, 'Doris', 'Pratty', '1992-03-01', 'Female', '88 John St, Freetown', '232-77-786-906'),
(20, 'Hassan', 'Cantay', '1997-09-20', 'Male', '111 Fullah mosque', '23279 -674-904');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int NOT NULL,
  `bill_id` int NOT NULL,
  `amount_paid` decimal(10,2) NOT NULL,
  `payment_date` datetime DEFAULT CURRENT_TIMESTAMP
) ;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `bill_id`, `amount_paid`, `payment_date`) VALUES
(1, 1, 30.00, '2026-06-29 14:08:19'),
(2, 2, 90.00, '2026-06-29 14:40:17'),
(3, 3, 100.00, '2026-06-29 14:40:17'),
(4, 4, 50.00, '2026-06-29 14:42:24'),
(5, 5, 300.00, '2026-06-29 14:42:24'),
(6, 6, 150.00, '2026-06-29 14:44:03'),
(7, 7, 120.00, '2026-06-29 14:44:03'),
(8, 8, 150.00, '2026-06-29 21:33:40'),
(9, 9, 120.00, '2026-06-29 21:33:40'),
(11, 11, 100.00, '2026-06-29 21:36:14'),
(12, 12, 300.00, '2026-06-29 21:36:14');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `clinic_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `first_name`, `last_name`, `role`, `specialization`, `clinic_id`) VALUES
(1, 'Dr. Emily', 'White', 'Doctor', 'General Practitioner', 1),
(2, 'Nurse Sarah', 'Davis', 'Nurse', 'Pediatrics', 1),
(3, 'Dr. John', 'Doe', 'Doctor', 'Cardiology', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`appointment_id`),
  ADD KEY `patient_id` (`patient_id`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`bill_id`),
  ADD KEY `record_id` (`record_id`);

--
-- Indexes for table `cliniccenter`
--
ALTER TABLE `cliniccenter`
  ADD PRIMARY KEY (`clinic_id`);

--
-- Indexes for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  ADD PRIMARY KEY (`record_id`),
  ADD UNIQUE KEY `appointment_id` (`appointment_id`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `bill_id` (`bill_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`),
  ADD KEY `clinic_id` (`clinic_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `appointment_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `bill_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cliniccenter`
--
ALTER TABLE `cliniccenter`
  MODIFY `clinic_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  MODIFY `record_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `patient_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointments`
--
ALTER TABLE `appointments`
  ADD CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  ADD CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`);

--
-- Constraints for table `billing`
--
ALTER TABLE `billing`
  ADD CONSTRAINT `billing_ibfk_1` FOREIGN KEY (`record_id`) REFERENCES `medicalrecords` (`record_id`);

--
-- Constraints for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  ADD CONSTRAINT `medicalrecords_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`appointment_id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `billing` (`bill_id`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`clinic_id`) REFERENCES `cliniccenter` (`clinic_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
