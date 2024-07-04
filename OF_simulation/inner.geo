Geometry.CopyMeshingMethod = 1;
dTank =2.09;
rTank =1.045;
hTank =7.550059999999999;
hemiRatio =2.213514;
dImpeller =0.6966666666666665;
rImpeller =0.3483333333333333;
rRod =0.05573333333333332;
hRod =0.08791548165812377;
rDish =0.25079999999999997;
lBlade =0.17416666666666664;
wBlade =0.1393333333333333;
hImpeller =0.6479309816581238;
delhImpeller =1.449833;
wBaffle =0.16699099999999997;
rRotatingZone =0.40058333333333324;
hRotatingZone =0.2786666666666666;
xHemiBottom1 =-0.5179304029944437;
zHemiBottom1 =-0.2523473249317676;
xHemiBottom2 =-0.288453507212936;
zHemiBottom2 =-0.2926343645790717;
xHemiBottom3 =-0.6380863095109114;
zHemiBottom3 =-0.38163264429209875;
xHemiBottom4 =-0.3506802508355969;
zHemiBottom4 =-0.45062888940997764;
nx1 =20;
nx2 =20;
nx3 =20;
nx4 =20;
nyAboveDish =10;
nyBelowDish =10;
nxyAroundBlade =10;
nyTop =30;
nyBottom =15;
nyHemiBottom =10;
nyRod =5;
nyGap =30;
nr =5;

Point(0) = {0, 0, -rTank/hemiRatio};
Point(newp) = {-rRod/2, 0, -rTank/hemiRatio};
Point(newp) = {-rRod, 0, -rTank/hemiRatio};

//+
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{1}; Point{2}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{3}; Point{4}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{5}; Point{6}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{7}; Point{8}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{9}; Point{10}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{11}; Point{12}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{13}; Point{14}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{15}; Point{16}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{17}; Point{18}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{19}; Point{20}; }
}
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Duplicata { Point{21}; Point{22}; }
}

//+
Circle(1) = {2, 0, 4};
Circle(2) = {4, 0, 6};
Circle(3) = {6, 0, 8};
Circle(4) = {8, 0, 10};
Circle(5) = {10, 0, 12};
Circle(6) = {12, 0, 14};
Circle(7) = {14, 0, 16};
Circle(8) = {16, 0, 18};
Circle(9) = {18, 0, 20};
Circle(10) = {20, 0, 22};
Circle(11) = {22, 0, 24};
Circle(12) = {24, 0, 2};

//+
Line(13) = {1, 3};
Line(14) = {3, 5};
Line(15) = {5, 7};
Line(16) = {7, 9};
Line(17) = {9, 11};
Line(18) = {11, 13};
Line(19) = {13, 15};
Line(20) = {15, 17};
Line(21) = {17, 19};
Line(22) = {19, 21};
Line(23) = {21, 23};
Line(24) = {23, 1};
Line(25) = {2, 1};
Line(26) = {4, 3};
Line(27) = {6, 5};
Line(28) = {8, 7};
Line(29) = {10, 9};
Line(30) = {12, 11};
Line(31) = {14, 13};
Line(32) = {16, 15};
Line(33) = {18, 17};
Line(34) = {20, 19};
Line(35) = {22, 21};
Line(36) = {24, 23};
Line(37) = {3, 0};
Line(38) = {0, 7};
Line(39) = {0, 11};
Line(41) = {0, 15};
Line(42) = {0, 19};
Line(43) = {0, 23};
//+
Curve Loop(1) = {1, 26, -13, -25};
Plane Surface(1) = {1};
Curve Loop(2) = {2, 27, -14, -26};
Plane Surface(2) = {2};
Curve Loop(3) = {3, 28, -15, -27};
Plane Surface(3) = {3};
Curve Loop(4) = {4, 29, -16, -28};
Plane Surface(4) = {4};
Curve Loop(5) = {29, 17, -30, -5};
Plane Surface(5) = {5};
Curve Loop(6) = {18, -31, -6, 30};
Plane Surface(6) = {6};
Curve Loop(7) = {19, -32, -7, 31};
Plane Surface(7) = {7};
Curve Loop(8) = {20, -33, -8, 32};
Plane Surface(8) = {8};
Curve Loop(9) = {34, -21, -33, 9};
Plane Surface(9) = {9};
Curve Loop(10) = {35, -22, -34, 10};
Plane Surface(10) = {10};
Curve Loop(11) = {36, -23, -35, 11};
Plane Surface(11) = {11};
Curve Loop(12) = {12, 25, -24, -36};
Plane Surface(12) = {12};
Curve Loop(13) = {24, 13, 37, 43};
Plane Surface(13) = {13};
Curve Loop(14) = {37, 38, -15, -14};
Plane Surface(14) = {14};
Curve Loop(15) = {38, 16, 17, -39};
Plane Surface(15) = {15};
Curve Loop(16) = {39, 18, 19, -41};
Plane Surface(16) = {16};
Curve Loop(17) = {41, 20, 21, -42};
Plane Surface(17) = {17};
Curve Loop(18) = {42, 22, 23, -43};
Plane Surface(18) = {18};

