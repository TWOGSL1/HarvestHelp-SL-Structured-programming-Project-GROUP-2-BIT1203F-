-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 28, 2026 at 09:07 PM
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
-- Database: `clinic_database new`
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
(4, 1, 1, '2026-06-20 10:00:00', 'Completed'),
(5, 2, 3, '2026-06-22 11:30:00', 'Scheduled'),
(6, 1, 2, '2026-06-25 09:00:00', 'Scheduled'),
(7, 1, 1, '2026-06-20 10:00:00', 'Completed'),
(8, 2, 3, '2026-06-22 11:30:00', 'Scheduled'),
(9, 1, 2, '2026-06-25 09:00:00', 'Scheduled'),
(10, 1, 1, '2026-06-28 20:35:49', 'Scheduled');

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `bill_id` int NOT NULL,
  `record_id` int NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` enum('Pending','paid','Overdue') DEFAULT 'Pending'
) ;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`bill_id`, `record_id`, `total_amount`, `status`) VALUES
(1, 1, 50.00, 'paid'),
(2, 1, 70.00, 'paid'),
(3, 1, 100.00, 'Pending'),
(4, 1, 90.00, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `clinics`
--

CREATE TABLE `clinics` (
  `clinic_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `clinics`
--

INSERT INTO `clinics` (`clinic_id`, `name`, `location`, `phone`) VALUES
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
(5, 2, 'Cold', 'Full cold treatment', '2026-06-30');

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
(4, 'Alice', 'Smith', '1990-05-15', 'Female', '789 Pine Ln, Freetown', '232-77-111222'),
(5, 'Bob', 'Johnson', '1985-11-20', 'Male', '101 Elm St, Bo', '232-78-333444'),
(6, 'Charlie', 'Brown', '1992-03-01', 'Male', '202 Maple Dr, Freetown', '232-77-555666'),
(7, 'Alice', 'Smith', '1990-05-15', 'Female', '789 Pine Ln, Freetown', '232-77-111222'),
(8, 'Bob', 'Johnson', '1985-11-20', 'Male', '101 Elm St, Bo', '232-78-333444'),
(9, 'Charlie', 'Brown', '1992-03-01', 'Male', '202 Maple Dr, Freetown', '232-77-555666'),
(12, 'Moses', 'Mansaray', '1997-05-15', NULL, '1 Mansaray Ln', '232-77-891222');

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
(1, 1, 50.00, '2026-06-28 17:30:51'),
(2, 1, 70.00, '2026-06-21 00:00:00'),
(3, 1, 100.00, '2026-06-28 18:31:00'),
(4, 1, 90.00, '2026-06-19 18:42:22');

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
(3, 'Dr. John', 'Doe', 'Doctor', 'Cardiology', 2),
(4, 'Moses', 'Mansaray', 'Doctor', 'Internal Medicine', 1);

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
-- Indexes for table `clinics`
--
ALTER TABLE `clinics`
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
-- AUTO_INCREMENT for table `clinics`
--
ALTER TABLE `clinics`
  MODIFY `clinic_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  MODIFY `record_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `patient_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`clinic_id`) REFERENCES `clinics` (`clinic_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
