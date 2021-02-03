-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 03, 2021 at 02:32 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `robotic`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone_num` varchar(12) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `msg` longtext NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `subject`, `msg`, `date`) VALUES
(1, 'Abhi', '123@gmail.com', '1234567894', 'programming', 'thank you!', '2021-02-02 11:28:24'),
(2, 'Abhishek Ashok Kadam', 'en19219440@git-india', '7066920049', 'sales', 'hii', '2021-02-02 11:53:12');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(50) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(21) NOT NULL,
  `content` longtext NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `video_file` varchar(12) NOT NULL,
  `fronted_img` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `date`, `video_file`, `fronted_img`) VALUES
(1, 'How to fix \"pending install in Window 10\"', 'video-1', ' in this video i gonna show to you how to fix pending install in window 10', '2021-02-02 11:38:25', 'Untitled 11_', 'fronted.png');

-- --------------------------------------------------------

--
-- Table structure for table `suscribes`
--

CREATE TABLE `suscribes` (
  `sno` int(50) NOT NULL,
  `email` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suscribes`
--

INSERT INTO `suscribes` (`sno`, `email`, `date`) VALUES
(1, '123@gmail.com', '2021-02-02 11:38:48'),
(2, 'kadamabhi049@gmail.c', '2021-02-02 11:53:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `suscribes`
--
ALTER TABLE `suscribes`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `suscribes`
--
ALTER TABLE `suscribes`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
