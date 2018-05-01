<?php
require_once __DIR__ . '/../vendor/autoload.php';
use Phpml\Classification\KNearestNeighbors;

$samples = [
    [3.4, 2.3],
    [3.1, 1.8],
    [1.3, 3.4],
    [3.6, 4.7],
    [2.3, 2.9],
    [7.4, 4.7],
    [5.7, 3.5],
    [9.2, 2.5],
    [7.8, 3.4],
    [7.9, 0.8],
];
$labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1];
$x = [8.1, 3.4];

$classifier = new KNearestNeighbors();
$classifier->train($samples,$labels);
echo $classifier->predict($x);