Transfinite Curve {1, 13, 43, 22, 10, 2, 14, 38, 17, 5, 3, 15, 37, 24, 12, 4, 16, 39, 19, 7, 6, 18, 41, 21, 9, 8, 20, 42, 23, 11} = nr+1 Using Progression 1;

Transfinite Curve {36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25} = 10 Using Progression 1;

Transfinite Surface {1};
Transfinite Surface {2};
Transfinite Surface {3};
Transfinite Surface {4};
Transfinite Surface {5};
Transfinite Surface {6};
Transfinite Surface {7};
Transfinite Surface {8};
Transfinite Surface {9};
Transfinite Surface {10};
Transfinite Surface {11};
Transfinite Surface {12};
Transfinite Surface {13};
Transfinite Surface {14};
Transfinite Surface {15};
Transfinite Surface {16};
Transfinite Surface {17};
Transfinite Surface {18};

Recombine Surface {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18};

Extrude {0, 0, wBaffle} {
  Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{14}; Surface{15}; Surface{16}; Surface{17}; Surface{18}; Layers{nx1-1}; Recombine; 
}

Extrude {0, 0, (rTank/hemiRatio - wBaffle)/2} {
  Surface{109}; Surface{131}; Surface{153}; Surface{175}; Surface{197}; Surface{219}; Surface{241}; Surface{263}; Surface{285}; Surface{307}; Surface{65}; Surface{87}; Surface{351}; Surface{373}; Surface{395}; Surface{417}; Surface{439}; Surface{329};
Layers{nx2-1}; Recombine;  
}

Extrude {0, 0, (rTank/hemiRatio - wBaffle)/2} {
  Surface{461}; Surface{703}; Surface{681}; Surface{659}; Surface{637}; Surface{615}; Surface{593}; Surface{571}; Surface{549}; Surface{527}; Surface{505}; Surface{483}; Surface{747}; Surface{725}; Surface{835}; Surface{769}; Surface{791}; Surface{813}; Layers{nyHemiBottom-1}; Recombine; 
}

Extrude {0, 0, hRod} {
  Surface{879}; Surface{901}; Surface{923}; Surface{945}; Surface{967}; Surface{989}; Surface{1011}; Surface{1033}; Surface{1055}; Surface{1077}; Surface{1099}; Surface{857}; Surface{1143}; Surface{1165}; Surface{1231}; Surface{1209}; Surface{1187}; Surface{1121}; Layers{nyRod-1}; Recombine; 
}

Physical Surface("rod", 1628) = {1275, 1253, 1495, 1473, 1451, 1429, 1407, 1385, 1363, 1341, 1319, 1297, 1561, 1583, 1605, 1627, 1517, 1539};

Physical Surface("wall", 1629) = {4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 15, 14, 13, 18, 17, 16};

Physical Surface("internalToMerge4", 1630) = {214, 240, 192, 170, 522, 1050, 1424, 152, 504, 1076, 1450, 118, 470, 1086, 1460, 96, 448, 844, 1482, 74, 690, 866, 1240, 52, 668, 888, 1262, 294, 646, 910, 1284, 284, 636, 262, 614, 966, 1340, 944, 1318, 592, 988, 1362, 566, 1006, 1380, 544, 1028, 1402};

Physical Volume("tank") = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72};
