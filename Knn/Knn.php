<?php
$raw_data_X = [
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
$raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1];

$x = [8.1, 3.4];

$distances = [];

foreach ($raw_data_X as $point) {
    $distances[] = sqrt(pow($point[0] - $x[0], 2) + pow($point[1] - $x[1], 2));
}
(asort($distances));
print_r(($distances));
$k = 6;
$topK_y = array_keys(array_slice($distances, 0, $k, true));
$counters = [];
foreach ($topK_y as $i) {
    if (!isset($counters[$raw_data_y[$i]])) {
        $counters[$raw_data_y[$i]] = 0;
    }
    $counters[$raw_data_y[$i]]++;
}

(arsort($counters, true));
print_r(array_keys($counters)[0]);
